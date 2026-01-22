"""Dash Mantine theme configuration."""

from typing import Any

from aiml_studio.constants import COLORS

# Mantine Theme Configuration
MANTINE_THEME: dict[str, Any] = {
    "colorScheme": "light",
    "primaryColor": "blue",
    "fontFamily": "'Inter', sans-serif",
    "headings": {
        "fontFamily": "'Inter', sans-serif",
        "fontWeight": 600,
    },
    "colors": {
        "primary": [
            "#e3f2fd",
            "#bbdefb",
            "#90caf9",
            "#64b5f6",
            "#42a5f5",
            COLORS["primary"],
            "#1e88e5",
            "#1976d2",
            "#1565c0",
            "#0d47a1",
        ],
    },
    "components": {
        "Button": {
            "defaultProps": {
                "radius": "md",
            },
        },
        "Card": {
            "defaultProps": {
                "shadow": "sm",
                "radius": "md",
                "withBorder": True,
            },
        },
        "Paper": {
            "defaultProps": {
                "shadow": "xs",
                "radius": "md",
                "p": "md",
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
