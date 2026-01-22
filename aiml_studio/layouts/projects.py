"""Projects page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import create_projects_grid
from aiml_studio.settings import PROJECT_STATUSES


def create_projects_layout() -> html.Div:
    """Create the projects page layout.

    Returns:
        Projects page layout component
    """
    # Sample projects
    sample_projects = [
        {
            "name": "Customer Churn Prediction",
            "status": "Active",
            "created": "2024-01-15",
            "modified": "2024-01-22",
            "description": "ML model to predict customer churn",
        },
        {
            "name": "Sales Forecasting",
            "status": "Active",
            "created": "2024-01-10",
            "modified": "2024-01-20",
            "description": "Time series forecasting for sales data",
        },
        {
            "name": "Sentiment Analysis",
            "status": "Completed",
            "created": "2023-12-20",
            "modified": "2024-01-05",
            "description": "Analyze customer feedback sentiment",
        },
        {
            "name": "Image Classification",
            "status": "Inactive",
            "created": "2023-11-15",
            "modified": "2023-12-10",
            "description": "Classify product images",
        },
    ]

    projects_grid = create_projects_grid()
    projects_grid.rowData = sample_projects

    return html.Div([
        dmc.Stack(
            [
                # Header with create button
                dmc.Group(
                    [
                        dmc.Title("Projects", order=2),
                        dmc.Button(
                            "Create New Project",
                            leftSection=DashIconify(icon="tabler:plus", width=20),
                            id="create-project-button",
                        ),
                    ],
                    justify="space-between",
                    mb="md",
                ),
                # Project statistics
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 4},
                    spacing="md",
                    children=[
                        dmc.Card(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:folder", width=30, color="blue"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Total Projects", size="sm", c="dimmed"),
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
                                        DashIconify(icon="tabler:player-play", width=30, color="green"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Active", size="sm", c="dimmed"),
                                                dmc.Title("2", order=3),
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
                                        DashIconify(icon="tabler:check", width=30, color="teal"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Completed", size="sm", c="dimmed"),
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
                                        DashIconify(icon="tabler:player-pause", width=30, color="gray"),
                                        dmc.Stack(
                                            [
                                                dmc.Text("Inactive", size="sm", c="dimmed"),
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
                    ],
                ),
                # Project cards view
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                dmc.Title("Project Cards", order=4),
                                dmc.SegmentedControl(
                                    id="project-view-toggle",
                                    value="grid",
                                    data=[
                                        {"label": "Cards", "value": "cards"},
                                        {"label": "Table", "value": "table"},
                                    ],
                                ),
                            ],
                            justify="space-between",
                            mb="md",
                        ),
                        dmc.SimpleGrid(
                            id="projects-cards-view",
                            cols={"base": 1, "sm": 2, "md": 3},
                            spacing="md",
                            children=[
                                dmc.Card(
                                    [
                                        dmc.Stack(
                                            [
                                                dmc.Group(
                                                    [
                                                        DashIconify(
                                                            icon="tabler:folder-filled", width=24, color="blue"
                                                        ),
                                                        dmc.Badge(
                                                            project["status"],
                                                            color="green"
                                                            if project["status"] == "Active"
                                                            else "blue"
                                                            if project["status"] == "Completed"
                                                            else "gray",
                                                        ),
                                                    ],
                                                    justify="space-between",
                                                ),
                                                dmc.Title(project["name"], order=5),
                                                dmc.Text(project["description"], size="sm", c="dimmed"),
                                                dmc.Divider(),
                                                dmc.Group(
                                                    [
                                                        dmc.Text(
                                                            f"Created: {project['created']}", size="xs", c="dimmed"
                                                        ),
                                                        dmc.Text(
                                                            f"Modified: {project['modified']}", size="xs", c="dimmed"
                                                        ),
                                                    ],
                                                    gap="xs",
                                                    wrap="wrap",
                                                ),
                                                dmc.Group(
                                                    [
                                                        dmc.ActionIcon(
                                                            DashIconify(icon="tabler:eye", width=16),
                                                            variant="light",
                                                            size="sm",
                                                        ),
                                                        dmc.ActionIcon(
                                                            DashIconify(icon="tabler:edit", width=16),
                                                            variant="light",
                                                            size="sm",
                                                        ),
                                                        dmc.ActionIcon(
                                                            DashIconify(icon="tabler:trash", width=16),
                                                            variant="light",
                                                            color="red",
                                                            size="sm",
                                                        ),
                                                    ],
                                                    gap="xs",
                                                ),
                                            ],
                                            gap="sm",
                                        )
                                    ],
                                    withBorder=True,
                                    shadow="sm",
                                    radius="md",
                                    p="md",
                                )
                                for project in sample_projects
                            ],
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
                # Projects table
                dmc.Card(
                    [
                        dmc.Title("All Projects", order=4, mb="md"),
                        projects_grid,
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
            ],
            gap="lg",
        ),
        # Create Project Modal
        dmc.Modal(
            id="create-project-modal",
            title="Create New Project",
            size="lg",
            children=[
                dmc.Stack(
                    [
                        dmc.TextInput(
                            label="Project Name",
                            placeholder="Enter project name",
                            id="project-name-input",
                            required=True,
                        ),
                        dmc.Textarea(
                            label="Description",
                            placeholder="Enter project description",
                            id="project-description-input",
                            minRows=3,
                            required=True,
                        ),
                        dmc.Select(
                            label="Project Status",
                            placeholder="Select status",
                            id="project-status-select",
                            data=[{"label": s, "value": s} for s in PROJECT_STATUSES],
                            value="Active",
                            required=True,
                        ),
                        dmc.MultiSelect(
                            label="Tags",
                            placeholder="Add tags",
                            id="project-tags-input",
                            data=[
                                {"label": "Machine Learning", "value": "ml"},
                                {"label": "Data Analysis", "value": "analysis"},
                                {"label": "Prediction", "value": "prediction"},
                                {"label": "Classification", "value": "classification"},
                            ],
                        ),
                        dmc.Group(
                            [
                                dmc.Button(
                                    "Cancel",
                                    variant="subtle",
                                    id="cancel-project-button",
                                ),
                                dmc.Button(
                                    "Create Project",
                                    id="save-project-button",
                                ),
                            ],
                            justify="flex-end",
                        ),
                    ],
                    gap="md",
                )
            ],
        ),
    ])
