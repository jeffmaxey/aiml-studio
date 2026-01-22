"""Projects page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from aiml_studio.components import (
    create_confirm_modal,
    create_form_modal,
    create_help_icon,
    create_inline_alert,
    create_label_with_help,
    create_projects_grid,
    create_tooltip,
)
from aiml_studio.constants_help import FIELD_HELP, TOOLTIPS
from aiml_studio.settings import PROJECT_STATUSES


def create_project_stat_card(label: str, value: str, icon: str, color: str) -> dmc.Card:
    """Create a project statistics card.

    Args:
        label: Stat label
        value: Stat value
        icon: Icon identifier
        color: Color theme

    Returns:
        Statistics card
    """
    return dmc.Card(
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
                            dmc.Text(label, size="sm", c="dimmed", fw=500),
                            dmc.Title(value, order=2),
                        ],
                        gap=2,
                    ),
                ],
                gap="md",
                align="center",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="lg",
        p="lg",
        className="scale-in",
    )


def create_project_card(project: dict) -> dmc.Card:
    """Create a project card.

    Args:
        project: Project data

    Returns:
        Project card component
    """
    status_colors = {"Active": "green", "Completed": "blue", "Inactive": "gray"}
    status_icons = {"Active": "tabler:player-play", "Completed": "tabler:check", "Inactive": "tabler:player-pause"}

    return dmc.Card(
        [
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.ThemeIcon(
                                DashIconify(icon="tabler:folder-filled", width=24),
                                size="lg",
                                radius="md",
                                variant="light",
                                color="blue",
                            ),
                            dmc.Badge(
                                [
                                    DashIconify(icon=status_icons.get(project["status"], "tabler:circle"), width=12),
                                    " ",
                                    project["status"],
                                ],
                                color=status_colors.get(project["status"], "gray"),
                                variant="light",
                            ),
                        ],
                        justify="space-between",
                    ),
                    dmc.Stack(
                        [
                            dmc.Title(project["name"], order=5, fw=700),
                            dmc.Text(project["description"], size="sm", c="dimmed", lineClamp=2),
                        ],
                        gap="xs",
                    ),
                    dmc.Divider(),
                    dmc.Group(
                        [
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:calendar", width=14, color="gray"),
                                    dmc.Text(f"Created: {project['created']}", size="xs", c="dimmed"),
                                ],
                                gap=4,
                            ),
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:clock", width=14, color="gray"),
                                    dmc.Text(f"Updated: {project['modified']}", size="xs", c="dimmed"),
                                ],
                                gap=4,
                            ),
                        ],
                        gap="md",
                        wrap="wrap",
                    ),
                    dmc.Group(
                        [
                            dmc.ActionIcon(
                                DashIconify(icon="tabler:eye", width=16),
                                variant="light",
                                color="blue",
                                size="md",
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="tabler:edit", width=16),
                                variant="light",
                                color="blue",
                                size="md",
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="tabler:trash", width=16),
                                variant="light",
                                color="red",
                                size="md",
                            ),
                        ],
                        gap="xs",
                        justify="flex-end",
                    ),
                ],
                gap="md",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="lg",
        p="lg",
        style={"height": "100%"},
        className="scale-in",
    )


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
            "description": "ML model to predict customer churn using historical data and behavioral patterns",
        },
        {
            "name": "Sales Forecasting",
            "status": "Active",
            "created": "2024-01-10",
            "modified": "2024-01-20",
            "description": "Time series forecasting for sales data with seasonal analysis",
        },
        {
            "name": "Sentiment Analysis",
            "status": "Completed",
            "created": "2023-12-20",
            "modified": "2024-01-05",
            "description": "Analyze customer feedback sentiment from reviews and support tickets",
        },
        {
            "name": "Image Classification",
            "status": "Inactive",
            "created": "2023-11-15",
            "modified": "2023-12-10",
            "description": "Classify product images into categories using deep learning",
        },
    ]

    projects_grid = create_projects_grid()
    projects_grid.rowData = sample_projects

    return html.Div([
        dmc.Stack(
            [
                # Page header
                dmc.Group(
                    [
                        dmc.Stack(
                            [
                                dmc.Group(
                                    [
                                        dmc.Title("Projects", order=2),
                                        create_help_icon("Create and manage your machine learning projects"),
                                    ],
                                    gap="xs",
                                ),
                                dmc.Text("Manage your machine learning projects", c="dimmed", size="sm"),
                            ],
                            gap=4,
                        ),
                        create_tooltip(
                            dmc.Button(
                                "Create New Project",
                                leftSection=DashIconify(icon="tabler:plus", width=18),
                                id="create-project-button",
                                variant="gradient",
                                gradient={"from": "blue", "to": "cyan", "deg": 135},
                            ),
                            label=TOOLTIPS.get("project_create", "Create a new machine learning project"),
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
                        create_project_stat_card("Total Projects", "4", "tabler:folder", "blue"),
                        create_project_stat_card("Active", "2", "tabler:player-play", "green"),
                        create_project_stat_card("Completed", "1", "tabler:check", "teal"),
                        create_project_stat_card("Inactive", "1", "tabler:player-pause", "gray"),
                    ],
                ),
                # View toggle and project cards
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                dmc.Title("Your Projects", order=4),
                                dmc.Group(
                                    [
                                        dmc.SegmentedControl(
                                            id="project-view-toggle",
                                            value="cards",
                                            data=[
                                                {"label": "Cards", "value": "cards"},
                                                {"label": "Table", "value": "table"},
                                            ],
                                        ),
                                        dmc.ActionIcon(
                                            DashIconify(icon="tabler:filter", width=18),
                                            variant="light",
                                            size="lg",
                                        ),
                                    ],
                                    gap="sm",
                                ),
                            ],
                            justify="space-between",
                            mb="lg",
                        ),
                        dmc.SimpleGrid(
                            id="projects-cards-view",
                            cols={"base": 1, "sm": 2, "lg": 3},
                            spacing="md",
                            children=[create_project_card(project) for project in sample_projects],
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="lg",
                    p="lg",
                ),
                # Projects table
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                dmc.Title("All Projects (Table View)", order=4),
                                dmc.Group(
                                    [
                                        dmc.ActionIcon(
                                            DashIconify(icon="tabler:refresh", width=18),
                                            variant="light",
                                            size="lg",
                                        ),
                                        dmc.ActionIcon(
                                            DashIconify(icon="tabler:download", width=18),
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
                        projects_grid,
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="lg",
                    p="lg",
                    className="slide-in",
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
                            leftSection=DashIconify(icon="tabler:folder", width=16),
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
                            leftSection=DashIconify(icon="tabler:player-play", width=16),
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
                                    leftSection=DashIconify(icon="tabler:check", width=16),
                                ),
                            ],
                            justify="flex-end",
                            mt="md",
                        ),
                    ],
                    gap="md",
                )
            ],
        ),
    ])
