"""Navigation sidebar component for AIML Studio admin dashboard.

This module provides a reusable navigation sidebar with links to all
admin dashboard pages.
"""

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_sidebar() -> dmc.Stack:
    """Create a navigation sidebar with links to all dashboard pages.

    Returns:
        A Mantine Stack component containing navigation links.
    """
    return dmc.Stack(
        children=[
            # Application header
            dmc.Title("AIML Studio", order=2, style={"marginBottom": "20px"}),
            dmc.Text("Admin Dashboard", size="sm", c="dimmed", style={"marginBottom": "30px"}),
            # Navigation links
            dmc.NavLink(
                label="Analytics",
                leftSection=DashIconify(icon="carbon:analytics", width=20),
                href="/",
                variant="subtle",
                style={"marginBottom": "10px"},
            ),
            dmc.NavLink(
                label="Data Sources",
                leftSection=DashIconify(icon="carbon:data-table", width=20),
                href="/data-sources",
                variant="subtle",
                style={"marginBottom": "10px"},
            ),
            dmc.NavLink(
                label="Projects",
                leftSection=DashIconify(icon="carbon:folder", width=20),
                href="/projects",
                variant="subtle",
                style={"marginBottom": "10px"},
            ),
        ],
        gap="xs",
    )
