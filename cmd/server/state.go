package main

import (
	"log"
	"sort"

	"github.com/rhnvrm/stock-market-circulars/internal/content"
	"github.com/rhnvrm/stock-market-circulars/internal/models"
	"github.com/rhnvrm/stock-market-circulars/internal/render"
)

type taxonomyView struct {
	TotalCount  int
	TopByCount  []content.TaxonomyStat
	TopByRecent []content.TaxonomyStat
	AllItems    []content.TaxonomyStat
}

type appState struct {
	index        *content.SiteIndex
	circularByID map[string]*models.Circular
	allCirculars []*models.Circular
	tags         taxonomyView
	stocks       taxonomyView
}

func buildAppState(contentPath string, markdown *render.Markdown) (*appState, error) {
	loader := content.NewLoader(contentPath)
	builder := content.NewBuilder(contentPath, loader)
	idx, err := builder.Build()
	if err != nil {
		return nil, err
	}

	result := idx.Query(content.QueryOptions{PageSize: idx.TotalCount})
	circularByID := make(map[string]*models.Circular, len(result.Items))
	allCirculars := make([]*models.Circular, 0, len(result.Items))

	for _, summary := range result.Items {
		circular, err := loader.LoadFull(summary.FilePath)
		if err != nil {
			log.Printf("Warning: Failed to load circular %s into app state: %v", summary.CircularID, err)
			continue
		}
		if circular.RawContent != "" {
			circular.HTMLContent = markdown.Render(circular.RawContent)
		}
		circularByID[circular.CircularID] = circular
		allCirculars = append(allCirculars, circular)
	}

	return &appState{
		index:        idx,
		circularByID: circularByID,
		allCirculars: allCirculars,
		tags:         buildTaxonomyView(idx.GetTagStats()),
		stocks:       buildTaxonomyView(idx.GetStockStats()),
	}, nil
}

func (s *appState) queryCirculars(opts content.QueryOptions) (*content.QueryResult, []*models.Circular) {
	result := s.index.Query(opts)
	circulars := make([]*models.Circular, 0, len(result.Items))
	for _, summary := range result.Items {
		circular, ok := s.circularByID[summary.CircularID]
		if !ok {
			continue
		}
		circulars = append(circulars, circular)
	}
	return result, circulars
}

func buildTaxonomyView(stats []content.TaxonomyStat) taxonomyView {
	topByCount := make([]content.TaxonomyStat, len(stats))
	copy(topByCount, stats)
	sort.Slice(topByCount, func(i, j int) bool {
		return topByCount[i].Count > topByCount[j].Count
	})
	if len(topByCount) > 20 {
		topByCount = topByCount[:20]
	}

	topByRecent := make([]content.TaxonomyStat, len(stats))
	copy(topByRecent, stats)
	sort.Slice(topByRecent, func(i, j int) bool {
		return topByRecent[i].LastUpdate.After(topByRecent[j].LastUpdate)
	})
	if len(topByRecent) > 20 {
		topByRecent = topByRecent[:20]
	}

	allItems := make([]content.TaxonomyStat, len(stats))
	copy(allItems, stats)
	sort.Slice(allItems, func(i, j int) bool {
		return allItems[i].Count > allItems[j].Count
	})

	return taxonomyView{
		TotalCount:  len(stats),
		TopByCount:  topByCount,
		TopByRecent: topByRecent,
		AllItems:    allItems,
	}
}
