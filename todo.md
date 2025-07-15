# Stock Market Circulars - TODO List

## High Priority (Current Sprint)

### ✅ Completed
- [x] Set up Nix development environment with .envrc
- [x] Create RSS feed scraper script for NSE/BSE/SEBI circulars

### 🔄 In Progress
- [ ] Implement circular processing with Gemini API for summary extraction
- [ ] Use Claude for tagging and markdown generation

### ⏳ Pending (High Priority)
- [ ] Set up Hugo static site generator with Zerodha design
- [ ] Create markdown templates with frontmatter for circulars

## Medium Priority

- [ ] Implement filtering and tagging system
- [ ] Create Hugo theme with Zerodha design language
- [ ] Set up content taxonomies (source, tags, severity, impact)
- [ ] Implement PDF embedding functionality

## Low Priority

- [ ] Add Alpine.js and DaisyUI for interactivity
- [ ] Add Hugo and dev tools via npm (later migrate to Nix)
- [ ] Create responsive design components
- [ ] Implement search functionality

## Future Enhancements

- [ ] Add cron automation for RSS feeds
- [ ] Email notifications for high-importance circulars
- [ ] API endpoints for external integrations
- [ ] Analytics and usage tracking
- [ ] Performance optimization
- [ ] Mobile app considerations

## Technical Debt

- [ ] Migrate Hugo installation from npm to Nix
- [ ] Add comprehensive error handling
- [ ] Implement logging system
- [ ] Add unit tests for core functions
- [ ] Performance benchmarking
- [ ] Security audit

## Documentation

- [x] Create project specification
- [x] Document RSS data sources and formats
- [ ] Create user guide for running the system
- [ ] Document AI processing pipeline
- [ ] Create deployment guide
- [ ] API documentation (future)

## Current Questions/Blockers

1. Should we implement rate limiting for RSS feed requests?
2. What's the preferred Hugo theme structure for custom Zerodha design?
3. How should we handle circular updates vs new versions?
4. What's the ideal taxonomy structure for filtering?

---

**Last Updated**: 2025-07-15
**Current Sprint Goal**: Complete core AI processing pipeline and basic Hugo site setup