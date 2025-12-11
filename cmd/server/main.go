package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/handlers"
	"github.com/rhnvrm/stock-market-circulars/internal/models"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
	"github.com/rhnvrm/stock-market-circulars/internal/search"
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

		w.Header().Set("Content-Type", "text/html")
		fmt.Fprintf(w, `<!DOCTYPE html>
<html>
<head>
    <title>Stock Market Circulars</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <h1>Stock Market Circulars</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/circulars/nse/">NSE</a>
            <a href="/circulars/bse/">BSE</a>
            <a href="/circulars/sebi/">SEBI</a>
        </nav>
    </header>
    <main>
        <h2>Recent Circulars (%d total)</h2>
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Source</th>
                    <th>Title</th>
                    <th>Category</th>
                </tr>
            </thead>
            <tbody>`, result.Total)

		for _, c := range result.Items {
			fmt.Fprintf(w, `
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td><a href="/circulars/%s/%d/%s/">%s</a></td>
                    <td>%s</td>
                </tr>`,
				c.Date.Time.Format("2006-01-02"),
				c.Source,
				c.Source, c.Year, c.Slug,
				c.Title,
				c.Category,
			)
		}

		fmt.Fprintf(w, `
            </tbody>
        </table>
        <p>Page %d of %d</p>
    </main>
</body>
</html>`, result.Page, result.TotalPages)
	})

	r.Get("/circulars/{source}/", func(w http.ResponseWriter, r *http.Request) {
		source := chi.URLParam(r, "source")
		result := idx.Query(content.QueryOptions{
			Source:   source,
			Page:     1,
			PageSize: 50,
		})

		w.Header().Set("Content-Type", "text/html")
		fmt.Fprintf(w, `<!DOCTYPE html>
<html>
<head>
    <title>%s Circulars</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <h1>%s Circulars (%d)</h1>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>`, source, source, result.Total)

		for _, c := range result.Items {
			fmt.Fprintf(w, `
        <tr>
            <td>%s</td>
            <td><a href="/circulars/%s/%d/%s/">%s</a></td>
        </tr>`,
				c.Date.Time.Format("2006-01-02"),
				c.Source, c.Year, c.Slug,
				c.Title,
			)
		}

		fmt.Fprint(w, `
        </tbody>
    </table>
</body>
</html>`)
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

		// Render markdown
		circular.HTMLContent = markdown.Render(circular.RawContent)

		w.Header().Set("Content-Type", "text/html")
		fmt.Fprintf(w, `<!DOCTYPE html>
<html>
<head>
    <title>%s</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <article>
        <h1>%s</h1>
        <p><strong>Source:</strong> %s | <strong>Date:</strong> %s</p>
        <p><strong>Category:</strong> %s | <strong>Impact:</strong> %s</p>

        <h2>Description</h2>
        <p>%s</p>

        <h2>Content</h2>
        %s

        <p><a href="%s" target="_blank">View PDF</a></p>
    </article>
</body>
</html>`,
			circular.Title,
			circular.Title,
			circular.Source,
			circular.Date.Time.Format("January 2, 2006"),
			circular.Category,
			circular.Impact,
			circular.Description,
			circular.HTMLContent,
			circular.PDFURL,
		)
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

		// Show search form if no query
		if query == "" {
			w.Header().Set("Content-Type", "text/html")
			fmt.Fprint(w, `<!DOCTYPE html>
<html>
<head>
    <title>Search Circulars</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <h1>Search Stock Market Circulars</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/circulars/nse/">NSE</a>
            <a href="/circulars/bse/">BSE</a>
            <a href="/circulars/sebi/">SEBI</a>
        </nav>
    </header>
    <main>
        <form method="get" action="/search">
            <input type="text" name="q" placeholder="Search circulars..." size="50">
            <button type="submit">Search</button>
        </form>
    </main>
</body>
</html>`)
			return
		}

		// Check if search is enabled
		if !searchSvc.IsEnabled() {
			w.Header().Set("Content-Type", "text/html")
			fmt.Fprint(w, `<!DOCTYPE html>
<html>
<head>
    <title>Search Unavailable</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <h1>Search Unavailable</h1>
    <p>Search functionality is not configured. Please set TYPESENSE_API_KEY environment variable.</p>
    <p><a href="/">Return to home</a></p>
</body>
</html>`)
			return
		}

		// Perform search
		result, err := searchSvc.Search(search.SearchOptions{
			Query:   query,
			Page:    1,
			PerPage: 20,
		})
		if err != nil {
			http.Error(w, "Search error: "+err.Error(), 500)
			return
		}

		// Render results
		w.Header().Set("Content-Type", "text/html")
		fmt.Fprintf(w, `<!DOCTYPE html>
<html>
<head>
    <title>Search Results: %s</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <h1>Search Results</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/search">New Search</a>
        </nav>
    </header>
    <main>
        <h2>Results for: %s</h2>
        <p>Found %d results</p>
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Source</th>
                    <th>Title</th>
                    <th>Category</th>
                </tr>
            </thead>
            <tbody>`, query, query, result.Total)

		for _, item := range result.Items {
			fmt.Fprintf(w, `
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td><a href="%s">%s</a></td>
                    <td>%s</td>
                </tr>`,
				item.Date,
				item.Source,
				item.URL,
				item.Title,
				item.Category,
			)
		}

		fmt.Fprintf(w, `
            </tbody>
        </table>
        <p>Page %d of %d</p>
    </main>
</body>
</html>`, result.Page, result.TotalPages)
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
