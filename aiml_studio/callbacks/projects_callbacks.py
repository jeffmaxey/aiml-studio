"""Projects page callbacks."""

from typing import Any

from dash import Input, Output, State, callback

from aiml_studio.utilities import create_download_link, export_to_csv, export_to_json, generate_export_filename


@callback(
    Output("download-projects-data", "data"),
    Input("export-projects-csv", "n_clicks"),
    Input("export-projects-json", "n_clicks"),
    State("projects-grid", "rowData"),
    prevent_initial_call=True,
)
def export_projects_data(
    csv_clicks: int | None, json_clicks: int | None, row_data: list[dict] | None
) -> dict[str, str] | None:
    """Export projects data to CSV or JSON.

    Args:
        csv_clicks: Number of clicks on CSV export button
        json_clicks: Number of clicks on JSON export button
        row_data: Current data from the projects grid

    Returns:
        Download data dictionary or None
    """
    if not row_data:
        return None

    # Determine which export format was requested
    from dash import ctx

    if not ctx.triggered:
        return None

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_id == "export-projects-csv":
        csv_data = export_to_csv(row_data)
        filename = generate_export_filename("projects", "csv")
        return create_download_link(csv_data, filename, "text/csv")

    if triggered_id == "export-projects-json":
        json_data = export_to_json(row_data)
        filename = generate_export_filename("projects", "json")
        return create_download_link(json_data, filename, "application/json")

    return None


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
