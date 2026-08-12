# Configuration Files

This directory contains human-editable configuration files for the stock market circulars processing pipeline.

## Files

### `config.toml` 
Complete pipeline configuration including:
- Processing delays and timeouts
- RSS feed URLs for NSE, BSE, SEBI
- Concurrency limits for parallel processing
- Directory structure (content-based state management)
- AI prompts for Gemini analysis (JSON output format)
- Gemini API configuration

## Editing Tips

### Prompts (in config.toml [prompts] section)
- Use clear, specific instructions for Gemini
- Test prompt changes with sample documents
- Keep the YAML frontmatter format consistent
- Include examples for complex requirements

### General Configuration
- **Concurrency**: Adjust `max_concurrent_*` settings based on system resources
- **Delays**: Modify `request_delay` and `gemini_delay` based on API rate limits
- **RSS Feeds**: Add new sources to the `[rss_feeds]` section
- **Directories**: Content stored in `content_dir`, logs in root `combined_pipeline.log`
- **State Management**: No JSON files needed - all state in markdown frontmatter

## Environment Variables

Settings can be overridden with environment variables (useful for CI/CD):
- `GEMINI_API_KEY` - Your Gemini API key
- `DEBUG` - Enable debug logging (true/false/1/yes)
- `LOG_LEVEL` - Set logging level (DEBUG, INFO, WARN, ERROR)
- `LOG_TO_FILE` - Write logs to file (true/false) - set to false for CI/CD
- `LOG_TO_CONSOLE` - Output logs to console (true/false)
- `REQUEST_DELAY` - Delay between requests in seconds (float)
- `GEMINI_DELAY` - Delay for Gemini API calls in seconds (float)
- `TIMEOUT` - Request timeout in seconds (integer)

**Priority Order**: CLI arguments > Environment variables > Config file > Defaults

## GitHub Actions State Persistence

**The Problem**: GitHub Actions runners do not persist local filesystem state between runs, which would otherwise cause duplicate processing and loss of in-progress markers.

**The Solution**: The workflow commits updated markdown content back to the repository. Each circular file carries its own processing state in YAML frontmatter, so state persists with the content itself instead of separate JSON progress files.

**Current behavior**:
- Processing state lives in each markdown file under the `processing` frontmatter key
- New pipeline runs reuse existing content files to determine prior state
- Historical stage values like `claude_processing` and `claude_failed` are still recognized by reporting scripts
- New pipeline writes provider-neutral stages like `ai_processing` and `ai_failed`
- Log files are not committed

## Retry and Resilience Features

The pipeline preserves failure and progress state in frontmatter so subsequent runs can avoid blindly reprocessing everything and can surface historical failures in stats.

**BSE-Specific Fixes**: Special handling for BSE's attachment system:
- Extract `Noticeid` GUIDs from RSS URLs
- Replace empty `attachedId` parameters with proper GUIDs
- Graceful handling of BSE server-side errors
- Automatic retry when BSE infrastructure recovers

## Testing Changes

After editing configuration files:
1. Run `just deps` to check setup
2. Test with a single source: `uv run scripts/combined_pipeline.py nse`
3. Check logs in `combined_pipeline.log`
4. Review generated content in `hugo-site/content/circulars/`