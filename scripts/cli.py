"""Command-line interface for the stock market circulars pipeline."""

import asyncio
import subprocess
import time
from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from config import load_config
from pipeline import CircularsPipeline

app = typer.Typer()
console = Console()


@app.command()
def main(
    sources: List[str] = typer.Argument(None, help="Sources to process (nse, bse, sebi)"),
    max_items: Optional[int] = typer.Option(None, "--max-items", help="Maximum items per source"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
    request_delay: Optional[int] = typer.Option(None, "--request-delay", help="Delay between requests (overrides config)"),
    gemini_delay: int = typer.Option(None, "--gemini-delay", help="Delay for Gemini API calls (overrides config)"),
):
    """Process RSS feeds and generate markdown content using AI."""
    
    # Load configuration with overrides
    config_override = {"general": {}}
    if debug:
        config_override["general"]["debug"] = True
    if max_items is not None:
        config_override["general"]["max_items"] = max_items
    if request_delay is not None:
        config_override["general"]["request_delay"] = request_delay
    if gemini_delay is not None:
        config_override["general"]["gemini_delay"] = gemini_delay
    
    config = load_config()
    
    # Apply overrides
    for section, values in config_override.items():
        config.setdefault(section, {}).update(values)
    
    # Default sources if none provided
    if not sources:
        sources = ["nse", "bse", "sebi"]
    
    # Validate sources
    valid_sources = ["nse", "bse", "sebi"]
    invalid_sources = [s for s in sources if s not in valid_sources]
    if invalid_sources:
        console.print(f"❌ Invalid sources: {invalid_sources}. Valid sources: {valid_sources}", style="red")
        raise typer.Exit(1)
    
    # Initialize pipeline
    pipeline = CircularsPipeline(config)
    
    console.print("🚀 Parallel RSS Fetch & AI Processing Pipeline (MarkItDown + Gemini)")
    console.print(f"Working directory: {pipeline.state_dir.parent.absolute()}")
    console.print(f"Debug mode: {pipeline.debug}")
    console.print(f"Request delay: {pipeline.request_delay}s, Gemini delay: {pipeline.gemini_delay}s")
    console.print(f"Parallel limits: {pipeline.max_concurrent_items} items/source, {pipeline.max_concurrent_sources} sources, {pipeline.gemini_processor.gemini_semaphore._value} Gemini calls, {pipeline.file_downloader.download_semaphore._value} downloads")
    
    # Check dependencies
    if not check_dependencies():
        raise typer.Exit(1)
    
    # Run pipeline
    start_time = time.time()
    try:
        stats = asyncio.run(pipeline.process_sources(sources, max_items))
        
        # Display results
        display_results(stats, time.time() - start_time)
        
    except KeyboardInterrupt:
        console.print("\\n❌ Pipeline interrupted by user", style="yellow")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"❌ Pipeline failed: {e}", style="red")
        raise typer.Exit(1)


def check_dependencies() -> bool:
    """Check if required tools are available"""
    try:
        subprocess.run(["gemini", "--help"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("❌ gemini CLI tool not found or not working", style="red")
        console.print("Install with: npm install -g @google/gemini-cli", style="yellow")
        return False


def display_results(stats, elapsed_time: float):
    """Display pipeline results in a formatted table"""
    console.print("\\n📊 Pipeline Results", style="bold green")
    
    # Overall stats
    table = Table(title="Overall Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Total Sources", str(stats.total_sources))
    table.add_row("Total Items", str(stats.total_items))
    table.add_row("Completed", str(stats.completed_items))
    table.add_row("Failed", str(stats.failed_items))
    table.add_row("Success Rate", f"{stats.success_rate:.1f}%")
    table.add_row("Processing Time", f"{elapsed_time:.1f}s")
    
    console.print(table)
    
    # Per-source stats
    if stats.source_results:
        console.print("\\n📈 Per-Source Statistics", style="bold blue")
        
        source_table = Table()
        source_table.add_column("Source", style="cyan")
        source_table.add_column("Items", style="white")
        source_table.add_column("Completed", style="green")
        source_table.add_column("Failed", style="red")
        source_table.add_column("Success Rate", style="yellow")
        
        for source_stat in stats.source_results.values():
            source_table.add_row(
                source_stat.source.upper(),
                str(source_stat.total_items),
                str(source_stat.completed_items),
                str(source_stat.failed_items),
                f"{source_stat.success_rate:.1f}%"
            )
        
        console.print(source_table)


@app.command()
def regenerate(
    item_ids: List[str] = typer.Argument(..., help="Item IDs to regenerate (e.g., 2d7ae7c3294c34e4)"),
    source: str = typer.Option(None, "--source", help="Source filter (nse, bse, sebi)"),
):
    """Regenerate markdown content for specific items with updated prompts."""
    
    config = load_config()
    pipeline = CircularsPipeline(config)
    
    console.print(f"🔄 Regenerating {len(item_ids)} items with updated Hugo frontmatter format")
    
    async def regenerate_items():
        for item_id in item_ids:
            console.print(f"Processing item: {item_id}")
            try:
                # Reset item to text_extracted stage to force regeneration
                success = await pipeline.regenerate_item_markdown(item_id, source)
                if success:
                    console.print(f"✅ Regenerated {item_id}", style="green")
                else:
                    console.print(f"❌ Failed to regenerate {item_id}", style="red")
            except Exception as e:
                console.print(f"❌ Error regenerating {item_id}: {e}", style="red")
    
    try:
        asyncio.run(regenerate_items())
    except KeyboardInterrupt:
        console.print("\n❌ Regeneration interrupted by user", style="yellow")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()