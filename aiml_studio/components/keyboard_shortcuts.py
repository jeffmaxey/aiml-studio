"""Keyboard shortcuts system for AIML Studio."""

from typing import Any

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


# Keyboard shortcut definitions
KEYBOARD_SHORTCUTS: dict[str, dict[str, Any]] = {
    "global": {
        "search": {"keys": ["Ctrl", "K"], "description": "Open global search", "action": "open-search"},
        "help": {"keys": ["?"], "description": "Show keyboard shortcuts", "action": "show-shortcuts"},
        "home": {"keys": ["G", "H"], "description": "Go to Home", "action": "navigate-home"},
        "projects": {"keys": ["G", "P"], "description": "Go to Projects", "action": "navigate-projects"},
        "analytics": {"keys": ["G", "A"], "description": "Go to Analytics", "action": "navigate-analytics"},
        "settings": {"keys": ["G", "S"], "description": "Go to Settings", "action": "navigate-settings"},
    },
    "tables": {
        "refresh": {"keys": ["R"], "description": "Refresh table data", "action": "refresh-table"},
        "export": {"keys": ["E"], "description": "Export table data", "action": "export-table"},
        "filter": {"keys": ["F"], "description": "Focus filter input", "action": "focus-filter"},
    },
    "forms": {
        "save": {"keys": ["Ctrl", "Enter"], "description": "Save form", "action": "save-form"},
        "cancel": {"keys": ["Esc"], "description": "Cancel/Close", "action": "cancel-form"},
    },
}


def create_keyboard_shortcuts_modal() -> dmc.Modal:
    """Create a modal displaying all available keyboard shortcuts.

    Returns:
        Modal component with keyboard shortcuts list
    """
    return dmc.Modal(
        id="keyboard-shortcuts-modal",
        title=dmc.Group(
            [
                DashIconify(icon="tabler:keyboard", width=24),
                dmc.Title("Keyboard Shortcuts", order=3),
            ],
            gap="sm",
        ),
        size="lg",
        centered=True,
        children=[
            dmc.Stack(
                [
                    # Global shortcuts section
                    dmc.Stack(
                        [
                            dmc.Text("Global", size="lg", fw=700, c="dimmed"),
                            dmc.Divider(),
                            create_shortcuts_section(KEYBOARD_SHORTCUTS["global"]),
                        ],
                        gap="sm",
                    ),
                    # Table shortcuts section
                    dmc.Stack(
                        [
                            dmc.Text("Tables", size="lg", fw=700, c="dimmed"),
                            dmc.Divider(),
                            create_shortcuts_section(KEYBOARD_SHORTCUTS["tables"]),
                        ],
                        gap="sm",
                    ),
                    # Form shortcuts section
                    dmc.Stack(
                        [
                            dmc.Text("Forms", size="lg", fw=700, c="dimmed"),
                            dmc.Divider(),
                            create_shortcuts_section(KEYBOARD_SHORTCUTS["forms"]),
                        ],
                        gap="sm",
                    ),
                ],
                gap="xl",
            )
        ],
    )


def create_shortcuts_section(shortcuts: dict[str, dict[str, Any]]) -> dmc.Stack:
    """Create a section of keyboard shortcuts.

    Args:
        shortcuts: Dictionary of shortcut definitions

    Returns:
        Stack of shortcut items
    """
    items = []
    for shortcut_data in shortcuts.values():
        items.append(create_shortcut_item(shortcut_data["keys"], shortcut_data["description"]))

    return dmc.Stack(items, gap="xs")


def create_shortcut_item(keys: list[str], description: str) -> dmc.Group:
    """Create a single keyboard shortcut display item.

    Args:
        keys: List of keys in the shortcut
        description: Description of what the shortcut does

    Returns:
        Group with keys and description
    """
    key_badges = []
    for i, key in enumerate(keys):
        key_badges.append(
            dmc.Badge(
                key,
                variant="light",
                size="lg",
                style={
                    "fontFamily": "monospace",
                    "minWidth": "40px",
                },
            )
        )
        if i < len(keys) - 1:
            key_badges.append(dmc.Text("+", size="sm", c="dimmed", mx="xs"))

    return dmc.Group(
        [
            dmc.Group(key_badges, gap=0),
            dmc.Text(description, size="sm", c="dimmed"),
        ],
        justify="space-between",
        gap="lg",
    )


def create_shortcut_hint(keys: list[str]) -> dmc.Group:
    """Create a subtle keyboard shortcut hint for UI elements.

    Args:
        keys: List of keys in the shortcut

    Returns:
        Group with key badges
    """
    key_badges = []
    for i, key in enumerate(keys):
        key_badges.append(
            dmc.Badge(
                key,
                size="xs",
                variant="light",
                color="gray",
                style={"fontFamily": "monospace"},
            )
        )
        if i < len(keys) - 1:
            key_badges.append(dmc.Text("+", size="xs", c="dimmed", mx="2px"))

    return dmc.Group(key_badges, gap=0)


def create_keyboard_shortcuts_script() -> html.Script:
    """Create a JavaScript snippet for handling keyboard shortcuts.

    Returns:
        Script tag with keyboard shortcut handling code
    """
    script_content = """
    // Global keyboard shortcuts handler
    document.addEventListener('keydown', function(e) {
        // Ignore if user is typing in an input
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            // Allow Ctrl+Enter in forms
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                // Trigger form save
                const saveButton = document.querySelector('[id*="save"]');
                if (saveButton) saveButton.click();
            }
            return;
        }

        // Ctrl/Cmd + K: Open search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.getElementById('global-search-input');
            if (searchInput) searchInput.focus();
        }

        // ?: Show keyboard shortcuts
        if (e.key === '?') {
            e.preventDefault();
            // Trigger shortcuts modal
            const shortcutsBtn = document.getElementById('show-shortcuts-btn');
            if (shortcutsBtn) shortcutsBtn.click();
        }

        // G + H: Go to home
        if (e.key === 'h' && sessionStorage.getItem('lastKey') === 'g') {
            e.preventDefault();
            window.location.href = '/';
            sessionStorage.removeItem('lastKey');
        }

        // G + P: Go to projects
        if (e.key === 'p' && sessionStorage.getItem('lastKey') === 'g') {
            e.preventDefault();
            window.location.href = '/projects';
            sessionStorage.removeItem('lastKey');
        }

        // G + A: Go to analytics
        if (e.key === 'a' && sessionStorage.getItem('lastKey') === 'g') {
            e.preventDefault();
            window.location.href = '/analytics';
            sessionStorage.removeItem('lastKey');
        }

        // G + S: Go to settings
        if (e.key === 's' && sessionStorage.getItem('lastKey') === 'g') {
            e.preventDefault();
            window.location.href = '/settings';
            sessionStorage.removeItem('lastKey');
        }

        // Store 'g' key for navigation shortcuts
        if (e.key === 'g') {
            sessionStorage.setItem('lastKey', 'g');
            setTimeout(() => sessionStorage.removeItem('lastKey'), 1000);
        }

        // R: Refresh (when applicable)
        if (e.key === 'r') {
            const refreshBtn = document.querySelector('[id*="refresh"]');
            if (refreshBtn) {
                e.preventDefault();
                refreshBtn.click();
            }
        }

        // E: Export (when applicable)
        if (e.key === 'e') {
            const exportBtn = document.querySelector('[id*="export"]');
            if (exportBtn) {
                e.preventDefault();
                exportBtn.click();
            }
        }
    });
    """

    return html.Script(script_content)


def get_shortcut_for_action(action: str) -> list[str] | None:
    """Get keyboard shortcut keys for a specific action.

    Args:
        action: Action identifier

    Returns:
        List of keys for the shortcut, or None if not found
    """
    for category in KEYBOARD_SHORTCUTS.values():
        for shortcut_data in category.values():
            if shortcut_data["action"] == action:
                return shortcut_data["keys"]
    return None
