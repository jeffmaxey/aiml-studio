"""Application settings and configuration."""

import os
from typing import Any

# Server Configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8050"))

# Dash Configuration
SUPPRESS_CALLBACK_EXCEPTIONS = True
SERVE_LOCALLY = True

# Feature Flags
ENABLE_ANALYTICS = True
ENABLE_DATA_SOURCES = True
ENABLE_PROJECTS = True

# Application Settings
DEFAULT_THEME = "light"
ENABLE_DARK_MODE = True

# Security Settings
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

# Data Sources (Example Configuration)
DATA_SOURCE_TYPES: list[str] = ["PostgreSQL", "MySQL", "SQLite", "MongoDB", "API"]

# Project Status Options
PROJECT_STATUSES: list[str] = ["Active", "Inactive", "Completed", "Archived"]

# Application Configuration
APP_CONFIG: dict[str, Any] = {
    "server": {
        "debug": DEBUG,
        "host": HOST,
        "port": PORT,
    },
    "dash": {
        "suppress_callback_exceptions": SUPPRESS_CALLBACK_EXCEPTIONS,
        "serve_locally": SERVE_LOCALLY,
    },
    "features": {
        "analytics": ENABLE_ANALYTICS,
        "data_sources": ENABLE_DATA_SOURCES,
        "projects": ENABLE_PROJECTS,
    },
    "ui": {
        "default_theme": DEFAULT_THEME,
        "enable_dark_mode": ENABLE_DARK_MODE,
    },
}
