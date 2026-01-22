"""Centralized constants for the AIML Studio application."""

from typing import Any

# Application Information
APP_TITLE = "AIML Studio"
APP_VERSION = "0.0.1"
APP_DESCRIPTION = "A Python web platform for running predictive analytics and machine learning experiments"

# Color Scheme
COLORS: dict[str, str] = {
    "primary": "#339af0",
    "secondary": "#748ffc",
    "success": "#51cf66",
    "warning": "#ffd43b",
    "error": "#ff6b6b",
    "info": "#4dabf7",
    "dark": "#1a1b1e",
    "light": "#f8f9fa",
}

# Layout Sizes
HEADER_HEIGHT = 60
NAVBAR_WIDTH = 250
NAVBAR_WIDTH_COLLAPSED = 80
FOOTER_HEIGHT = 50
ASIDE_WIDTH = 300

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
