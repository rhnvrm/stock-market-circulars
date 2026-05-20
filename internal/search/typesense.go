package search

import (
	"context"
	"fmt"
	"log"
	"strings"

	"github.com/rhnvrm/stock-market-circulars/internal/models"
	"github.com/typesense/typesense-go/typesense"
	"github.com/typesense/typesense-go/typesense/api"
	"github.com/typesense/typesense-go/typesense/api/pointer"
)

// Service handles Typesense search operations
type Service struct {
	client     *typesense.Client
	collection string
	enabled    bool
}

// NewService creates a new Typesense search service
func NewService(host, apiKey, collection string) *Service {
	// Check if Typesense is configured
	if apiKey == "" {
		return &Service{enabled: false}
	}

	// Ensure host has protocol
	if host != "" && !strings.HasPrefix(host, "http://") && !strings.HasPrefix(host, "https://") {
		host = "http://" + host
	}

	client := typesense.NewClient(
		typesense.WithServer(host),
		typesense.WithAPIKey(apiKey),
	)

	return &Service{
		client:     client,
		collection: collection,
		enabled:    true,
	}
}

// SearchOptions configures a search query
type SearchOptions struct {
	Query   string
	Source  string // Filter by source: nse, bse, sebi
	Page    int
	PerPage int
}

// SearchResult contains search results
type SearchResult struct {
	Items      []SearchItem `json:"items"`
	Total      int          `json:"total"`
	Page       int          `json:"page"`
	TotalPages int          `json:"total_pages"`
}

// SearchItem represents a single search result
type SearchItem struct {
	CircularID  string            `json:"circular_id"`
	Title       string            `json:"title"`
	Description string            `json:"description"`
	Date        string            `json:"date"`
	Source      string            `json:"source"`
	Category    string            `json:"category"`
	URL         string            `json:"url"`
	Highlights  map[string]string `json:"highlights,omitempty"`
}

// Search performs a search query against Typesense
func (s *Service) Search(opts SearchOptions) (*SearchResult, error) {
	if !s.enabled {
		return nil, fmt.Errorf("search is not enabled - TYPESENSE_API_KEY not configured")
	}

	// Set defaults
	if opts.PerPage == 0 {
		opts.PerPage = 20
	}
	if opts.Page == 0 {
		opts.Page = 1
	}

	// Build search parameters
	params := &api.SearchCollectionParams{
		Q:        opts.Query,
		QueryBy:  "title,description,content",
		Page:     pointer.Int(opts.Page),
		PerPage:  pointer.Int(opts.PerPage),
		SortBy:   pointer.String("date:desc"),
	}

	// Add source filter if specified
	if opts.Source != "" {
		params.FilterBy = pointer.String("source:=" + opts.Source)
	}

	// Execute search
	ctx := context.Background()
	result, err := s.client.Collection(s.collection).Documents().Search(ctx, params)
	if err != nil {
		return nil, fmt.Errorf("search failed: %w", err)
	}

	// Parse results
	searchResult := &SearchResult{
		Total: *result.Found,
		Page:  opts.Page,
		Items: []SearchItem{},
	}

	// Convert Typesense hits to our format
	if result.Hits != nil {
		for _, hit := range *result.Hits {
			if hit.Document == nil {
				continue
			}

			doc := hit.Document
			item := SearchItem{
				CircularID:  getString(doc, "circular_id"),
				Title:       getString(doc, "title"),
				Description: getString(doc, "description"),
				Date:        getString(doc, "date"),
				Source:      getString(doc, "source"),
				Category:    getString(doc, "category"),
				URL:         getString(doc, "url"),
				Highlights:  getHighlights(&hit),
			}
			searchResult.Items = append(searchResult.Items, item)
		}
	}

	// Calculate total pages
	searchResult.TotalPages = (searchResult.Total + opts.PerPage - 1) / opts.PerPage

	return searchResult, nil
}

// IsEnabled returns whether search is configured and enabled
func (s *Service) IsEnabled() bool {
	return s.enabled
}

// getString safely extracts a string value from a document
func getString(doc *map[string]interface{}, key string) string {
	if val, ok := (*doc)[key]; ok {
		if str, ok := val.(string); ok {
			return str
		}
	}
	return ""
}

// getHighlights extracts search highlights from a hit
func getHighlights(hit *api.SearchResultHit) map[string]string {
	highlights := make(map[string]string)
	if hit.Highlights != nil {
		for _, h := range *hit.Highlights {
			if h.Field != nil && h.Snippet != nil {
				highlights[*h.Field] = *h.Snippet
			}
		}
	}
	return highlights
}

// GetSchema returns the Typesense collection schema for circulars
func (s *Service) GetSchema() *api.CollectionSchema {
	return &api.CollectionSchema{
		Name: s.collection,
		Fields: []api.Field{
			{
				Name: "circular_id",
				Type: "string",
			},
			{
				Name: "title",
				Type: "string",
			},
			{
				Name: "description",
				Type: "string",
			},
			{
				Name: "content",
				Type: "string",
			},
			{
				Name: "date",
				Type: "int64",
			},
			{
				Name: "source",
				Type: "string",
				Facet: pointer.True(),
			},
			{
				Name: "category",
				Type: "string",
				Facet: pointer.True(),
			},
			{
				Name: "impact",
				Type: "string",
				Facet: pointer.True(),
				Optional: pointer.True(),
			},
			{
				Name: "severity",
				Type: "string",
				Facet: pointer.True(),
				Optional: pointer.True(),
			},
			{
				Name: "tags",
				Type: "string[]",
				Facet: pointer.True(),
				Optional: pointer.True(),
			},
			{
				Name: "stocks",
				Type: "string[]",
				Facet: pointer.True(),
				Optional: pointer.True(),
			},
			{
				Name: "url",
				Type: "string",
			},
		},
		DefaultSortingField: pointer.String("date"),
	}
}

// EnsureCollection ensures the collection exists, creating it if necessary
func (s *Service) EnsureCollection() error {
	if !s.enabled {
		return nil // Not an error, just disabled
	}

	ctx := context.Background()

	// Check if collection exists
	_, err := s.client.Collection(s.collection).Retrieve(ctx)
	if err == nil {
		log.Printf("Typesense collection '%s' already exists", s.collection)
		return nil
	}

	// Collection doesn't exist, create it
	schema := s.GetSchema()
	_, err = s.client.Collections().Create(ctx, schema)
	if err != nil {
		return fmt.Errorf("failed to create collection: %w", err)
	}

	log.Printf("Created Typesense collection '%s' with schema", s.collection)
	return nil
}

// CreateCollection creates the Typesense collection with schema
func (s *Service) CreateCollection() error {
	if !s.enabled {
		return fmt.Errorf("search is not enabled")
	}

	ctx := context.Background()
	schema := s.GetSchema()

	_, err := s.client.Collections().Create(ctx, schema)
	if err != nil {
		return fmt.Errorf("failed to create collection: %w", err)
	}

	log.Printf("Created Typesense collection: %s", s.collection)
	return nil
}

// DeleteCollection deletes the Typesense collection
func (s *Service) DeleteCollection() error {
	if !s.enabled {
		return fmt.Errorf("search is not enabled")
	}

	ctx := context.Background()
	_, err := s.client.Collection(s.collection).Delete(ctx)
	if err != nil {
		return fmt.Errorf("failed to delete collection: %w", err)
	}

	log.Printf("Deleted Typesense collection: %s", s.collection)
	return nil
}

// CircularDocument represents a circular document for indexing
type CircularDocument struct {
	CircularID  string   `json:"circular_id"`
	Title       string   `json:"title"`
	Description string   `json:"description"`
	Content     string   `json:"content"`
	Date        int64    `json:"date"`
	Source      string   `json:"source"`
	Category    string   `json:"category"`
	Impact      string   `json:"impact,omitempty"`
	Severity    string   `json:"severity,omitempty"`
	Tags        []string `json:"tags,omitempty"`
	Stocks      []string `json:"stocks,omitempty"`
	URL         string   `json:"url"`
}

// EnsureIndexed ensures the collection has documents, indexing if empty and auto-index is enabled
func (s *Service) EnsureIndexed(circulars []*models.Circular, baseURL string, autoIndex bool) error {
	if !s.enabled {
		return nil // Not an error, just disabled
	}

	ctx := context.Background()

	// Check document count
	params := &api.SearchCollectionParams{
		Q:       "*",
		PerPage: pointer.Int(0), // Just get count
	}

	result, err := s.client.Collection(s.collection).Documents().Search(ctx, params)
	if err != nil {
		return fmt.Errorf("failed to check document count: %w", err)
	}

	count := 0
	if result.Found != nil {
		count = *result.Found
	}

	if count > 0 {
		log.Printf("Typesense collection '%s' already has %d documents", s.collection, count)
		return nil
	}

	// Collection is empty
	if !autoIndex {
		log.Printf("Typesense collection '%s' is empty but auto-indexing is disabled", s.collection)
		return nil
	}

	// Auto-index
	log.Printf("Auto-indexing %d circulars into Typesense...", len(circulars))
	if err := s.IndexCirculars(circulars, baseURL); err != nil {
		return fmt.Errorf("failed to auto-index: %w", err)
	}

	return nil
}

// IndexCirculars indexes a batch of circulars
func (s *Service) IndexCirculars(circulars []*models.Circular, baseURL string) error {
	if !s.enabled {
		return fmt.Errorf("search is not enabled")
	}

	ctx := context.Background()
	documents := make([]interface{}, 0, len(circulars))

	for _, c := range circulars {
		doc := CircularDocument{
			CircularID:  c.CircularID,
			Title:       c.Title,
			Description: c.Description,
			Content:     c.RawContent,
			Date:        c.PublishedDate.Unix(),
			Source:      c.Source,
			Category:    c.Category,
			Impact:      c.Impact,
			Severity:    c.Severity,
			Tags:        c.Tags,
			Stocks:      c.Stocks,
			URL:         baseURL + c.Permalink(),
		}
		documents = append(documents, doc)
	}

	// Use import API for bulk indexing
	params := &api.ImportDocumentsParams{
		Action:    pointer.String("upsert"),
		BatchSize: pointer.Int(100),
	}

	_, err := s.client.Collection(s.collection).Documents().Import(ctx, documents, params)
	if err != nil {
		return fmt.Errorf("failed to index circulars: %w", err)
	}

	log.Printf("Indexed %d circulars into Typesense", len(circulars))
	return nil
}
