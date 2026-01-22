"""Main application entry point for AIML Studio."""

import dash
import dash_mantine_components as dmc

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


# Note: Navbar toggle callback removed due to conflict with AppShell props
# The navbar toggle is handled by Mantine's built-in responsive behavior


# Import callbacks from all pages
# This ensures all callbacks are registered
try:
    from aiml_studio.callbacks import (  # noqa: F401
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
