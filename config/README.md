# Configuration Files

This directory contains human-editable configuration files for the stock market circulars processing pipeline.

## Files

### `config.toml` 
Complete pipeline configuration including:
- Processing delays and timeouts
- RSS feed URLs  
- File validation settings
- Output formatting options
- Directory structure
- AI prompts for Claude analysis
- Claude API configuration

## Editing Tips

### Prompts (in config.toml [prompts] section)
- Use clear, specific instructions for Claude
- Test prompt changes with sample documents
- Keep the YAML frontmatter format consistent
- Include examples for complex requirements

### General Configuration
- Adjust delays based on API rate limits
- Modify file size limits based on your needs
- Add new RSS feeds to the `[rss_feeds]` section
- Customize category mappings for better tagging

## Environment Variables

Settings can be overridden with environment variables (useful for CI/CD):
- `CLAUDE_API_KEY` - Your Claude API key
- `DEBUG` - Enable debug logging (true/false/1/yes)
- `LOG_LEVEL` - Set logging level (DEBUG, INFO, WARN, ERROR)
- `LOG_TO_FILE` - Write logs to file (true/false) - set to false for CI/CD
- `LOG_TO_CONSOLE` - Output logs to console (true/false)
- `REQUEST_DELAY` - Delay between requests in seconds (float)
- `CLAUDE_DELAY` - Delay for Claude API calls in seconds (float)
- `TIMEOUT` - Request timeout in seconds (integer)

**Priority Order**: CLI arguments > Environment variables > Config file > Defaults

## GitHub Actions State Persistence

**The Problem**: GitHub Actions runners don't persist state between runs, which would cause:
- Duplicate processing of the same circulars
- Loss of progress tracking and error history
- No incremental processing capability

**The Solution**: The workflow automatically commits and pushes essential state files back to the repository:
- `state/combined_progress/*.json` - Individual item progress tracking
- `state/*_combined_seen_guids.txt` - GUID deduplication tracking  
- `state/combined_errors/*.json` - Error tracking for debugging

**Note**: Log files (`*.log`) are NOT committed (to avoid repo bloat). In GitHub Actions, logging is configured to output directly to console (set via `LOG_TO_FILE=false`), making logs available in the workflow output.

**Behavior**:
- ✅ State preserved even if pipeline fails (configurable)
- ✅ Incremental processing - only new circulars processed
- ✅ Resume capability - failed items can be retried up to 3 times
- ✅ Automatic retry logic for temporary failures (BSE server issues, network problems)
- ✅ Attempt counting and progress tracking across pipeline runs
- ✅ Commit messages include processing statistics
- ✅ Hugo site only deployed on successful runs

## Retry and Resilience Features

**3-Attempt Retry System**: The pipeline automatically retries failed items up to 3 times before marking them as permanently failed. This handles:
- Temporary network issues
- Server-side errors (like BSE's 500 responses) 
- Infrastructure outages
- Rate limiting

**State Preservation**: Progress files include attempt counts and error history, allowing the pipeline to:
- Resume processing exactly where it left off
- Track retry attempts across different pipeline runs
- Maintain consistency in ephemeral GitHub Actions environments
- Handle items that may disappear from RSS feeds but still need retry attempts

**BSE-Specific Fixes**: Special handling for BSE's attachment system:
- Extract `Noticeid` GUIDs from RSS URLs
- Replace empty `attachedId` parameters with proper GUIDs
- Graceful handling of BSE server-side errors
- Automatic retry when BSE infrastructure recovers

## Testing Changes

After editing configuration files:
1. Run `just deps` to check setup
2. Test with a single source: `uv run scripts/combined_pipeline.py nse`
3. Check logs in `state/combined_pipeline.log`
4. Review generated content in `hugo-site/content/circulars/`