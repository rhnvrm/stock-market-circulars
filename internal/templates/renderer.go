package templates

import (
	"embed"
	"fmt"
	"html/template"
	"net/http"
	"strings"
	"time"
)

//go:embed *.html
var templateFS embed.FS

// Renderer handles template rendering
type Renderer struct {
	templates *template.Template
}

// NewRenderer creates a new template renderer
func NewRenderer() (*Renderer, error) {
	funcs := template.FuncMap{
		"formatDate": func(t time.Time) string {
			return t.Format("02/01/06")
		},
		"formatDateTime": func(t time.Time) string {
			return t.Format("2006-01-02T15:04:05Z07:00")
		},
		"formatDateLong": func(t time.Time) string {
			return t.Format("January 2, 2006")
		},
		"formatDay": func(t time.Time) string {
			return t.Format("02")
		},
		"formatMonth": func(t time.Time) string {
			return strings.ToUpper(t.Format("Jan"))
		},
		"formatYear": func(t time.Time) string {
			return t.Format("06")
		},
		"upper": strings.ToUpper,
		"lower": strings.ToLower,
		"title": strings.Title,
		"truncate": func(s string, length int) string {
			if len(s) <= length {
				return s
			}
			return s[:length] + "..."
		},
		"slice": func(items []string, start, end int) []string {
			if len(items) == 0 {
				return items
			}
			if start >= len(items) {
				return []string{}
			}
			if end > len(items) {
				end = len(items)
			}
			return items[start:end]
		},
		"safeHTML": func(s string) template.HTML {
			return template.HTML(s)
		},
		"add": func(a, b int) int {
			return a + b
		},
		"sub": func(a, b int) int {
			return a - b
		},
		"gt": func(a, b int) bool {
			return a > b
		},
		"lt": func(a, b int) bool {
			return a < b
		},
		"len": func(items []string) int {
			return len(items)
		},
		"hasSuffix": func(s, suffix string) bool {
			return strings.HasSuffix(s, suffix)
		},
	}

	tmpl, err := template.New("").Funcs(funcs).ParseFS(templateFS, "*.html")
	if err != nil {
		return nil, fmt.Errorf("failed to parse templates: %w", err)
	}

	return &Renderer{
		templates: tmpl,
	}, nil
}

// Render renders a template with the given data
func (r *Renderer) Render(w http.ResponseWriter, name string, data interface{}) error {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")

	if err := r.templates.ExecuteTemplate(w, name, data); err != nil {
		return fmt.Errorf("failed to render template %s: %w", name, err)
	}

	return nil
}
