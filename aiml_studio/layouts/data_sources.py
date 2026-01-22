"""Data Sources management page for AIML Studio.

This module provides an interface for managing data sources used in ML experiments.
It includes an interactive AG Grid table with filtering, sorting, and pagination.

Features:
    - Interactive data table with AG Grid
    - Add, edit, and delete data sources
    - Filter and search capabilities
    - Connection status monitoring
"""

import dash_ag_grid as dag
import dash_mantine_components as dmc
import pandas as pd
from dash import html


def _generate_sample_data_sources() -> pd.DataFrame:
    """Generate sample data sources for the table.

    Returns:
        DataFrame containing sample data source information.
    """
    return pd.DataFrame(
        {
            "id": range(1, 9),
            "name": [
                "Production DB",
                "Staging DB",
                "Data Lake S3",
                "Analytics Warehouse",
                "Customer API",
                "IoT Sensors",
                "External API",
                "CSV Files",
            ],
            "type": [
                "PostgreSQL",
                "PostgreSQL",
                "S3 Bucket",
                "Snowflake",
                "REST API",
                "MQTT",
                "REST API",
                "File System",
            ],
            "status": [
                "Connected",
                "Connected",
                "Connected",
                "Disconnected",
                "Connected",
                "Connected",
                "Error",
                "Connected",
            ],
            "records": [
                "1.2M",
                "850K",
                "5.6TB",
                "3.2TB",
                "45K",
                "2.1M",
                "120K",
                "25K",
            ],
            "last_sync": [
                "2 min ago",
                "5 min ago",
                "1 hour ago",
                "N/A",
                "10 min ago",
                "30 sec ago",
                "N/A",
                "3 hours ago",
            ],
        }
    )


def _create_column_defs() -> list[dict]:
    """Create column definitions for AG Grid.

    Returns:
        List of column definition dictionaries for AG Grid.
    """
    return [
        {
            "field": "id",
            "headerName": "ID",
            "width": 80,
            "filter": "agNumberColumnFilter",
        },
        {
            "field": "name",
            "headerName": "Data Source Name",
            "filter": "agTextColumnFilter",
            "minWidth": 200,
        },
        {
            "field": "type",
            "headerName": "Type",
            "filter": "agTextColumnFilter",
            "minWidth": 150,
        },
        {
            "field": "status",
            "headerName": "Status",
            "filter": "agTextColumnFilter",
            "cellStyle": {
                "styleConditions": [
                    {
                        "condition": "params.value === 'Connected'",
                        "style": {"color": "#40c057", "fontWeight": "bold"},
                    },
                    {
                        "condition": "params.value === 'Disconnected'",
                        "style": {"color": "#868e96", "fontWeight": "bold"},
                    },
                    {
                        "condition": "params.value === 'Error'",
                        "style": {"color": "#fa5252", "fontWeight": "bold"},
                    },
                ]
            },
        },
        {
            "field": "records",
            "headerName": "Records",
            "filter": "agTextColumnFilter",
        },
        {
            "field": "last_sync",
            "headerName": "Last Sync",
            "filter": "agTextColumnFilter",
            "minWidth": 150,
        },
    ]


# Generate sample data
sample_data = _generate_sample_data_sources()

# Main layout for the data sources page
layout = dmc.Stack(
    children=[
        # Page header
        dmc.Group(
            children=[
                dmc.Stack(
                    children=[
                        dmc.Title("Data Sources", order=1),
                        dmc.Text(
                            "Manage and monitor your data connections",
                            size="sm",
                            c="dimmed",
                        ),
                    ],
                    gap="xs",
                ),
                dmc.Button(
                    "Add Data Source",
                    leftSection=html.I(className="fas fa-plus"),
                    color="blue",
                    variant="filled",
                ),
            ],
            justify="space-between",
            style={"marginBottom": "20px"},
        ),
        # Summary cards
        dmc.SimpleGrid(
            cols=4,
            spacing="lg",
            children=[
                dmc.Card(
                    children=[
                        dmc.Text("Total Sources", size="sm", c="dimmed"),
                        dmc.Title("8", order=2, style={"marginTop": "5px"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("Active Connections", size="sm", c="dimmed"),
                        dmc.Title("6", order=2, style={"marginTop": "5px", "color": "#40c057"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("Disconnected", size="sm", c="dimmed"),
                        dmc.Title("1", order=2, style={"marginTop": "5px", "color": "#868e96"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("Errors", size="sm", c="dimmed"),
                        dmc.Title("1", order=2, style={"marginTop": "5px", "color": "#fa5252"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
            ],
            style={"marginBottom": "20px"},
        ),
        # AG Grid table
        dmc.Card(
            children=[
                dag.AgGrid(
                    id="data-sources-grid",
                    rowData=sample_data.to_dict("records"),
                    columnDefs=_create_column_defs(),
                    defaultColDef={
                        "resizable": True,
                        "sortable": True,
                        "filter": True,
                    },
                    dashGridOptions={
                        "pagination": True,
                        "paginationPageSize": 10,
                        "rowSelection": "single",
                    },
                    style={"height": "500px"},
                )
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"padding": "20px"},
        ),
    ],
    gap="md",
)
