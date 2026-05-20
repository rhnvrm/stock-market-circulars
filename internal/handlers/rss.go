package handlers

import (
	"encoding/xml"
	"net/http"
	"time"

	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
)

// RSS represents the root RSS element with namespaces
type RSS struct {
	XMLName  xml.Name `xml:"rss"`
	Version  string   `xml:"version,attr"`
	Atom     string   `xml:"xmlns:atom,attr"`
	Content  string   `xml:"xmlns:content,attr"`
	Circular string   `xml:"xmlns:circular,attr"`
	Channel  Channel  `xml:"channel"`
}

// Channel contains feed metadata and items
type Channel struct {
	Title         string   `xml:"title"`
	Link          string   `xml:"link"`
	Description   string   `xml:"description"`
	Generator     string   `xml:"generator"`
	Language      string   `xml:"language"`
	LastBuildDate string   `xml:"lastBuildDate"`
	AtomLink      AtomLink `xml:"atom:link"`
	Items         []Item   `xml:"item"`
}

// AtomLink provides self-referencing feed link
type AtomLink struct {
	Href string `xml:"href,attr"`
	Rel  string `xml:"rel,attr"`
	Type string `xml:"type,attr"`
}

// Item represents a single RSS item (circular)
type Item struct {
	Title       string `xml:"title"`
	Link        string `xml:"link"`
	PubDate     string `xml:"pubDate"`
	GUID        string `xml:"guid"`
	Description string `xml:"description"`

	// Custom circular namespace elements
	Source     string `xml:"circular:source,omitempty"`
	Category   string `xml:"circular:category,omitempty"`
	Impact     string `xml:"circular:impact,omitempty"`
	Severity   string `xml:"circular:severity,omitempty"`
	Importance string `xml:"circular:importance,omitempty"`
	ID         string `xml:"circular:id,omitempty"`
	PDFUrl     string `xml:"circular:pdfUrl,omitempty"`

	// Multiple stock elements need special handling
	Stocks []string `xml:"circular:stock,omitempty"`

	// Standard categories for tags
	Categories []string `xml:"category,omitempty"`

	// Full content in CDATA
	ContentEncoded *CDATA `xml:"content:encoded,omitempty"`
}

// CDATA wraps content in CDATA section
type CDATA struct {
	Text string `xml:",cdata"`
}

// FeedOptions configures RSS feed generation
type FeedOptions struct {
	Title       string
	Link        string
	Description string
	SelfLink    string
	BaseURL     string
	Source      string // Filter by source
	Tag         string // Filter by tag
}

// GenerateRSSFeed generates and writes an RSS feed to the response
func GenerateRSSFeed(w http.ResponseWriter, opts FeedOptions, idx *content.SiteIndex, loader *content.Loader, markdown *render.Markdown) {
	// Query circulars based on filter options
	result := idx.Query(content.QueryOptions{
		Source:   opts.Source,
		Tag:      opts.Tag,
		PageSize: 50, // 50 items per feed
	})

	// Build RSS structure
	rss := RSS{
		Version:  "2.0",
		Atom:     "http://www.w3.org/2005/Atom",
		Content:  "http://purl.org/rss/1.0/modules/content/",
		Circular: "https://rhnvrm.github.io/stock-market-circulars/ns",
		Channel: Channel{
			Title:         opts.Title,
			Link:          opts.Link,
			Description:   opts.Description,
			Generator:     "Stock Market Circulars Go Server",
			Language:      "en-us",
			LastBuildDate: time.Now().Format(time.RFC1123Z),
			AtomLink: AtomLink{
				Href: opts.SelfLink,
				Rel:  "self",
				Type: "application/rss+xml",
			},
			Items: []Item{},
		},
	}

	// Build items from query results
	for _, summary := range result.Items {
		// Load full circular to get PDFURL, ImportanceRanking, and content
		circular, err := loader.LoadFull(summary.FilePath)
		if err != nil {
			// Skip items that fail to load
			continue
		}

		// Render markdown to HTML for content:encoded
		htmlContent := ""
		if circular.RawContent != "" {
			htmlContent = markdown.Render(circular.RawContent)
		}

		// Determine pubDate - prefer PublishedDate, fallback to Date
		pubDate := circular.Date
		if !circular.PublishedDate.Time.IsZero() {
			pubDate = circular.PublishedDate
		}

		// Build RSS item
		item := Item{
			Title:       circular.Title,
			Link:        opts.BaseURL + circular.Permalink(),
			PubDate:     pubDate.Time.Format(time.RFC1123Z),
			GUID:        opts.BaseURL + circular.Permalink(),
			Description: circular.Description,
			Source:      circular.Source,
			Category:    circular.Category,
			Impact:      circular.Impact,
			Severity:    circular.Severity,
			Importance:  circular.ImportanceRanking,
			ID:          circular.CircularID,
			PDFUrl:      circular.PDFURL,
			Stocks:      circular.Stocks,
			Categories:  circular.Tags,
		}

		// Add CDATA-wrapped content if available
		if htmlContent != "" {
			item.ContentEncoded = &CDATA{Text: htmlContent}
		}

		rss.Channel.Items = append(rss.Channel.Items, item)
	}

	// Write RSS XML response
	w.Header().Set("Content-Type", "application/rss+xml; charset=utf-8")
	w.Write([]byte(xml.Header))
	enc := xml.NewEncoder(w)
	enc.Indent("", "  ")
	enc.Encode(rss)
}
