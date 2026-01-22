"""Projects page callbacks."""

from typing import Any

from dash import Input, Output, State, callback


@callback(
    Output("create-project-modal", "opened"),
    Input("create-project-button", "n_clicks"),
    State("create-project-modal", "opened"),
    prevent_initial_call=True,
)
def toggle_create_project_modal(n_clicks: int, opened: bool) -> bool:
    """Toggle the create project modal.

    Args:
        n_clicks: Number of clicks on create button
        opened: Current modal state

    Returns:
        Updated modal state
    """
    return not opened


@callback(
    Output("projects-grid", "rowData"),
    Input("save-project-button", "n_clicks"),
    State("project-name-input", "value"),
    State("project-description-input", "value"),
    State("project-status-select", "value"),
    prevent_initial_call=True,
)
def save_project(
    n_clicks: int,
    name: str,
    description: str,
    status: str,
) -> list[dict[str, Any]]:
    """Save a new project.

    Args:
        n_clicks: Number of clicks on save button
        name: Project name
        description: Project description
        status: Project status

    Returns:
        Updated projects list
    """
    # Placeholder for actual save logic
    return []
