"""Centralized constants for the AIML Studio application."""

from typing import Any

# Application Information
APP_TITLE = "AIML Studio"
APP_VERSION = "0.0.1"
APP_DESCRIPTION = "A Python web platform for running predictive analytics and machine learning experiments"

# Color Scheme - Inspired by MLflow's professional palette
COLORS: dict[str, str] = {
    "primary": "#0194E2",  # MLflow blue
    "secondary": "#43C9ED",  # Light blue accent
    "success": "#00B388",  # Professional green
    "warning": "#FFB240",  # Amber warning
    "error": "#FF5252",  # Clear error red
    "info": "#2196F3",  # Information blue
    "dark": "#1E1E1E",  # Deep dark
    "light": "#F5F7FA",  # Soft light background
    "gray": "#6C757D",  # Neutral gray
    "purple": "#7B61FF",  # Accent purple
    "teal": "#14B8A6",  # Modern teal
}

# Layout Sizes - Optimized for professional ML platform
HEADER_HEIGHT = 64  # Slightly taller for better presence
NAVBAR_WIDTH = 260  # Wider for better readability
NAVBAR_WIDTH_COLLAPSED = 80
FOOTER_HEIGHT = 48  # Balanced footer height
ASIDE_WIDTH = 320  # More space for contextual info

# Breakpoints (Mantine defaults)
BREAKPOINTS: dict[str, str] = {
    "xs": "36em",
    "sm": "48em",
    "md": "62em",
    "lg": "75em",
    "xl": "88em",
}

# Navigation Links
NAV_LINKS: list[dict[str, Any]] = [
    {"label": "Home", "icon": "tabler:home", "href": "/", "section": "core"},
    {"label": "Settings", "icon": "tabler:settings", "href": "/settings", "section": "core"},
    {"label": "Help", "icon": "tabler:help", "href": "/help", "section": "core"},
    {"label": "Logs", "icon": "tabler:list", "href": "/logs", "section": "core"},
    {"label": "Analytics", "icon": "tabler:chart-bar", "href": "/analytics", "section": "admin"},
    {"label": "Data Sources", "icon": "tabler:database", "href": "/data-sources", "section": "admin"},
    {"label": "Projects", "icon": "tabler:folder", "href": "/projects", "section": "admin"},
]

# Table Configuration
DEFAULT_TABLE_PAGE_SIZE = 20
TABLE_PAGE_SIZE_OPTIONS = [10, 20, 50, 100]

# Log Levels
LOG_LEVELS: dict[str, str] = {
    "DEBUG": "info",
    "INFO": "success",
    "WARNING": "warning",
    "ERROR": "error",
    "CRITICAL": "error",
}
