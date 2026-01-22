"""Dash Mantine theme configuration."""

from typing import Any

from aiml_studio.constants import COLORS

# Mantine Theme Configuration - Professional ML Platform Design
MANTINE_THEME: dict[str, Any] = {
    "colorScheme": "light",
    "primaryColor": "blue",
    "fontFamily": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    "fontFamilyMonospace": "'Fira Code', 'Courier New', monospace",
    "headings": {
        "fontFamily": "'Inter', sans-serif",
        "fontWeight": 700,
        "sizes": {
            "h1": {"fontSize": "2.5rem", "lineHeight": "1.2"},
            "h2": {"fontSize": "2rem", "lineHeight": "1.3"},
            "h3": {"fontSize": "1.5rem", "lineHeight": "1.4"},
            "h4": {"fontSize": "1.25rem", "lineHeight": "1.4"},
        },
    },
    "colors": {
        "primary": [
            "#E6F7FF",  # Lightest
            "#B3E5FF",
            "#80D3FF",
            "#4DC2FF",
            "#1AB0FF",
            COLORS["primary"],  # Base: #0194E2
            "#0178B8",
            "#015C8E",
            "#014164",
            "#00253A",  # Darkest
        ],
        "success": [
            "#E6F9F3",
            "#B3EBD9",
            "#80DDBF",
            "#4DCFA5",
            "#1AC18B",
            COLORS["success"],  # Base: #00B388
            "#00906B",
            "#006D4F",
            "#004A33",
            "#002717",
        ],
    },
    "spacing": {
        "xs": "0.5rem",   # 8px
        "sm": "0.75rem",  # 12px
        "md": "1rem",     # 16px
        "lg": "1.5rem",   # 24px
        "xl": "2rem",     # 32px
    },
    "radius": {
        "xs": "0.25rem",  # 4px
        "sm": "0.375rem", # 6px
        "md": "0.5rem",   # 8px
        "lg": "0.75rem",  # 12px
        "xl": "1rem",     # 16px
    },
    "shadows": {
        "xs": "0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.1)",
        "sm": "0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 10px rgba(0, 0, 0, 0.1)",
        "md": "0 4px 6px rgba(0, 0, 0, 0.05), 0 10px 20px rgba(0, 0, 0, 0.1)",
        "lg": "0 10px 15px rgba(0, 0, 0, 0.05), 0 20px 40px rgba(0, 0, 0, 0.1)",
        "xl": "0 20px 25px rgba(0, 0, 0, 0.05), 0 30px 60px rgba(0, 0, 0, 0.15)",
    },
    "components": {
        "Button": {
            "defaultProps": {
                "radius": "md",
                "size": "md",
            },
            "styles": {
                "root": {
                    "fontWeight": 600,
                    "transition": "all 0.2s ease",
                },
            },
        },
        "Card": {
            "defaultProps": {
                "shadow": "sm",
                "radius": "lg",
                "withBorder": True,
                "padding": "lg",
            },
        },
        "Paper": {
            "defaultProps": {
                "shadow": "xs",
                "radius": "md",
                "p": "lg",
            },
        },
        "Input": {
            "defaultProps": {
                "radius": "md",
            },
        },
        "Badge": {
            "defaultProps": {
                "radius": "sm",
                "size": "md",
            },
        },
        "ActionIcon": {
            "defaultProps": {
                "radius": "md",
            },
        },
    },
}

# Dark Theme Configuration
DARK_THEME: dict[str, Any] = {
    **MANTINE_THEME,
    "colorScheme": "dark",
}


def get_theme(color_scheme: str = "light") -> dict[str, Any]:
    """Get theme configuration based on color scheme.

    Args:
        color_scheme: Color scheme ('light' or 'dark')

    Returns:
        Theme configuration dictionary
    """
    return DARK_THEME if color_scheme == "dark" else MANTINE_THEME
