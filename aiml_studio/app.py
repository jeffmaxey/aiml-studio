"""Main Dash application entry point for AIML Studio.

This module sets up the Dash application with routing, layouts, and callbacks
for the admin dashboard. It uses dash-mantine-components for styling and
provides a comprehensive admin interface.

Example:
    Run the application::

        $ python -m aiml_studio.app

    The dashboard will be available at http://localhost:8050
"""

from typing import Any

import dash
import dash_mantine_components as dmc
from dash import Input, Output, callback, dcc, html

from aiml_studio.components.navigation import create_sidebar
from aiml_studio.layouts import analytics, data_sources, projects

# Initialize the Dash application
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="AIML Studio - Admin Dashboard",
    update_title="Loading...",
)

# Main layout with navigation and content area
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "light", "primaryColor": "blue"},
    children=[
        dcc.Location(id="url", refresh=False),
        dmc.Grid(
            children=[
                # Sidebar navigation (3 columns)
                dmc.GridCol(
                    span=2,
                    children=[create_sidebar()],
                    style={
                        "backgroundColor": "#f8f9fa",
                        "minHeight": "100vh",
                        "padding": "20px",
                    },
                ),
                # Main content area (9 columns)
                dmc.GridCol(
                    span=10,
                    children=[
                        dmc.Container(
                            id="page-content",
                            size="xl",
                            style={"padding": "20px"},
                        )
                    ],
                ),
            ],
            gutter="md",
            style={"margin": 0},
        ),
    ],
)


@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname: str | None) -> Any:
    """Route to appropriate page based on URL pathname.

    Args:
        pathname: The URL pathname (e.g., "/analytics", "/data-sources", "/projects")

    Returns:
        The layout component for the requested page, or the analytics page as default.
    """
    if pathname == "/data-sources":
        return data_sources.layout
    elif pathname == "/projects":
        return projects.layout
    else:
        # Default to analytics page
        return analytics.layout


def main() -> None:
    """Run the Dash application server.

    This function starts the Flask development server for the Dash app.
    The server runs on localhost:8050 with debug mode enabled.
    """
    app.run(debug=True, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    main()
