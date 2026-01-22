"""Analytics dashboard page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_ag_grid


def create_analytics_layout() -> html.Div:
    """Create the analytics dashboard page layout.

    Returns:
        Analytics page layout component
    """
    # Sample analytics data
    metrics_summary_columns = [
        {"field": "metric", "headerName": "Metric"},
        {"field": "value", "headerName": "Value"},
        {"field": "change", "headerName": "Change"},
        {"field": "status", "headerName": "Status"},
    ]

    metrics_summary_data = [
        {"metric": "Total Users", "value": "1,234", "change": "+12%", "status": "Good"},
        {"metric": "Active Projects", "value": "45", "change": "+8%", "status": "Good"},
        {"metric": "Data Sources", "value": "12", "change": "0%", "status": "Stable"},
        {"metric": "API Calls", "value": "23,456", "change": "+23%", "status": "Good"},
    ]

    return html.Div([
        dmc.Stack(
            [
                dmc.Title("Analytics Dashboard", order=2, mb="md"),
                # Key metrics cards
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 4},
                    spacing="md",
                    children=[
                        dmc.Card(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:users", width=30, color="blue"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Total Users", size="sm", c="dimmed"),
                                                dmc.Title("1,234", order=3),
                                                dmc.Badge("↑ 12%", color="green", variant="light"),
                                            ],
                                            gap=0,
                                        ),
                                    ],
                                    gap="md",
                                    align="center",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                        dmc.Card(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:folder", width=30, color="green"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Active Projects", size="sm", c="dimmed"),
                                                dmc.Title("45", order=3),
                                                dmc.Badge("↑ 8%", color="green", variant="light"),
                                            ],
                                            gap=0,
                                        ),
                                    ],
                                    gap="md",
                                    align="center",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                        dmc.Card(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:database", width=30, color="orange"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Data Sources", size="sm", c="dimmed"),
                                                dmc.Title("12", order=3),
                                                dmc.Badge("0%", color="gray", variant="light"),
                                            ],
                                            gap=0,
                                        ),
                                    ],
                                    gap="md",
                                    align="center",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                        dmc.Card(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:api", width=30, color="purple"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("API Calls", size="sm", c="dimmed"),
                                                dmc.Title("23.4K", order=3),
                                                dmc.Badge("↑ 23%", color="green", variant="light"),
                                            ],
                                            gap=0,
                                        ),
                                    ],
                                    gap="md",
                                    align="center",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                    ],
                ),
                # Charts placeholder
                dmc.SimpleGrid(
                    cols={"base": 1, "md": 2},
                    spacing="md",
                    children=[
                        dmc.Card(
                            [
                                dmc.Title("Usage Trends", order=4, mb="md"),
                                dmc.Center(
                                    dmc.Stack(
                                        [
                                            DashIconify(icon="tabler:chart-line", width=60, color="gray"),
                                            dmc.Text("Chart placeholder", c="dimmed"),
                                        ],
                                        gap="sm",
                                        align="center",
                                    ),
                                    style={"minHeight": "300px"},
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                        dmc.Card(
                            [
                                dmc.Title("Performance Metrics", order=4, mb="md"),
                                dmc.Center(
                                    dmc.Stack(
                                        [
                                            DashIconify(icon="tabler:chart-bar", width=60, color="gray"),
                                            dmc.Text("Chart placeholder", c="dimmed"),
                                        ],
                                        gap="sm",
                                        align="center",
                                    ),
                                    style={"minHeight": "300px"},
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            p="lg",
                        ),
                    ],
                ),
                # Metrics summary table
                dmc.Card(
                    [
                        dmc.Title("Metrics Summary", order=4, mb="md"),
                        create_ag_grid(
                            grid_id="metrics-summary-grid",
                            column_defs=metrics_summary_columns,
                            row_data=metrics_summary_data,
                            pagination=False,
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
            ],
            gap="lg",
        )
    ])
