"""Main application entry point for AIML Studio."""

from typing import Any

import dash
import dash_mantine_components as dmc
from dash import Input, Output, State, callback, html

from aiml_studio import settings
from aiml_studio.components import create_aside, create_footer, create_header, create_navbar
from aiml_studio.constants import FOOTER_HEIGHT, HEADER_HEIGHT, NAVBAR_WIDTH

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
        navbar={"width": NAVBAR_WIDTH, "breakpoint": "sm", "collapsed": {"mobile": True}},
        aside={"width": 0, "breakpoint": "md", "collapsed": {"desktop": True, "mobile": True}},
        footer={"height": FOOTER_HEIGHT},
        padding="md",
        id="appshell",
    ),
    id="mantine-provider",
)


# Navbar toggle callback
@callback(
    Output("appshell", "navbar"),
    Input("navbar-toggle", "n_clicks"),
    State("appshell", "navbar"),
    prevent_initial_call=True,
)
def toggle_navbar(n_clicks: int, navbar_config: dict[str, Any]) -> dict[str, Any]:
    """Toggle navbar collapsed state on mobile.

    Args:
        n_clicks: Number of clicks on toggle button
        navbar_config: Current navbar configuration

    Returns:
        Updated navbar configuration
    """
    if navbar_config["collapsed"]["mobile"]:
        navbar_config["collapsed"]["mobile"] = False
    else:
        navbar_config["collapsed"]["mobile"] = True
    return navbar_config


# Import callbacks from all pages
# This ensures all callbacks are registered
try:
    from aiml_studio.callbacks import (
        analytics_callbacks,
        data_sources_callbacks,
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
    app.run(
        debug=settings.DEBUG,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    main()
