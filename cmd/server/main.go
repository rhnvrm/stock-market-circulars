package main

import (
	"encoding/json"
	"fmt"
	"io/fs"
	"log"
	"net/http"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/gitsync"
	"github.com/rhnvrm/stock-market-circulars/internal/handlers"
	"github.com/rhnvrm/stock-market-circulars/internal/models"
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

	searchSvc := search.NewService(typesenseHost, typesenseKey, typesenseCollection)

	// Index lock for thread-safe access during sync
	var indexLock sync.RWMutex
	var idx *content.SiteIndex
	var loader *content.Loader

	// Function to rebuild index and re-index Typesense
	rebuildIndex := func(contentPath string) {
		log.Println("Rebuilding content index...")
		start := time.Now()

		newLoader := content.NewLoader(contentPath)
		builder := content.NewBuilder(contentPath, newLoader)
		newIdx, err := builder.Build()
		if err != nil {
			log.Printf("Error rebuilding index: %v", err)
			return
		}

		// Atomic swap
		indexLock.Lock()
		idx = newIdx
		loader = newLoader
		indexLock.Unlock()

		log.Printf("Index rebuilt: %d circulars in %v", newIdx.TotalCount, time.Since(start))

		// Re-index Typesense if enabled
		if searchSvc.IsEnabled() && typesenseAutoIndex {
			log.Println("Re-indexing Typesense...")
			indexLock.RLock()
			allCirculars := idx.Query(content.QueryOptions{PageSize: idx.TotalCount})
			circulars := make([]*models.Circular, 0, len(allCirculars.Items))
			for _, summary := range allCirculars.Items {
				circular, err := loader.LoadFull(summary.FilePath)
				if err != nil {
					continue
				}
				circulars = append(circulars, circular)
			}
			indexLock.RUnlock()

			if err := searchSvc.EnsureIndexed(circulars, baseURL, true); err != nil {
				log.Printf("Warning: Failed to re-index Typesense: %v", err)
			} else {
				log.Println("Typesense re-indexing completed")
			}
		}
	}

	// Initialize git sync if configured
	var gitSync *gitsync.SyncManager
	var sched *scheduler.Scheduler

	if gitRepoURL != "" {
		log.Printf("Git sync mode enabled: %s -> %s", gitRepoURL, gitDataPath)

		gitSync = gitsync.NewSyncManager(gitRepoURL, gitDataPath, func() {
			rebuildIndex(gitSync.ContentPath())
		})
		gitSync.SetBranch(gitBranch)

		// Clone repository on startup
		if err := gitSync.Clone(); err != nil {
			log.Fatalf("Failed to clone git repository: %v", err)
		}

		// Use git-synced content path
		contentDir = gitSync.ContentPath()

		// Start scheduler for periodic sync
		sched = scheduler.New()
		if err := sched.AddSyncJob(syncInterval, func() {
			if err := gitSync.Pull(); err != nil {
				log.Printf("Scheduled sync error: %v", err)
			}
		}); err != nil {
			log.Printf("Warning: Failed to add sync job: %v", err)
		}
		sched.Start()
		defer sched.Stop()
	}

	// Initial index build
	loader = content.NewLoader(contentDir)
	log.Println("Building initial content index...")
	start := time.Now()
	builder := content.NewBuilder(contentDir, loader)
	idx, err = builder.Build()
	if err != nil {
		log.Fatalf("Failed to build index: %v", err)
	}
	log.Printf("Index built: %d circulars in %v", idx.TotalCount, time.Since(start))

	// Initialize Typesense search
	if searchSvc.IsEnabled() {
		log.Println("Typesense search enabled")

		if err := searchSvc.EnsureCollection(); err != nil {
			log.Printf("Warning: Failed to ensure Typesense collection: %v", err)
		}

		if typesenseAutoIndex {
			log.Println("Auto-indexing enabled, loading circulars...")
			allCirculars := idx.Query(content.QueryOptions{PageSize: idx.TotalCount})

			circulars := make([]*models.Circular, 0, len(allCirculars.Items))
			for _, summary := range allCirculars.Items {
				circular, err := loader.LoadFull(summary.FilePath)
				if err != nil {
					log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
					continue
				}
				circulars = append(circulars, circular)
			}

			if err := searchSvc.EnsureIndexed(circulars, baseURL, typesenseAutoIndex); err != nil {
				log.Printf("Warning: Failed to ensure indexing: %v", err)
			}
		}
	} else {
		log.Println("Typesense search disabled (TYPESENSE_API_KEY not set)")
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
		page := getPage(r)
		result := idx.Query(content.QueryOptions{Page: page, PageSize: 50})

		// Load full circulars for template
		circulars := make([]*models.Circular, 0, len(result.Items))
		for _, summary := range result.Items {
			circular, err := loader.LoadFull(summary.FilePath)
			if err != nil {
				log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
				continue
			}
			circulars = append(circulars, circular)
		}

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
		page := getPage(r)
		result := idx.Query(content.QueryOptions{
			Page:     page,
			PageSize: 50,
		})

		// Load full circulars for template
		circulars := make([]*models.Circular, 0, len(result.Items))
		for _, summary := range result.Items {
			circular, err := loader.LoadFull(summary.FilePath)
			if err != nil {
				log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
				continue
			}
			circulars = append(circulars, circular)
		}

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
		source := chi.URLParam(r, "source")
		page := getPage(r)
		result := idx.Query(content.QueryOptions{
			Source:   source,
			Page:     page,
			PageSize: 50,
		})

		// Load full circulars for template
		circulars := make([]*models.Circular, 0, len(result.Items))
		for _, summary := range result.Items {
			circular, err := loader.LoadFull(summary.FilePath)
			if err != nil {
				log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
				continue
			}
			circulars = append(circulars, circular)
		}

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
		stats := idx.GetTagStats()

		// Sort by count for top by count
		topByCount := make([]content.TaxonomyStat, len(stats))
		copy(topByCount, stats)
		sort.Slice(topByCount, func(i, j int) bool {
			return topByCount[i].Count > topByCount[j].Count
		})
		if len(topByCount) > 20 {
			topByCount = topByCount[:20]
		}

		// Sort by recent activity
		topByRecent := make([]content.TaxonomyStat, len(stats))
		copy(topByRecent, stats)
		sort.Slice(topByRecent, func(i, j int) bool {
			return topByRecent[i].LastUpdate.After(topByRecent[j].LastUpdate)
		})
		if len(topByRecent) > 20 {
			topByRecent = topByRecent[:20]
		}

		// Sort alphabetically for all items
		allItems := make([]content.TaxonomyStat, len(stats))
		copy(allItems, stats)
		sort.Slice(allItems, func(i, j int) bool {
			return allItems[i].Name < allItems[j].Name
		})

		data := map[string]interface{}{
			"Title":       "Tags",
			"Description": "Browse all tags for stock market circulars",
			"BaseURL":     baseURL,
			"Path":        "/tags/",
			"BasePath":    "/tags/",
			"IsStocks":    false,
			"TotalCount":  len(stats),
			"TopByCount":  topByCount,
			"TopByRecent": topByRecent,
			"AllItems":    allItems,
		}

		if err := tmplRenderer.Render(w, "page-terms", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Tag-specific page
	r.Get("/tags/{tag}/", func(w http.ResponseWriter, r *http.Request) {
		tag := chi.URLParam(r, "tag")
		page := getPage(r)
		result := idx.Query(content.QueryOptions{
			Tag:      tag,
			Page:     page,
			PageSize: 50,
		})

		if result.Total == 0 {
			http.NotFound(w, r)
			return
		}

		// Load full circulars for template
		circulars := make([]*models.Circular, 0, len(result.Items))
		for _, summary := range result.Items {
			circular, err := loader.LoadFull(summary.FilePath)
			if err != nil {
				log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
				continue
			}
			circulars = append(circulars, circular)
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
		stats := idx.GetStockStats()

		// Sort by count for top by count
		topByCount := make([]content.TaxonomyStat, len(stats))
		copy(topByCount, stats)
		sort.Slice(topByCount, func(i, j int) bool {
			return topByCount[i].Count > topByCount[j].Count
		})
		if len(topByCount) > 20 {
			topByCount = topByCount[:20]
		}

		// Sort by recent activity
		topByRecent := make([]content.TaxonomyStat, len(stats))
		copy(topByRecent, stats)
		sort.Slice(topByRecent, func(i, j int) bool {
			return topByRecent[i].LastUpdate.After(topByRecent[j].LastUpdate)
		})
		if len(topByRecent) > 20 {
			topByRecent = topByRecent[:20]
		}

		// Sort alphabetically for all items
		allItems := make([]content.TaxonomyStat, len(stats))
		copy(allItems, stats)
		sort.Slice(allItems, func(i, j int) bool {
			return allItems[i].Name < allItems[j].Name
		})

		data := map[string]interface{}{
			"Title":       "Stocks",
			"Description": "Browse circulars by stock symbol",
			"BaseURL":     baseURL,
			"Path":        "/stocks/",
			"BasePath":    "/stocks/",
			"IsStocks":    true,
			"TotalCount":  len(stats),
			"TopByCount":  topByCount,
			"TopByRecent": topByRecent,
			"AllItems":    allItems,
		}

		if err := tmplRenderer.Render(w, "page-terms", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	// Stock-specific page
	r.Get("/stocks/{stock}/", func(w http.ResponseWriter, r *http.Request) {
		stock := strings.ToLower(chi.URLParam(r, "stock"))
		page := getPage(r)
		result := idx.Query(content.QueryOptions{
			Stock:    stock,
			Page:     page,
			PageSize: 50,
		})

		if result.Total == 0 {
			http.NotFound(w, r)
			return
		}

		// Load full circulars for template
		circulars := make([]*models.Circular, 0, len(result.Items))
		for _, summary := range result.Items {
			circular, err := loader.LoadFull(summary.FilePath)
			if err != nil {
				log.Printf("Warning: Failed to load circular %s: %v", summary.CircularID, err)
				continue
			}
			circulars = append(circulars, circular)
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
		source := chi.URLParam(r, "source")
		year := chi.URLParam(r, "year")
		slug := chi.URLParam(r, "slug")

		pathKey := fmt.Sprintf("%s/%s/%s", source, year, slug)
		circularID, ok := idx.ByPath[pathKey]
		if !ok {
			http.NotFound(w, r)
			return
		}

		summary := idx.ByID[circularID]
		if summary == nil {
			http.NotFound(w, r)
			return
		}

		// Load full content
		circular, err := loader.LoadFull(summary.FilePath)
		if err != nil {
			http.Error(w, "Error loading circular", 500)
			return
		}

		// Render markdown to HTML
		circular.HTMLContent = markdown.Render(circular.RawContent)

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
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "Stock Market Circulars",
			Link:        baseURL,
			Description: "Latest stock market circulars from NSE, BSE, and SEBI",
			SelfLink:    baseURL + "/feed.xml",
			BaseURL:     baseURL,
		}, idx, loader, markdown)
	})

	// All circulars feed
	r.Get("/circulars/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "All Stock Market Circulars",
			Link:        baseURL + "/circulars/",
			Description: "All circulars from NSE, BSE, and SEBI",
			SelfLink:    baseURL + "/circulars/feed.xml",
			BaseURL:     baseURL,
		}, idx, loader, markdown)
	})

	// Source-specific RSS feeds
	r.Get("/circulars/{source}/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		source := chi.URLParam(r, "source")
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       fmt.Sprintf("%s Circulars", source),
			Link:        baseURL + "/circulars/" + source + "/",
			Description: fmt.Sprintf("Latest circulars from %s", source),
			SelfLink:    baseURL + "/circulars/" + source + "/feed.xml",
			BaseURL:     baseURL,
			Source:      source,
		}, idx, loader, markdown)
	})

	// Tag-specific RSS feeds
	r.Get("/tags/{tag}/feed.xml", func(w http.ResponseWriter, r *http.Request) {
		tag := chi.URLParam(r, "tag")
		handlers.GenerateRSSFeed(w, handlers.FeedOptions{
			Title:       "Circulars tagged: " + tag,
			Link:        baseURL + "/tags/" + tag + "/",
			Description: fmt.Sprintf("Stock market circulars tagged with %s", tag),
			SelfLink:    baseURL + "/tags/" + tag + "/feed.xml",
			BaseURL:     baseURL,
			Tag:         tag,
		}, idx, loader, markdown)
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
			w.WriteHeader(503)
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
			w.WriteHeader(500)
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
		indexLock.RLock()
		count := idx.TotalCount
		indexLock.RUnlock()
		fmt.Fprintf(w, "OK - %d circulars indexed (Build: %s)\n", count, buildString)
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
