package main

import (
	"encoding/json"
	"fmt"
	"io/fs"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/gitsync"
	"github.com/rhnvrm/stock-market-circulars/internal/handlers"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
	"github.com/rhnvrm/stock-market-circulars/internal/scheduler"
	"github.com/rhnvrm/stock-market-circulars/internal/search"
	"github.com/rhnvrm/stock-market-circulars/internal/templates"
	"github.com/rhnvrm/stock-market-circulars/static"
)

// Build information - injected via ldflags
var buildString = "dev"

func main() {
	// Configuration
	addr := getEnv("ADDR", ":8080")
	contentDir := getEnv("CONTENT_DIR", "./hugo-site/content")
	baseURL := getEnv("BASE_URL", "http://localhost:8080")

	// Git sync configuration
	gitRepoURL := getEnv("GIT_REPO_URL", "")
	gitDataPath := getEnv("GIT_DATA_PATH", "/tmp/stock-market-circulars-data")
	gitBranch := getEnv("GIT_BRANCH", "master")
	syncInterval := getEnv("SYNC_INTERVAL", "@every 1h")

	log.Printf("Starting Stock Market Circulars Server (Build: %s)...", buildString)

	// Initialize template renderer
	tmplRenderer, err := templates.NewRenderer()
	if err != nil {
		log.Fatalf("Failed to initialize templates: %v", err)
	}

	markdown := render.NewMarkdown()

	// Typesense configuration
	typesenseHost := getEnv("TYPESENSE_HOST", "localhost:8108")
	typesenseKey := getEnv("TYPESENSE_API_KEY", "")
	typesenseCollection := getEnv("TYPESENSE_COLLECTION", "circulars")
	typesenseAutoIndex := getEnv("TYPESENSE_AUTO_INDEX", "true") == "true"
	typesenseReindexOnSync := getEnv("TYPESENSE_REINDEX_ON_SYNC", "true") == "true"

	searchSvc := search.NewService(typesenseHost, typesenseKey, typesenseCollection)

	var currentState atomic.Pointer[appState]
	var reindexInFlight atomic.Bool
	var syncInFlight atomic.Bool

	buildAndSwapState := func(contentPath string) (*appState, error) {
		log.Printf("Building content state from %s...", contentPath)
		start := time.Now()

		state, err := buildAppState(contentPath, markdown)
		if err != nil {
			return nil, err
		}

		currentState.Store(state)
		log.Printf("Content state ready: %d circulars in %v", state.index.TotalCount, time.Since(start))
		return state, nil
	}

	triggerTypesenseReindex := func(state *appState) {
		if !searchSvc.IsEnabled() || !typesenseAutoIndex || !typesenseReindexOnSync {
			return
		}
		if !reindexInFlight.CompareAndSwap(false, true) {
			log.Println("Skipping Typesense reindex: previous run still in progress")
			return
		}

		go func(snapshot *appState) {
			defer reindexInFlight.Store(false)
			log.Println("Background Typesense reindex started")
			start := time.Now()
			if err := searchSvc.IndexCirculars(snapshot.allCirculars, baseURL); err != nil {
				log.Printf("Warning: Background Typesense reindex failed: %v", err)
				return
			}
			log.Printf("Background Typesense reindex completed with %d circulars in %v", len(snapshot.allCirculars), time.Since(start))
		}(state)
	}

	getState := func(w http.ResponseWriter) *appState {
		state := currentState.Load()
		if state == nil {
			http.Error(w, "Content state unavailable", http.StatusServiceUnavailable)
			return nil
		}
		return state
	}

	// Initialize git sync if configured
	var gitSync *gitsync.SyncManager
	var sched *scheduler.Scheduler
	startupSyncChanged := false

	if gitRepoURL != "" {
		log.Printf("Git sync mode enabled: %s -> %s", gitRepoURL, gitDataPath)

		gitSync = gitsync.NewSyncManager(gitRepoURL, gitDataPath)
		gitSync.SetBranch(gitBranch)

		// Clone repository on startup
		startupSyncChanged, err = gitSync.Clone()
		if err != nil {
			log.Fatalf("Failed to clone git repository: %v", err)
		}

		// Use git-synced content path
		contentDir = gitSync.ContentPath()
	}

	// Initial state build
	state, err := buildAndSwapState(contentDir)
	if err != nil {
		log.Fatalf("Failed to build content state: %v", err)
	}

	// Initialize Typesense search
	if searchSvc.IsEnabled() {
		log.Println("Typesense search enabled")

		if err := searchSvc.EnsureCollection(); err != nil {
			log.Printf("Warning: Failed to ensure Typesense collection: %v", err)
		}

		if typesenseAutoIndex {
			if startupSyncChanged && typesenseReindexOnSync {
				log.Println("Startup git sync changed content, refreshing Typesense index...")
				if err := searchSvc.IndexCirculars(state.allCirculars, baseURL); err != nil {
					log.Printf("Warning: Failed to refresh Typesense index after startup sync: %v", err)
				}
			} else if err := searchSvc.EnsureIndexed(state.allCirculars, baseURL, typesenseAutoIndex); err != nil {
				log.Printf("Warning: Failed to ensure indexing: %v", err)
			}
		}

		if !typesenseReindexOnSync {
			log.Println("Typesense sync reindex disabled; search will only be refreshed automatically when the collection is empty at startup")
		}
	} else {
		log.Println("Typesense search disabled (TYPESENSE_API_KEY not set)")
	}

	if gitSync != nil {
		// Start scheduler for periodic sync after initial state/search setup
		sched = scheduler.New()
		if err := sched.AddSyncJob(syncInterval, func() {
			if !syncInFlight.CompareAndSwap(false, true) {
				log.Println("Scheduled sync skipped: previous run still in progress")
				return
			}
			defer syncInFlight.Store(false)

			changed, err := gitSync.Pull()
			if err != nil {
				log.Printf("Scheduled sync error: %v", err)
				return
			}
			if !changed {
				return
			}

			state, err := buildAndSwapState(gitSync.ContentPath())
			if err != nil {
				log.Printf("Error rebuilding content state after sync: %v", err)
				return
			}
			triggerTypesenseReindex(state)
		}); err != nil {
			log.Printf("Warning: Failed to add sync job: %v", err)
		}
		sched.Start()
		defer sched.Stop()
	}

	// Setup router
	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)
	r.Use(middleware.Compress(5))

	// Static files (embedded in binary)
	cssFS, _ := fs.Sub(static.Files, "css")
	r.Handle("/css/*", http.StripPrefix("/css/", http.FileServer(http.FS(cssFS))))

	// Routes - Minimal MVP
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		page := getPage(r)
		result, circulars := state.queryCirculars(content.QueryOptions{Page: page, PageSize: 50})

		data := map[string]interface{}{
			"Title":      "Recent Circulars",
			"BaseURL":    baseURL,
			"Path":       "/",
			"TotalCount": result.Total,
			"Circulars":  circulars,
			"Pagination": map[string]interface{}{
				"CurrentPage": result.Page,
				"TotalPages":  result.TotalPages,
				"HasPrev":     result.HasPrev,
				"HasNext":     result.HasNext,
			},
		}

		if err := tmplRenderer.Render(w, "page-home", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// All circulars page (must be before {source} route)
	r.Get("/circulars/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		page := getPage(r)
		result, circulars := state.queryCirculars(content.QueryOptions{
			Page:     page,
			PageSize: 50,
		})

		data := map[string]interface{}{
			"Title":      "All Circulars",
			"BaseURL":    baseURL,
			"Path":       "/circulars/",
			"TotalCount": result.Total,
			"Circulars":  circulars,
			"Pagination": map[string]interface{}{
				"CurrentPage": result.Page,
				"TotalPages":  result.TotalPages,
				"HasPrev":     result.HasPrev,
				"HasNext":     result.HasNext,
			},
		}

		if err := tmplRenderer.Render(w, "page-all", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	r.Get("/circulars/{source}/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		source := chi.URLParam(r, "source")
		page := getPage(r)
		result, circulars := state.queryCirculars(content.QueryOptions{
			Source:   source,
			Page:     page,
			PageSize: 50,
		})

		data := map[string]interface{}{
			"Title":      fmt.Sprintf("%s Circulars", strings.ToUpper(source)),
			"BaseURL":    baseURL,
			"Path":       fmt.Sprintf("/circulars/%s/", source),
			"TotalCount": result.Total,
			"Circulars":  circulars,
			"Pagination": map[string]interface{}{
				"CurrentPage": result.Page,
				"TotalPages":  result.TotalPages,
				"HasPrev":     result.HasPrev,
				"HasNext":     result.HasNext,
			},
		}

		if err := tmplRenderer.Render(w, "page-source", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Tags listing page
	r.Get("/tags/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		data := map[string]interface{}{
			"Title":       "Tags",
			"Description": "Browse all tags for stock market circulars",
			"BaseURL":     baseURL,
			"Path":        "/tags/",
			"BasePath":    "/tags/",
			"IsStocks":    false,
			"TotalCount":  state.tags.TotalCount,
			"TopByCount":  state.tags.TopByCount,
			"TopByRecent": state.tags.TopByRecent,
			"AllItems":    state.tags.AllItems,
		}

		if err := tmplRenderer.Render(w, "page-terms", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Tag-specific page
	r.Get("/tags/{tag}/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		tag := chi.URLParam(r, "tag")
		page := getPage(r)
		result, circulars := state.queryCirculars(content.QueryOptions{
			Tag:      tag,
			Page:     page,
			PageSize: 50,
		})

		if result.Total == 0 {
			http.NotFound(w, r)
			return
		}

		data := map[string]interface{}{
			"Title":       fmt.Sprintf("Tag: %s", tag),
			"Description": fmt.Sprintf("Circulars tagged with %s", tag),
			"BaseURL":     baseURL,
			"Path":        fmt.Sprintf("/tags/%s/", tag),
			"FeedURL":     fmt.Sprintf("/tags/%s/feed.xml", tag),
			"TotalCount":  result.Total,
			"Circulars":   circulars,
			"Pagination": map[string]interface{}{
				"CurrentPage": result.Page,
				"TotalPages":  result.TotalPages,
				"HasPrev":     result.HasPrev,
				"HasNext":     result.HasNext,
			},
		}

		if err := tmplRenderer.Render(w, "page-taxonomy", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Stocks listing page
	r.Get("/stocks/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		data := map[string]interface{}{
			"Title":       "Stocks",
			"Description": "Browse circulars by stock symbol",
			"BaseURL":     baseURL,
			"Path":        "/stocks/",
			"BasePath":    "/stocks/",
			"IsStocks":    true,
			"TotalCount":  state.stocks.TotalCount,
			"TopByCount":  state.stocks.TopByCount,
			"TopByRecent": state.stocks.TopByRecent,
			"AllItems":    state.stocks.AllItems,
		}

		if err := tmplRenderer.Render(w, "page-terms", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Stock-specific page
	r.Get("/stocks/{stock}/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		stock := strings.ToLower(chi.URLParam(r, "stock"))
		page := getPage(r)
		result, circulars := state.queryCirculars(content.QueryOptions{
			Stock:    stock,
			Page:     page,
			PageSize: 50,
		})

		if result.Total == 0 {
			http.NotFound(w, r)
			return
		}

		data := map[string]interface{}{
			"Title":       fmt.Sprintf("Stock: %s", strings.ToUpper(stock)),
			"Description": fmt.Sprintf("Circulars mentioning %s", strings.ToUpper(stock)),
			"BaseURL":     baseURL,
			"Path":        fmt.Sprintf("/stocks/%s/", stock),
			"FeedURL":     fmt.Sprintf("/stocks/%s/feed.xml", stock),
			"TotalCount":  result.Total,
			"Circulars":   circulars,
			"Pagination": map[string]interface{}{
				"CurrentPage": result.Page,
				"TotalPages":  result.TotalPages,
				"HasPrev":     result.HasPrev,
				"HasNext":     result.HasNext,
			},
		}

		if err := tmplRenderer.Render(w, "page-taxonomy", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Feeds info page
	r.Get("/feeds/", func(w http.ResponseWriter, r *http.Request) {
		data := map[string]interface{}{
			"Title":   "RSS Feeds",
			"BaseURL": baseURL,
			"Path":    "/feeds/",
		}

		if err := tmplRenderer.Render(w, "page-feeds", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	r.Get("/circulars/{source}/{year}/{slug}/", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		source := chi.URLParam(r, "source")
		year := chi.URLParam(r, "year")
		slug := chi.URLParam(r, "slug")

		pathKey := fmt.Sprintf("%s/%s/%s", source, year, slug)
		circularID, ok := state.index.ByPath[pathKey]
		if !ok {
			http.NotFound(w, r)
			return
		}

		circular, ok := state.circularByID[circularID]
		if !ok {
			http.Error(w, "Error loading circular", http.StatusInternalServerError)
			return
		}

		data := map[string]interface{}{
			"Title":    circular.Title,
			"BaseURL":  baseURL,
			"Path":     circular.Permalink(),
			"Circular": circular,
		}

		if err := tmplRenderer.Render(w, "page-circular", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// RSS Feeds
	// Main RSS feed (all sources)
	r.Get("/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "Stock Market Circulars",
			Link:        baseURL,
			Description: "Latest stock market circulars from NSE, BSE, and SEBI",
			SelfLink:    baseURL + "/feed.xml",
			BaseURL:     baseURL,
		}, state.index, state.circularByID)
	})

	// All circulars feed
	r.Get("/circulars/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "All Stock Market Circulars",
			Link:        baseURL + "/circulars/",
			Description: "All circulars from NSE, BSE, and SEBI",
			SelfLink:    baseURL + "/circulars/feed.xml",
			BaseURL:     baseURL,
		}, state.index, state.circularByID)
	})

	// Source-specific RSS feeds
	r.Get("/circulars/{source}/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		source := chi.URLParam(r, "source")
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       fmt.Sprintf("%s Circulars", source),
			Link:        baseURL + "/circulars/" + source + "/",
			Description: fmt.Sprintf("Latest circulars from %s", source),
			SelfLink:    baseURL + "/circulars/" + source + "/feed.xml",
			BaseURL:     baseURL,
			Source:      source,
		}, state.index, state.circularByID)
	})

	// Tag-specific RSS feeds
	r.Get("/tags/{tag}/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}

		tag := chi.URLParam(r, "tag")
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "Circulars tagged: " + tag,
			Link:        baseURL + "/tags/" + tag + "/",
			Description: fmt.Sprintf("Stock market circulars tagged with %s", tag),
			SelfLink:    baseURL + "/tags/" + tag + "/feed.xml",
			BaseURL:     baseURL,
			Tag:         tag,
		}, state.index, state.circularByID)
	})

	// Search endpoints
	// HTML search page
	r.Get("/search", func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query().Get("q")
		source := r.URL.Query().Get("source")
		pageStr := r.URL.Query().Get("page")

		// Parse page number
		page := 1
		if pageStr != "" {
			if p, err := strconv.Atoi(pageStr); err == nil && p > 0 {
				page = p
			}
		}

		data := map[string]interface{}{
			"Title":   "Search Circulars",
			"BaseURL": baseURL,
			"Path":    "/search",
			"Query":   query,
			"Source":  source,
		}

		// Show search form if no query
		if query == "" {
			if err := tmplRenderer.Render(w, "page-search", data); err != nil {
				log.Printf("Error rendering template: %v", err)
				http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			}
			return
		}

		// Check if search is enabled
		if !searchSvc.IsEnabled() {
			data["Error"] = "Search functionality is not configured. Please set TYPESENSE_API_KEY environment variable."
			if err := tmplRenderer.Render(w, "page-search", data); err != nil {
				log.Printf("Error rendering template: %v", err)
				http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			}
			return
		}

		// Perform search
		result, err := searchSvc.Search(search.SearchOptions{
			Query:   query,
			Source:  source,
			Page:    page,
			PerPage: 20,
		})
		if err != nil {
			data["Error"] = "Search error: " + err.Error()
			if err := tmplRenderer.Render(w, "page-search", data); err != nil {
				log.Printf("Error rendering template: %v", err)
				http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			}
			return
		}

		// Render results
		data["Results"] = result.Items
		data["TotalResults"] = result.Total
		data["CurrentPage"] = result.Page
		data["TotalPages"] = result.TotalPages
		data["HasPrev"] = result.Page > 1
		data["HasNext"] = result.Page < result.TotalPages
		data["PrevPage"] = result.Page - 1
		data["NextPage"] = result.Page + 1

		if err := tmplRenderer.Render(w, "page-search", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// JSON API endpoint
	r.Get("/api/search", func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query().Get("q")

		// Check if search is enabled
		if !searchSvc.IsEnabled() {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusServiceUnavailable)
			json.NewEncoder(w).Encode(map[string]string{
				"error": "Search is not enabled - TYPESENSE_API_KEY not configured",
			})
			return
		}

		// Perform search
		result, err := searchSvc.Search(search.SearchOptions{
			Query: query,
		})
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusInternalServerError)
			json.NewEncoder(w).Encode(map[string]string{
				"error": err.Error(),
			})
			return
		}

		// Return JSON response
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(result)
	})

	// Health check
	r.Get("/health", func(w http.ResponseWriter, r *http.Request) {
		state := getState(w)
		if state == nil {
			return
		}
		fmt.Fprintf(w, "OK - %d circulars indexed (Build: %s)\n", state.index.TotalCount, buildString)
	})

	// Start server
	log.Printf("Server starting on %s (base URL: %s)", addr, baseURL)
	log.Printf("Try: http://localhost%s", addr)
	if err := http.ListenAndServe(addr, r); err != nil {
		log.Fatal(err)
	}
}

func getEnv(key, defaultValue string) string {
	if value := os.Getenv(key); value != "" {
		return value
	}
	return defaultValue
}

// getPage extracts page number from query string
func getPage(r *http.Request) int {
	page := 1
	if p := r.URL.Query().Get("page"); p != "" {
		if parsed, err := strconv.Atoi(p); err == nil && parsed > 0 {
			page = parsed
		}
	}
	return page
}
