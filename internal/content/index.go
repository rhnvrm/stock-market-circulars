package content

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"sync"
	"time"

	"github.com/rhnvrm/stock-market-circulars/internal/models"
)

// SiteIndex holds all circular indexes for fast querying
type SiteIndex struct {
	mu sync.RWMutex

	All       []*models.CircularSummary            // Sorted by date desc
	BySource  map[string][]*models.CircularSummary // nse, bse, sebi
	ByTag     map[string][]*models.CircularSummary
	ByStock   map[string][]*models.CircularSummary
	ByPath    map[string]string // path key -> circular_id
	ByID      map[string]*models.CircularSummary

	TagCounts   map[string]int
	StockCounts map[string]int

	TotalCount    int
	LastBuildTime time.Duration
}

// Builder constructs the site index
type Builder struct {
	loader     *Loader
	contentDir string
}

// NewBuilder creates a new index builder
func NewBuilder(contentDir string, loader *Loader) *Builder {
	return &Builder{
		contentDir: contentDir,
		loader:     loader,
	}
}

// Build constructs the index by walking all circular files
func (b *Builder) Build() (*SiteIndex, error) {
	start := time.Now()

	idx := &SiteIndex{
		BySource:    make(map[string][]*models.CircularSummary),
		ByTag:       make(map[string][]*models.CircularSummary),
		ByStock:     make(map[string][]*models.CircularSummary),
		ByPath:      make(map[string]string),
		ByID:        make(map[string]*models.CircularSummary),
		TagCounts:   make(map[string]int),
		StockCounts: make(map[string]int),
	}

	circularsDir := filepath.Join(b.contentDir, "circulars")
	sources := []string{"nse", "bse", "sebi"}

	for _, source := range sources {
		sourceDir := filepath.Join(circularsDir, source)
		if _, err := os.Stat(sourceDir); os.IsNotExist(err) {
			log.Printf("Warning: source directory not found: %s", sourceDir)
			continue
		}

		err := filepath.WalkDir(sourceDir, func(path string, d os.DirEntry, err error) error {
			if err != nil {
				return err
			}

			if d.IsDir() || !strings.HasSuffix(d.Name(), ".md") {
				return nil
			}

			// Skip index files
			if d.Name() == "_index.md" {
				return nil
			}

			summary, err := b.loader.LoadSummary(path)
			if err != nil {
				log.Printf("Warning: failed to load %s: %v", path, err)
				return nil // Continue processing other files
			}

			idx.addCircular(summary)
			return nil
		})

		if err != nil {
			return nil, fmt.Errorf("failed to walk %s: %w", sourceDir, err)
		}
	}

	// Sort all lists by date descending
	idx.sortAll()

	// Calculate counts
	idx.TotalCount = len(idx.All)
	idx.LastBuildTime = time.Since(start)

	log.Printf("Index built: %d circulars in %v", idx.TotalCount, idx.LastBuildTime)

	return idx, nil
}

// addCircular adds a circular to all relevant indexes
func (idx *SiteIndex) addCircular(c *models.CircularSummary) {
	idx.mu.Lock()
	defer idx.mu.Unlock()

	idx.All = append(idx.All, c)
	idx.BySource[c.Source] = append(idx.BySource[c.Source], c)
	idx.ByID[c.CircularID] = c

	// Build path lookup: source/year/slug
	pathKey := fmt.Sprintf("%s/%d/%s", c.Source, c.Year, c.Slug)
	idx.ByPath[pathKey] = c.CircularID

	// Taxonomies
	for _, tag := range c.Tags {
		slug := slugify(tag)
		idx.ByTag[slug] = append(idx.ByTag[slug], c)
		idx.TagCounts[slug]++
	}

	for _, stock := range c.Stocks {
		slug := strings.ToLower(stock)
		idx.ByStock[slug] = append(idx.ByStock[slug], c)
		idx.StockCounts[slug]++
	}
}

// sortAll sorts all lists by date descending
func (idx *SiteIndex) sortAll() {
	sortByDate := func(list []*models.CircularSummary) {
		sort.Slice(list, func(i, j int) bool {
			return list[i].Date.Time.After(list[j].Date.Time)
		})
	}

	sortByDate(idx.All)

	for _, list := range idx.BySource {
		sortByDate(list)
	}

	for _, list := range idx.ByTag {
		sortByDate(list)
	}

	for _, list := range idx.ByStock {
		sortByDate(list)
	}
}

// Query options
type QueryOptions struct {
	Page     int
	PageSize int
	Source   string
	Tag      string
	Stock    string
}

// QueryResult holds paginated results
type QueryResult struct {
	Items      []*models.CircularSummary
	Total      int
	Page       int
	PageSize   int
	TotalPages int
	HasPrev    bool
	HasNext    bool
}

// Query performs a filtered and paginated query
func (idx *SiteIndex) Query(opts QueryOptions) *QueryResult {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	if opts.PageSize <= 0 {
		opts.PageSize = 50 // Default
	}
	if opts.Page <= 0 {
		opts.Page = 1
	}

	var items []*models.CircularSummary

	// Select source list
	if opts.Source != "" {
		items = idx.BySource[opts.Source]
	} else if opts.Tag != "" {
		items = idx.ByTag[opts.Tag]
	} else if opts.Stock != "" {
		items = idx.ByStock[opts.Stock]
	} else {
		items = idx.All
	}

	total := len(items)
	totalPages := (total + opts.PageSize - 1) / opts.PageSize

	// Paginate
	start := (opts.Page - 1) * opts.PageSize
	end := start + opts.PageSize
	if start > total {
		start = total
	}
	if end > total {
		end = total
	}

	return &QueryResult{
		Items:      items[start:end],
		Total:      total,
		Page:       opts.Page,
		PageSize:   opts.PageSize,
		TotalPages: totalPages,
		HasPrev:    opts.Page > 1,
		HasNext:    opts.Page < totalPages,
	}
}

// slugify converts a string to URL-friendly slug
func slugify(s string) string {
	s = strings.ToLower(s)
	s = strings.ReplaceAll(s, " ", "-")
	return s
}

// TaxonomyStat holds statistics for a tag or stock
type TaxonomyStat struct {
	Name       string
	Slug       string
	Count      int
	LastUpdate time.Time
}

// GetTagStats returns statistics for all tags
func (idx *SiteIndex) GetTagStats() []TaxonomyStat {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	stats := make([]TaxonomyStat, 0, len(idx.TagCounts))
	for slug, count := range idx.TagCounts {
		var lastUpdate time.Time
		if items, ok := idx.ByTag[slug]; ok && len(items) > 0 {
			lastUpdate = items[0].Date.Time // Items are sorted by date desc
		}
		stats = append(stats, TaxonomyStat{
			Name:       slug, // For tags, slug is the display name
			Slug:       slug,
			Count:      count,
			LastUpdate: lastUpdate,
		})
	}
	return stats
}

// GetStockStats returns statistics for all stocks
func (idx *SiteIndex) GetStockStats() []TaxonomyStat {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	stats := make([]TaxonomyStat, 0, len(idx.StockCounts))
	for slug, count := range idx.StockCounts {
		var lastUpdate time.Time
		if items, ok := idx.ByStock[slug]; ok && len(items) > 0 {
			lastUpdate = items[0].Date.Time // Items are sorted by date desc
		}
		stats = append(stats, TaxonomyStat{
			Name:       strings.ToUpper(slug), // Stocks display as uppercase
			Slug:       slug,
			Count:      count,
			LastUpdate: lastUpdate,
		})
	}
	return stats
}
