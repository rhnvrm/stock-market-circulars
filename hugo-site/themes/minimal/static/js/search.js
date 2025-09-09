// Typesense Search Integration
// This script provides search functionality for the stock market circulars site

class TypesenseSearch {
    constructor(config = {}) {
        this.config = {
            host: config.host || '127.0.0.1',
            port: config.port || 8108,
            protocol: config.protocol || 'http',
            apiKey: config.apiKey || 'xyz',
            collectionName: config.collectionName || 'circulars',
            ...config
        };
        
        this.client = null;
        this.searchParams = {
            q: '',
            query_by: 'title,description,content,tags,stocks',
            filter_by: '',
            facet_by: 'source,category,impact,severity,tags,stocks',
            sort_by: 'timestamp:desc',
            per_page: 20,
            page: 1
        };
        
        this.init();
    }
    
    init() {
        // Initialize Typesense client
        if (typeof Typesense !== 'undefined') {
            this.client = new Typesense.Client({
                nodes: [{
                    host: this.config.host,
                    port: this.config.port,
                    protocol: this.config.protocol
                }],
                apiKey: this.config.apiKey,
                connectionTimeoutSeconds: 2
            });
        }
    }
    
    async search(query, filters = {}) {
        if (!this.client) {
            throw new Error('Typesense client not initialized');
        }
        
        const searchParams = {
            ...this.searchParams,
            q: query,
            page: filters.page || 1,
            filter_by: this.buildFilterString(filters)
        };
        
        try {
            const results = await this.client.collections(this.config.collectionName)
                .documents()
                .search(searchParams);
            
            return this.formatResults(results);
        } catch (error) {
            console.error('Search error:', error);
            throw error;
        }
    }
    
    buildFilterString(filters) {
        const filterParts = [];
        
        if (filters.source) {
            filterParts.push(`source:=${filters.source}`);
        }
        
        if (filters.category) {
            filterParts.push(`category:=${filters.category}`);
        }
        
        if (filters.impact) {
            filterParts.push(`impact:=${filters.impact}`);
        }
        
        if (filters.severity) {
            filterParts.push(`severity:=${filters.severity}`);
        }
        
        if (filters.tags && filters.tags.length > 0) {
            filterParts.push(`tags:=[${filters.tags.map(tag => `'${tag}'`).join(',')}]`);
        }
        
        if (filters.stocks && filters.stocks.length > 0) {
            filterParts.push(`stocks:=[${filters.stocks.map(stock => `'${stock}'`).join(',')}]`);
        }
        
        if (filters.dateFrom) {
            filterParts.push(`date:>=${filters.dateFrom}`);
        }
        
        if (filters.dateTo) {
            filterParts.push(`date:<=${filters.dateTo}`);
        }
        
        return filterParts.join(' && ');
    }
    
    formatResults(results) {
        return {
            found: results.found,
            page: results.page,
            per_page: results.per_page,
            total_pages: Math.ceil(results.found / results.per_page),
            items: results.hits.map(hit => ({
                document: hit.document,
                highlights: hit.highlights?.map(h => 
                    h.snippet ? h.snippet.replace(/<mark>/g, '<mark class="search-highlight">') : ''
                ).filter(h => h) || []
            })),
            facets: results.facet_counts?.map(facet => ({
                field: facet.field_name,
                values: facet.counts.map(count => ({
                    value: count.value,
                    count: count.count
                }))
            })) || []
        };
    }
}

// Alpine.js component for search modal
function searchModal() {
    return {
        isOpen: false,
        query: '',
        loading: false,
        results: [],
        facets: [],
        selectedSource: '',
        selectedCategory: '',
        selectedImpact: '',
        selectedFacets: {},
        currentPage: 1,
        hasMoreResults: false,
        showFacets: false,
        searchInstance: null,
        searchTimeout: null,
        searching: false,
        
        init() {
            // Initialize search instance
            this.searchInstance = new TypesenseSearch({
                host: window.TYPESENSE_CONFIG?.host || '127.0.0.1',
                port: window.TYPESENSE_CONFIG?.port || 8108,
                protocol: window.TYPESENSE_CONFIG?.protocol || 'http',
                apiKey: window.TYPESENSE_CONFIG?.apiKey || 'xyz',
                collectionName: window.TYPESENSE_CONFIG?.collectionName || 'circulars'
            });
            
            // Focus input when modal opens
            this.$watch('isOpen', (value) => {
                if (value) {
                    this.$nextTick(() => {
                        this.$refs.searchInput?.focus();
                    });
                }
            });
            
            // Keyboard shortcut (Ctrl/Cmd + K)
            document.addEventListener('keydown', (e) => {
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    this.isOpen = true;
                }
            });
        },
        
        debouncedSearch() {
            clearTimeout(this.searchTimeout);
            this.searching = this.query.trim().length > 0;
            this.searchTimeout = setTimeout(() => {
                this.performSearch();
            }, 300);
        },
        
        async performSearch() {
            if (!this.query.trim()) {
                this.results = [];
                this.facets = [];
                this.loading = false;
                this.searching = false;
                return;
            }
            
            // Only show loading if we don't have existing results to prevent flicker
            const hadResults = this.results.length > 0;
            if (!hadResults) {
                this.loading = true;
            }
            
            this.currentPage = 1;
            
            try {
                const filters = {
                    source: this.selectedSource,
                    category: this.selectedCategory,
                    impact: this.selectedImpact,
                    page: this.currentPage,
                    ...this.selectedFacets
                };
                
                const response = await this.searchInstance.search(this.query, filters);
                
                this.results = response.items;
                this.facets = response.facets;
                this.hasMoreResults = response.page < response.total_pages;
                
            } catch (error) {
                console.error('Search failed:', error);
                // Show error message or fallback
                this.results = [];
                this.facets = [];
            } finally {
                this.loading = false;
                this.searching = false;
            }
        },
        
        async loadMoreResults() {
            if (!this.hasMoreResults) return;
            
            this.loading = true;
            this.currentPage++;
            
            try {
                const filters = {
                    source: this.selectedSource,
                    category: this.selectedCategory,
                    impact: this.selectedImpact,
                    page: this.currentPage,
                    ...this.selectedFacets
                };
                
                const response = await this.searchInstance.search(this.query, filters);
                
                this.results = [...this.results, ...response.items];
                this.hasMoreResults = response.page < response.total_pages;
                
            } catch (error) {
                console.error('Load more results failed:', error);
            } finally {
                this.loading = false;
            }
        },
        
        toggleFacet(field, value) {
            if (!this.selectedFacets[field]) {
                this.selectedFacets[field] = [];
            }
            
            const index = this.selectedFacets[field].indexOf(value);
            if (index > -1) {
                this.selectedFacets[field].splice(index, 1);
                if (this.selectedFacets[field].length === 0) {
                    delete this.selectedFacets[field];
                }
            } else {
                this.selectedFacets[field].push(value);
            }
            
            this.performSearch();
        },
        
        formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            });
        }
    };
}

// Typesense configuration (can be overridden in Hugo config)
window.TYPESENSE_CONFIG = {
    host: '127.0.0.1',
    port: 8108,
    protocol: 'http',
    apiKey: 'xyz',
    collectionName: 'circulars'
};

// Register Alpine component before Alpine initializes
if (typeof Alpine !== 'undefined') {
    // If Alpine is already loaded (shouldn't happen with our script order)
    Alpine.data('searchModal', searchModal);
} else {
    // Wait for Alpine to be available and register component
    document.addEventListener('alpine:init', () => {
        Alpine.data('searchModal', searchModal);
    });
}

// Also make it available globally for compatibility
window.searchModal = searchModal;

// Global function to open search modal from any context
window.openSearchModal = function() {
    // Dispatch the Alpine.js event to open the modal
    window.dispatchEvent(new CustomEvent('open-search'));
};