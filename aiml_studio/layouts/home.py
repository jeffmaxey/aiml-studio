"""Home page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_ag_grid


def create_home_layout() -> html.Div:
    """Create the home page layout.

    Returns:
        Home page layout component
    """
    quick_actions = [
        {
            "title": "Analytics",
            "description": "View analytics dashboard",
            "icon": "tabler:chart-bar",
            "href": "/analytics",
        },
        {
            "title": "Data Sources",
            "description": "Manage data connections",
            "icon": "tabler:database",
            "href": "/data-sources",
        },
        {"title": "Projects", "description": "Manage your projects", "icon": "tabler:folder", "href": "/projects"},
        {"title": "Settings", "description": "Configure application", "icon": "tabler:settings", "href": "/settings"},
    ]

    action_cards = [
        dmc.Card(
            [
                dmc.Group(
                    [
                        DashIconify(icon=action["icon"], width=30, color="blue"),
                        dmc.Stack(
                            [
                                dmc.Title(action["title"], order=4),
                                dmc.Text(action["description"], size="sm", c="dimmed"),
                            ],
                            gap="xs",
                        ),
                    ],
                    gap="md",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"cursor": "pointer"},
            id={"type": "action-card", "index": action["href"]},
        )
        for action in quick_actions
    ]

    # Sample recent activity data
    recent_activity_columns = [
        {"field": "timestamp", "headerName": "Time", "width": 200},
        {"field": "action", "headerName": "Action", "width": 200},
        {"field": "details", "headerName": "Details", "flex": 1},
    ]

    recent_activity_data = [
        {"timestamp": "2024-01-22 10:30:00", "action": "Project Created", "details": "Created new ML project"},
        {
            "timestamp": "2024-01-22 09:15:00",
            "action": "Data Source Added",
            "details": "Connected to PostgreSQL database",
        },
        {"timestamp": "2024-01-22 08:45:00", "action": "Settings Updated", "details": "Changed theme to dark mode"},
    ]

    return html.Div([
        dmc.Stack(
            [
                # Welcome section
                dmc.Paper(
                    [
                        dmc.Title("Welcome to AIML Studio", order=2, mb="sm"),
                        dmc.Text(
                            "Your platform for running predictive analytics and machine learning experiments.",
                            size="lg",
                            c="dimmed",
                        ),
                    ],
                    p="xl",
                    withBorder=True,
                    radius="md",
                ),
                # Quick actions
                dmc.Stack(
                    [
                        dmc.Title("Quick Actions", order=3),
                        dmc.SimpleGrid(
                            cols={"base": 1, "sm": 2, "md": 4},
                            spacing="md",
                            children=action_cards,
                        ),
                    ],
                    gap="md",
                ),
                # Recent activity
                dmc.Stack(
                    [
                        dmc.Title("Recent Activity", order=3),
                        create_ag_grid(
                            grid_id="recent-activity-grid",
                            column_defs=recent_activity_columns,
                            row_data=recent_activity_data,
                            pagination=False,
                        ),
                    ],
                    gap="md",
                ),
            ],
            gap="xl",
        )
    ])
