"""Analytics dashboard page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_ag_grid


def create_stat_card(metric: str, value: str, change: str, status: str) -> dmc.Card:
    """Create a statistics card.

    Args:
        metric: Metric name
        value: Metric value
        change: Change percentage
        status: Status indicator

    Returns:
        Styled statistics card
    """
    status_colors = {"Good": "green", "Stable": "blue", "Warning": "yellow", "Critical": "red"}
    change_color = "green" if "+" in change else "red" if "-" in change else "gray"

    return dmc.Card(
        [
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Badge(status, color=status_colors.get(status, "gray"), variant="dot", size="sm"),
                            dmc.Text(metric, size="sm", c="dimmed", fw=500),
                        ],
                        justify="space-between",
                    ),
                    dmc.Title(value, order=2),
                    dmc.Group(
                        [
                            dmc.Text(
                                change,
                                size="sm",
                                c=change_color,
                                fw=600,
                            ),
                            dmc.Text("vs last period", size="xs", c="dimmed"),
                        ],
                        gap="xs",
                    ),
                ],
                gap="sm",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="lg",
        p="lg",
        className="scale-in",
    )


def create_analytics_layout() -> html.Div:
    """Create the analytics dashboard page layout.

    Returns:
        Analytics page layout component
    """
    # Sample analytics data
    metrics_summary_columns = [
        {"field": "metric", "headerName": "Metric", "width": 200},
        {"field": "value", "headerName": "Value", "width": 120},
        {"field": "change", "headerName": "Change", "width": 120},
        {"field": "status", "headerName": "Status", "width": 120},
        {"field": "lastUpdated", "headerName": "Last Updated", "flex": 1},
    ]

    metrics_summary_data = [
        {
            "metric": "Total Users",
            "value": "1,234",
            "change": "+12%",
            "status": "Good",
            "lastUpdated": "2 minutes ago",
        },
        {
            "metric": "Active Projects",
            "value": "45",
            "change": "+8%",
            "status": "Good",
            "lastUpdated": "5 minutes ago",
        },
        {
            "metric": "Data Sources",
            "value": "12",
            "change": "0%",
            "status": "Stable",
            "lastUpdated": "10 minutes ago",
        },
        {
            "metric": "API Calls",
            "value": "23,456",
            "change": "+23%",
            "status": "Good",
            "lastUpdated": "1 minute ago",
        },
        {
            "metric": "Model Accuracy",
            "value": "94.2%",
            "change": "+2.1%",
            "status": "Good",
            "lastUpdated": "15 minutes ago",
        },
    ]

    return html.Div(
        [
            dmc.Stack(
                [
                    # Page header
                    dmc.Group(
                        [
                            dmc.Stack(
                                [
                                    dmc.Title("Analytics Dashboard", order=2),
                                    dmc.Text("Real-time insights and performance metrics", c="dimmed", size="sm"),
                                ],
                                gap=4,
                            ),
                            dmc.Group(
                                [
                                    dmc.SegmentedControl(
                                        id="analytics-timeframe",
                                        value="7d",
                                        data=[
                                            {"label": "24h", "value": "24h"},
                                            {"label": "7d", "value": "7d"},
                                            {"label": "30d", "value": "30d"},
                                            {"label": "90d", "value": "90d"},
                                        ],
                                    ),
                                    dmc.Button(
                                        "Export",
                                        leftSection=DashIconify(icon="tabler:download", width=16),
                                        variant="light",
                                    ),
                                ],
                                gap="sm",
                            ),
                        ],
                        justify="space-between",
                        mb="md",
                    ),
                    # Key metrics cards
                    dmc.SimpleGrid(
                        cols={"base": 1, "sm": 2, "md": 4},
                        spacing="md",
                        children=[
                            create_stat_card("Total Users", "1,234", "+12%", "Good"),
                            create_stat_card("Active Projects", "45", "+8%", "Good"),
                            create_stat_card("Data Sources", "12", "0%", "Stable"),
                            create_stat_card("API Calls", "23.4K", "+23%", "Good"),
                        ],
                    ),
                    # Charts section
                    dmc.Grid(
                        [
                            dmc.GridCol(
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                dmc.Stack(
                                                    [
                                                        dmc.Title("Usage Trends", order=4),
                                                        dmc.Text("Last 7 days", size="sm", c="dimmed"),
                                                    ],
                                                    gap=4,
                                                ),
                                                dmc.ActionIcon(
                                                    DashIconify(icon="tabler:dots", width=18),
                                                    variant="subtle",
                                                    size="lg",
                                                ),
                                            ],
                                            justify="space-between",
                                            mb="md",
                                        ),
                                        dmc.Center(
                                            dmc.Stack(
                                                [
                                                    dmc.ThemeIcon(
                                                        DashIconify(icon="tabler:chart-line", width=60),
                                                        size=100,
                                                        radius="md",
                                                        variant="light",
                                                        color="blue",
                                                    ),
                                                    dmc.Text("Chart visualization placeholder", c="dimmed", size="sm"),
                                                    dmc.Text(
                                                        "Connect to your data source to see trends",
                                                        c="dimmed",
                                                        size="xs",
                                                        ta="center",
                                                    ),
                                                ],
                                                gap="md",
                                                align="center",
                                            ),
                                            style={"minHeight": "350px"},
                                        ),
                                    ],
                                    withBorder=True,
                                    shadow="sm",
                                    radius="lg",
                                    p="lg",
                                    className="fade-in",
                                ),
                                span={"base": 12, "md": 6},
                            ),
                            dmc.GridCol(
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                dmc.Stack(
                                                    [
                                                        dmc.Title("Performance Metrics", order=4),
                                                        dmc.Text("Model accuracy over time", size="sm", c="dimmed"),
                                                    ],
                                                    gap=4,
                                                ),
                                                dmc.ActionIcon(
                                                    DashIconify(icon="tabler:dots", width=18),
                                                    variant="subtle",
                                                    size="lg",
                                                ),
                                            ],
                                            justify="space-between",
                                            mb="md",
                                        ),
                                        dmc.Center(
                                            dmc.Stack(
                                                [
                                                    dmc.ThemeIcon(
                                                        DashIconify(icon="tabler:chart-bar", width=60),
                                                        size=100,
                                                        radius="md",
                                                        variant="light",
                                                        color="green",
                                                    ),
                                                    dmc.Text("Chart visualization placeholder", c="dimmed", size="sm"),
                                                    dmc.Text(
                                                        "Track your model performance metrics",
                                                        c="dimmed",
                                                        size="xs",
                                                        ta="center",
                                                    ),
                                                ],
                                                gap="md",
                                                align="center",
                                            ),
                                            style={"minHeight": "350px"},
                                        ),
                                    ],
                                    withBorder=True,
                                    shadow="sm",
                                    radius="lg",
                                    p="lg",
                                    className="fade-in",
                                ),
                                span={"base": 12, "md": 6},
                            ),
                        ],
                        gutter="md",
                    ),
                    # Metrics summary table
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    dmc.Title("Detailed Metrics", order=4),
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
                                grid_id="metrics-summary-grid",
                                column_defs=metrics_summary_columns,
                                row_data=metrics_summary_data,
                                pagination=False,
                            ),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="lg",
                        p="lg",
                        className="slide-in",
                    ),
                ],
                gap="lg",
            )
        ]
    )
