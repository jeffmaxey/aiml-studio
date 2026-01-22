"""Projects page callbacks."""

from typing import Any

from dash import Input, Output, State, callback

from aiml_studio.utilities import (
    create_download_link,
    export_to_csv,
    export_to_json,
    generate_export_filename,
    validate_min_length,
    validate_required,
)


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
    [
        Output("projects-grid", "rowData"),
        Output("project-name-input", "error"),
        Output("project-description-input", "error"),
        Output("create-project-modal", "opened", allow_duplicate=True),
    ],
    Input("save-project-button", "n_clicks"),
    [
        State("project-name-input", "value"),
        State("project-description-input", "value"),
        State("project-status-select", "value"),
    ],
    prevent_initial_call=True,
)
def save_project(
    n_clicks: int,
    name: str | None,
    description: str | None,
    status: str,
) -> tuple[list[dict[str, Any]], str, str, bool]:
    """Save a new project with validation.

    Args:
        n_clicks: Number of clicks on save button
        name: Project name
        description: Project description
        status: Project status

    Returns:
        Tuple of (updated_projects, name_error, description_error, modal_opened)
    """
    from dash import no_update

    # Validate project name
    name_valid, name_error = validate_required(name, "Project name")
    if name_valid:
        name_valid, name_error = validate_min_length(name or "", 3, "Project name")

    # Validate project description
    desc_valid, desc_error = validate_required(description, "Description")
    if desc_valid:
        desc_valid, desc_error = validate_min_length(description or "", 10, "Description")

    # If validation fails, return errors and keep modal open
    if not name_valid or not desc_valid:
        return no_update, name_error, desc_error, True

    # Validation passed - close modal and clear errors
    # In a real implementation, this would save to database
    return no_update, "", "", False
