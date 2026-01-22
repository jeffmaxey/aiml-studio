"""Main application entry point for AIML Studio."""

import dash
import dash_mantine_components as dmc
from dash import Input, Output, State, callback, clientside_callback, dcc, html

from aiml_studio import settings
from aiml_studio.components import (
    create_aside,
    create_footer,
    create_header,
    create_keyboard_shortcuts_modal,
    create_keyboard_shortcuts_script,
    create_modal_manager,
    create_navbar,
    create_notification_manager,
    create_search_modal,
)
from aiml_studio.constants import ASIDE_WIDTH, FOOTER_HEIGHT, HEADER_HEIGHT, NAVBAR_WIDTH
from aiml_studio.managers import (
    ApplicationManager,
    BrowserPersistenceManager,
    DataManager,
    LRUCacheManager,
)
from aiml_studio.managers.application_manager import DefaultApplicationManager
from aiml_studio.managers.data_manager import InMemoryDataManager

# Initialize managers
app_manager: ApplicationManager = DefaultApplicationManager()
data_manager: DataManager = InMemoryDataManager()
persistence_manager = BrowserPersistenceManager()
cache_manager = LRUCacheManager(max_size=100, default_ttl=3600)

# Initialize managers
app_manager.initialize()
data_manager.initialize()
persistence_manager.initialize()
cache_manager.initialize()

# Initialize Dash app with pages support
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=settings.SUPPRESS_CALLBACK_EXCEPTIONS,
    assets_folder="assets",
)

# Set the application title
app.title = "AIML Studio"

# Define the main layout with AppShell
app.layout = dmc.MantineProvider(
    [
        # Persistence stores for user preferences
        dcc.Store(id="user-preferences", storage_type="local", data={}),
        dcc.Store(id="session-data", storage_type="session", data={}),
        # Modal and notification managers
        create_modal_manager(),
        create_notification_manager(),
        create_search_modal(),
        create_keyboard_shortcuts_modal(),
        create_keyboard_shortcuts_script(),
        # Notification provider for toast notifications
        dmc.NotificationProvider(position="top-right"),
        # Main application shell
        dmc.AppShell(
            [
                create_header(),
                create_navbar(opened=True),
                create_aside(),
                dmc.AppShellMain(
                    dash.page_container,
                    id="main-content",
                ),
                create_footer(),
            ],
            header={"height": HEADER_HEIGHT},
            navbar={"width": NAVBAR_WIDTH, "breakpoint": "sm", "collapsed": {"mobile": True, "desktop": False}},
            aside={"width": ASIDE_WIDTH, "breakpoint": "md", "collapsed": {"desktop": True, "mobile": True}},
            footer={"height": FOOTER_HEIGHT},
            padding="md",
            id="appshell",
        ),
    ],
    id="mantine-provider",
    forceColorScheme="light",
)


# Navbar toggle callback
@callback(
    Output("appshell", "navbar"),
    Input("navbar-toggle-btn", "n_clicks"),
    State("appshell", "navbar"),
    prevent_initial_call=True,
)
def toggle_navbar(n_clicks: int, navbar_config: dict) -> dict:
    """Toggle navbar collapsed state.

    Args:
        n_clicks: Number of clicks
        navbar_config: Current navbar configuration

    Returns:
        Updated navbar configuration
    """
    if navbar_config["collapsed"]["desktop"]:
        navbar_config["collapsed"]["desktop"] = False
    else:
        navbar_config["collapsed"]["desktop"] = True
    return navbar_config


# Aside toggle callback
@callback(
    Output("appshell", "aside"),
    Input("aside-toggle-btn", "n_clicks"),
    State("appshell", "aside"),
    prevent_initial_call=True,
)
def toggle_aside(n_clicks: int, aside_config: dict) -> dict:
    """Toggle aside collapsed state.

    Args:
        n_clicks: Number of clicks
        aside_config: Current aside configuration

    Returns:
        Updated aside configuration
    """
    if aside_config["collapsed"]["desktop"]:
        aside_config["collapsed"]["desktop"] = False
    else:
        aside_config["collapsed"]["desktop"] = True
    return aside_config


# Theme toggle callback
@callback(
    Output("mantine-provider", "forceColorScheme"),
    Input("theme-switch", "checked"),
    prevent_initial_call=True,
)
def toggle_theme(checked: bool) -> str:
    """Toggle theme between light and dark.

    Args:
        checked: Switch state

    Returns:
        Theme name
    """
    theme = "dark" if checked else "light"
    app_manager.set_state("theme", theme)
    return theme


# RTL toggle callback using clientside callback for better performance
clientside_callback(
    """
    function(checked) {
        if (checked) {
            document.documentElement.setAttribute('dir', 'rtl');
        } else {
            document.documentElement.setAttribute('dir', 'ltr');
        }
        return checked;
    }
    """,
    Output("rtl-switch", "checked"),
    Input("rtl-switch", "checked"),
    prevent_initial_call=True,
)


# Import callbacks from all pages
# This ensures all callbacks are registered
try:
    from aiml_studio.callbacks import (  # noqa: F401
        analytics_callbacks,
        data_sources_callbacks,
        global_callbacks,
        help_callbacks,
        home_callbacks,
        logs_callbacks,
        projects_callbacks,
        settings_callbacks,
    )
except ImportError as e:
    print(f"Warning: Could not import some callbacks: {e}")


def main() -> None:
    """Run the Dash application."""
    try:
        app.run(
            debug=settings.DEBUG,
            host=settings.HOST,
            port=settings.PORT,
        )
    finally:
        # Cleanup on shutdown
        app_manager.shutdown()
        data_manager.shutdown()


if __name__ == "__main__":
    main()
