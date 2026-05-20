package render

import (
	"bytes"

	"github.com/yuin/goldmark"
	"github.com/yuin/goldmark/extension"
	"github.com/yuin/goldmark/renderer/html"
)

// Markdown handles markdown to HTML conversion
type Markdown struct {
	md goldmark.Markdown
}

// NewMarkdown creates a new markdown renderer
func NewMarkdown() *Markdown {
	md := goldmark.New(
		goldmark.WithExtensions(
			extension.GFM,        // GitHub Flavored Markdown
			extension.Typographer, // Smart quotes
		),
		goldmark.WithRendererOptions(
			html.WithUnsafe(), // Allow raw HTML in markdown
		),
	)

	return &Markdown{md: md}
}

// Render converts markdown to HTML
func (m *Markdown) Render(source string) string {
	var buf bytes.Buffer
	if err := m.md.Convert([]byte(source), &buf); err != nil {
		return "<p>Error rendering content</p>"
	}
	return buf.String()
}
