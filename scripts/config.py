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
            "gemini_delay": 3.0,
            "timeout": 300,
            "debug": False,
            "max_concurrent_items": 5,
            "max_concurrent_sources": 3,
            "max_concurrent_gemini_calls": 6,
            "max_concurrent_downloads": 3
        },
        "api": {
            "gemini_api_key": "",
            "gemini_model": "gemini-3.5-flash-lite"
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
    prompts = config.get("prompts", {})
    if not prompts.get("gemini_analysis") and prompts.get("claude_analysis"):
        config.setdefault("prompts", {})["gemini_analysis"] = prompts["claude_analysis"]
    if not config.get("prompts", {}).get("gemini_analysis"):
        raise ValueError("Missing required config: prompts.gemini_analysis")
    
    # Environment variable overrides
    env_overrides = {
        "gemini_api_key": os.getenv("GEMINI_API_KEY", "") or os.getenv("GOOGLE_API_KEY", "") or os.getenv("CLAUDE_CODE_OAUTH_TOKEN", ""),
        "gemini_model": os.getenv("GEMINI_MODEL", "") or None,
        "request_delay": float(os.getenv("REQUEST_DELAY", "0")) or None,
        "gemini_delay": float(os.getenv("GEMINI_DELAY", "0")) or float(os.getenv("CLAUDE_DELAY", "0")) or None,
        "timeout": int(os.getenv("TIMEOUT", "0")) or None,
        "debug": os.getenv("DEBUG", "").lower() in ("true", "1", "yes"),
        "max_items": int(os.getenv("MAX_ITEMS", "0")) or None,
    }
    
    # Apply non-None environment overrides
    if env_overrides["gemini_api_key"]:
        config.setdefault("api", {})["gemini_api_key"] = env_overrides["gemini_api_key"]
    if env_overrides["gemini_model"]:
        config.setdefault("api", {})["gemini_model"] = env_overrides["gemini_model"]
    
    for key in ["request_delay", "gemini_delay", "timeout", "max_items"]:
        if env_overrides[key]:
            config.setdefault("general", {})[key] = env_overrides[key]
    
    if env_overrides["debug"]:
        config.setdefault("general", {})["debug"] = True
    
    return config