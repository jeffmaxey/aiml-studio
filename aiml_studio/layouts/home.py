"""Home page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_ag_grid


def create_metric_card(title: str, value: str, icon: str, color: str, trend: str | None = None) -> dmc.Card:
    """Create a metric card for the dashboard.

    Args:
        title: Metric title
        value: Metric value
        icon: Icon identifier
        color: Color theme
        trend: Optional trend indicator

    Returns:
        Styled metric card
    """
    return dmc.Card(
        [
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.ThemeIcon(
                                DashIconify(icon=icon, width=24),
                                size="xl",
                                radius="md",
                                variant="light",
                                color=color,
                            ),
                            dmc.Stack(
                                [
                                    dmc.Text(title, size="sm", c="dimmed", fw=500),
                                    dmc.Title(value, order=2, style={"lineHeight": "1"}),
                                ],
                                gap=2,
                            ),
                        ],
                        justify="space-between",
                        align="flex-start",
                    ),
                    trend
                    and dmc.Group(
                        [
                            dmc.Badge(
                                trend,
                                color="green" if "↑" in trend else "red" if "↓" in trend else "gray",
                                variant="light",
                                size="sm",
                            ),
                            dmc.Text("vs last month", size="xs", c="dimmed"),
                        ],
                        gap="xs",
                    ),
                ],
                gap="md",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="lg",
        p="lg",
        className="metric-card scale-in",
    )


def create_home_layout() -> html.Div:
    """Create the home page layout.

    Returns:
        Home page layout component
    """
    quick_actions = [
        {
            "title": "New Project",
            "description": "Start a new ML project",
            "icon": "tabler:folder-plus",
            "color": "blue",
            "href": "/projects",
        },
        {
            "title": "Connect Data",
            "description": "Add data sources",
            "icon": "tabler:database-import",
            "color": "green",
            "href": "/data-sources",
        },
        {
            "title": "View Analytics",
            "description": "Check performance metrics",
            "icon": "tabler:chart-line",
            "color": "violet",
            "href": "/analytics",
        },
        {
            "title": "Documentation",
            "description": "Learn more about AIML Studio",
            "icon": "tabler:book-2",
            "color": "orange",
            "href": "/help",
        },
    ]

    action_cards = [
        dmc.Card(
            [
                dmc.Stack(
                    [
                        dmc.ThemeIcon(
                            DashIconify(icon=action["icon"], width=32),
                            size="xl",
                            radius="md",
                            variant="light",
                            color=action["color"],
                        ),
                        dmc.Stack(
                            [
                                dmc.Title(action["title"], order=4, fw=700),
                                dmc.Text(action["description"], size="sm", c="dimmed"),
                            ],
                            gap="xs",
                        ),
                        dmc.Button(
                            "Get Started",
                            variant="light",
                            color=action["color"],
                            fullWidth=True,
                            leftSection=DashIconify(icon="tabler:arrow-right", width=16),
                        ),
                    ],
                    gap="md",
                    align="stretch",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="lg",
            p="lg",
            style={"cursor": "pointer", "height": "100%"},
            className="scale-in",
            id={"type": "action-card", "index": action["href"]},
        )
        for action in quick_actions
    ]

    # Sample recent activity data
    recent_activity_columns = [
        {"field": "timestamp", "headerName": "Time", "width": 180},
        {"field": "action", "headerName": "Action", "width": 220},
        {"field": "user", "headerName": "User", "width": 150},
        {"field": "details", "headerName": "Details", "flex": 1},
    ]

    recent_activity_data = [
        {
            "timestamp": "2024-01-22 10:30:00",
            "action": "Project Created",
            "user": "Admin User",
            "details": "Created new ML project: Customer Churn Prediction",
        },
        {
            "timestamp": "2024-01-22 09:15:00",
            "action": "Data Source Added",
            "user": "Admin User",
            "details": "Connected to PostgreSQL database: production_db",
        },
        {
            "timestamp": "2024-01-22 08:45:00",
            "action": "Settings Updated",
            "user": "Admin User",
            "details": "Changed theme to dark mode",
        },
        {
            "timestamp": "2024-01-21 16:20:00",
            "action": "Model Deployed",
            "user": "Admin User",
            "details": "Deployed sentiment analysis model v2.1",
        },
    ]

    return html.Div([
        dmc.Stack(
            [
                # Welcome banner
                dmc.Paper(
                    [
                        dmc.Grid(
                            [
                                dmc.GridCol(
                                    dmc.Stack(
                                        [
                                            dmc.Group(
                                                [
                                                    dmc.ThemeIcon(
                                                        DashIconify(icon="tabler:sparkles", width=28),
                                                        size="xl",
                                                        radius="md",
                                                        variant="gradient",
                                                        gradient={"from": "blue", "to": "cyan", "deg": 135},
                                                    ),
                                                    dmc.Title(
                                                        "Welcome to AIML Studio", order=2, className="gradient-text"
                                                    ),
                                                ],
                                                gap="md",
                                            ),
                                            dmc.Text(
                                                "Your professional platform for running predictive analytics and machine learning experiments.",
                                                size="lg",
                                                c="dimmed",
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.Button(
                                                        "Get Started",
                                                        leftSection=DashIconify(icon="tabler:rocket", width=16),
                                                        size="md",
                                                        variant="gradient",
                                                        gradient={"from": "blue", "to": "cyan", "deg": 135},
                                                    ),
                                                    dmc.Button(
                                                        "View Documentation",
                                                        leftSection=DashIconify(icon="tabler:book", width=16),
                                                        size="md",
                                                        variant="light",
                                                    ),
                                                ],
                                                gap="md",
                                            ),
                                        ],
                                        gap="lg",
                                    ),
                                    span={"base": 12, "md": 8},
                                ),
                                dmc.GridCol(
                                    dmc.Center(
                                        DashIconify(
                                            icon="tabler:chart-dots-3",
                                            width=180,
                                            color="var(--color-primary)",
                                            style={"opacity": "0.1"},
                                        ),
                                        h="100%",
                                    ),
                                    span={"base": 12, "md": 4},
                                    className="hide-mobile",
                                ),
                            ],
                            gutter="xl",
                        )
                    ],
                    p="xl",
                    withBorder=True,
                    radius="lg",
                    shadow="md",
                    className="fade-in",
                ),
                # Key metrics
                dmc.Stack(
                    [
                        dmc.Group(
                            [
                                dmc.Title("Key Metrics", order=3),
                                dmc.Badge("Live", color="green", variant="dot", size="lg"),
                            ],
                            justify="space-between",
                        ),
                        dmc.SimpleGrid(
                            cols={"base": 1, "sm": 2, "md": 4},
                            spacing="md",
                            children=[
                                create_metric_card("Total Projects", "24", "tabler:folder", "blue", "↑ 12%"),
                                create_metric_card("Active Models", "8", "tabler:brain", "green", "↑ 3%"),
                                create_metric_card("Data Sources", "12", "tabler:database", "violet", "→ 0%"),
                                create_metric_card("API Calls", "23.4K", "tabler:api", "orange", "↑ 23%"),
                            ],
                        ),
                    ],
                    gap="md",
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
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                dmc.Title("Recent Activity", order=3),
                                dmc.Group(
                                    [
                                        dmc.ActionIcon(
                                            DashIconify(icon="tabler:refresh", width=18),
                                            variant="light",
                                            size="lg",
                                        ),
                                        dmc.ActionIcon(
                                            DashIconify(icon="tabler:filter", width=18),
                                            variant="light",
                                            size="lg",
                                        ),
                                    ],
                                    gap="xs",
                                ),
                            ],
                            justify="space-between",
                            mb="md",
                        ),
                        create_ag_grid(
                            grid_id="recent-activity-grid",
                            column_defs=recent_activity_columns,
                            row_data=recent_activity_data,
                            pagination=False,
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="lg",
                    p="lg",
                ),
            ],
            gap="xl",
        )
    ])
