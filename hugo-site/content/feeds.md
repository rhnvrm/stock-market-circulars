---
title: "RSS Feeds"
description: "Subscribe to stock market circular updates via RSS"
---

## Available RSS Feeds

Subscribe to these RSS feeds to stay updated on regulatory circulars from NSE, BSE, and SEBI.

### All Circulars

- **[All Circulars Feed]({{< feedurl "/feed.xml" >}})** - All circulars from NSE, BSE, and SEBI

### By Source

- **[NSE Circulars]({{< feedurl "/circulars/nse/feed.xml" >}})** - National Stock Exchange circulars only
- **[BSE Circulars]({{< feedurl "/circulars/bse/feed.xml" >}})** - Bombay Stock Exchange circulars only
- **[SEBI Circulars]({{< feedurl "/circulars/sebi/feed.xml" >}})** - Securities and Exchange Board of India circulars only

### By Tags

Browse all available tags at [/tags/]({{< feedurl "/tags/" >}}) and append `/feed.xml` to any tag URL to get its RSS feed.

Example: `{{< feedurl "/tags/trading/feed.xml" >}}`

### By Stock

Browse all stocks at [/stocks/]({{< feedurl "/stocks/" >}}) and append `/feed.xml` to any stock URL to get its RSS feed.

Example: `{{< feedurl "/stocks/RELIANCE/feed.xml" >}}`

## RSS Feed Features

Each RSS feed item includes:

- **Title** - Full descriptive title of the circular
- **Description** - Brief summary of the circular
- **Publication Date** - Official publication date and time
- **Link** - Direct link to the full circular on this website
- **PDF URL** - Link to the original PDF document
- **Source** - NSE, BSE, or SEBI
- **Category** - trading, compliance, listing, disclosure, etc.
- **Impact Level** - High, medium, or low market impact
- **Severity** - Regulatory severity level
- **Importance Ranking** - Overall importance assessment
- **Affected Stocks** - List of stock tickers mentioned in the circular
- **Tags** - Relevant categorization tags
- **Full Content** - Complete analyzed content including summary, key points, regulatory changes, compliance requirements, important dates, and impact assessment

## Using RSS Feeds

Copy any feed URL above and add it to your favorite RSS reader:

- **Web-based**: Feedly, Inoreader, The Old Reader
- **Desktop**: NetNewsWire (Mac), FeedReader (Windows), Akregator (Linux)
- **Mobile**: Reeder (iOS), Read You (Android)
- **Self-hosted**: FreshRSS, Miniflux, Tiny Tiny RSS

## Custom Namespace

Our RSS feeds use a custom XML namespace `circular:` for enhanced metadata:

```xml
xmlns:circular="https://rhnvrm.github.io/stock-market-circulars/ns"
```

This provides structured access to:
- `circular:source` - Regulatory source
- `circular:category` - Circular category
- `circular:impact` - Market impact level
- `circular:severity` - Regulatory severity
- `circular:importance` - Importance ranking
- `circular:id` - Unique circular identifier
- `circular:pdfUrl` - Original PDF URL
- `circular:stock` - Affected stock tickers (multiple)
