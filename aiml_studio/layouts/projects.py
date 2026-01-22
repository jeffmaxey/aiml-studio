"""Projects management page for AIML Studio.

This module provides an interface for managing ML projects and experiments.
It includes an interactive AG Grid table with project information and status.

Features:
    - Interactive project table with AG Grid
    - Project status tracking
    - Filter and search capabilities
    - Quick actions for project management
"""

import dash_ag_grid as dag
import dash_mantine_components as dmc
import pandas as pd
from dash import html


def _generate_sample_projects() -> pd.DataFrame:
    """Generate sample project data for the table.

    Returns:
        DataFrame containing sample project information.
    """
    return pd.DataFrame(
        {
            "id": range(1, 11),
            "name": [
                "Customer Churn Prediction",
                "Fraud Detection Model",
                "Recommendation Engine",
                "Image Classification",
                "Sentiment Analysis",
                "Sales Forecasting",
                "Anomaly Detection",
                "Text Summarization",
                "Price Optimization",
                "Demand Prediction",
            ],
            "owner": [
                "John Doe",
                "Jane Smith",
                "Bob Johnson",
                "Alice Williams",
                "Charlie Brown",
                "Diana Prince",
                "Eve Davis",
                "Frank Miller",
                "Grace Lee",
                "Henry Wilson",
            ],
            "status": [
                "Active",
                "Active",
                "Completed",
                "In Progress",
                "Active",
                "Completed",
                "In Progress",
                "Active",
                "On Hold",
                "Active",
            ],
            "experiments": [15, 23, 42, 8, 19, 35, 12, 6, 20, 14],
            "accuracy": [
                "92.5%",
                "95.8%",
                "88.3%",
                "91.2%",
                "89.7%",
                "94.1%",
                "87.6%",
                "90.4%",
                "N/A",
                "93.2%",
            ],
            "created": [
                "2024-01-15",
                "2024-02-20",
                "2023-11-10",
                "2024-03-05",
                "2024-01-28",
                "2023-12-01",
                "2024-02-15",
                "2024-03-10",
                "2023-10-20",
                "2024-02-01",
            ],
            "last_updated": [
                "2 days ago",
                "1 day ago",
                "2 weeks ago",
                "3 hours ago",
                "5 days ago",
                "1 month ago",
                "1 week ago",
                "4 hours ago",
                "3 months ago",
                "6 days ago",
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
            "width": 70,
            "filter": "agNumberColumnFilter",
        },
        {
            "field": "name",
            "headerName": "Project Name",
            "filter": "agTextColumnFilter",
            "minWidth": 250,
            "cellStyle": {"fontWeight": "500"},
        },
        {
            "field": "owner",
            "headerName": "Owner",
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
                        "condition": "params.value === 'Active'",
                        "style": {"color": "#40c057", "fontWeight": "bold"},
                    },
                    {
                        "condition": "params.value === 'Completed'",
                        "style": {"color": "#228be6", "fontWeight": "bold"},
                    },
                    {
                        "condition": "params.value === 'In Progress'",
                        "style": {"color": "#fab005", "fontWeight": "bold"},
                    },
                    {
                        "condition": "params.value === 'On Hold'",
                        "style": {"color": "#868e96", "fontWeight": "bold"},
                    },
                ]
            },
        },
        {
            "field": "experiments",
            "headerName": "Experiments",
            "filter": "agNumberColumnFilter",
            "width": 130,
        },
        {
            "field": "accuracy",
            "headerName": "Best Accuracy",
            "filter": "agTextColumnFilter",
            "width": 140,
        },
        {
            "field": "created",
            "headerName": "Created",
            "filter": "agDateColumnFilter",
            "minWidth": 120,
        },
        {
            "field": "last_updated",
            "headerName": "Last Updated",
            "filter": "agTextColumnFilter",
            "minWidth": 130,
        },
    ]


# Generate sample data
sample_data = _generate_sample_projects()

# Main layout for the projects page
layout = dmc.Stack(
    children=[
        # Page header
        dmc.Group(
            children=[
                dmc.Stack(
                    children=[
                        dmc.Title("Projects", order=1),
                        dmc.Text(
                            "Manage your ML projects and experiments",
                            size="sm",
                            c="dimmed",
                        ),
                    ],
                    gap="xs",
                ),
                dmc.Button(
                    "Create Project",
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
                        dmc.Text("Total Projects", size="sm", c="dimmed"),
                        dmc.Title("10", order=2, style={"marginTop": "5px"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("Active", size="sm", c="dimmed"),
                        dmc.Title("5", order=2, style={"marginTop": "5px", "color": "#40c057"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("In Progress", size="sm", c="dimmed"),
                        dmc.Title("2", order=2, style={"marginTop": "5px", "color": "#fab005"}),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "15px"},
                ),
                dmc.Card(
                    children=[
                        dmc.Text("Completed", size="sm", c="dimmed"),
                        dmc.Title("2", order=2, style={"marginTop": "5px", "color": "#228be6"}),
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
                    id="projects-grid",
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
