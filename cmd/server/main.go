package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/handlers"
	"github.com/rhnvrm/stock-market-circulars/internal/models"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
	"github.com/rhnvrm/stock-market-circulars/internal/search"
	"github.com/rhnvrm/stock-market-circulars/internal/templates"
)

func main() {
	// Configuration
	addr := getEnv("ADDR", ":8080")
	contentDir := getEnv("CONTENT_DIR", "./hugo-site/content")
	baseURL := getEnv("BASE_URL", "http://localhost:8080")

	log.Println("Starting Stock Market Circulars Server...")

	// Initialize components
	loader := content.NewLoader(contentDir)
	markdown := render.NewMarkdown()

	// Initialize template renderer
	tmplRenderer, err := templates.NewRenderer()
	if err != nil {
		log.Fatalf("Failed to initialize templates: %v", err)
	}

	// Build index
	log.Println("Building content index...")
	start := time.Now()
	builder := content.NewBuilder(contentDir, loader)
	idx, err := builder.Build()
	if err != nil {
		log.Fatalf("Failed to build index: %v", err)
	}
	log.Printf("Index built: %d circulars in %v", idx.TotalCount, time.Since(start))

	// Initialize Typesense search
	typesenseHost := getEnv("TYPESENSE_HOST", "localhost:8108")
	typesenseKey := getEnv("TYPESENSE_API_KEY", "")
	typesenseCollection := getEnv("TYPESENSE_COLLECTION", "circulars")
	typesenseAutoIndex := getEnv("TYPESENSE_AUTO_INDEX", "true") == "true"

	searchSvc := search.NewService(typesenseHost, typesenseKey, typesenseCollection)
	if searchSvc.IsEnabled() {
		log.Println("Typesense search enabled")

		// Ensure collection exists
		if err := searchSvc.EnsureCollection(); err != nil {
			log.Printf("Warning: Failed to ensure Typesense collection: %v", err)
		}

		// Auto-index if enabled
		if typesenseAutoIndex {
			log.Println("Auto-indexing enabled, loading circulars...")
			allCirculars := idx.Query(content.QueryOptions{PageSize: idx.TotalCount})

			// Load full content for indexing
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

	// Static files
	r.Handle("/css/*", http.StripPrefix("/css/", http.FileServer(http.Dir("./static/css"))))

	// Routes - Minimal MVP
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		result := idx.Query(content.QueryOptions{Page: 1, PageSize: 50})

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
			},
		}

		if err := tmplRenderer.Render(w, "page-home", data); err != nil {
			log.Printf("Error rendering template: %v", err)
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		}
	})

	r.Get("/circulars/{source}/", func(w http.ResponseWriter, r *http.Request) {
		source := chi.URLParam(r, "source")
		result := idx.Query(content.QueryOptions{
			Source:   source,
			Page:     1,
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
			},
		}

		if err := tmplRenderer.Render(w, "page-source", data); err != nil {
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
			"Path":     circular.Permalink,
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

		data := map[string]interface{}{
			"Title":   "Search Circulars",
			"BaseURL": baseURL,
			"Path":    "/search",
			"Query":   query,
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
			Page:    1,
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
		fmt.Fprintf(w, "OK - %d circulars indexed\n", idx.TotalCount)
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
