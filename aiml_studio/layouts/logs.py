"""Logs page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_logs_grid


def create_logs_layout() -> html.Div:
    """Create the logs page layout.

    Returns:
        Logs page layout component
    """
    # Sample log data
    sample_logs = [
        {"timestamp": "2024-01-22 10:30:15", "level": "INFO", "message": "Application started successfully"},
        {"timestamp": "2024-01-22 10:30:20", "level": "INFO", "message": "User authenticated: admin@example.com"},
        {"timestamp": "2024-01-22 10:35:10", "level": "WARNING", "message": "High memory usage detected: 85%"},
        {"timestamp": "2024-01-22 10:40:05", "level": "INFO", "message": "Data source connection established"},
        {"timestamp": "2024-01-22 10:45:30", "level": "ERROR", "message": "Failed to fetch data from API endpoint"},
        {"timestamp": "2024-01-22 10:50:00", "level": "DEBUG", "message": "Cache cleared successfully"},
        {"timestamp": "2024-01-22 10:55:45", "level": "INFO", "message": "Project 'ML-Analysis' created"},
    ]

    logs_grid = create_logs_grid()
    logs_grid.rowData = sample_logs

    return html.Div(
        [
            dmc.Stack(
                [
                    # Header with controls
                    dmc.Group(
                        [
                            dmc.Title("System Logs", order=2),
                            dmc.Group(
                                [
                                    dmc.Button(
                                        "Refresh",
                                        leftSection=DashIconify(icon="tabler:refresh", width=20),
                                        variant="light",
                                        id="refresh-logs-button",
                                    ),
                                    dmc.Button(
                                        "Clear Logs",
                                        leftSection=DashIconify(icon="tabler:trash", width=20),
                                        variant="outline",
                                        color="red",
                                        id="clear-logs-button",
                                    ),
                                ],
                                gap="sm",
                            ),
                        ],
                        justify="space-between",
                        mb="md",
                    ),
                    # Filters
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:filter", width=24),
                                    dmc.Title("Filters", order=5),
                                ],
                                gap="sm",
                                mb="md",
                            ),
                            dmc.Group(
                                [
                                    dmc.MultiSelect(
                                        label="Log Level",
                                        placeholder="Select levels",
                                        id="log-level-filter",
                                        data=[
                                            {"label": "DEBUG", "value": "DEBUG"},
                                            {"label": "INFO", "value": "INFO"},
                                            {"label": "WARNING", "value": "WARNING"},
                                            {"label": "ERROR", "value": "ERROR"},
                                            {"label": "CRITICAL", "value": "CRITICAL"},
                                        ],
                                        style={"minWidth": 200},
                                    ),
                                    dmc.TextInput(
                                        label="Search",
                                        placeholder="Search in messages...",
                                        id="log-search-input",
                                        leftSection=DashIconify(icon="tabler:search", width=20),
                                        style={"minWidth": 300},
                                    ),
                                    dmc.Stack(
                                        [
                                            dmc.Text("From Date", size="sm", fw=500),
                                            dmc.DatePicker(
                                                id="log-from-date",
                                            ),
                                        ],
                                        gap="xs",
                                        style={"minWidth": 150},
                                    ),
                                    dmc.Stack(
                                        [
                                            dmc.Text("To Date", size="sm", fw=500),
                                            dmc.DatePicker(
                                                id="log-to-date",
                                            ),
                                        ],
                                        gap="xs",
                                        style={"minWidth": 150},
                                    ),
                                ],
                                gap="md",
                                wrap="wrap",
                            ),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="lg",
                    ),
                    # Log statistics
                    dmc.SimpleGrid(
                        cols={"base": 1, "sm": 2, "md": 5},
                        spacing="md",
                        children=[
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:info-circle", width=20, color="blue"),
                                            dmc.Text("INFO", size="sm", c="dimmed"),
                                        ],
                                        justify="space-between",
                                    ),
                                    dmc.Title("4", order=3, mt="xs"),
                                ],
                                withBorder=True,
                                p="md",
                            ),
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:alert-triangle", width=20, color="yellow"),
                                            dmc.Text("WARNING", size="sm", c="dimmed"),
                                        ],
                                        justify="space-between",
                                    ),
                                    dmc.Title("1", order=3, mt="xs"),
                                ],
                                withBorder=True,
                                p="md",
                            ),
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:x-circle", width=20, color="red"),
                                            dmc.Text("ERROR", size="sm", c="dimmed"),
                                        ],
                                        justify="space-between",
                                    ),
                                    dmc.Title("1", order=3, mt="xs"),
                                ],
                                withBorder=True,
                                p="md",
                            ),
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:bug", width=20, color="gray"),
                                            dmc.Text("DEBUG", size="sm", c="dimmed"),
                                        ],
                                        justify="space-between",
                                    ),
                                    dmc.Title("1", order=3, mt="xs"),
                                ],
                                withBorder=True,
                                p="md",
                            ),
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:list", width=20),
                                            dmc.Text("TOTAL", size="sm", c="dimmed"),
                                        ],
                                        justify="space-between",
                                    ),
                                    dmc.Title("7", order=3, mt="xs"),
                                ],
                                withBorder=True,
                                p="md",
                            ),
                        ],
                    ),
                    # Logs table
                    dmc.Card(
                        [logs_grid],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="md",
                    ),
                ],
                gap="lg",
            )
        ]
    )
