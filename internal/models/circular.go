package models

import (
	"fmt"
	"strings"
	"time"
)

// FlexibleTime handles multiple date formats
type FlexibleTime struct {
	time.Time
}

// UnmarshalYAML handles multiple date formats
func (ft *FlexibleTime) UnmarshalYAML(unmarshal func(interface{}) error) error {
	var s string
	if err := unmarshal(&s); err != nil {
		return err
	}

	// Try different formats
	formats := []string{
		time.RFC3339,
		"2006-01-02T15:04:05Z07:00",
		"2006-01-02T15:04:05.999999",
		"2006-01-02",
		"'2006-01-02'",
	}

	s = strings.Trim(s, "'")

	for _, format := range formats {
		if t, err := time.Parse(format, s); err == nil {
			ft.Time = t
			return nil
		}
	}

	return fmt.Errorf("unable to parse date: %s", s)
}

// Circular represents a stock market circular with frontmatter and content
type Circular struct {
	// Core fields
	CircularID  string `yaml:"circular_id"`
	Title       string `yaml:"title"`
	Description string `yaml:"description"`

	// Dates
	Date          FlexibleTime `yaml:"date"`
	PublishedDate FlexibleTime `yaml:"published_date"`

	// Classification
	Source            string `yaml:"source"` // nse, bse, sebi
	Category          string `yaml:"category"`
	Impact            string `yaml:"impact"`
	Severity          string `yaml:"severity"`
	ImportanceRanking string `yaml:"importance_ranking"`
	Justification     string `yaml:"justification"`

	// Links
	PDFURL string `yaml:"pdf_url"`
	RSSURL string `yaml:"rss_url"`
	GUID   string `yaml:"guid"`

	// Taxonomies
	Tags   []string `yaml:"tags"`
	Stocks []string `yaml:"stocks"`

	// Draft status
	Draft bool `yaml:"draft"`

	// Processing metadata
	Processing ProcessingInfo `yaml:"processing"`

	// Derived fields (not in frontmatter)
	Slug        string
	Year        int
	FilePath    string
	RawContent  string // Markdown body
	HTMLContent string // Rendered HTML (cached)
}

// ProcessingInfo contains pipeline metadata
type ProcessingInfo struct {
	Status           string       `yaml:"status"`
	Stage            string       `yaml:"stage"`
	Attempts         int          `yaml:"attempts"`
	ContentHash      string       `yaml:"content_hash"`
	ProcessedAt      FlexibleTime `yaml:"processed_at"`
	ProcessorVersion string       `yaml:"processor_version"`
}

// CircularSummary is a lightweight version for index/list views
type CircularSummary struct {
	CircularID       string
	Slug             string
	Source           string
	Year             int
	Title            string
	Description      string
	Date             FlexibleTime
	Category         string
	Impact           string
	Severity         string
	Tags             []string
	Stocks           []string
	FilePath         string
	Draft            bool
	ProcessingStatus string
}

// ToSummary converts a Circular to CircularSummary
func (c *Circular) ToSummary() *CircularSummary {
	return &CircularSummary{
		CircularID:       c.CircularID,
		Slug:             c.Slug,
		Source:           c.Source,
		Year:             c.Year,
		Title:            c.Title,
		Description:      c.Description,
		Date:             c.Date,
		Category:         c.Category,
		Impact:           c.Impact,
		Severity:         c.Severity,
		Tags:             c.Tags,
		Stocks:           c.Stocks,
		FilePath:         c.FilePath,
		Draft:            c.Draft,
		ProcessingStatus: c.Processing.Status,
	}
}

// Permalink generates the URL path for this circular
func (c *Circular) Permalink() string {
	return fmt.Sprintf("/circulars/%s/%d/%s/", c.Source, c.Year, c.Slug)
}

// HasContent returns true if the circular has markdown body content
func (c *Circular) HasContent() bool {
	return strings.TrimSpace(c.RawContent) != ""
}

func (c *CircularSummary) Permalink() string {
	return fmt.Sprintf("/circulars/%s/%d/%s/", c.Source, c.Year, c.Slug)
}
