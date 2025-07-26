"""Configuration handling for the pipeline."""

import os
from pathlib import Path
from typing import Any, Dict

import tomli


def load_config() -> Dict[str, Any]:
    """Load configuration from TOML file with environment overrides"""
    config_path = Path("../config/config.toml").resolve()  # Resolve to absolute path
    
    # Default configuration
    config = {
        "general": {
            "request_delay": 2.0,
            "claude_delay": 3.0,
            "timeout": 30,
            "debug": False,
            "max_concurrent_items": 5,
            "max_concurrent_sources": 3,
            "max_concurrent_claude_calls": 2,
            "max_concurrent_downloads": 3
        },
        "api": {
            "claude_api_key": ""
        },
        "prompts": {},
        "rss_feeds": {}
    }
    
    # Load from TOML file - required
    if not config_path.exists():
        raise FileNotFoundError(f"Required config file not found: {config_path}")
    
    try:
        with open(config_path, "rb") as f:
            file_config = tomli.load(f)
            config.update(file_config)
    except Exception as e:
        raise RuntimeError(f"Failed to load config from {config_path}: {e}")
    
    # Validate required sections
    if not config.get("prompts", {}).get("claude_analysis"):
        raise ValueError("Missing required config: prompts.claude_analysis")
    
    # Environment variable overrides
    env_overrides = {
        "claude_api_key": os.getenv("CLAUDE_CODE_OAUTH_TOKEN", ""),
        "request_delay": float(os.getenv("REQUEST_DELAY", "0")) or None,
        "claude_delay": float(os.getenv("CLAUDE_DELAY", "0")) or None,
        "timeout": int(os.getenv("TIMEOUT", "0")) or None,
        "debug": os.getenv("DEBUG", "").lower() in ("true", "1", "yes"),
        "max_items": int(os.getenv("MAX_ITEMS", "0")) or None,
    }
    
    # Apply non-None environment overrides
    if env_overrides["claude_api_key"]:
        config.setdefault("api", {})["claude_api_key"] = env_overrides["claude_api_key"]
    
    for key in ["request_delay", "claude_delay", "timeout", "max_items"]:
        if env_overrides[key]:
            config.setdefault("general", {})[key] = env_overrides[key]
    
    if env_overrides["debug"]:
        config.setdefault("general", {})["debug"] = True
    
    return config