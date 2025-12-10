package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
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
