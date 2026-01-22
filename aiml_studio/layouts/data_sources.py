"""Data sources page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_data_sources_grid
from aiml_studio.settings import DATA_SOURCE_TYPES


def create_data_sources_layout() -> html.Div:
    """Create the data sources page layout.

    Returns:
        Data sources page layout component
    """
    # Sample data sources
    sample_data_sources = [
        {
            "name": "Production DB",
            "type": "PostgreSQL",
            "status": "Connected",
            "connection": "postgresql://prod.example.com:5432/maindb",
        },
        {
            "name": "Analytics DB",
            "type": "MySQL",
            "status": "Connected",
            "connection": "mysql://analytics.example.com:3306/analytics",
        },
        {
            "name": "Development DB",
            "type": "SQLite",
            "status": "Connected",
            "connection": "sqlite:///dev.db",
        },
        {
            "name": "External API",
            "type": "API",
            "status": "Disconnected",
            "connection": "https://api.example.com/v1",
        },
    ]

    data_sources_grid = create_data_sources_grid()
    data_sources_grid.rowData = sample_data_sources

    return html.Div(
        [
            dmc.Stack(
                [
                    # Header with add button
                    dmc.Group(
                        [
                            dmc.Title("Data Sources", order=2),
                            dmc.Button(
                                "Add Data Source",
                                leftSection=DashIconify(icon="tabler:plus", width=20),
                                id="add-data-source-button",
                            ),
                        ],
                        justify="space-between",
                        mb="md",
                    ),
                    # Connection status overview
                    dmc.SimpleGrid(
                        cols={"base": 1, "sm": 2, "md": 4},
                        spacing="md",
                        children=[
                            dmc.Card(
                                [
                                    dmc.Group(
                                        [
                                            DashIconify(icon="tabler:database", width=30, color="blue"),
                                            dmc.Stack(
                                                [
                                                    dmc.Text("Total Sources", size="sm", c="dimmed"),
                                                    dmc.Title("4", order=3),
                                                ],
                                                gap=0,
                                            ),
                                        ],
                                        gap="md",
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
                                            DashIconify(icon="tabler:plug-connected", width=30, color="green"),
                                            dmc.Stack(
                                                [
                                                    dmc.Text("Connected", size="sm", c="dimmed"),
                                                    dmc.Title("3", order=3),
                                                ],
                                                gap=0,
                                            ),
                                        ],
                                        gap="md",
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
                                            DashIconify(icon="tabler:plug-x", width=30, color="red"),
                                            dmc.Stack(
                                                [
                                                    dmc.Text("Disconnected", size="sm", c="dimmed"),
                                                    dmc.Title("1", order=3),
                                                ],
                                                gap=0,
                                            ),
                                        ],
                                        gap="md",
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
                                            DashIconify(icon="tabler:activity", width=30, color="orange"),
                                            dmc.Stack(
                                                [
                                                    dmc.Text("Active Queries", size="sm", c="dimmed"),
                                                    dmc.Title("12", order=3),
                                                ],
                                                gap=0,
                                            ),
                                        ],
                                        gap="md",
                                    ),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                p="lg",
                            ),
                        ],
                    ),
                    # Data sources table
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    dmc.Title("Configured Data Sources", order=4),
                                    dmc.Group(
                                        [
                                            dmc.Button(
                                                "Test Connections",
                                                leftSection=DashIconify(icon="tabler:refresh", width=20),
                                                variant="light",
                                                id="test-connections-button",
                                            ),
                                        ],
                                        gap="sm",
                                    ),
                                ],
                                justify="space-between",
                                mb="md",
                            ),
                            data_sources_grid,
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="lg",
                    ),
                ],
                gap="lg",
            ),
            # Add Data Source Modal
            dmc.Modal(
                id="add-data-source-modal",
                title="Add Data Source",
                size="lg",
                children=[
                    dmc.Stack(
                        [
                            dmc.TextInput(
                                label="Data Source Name",
                                placeholder="Enter a name for this data source",
                                id="data-source-name-input",
                                required=True,
                            ),
                            dmc.Select(
                                label="Data Source Type",
                                placeholder="Select type",
                                id="data-source-type-select",
                                data=[{"label": t, "value": t} for t in DATA_SOURCE_TYPES],
                                required=True,
                            ),
                            dmc.TextInput(
                                label="Connection String",
                                placeholder="Enter connection details",
                                id="data-source-connection-input",
                                required=True,
                            ),
                            dmc.Textarea(
                                label="Description",
                                placeholder="Optional description",
                                id="data-source-description-input",
                                minRows=3,
                            ),
                            dmc.Group(
                                [
                                    dmc.Button(
                                        "Test Connection",
                                        variant="light",
                                        id="test-connection-button",
                                    ),
                                    dmc.Button(
                                        "Save",
                                        id="save-data-source-button",
                                    ),
                                ],
                                justify="flex-end",
                            ),
                        ],
                        gap="md",
                    )
                ],
            ),
        ]
    )
