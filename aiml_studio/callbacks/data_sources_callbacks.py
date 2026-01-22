"""Data sources page callbacks."""

from typing import Any

from dash import Input, Output, State, callback


@callback(
    Output("add-data-source-modal", "opened"),
    Input("add-data-source-button", "n_clicks"),
    State("add-data-source-modal", "opened"),
    prevent_initial_call=True,
)
def toggle_add_data_source_modal(n_clicks: int, opened: bool) -> bool:
    """Toggle the add data source modal.

    Args:
        n_clicks: Number of clicks on add button
        opened: Current modal state

    Returns:
        Updated modal state
    """
    return not opened


@callback(
    Output("data-sources-grid", "rowData"),
    Input("save-data-source-button", "n_clicks"),
    State("data-source-name-input", "value"),
    State("data-source-type-select", "value"),
    State("data-source-connection-input", "value"),
    prevent_initial_call=True,
)
def save_data_source(
    n_clicks: int,
    name: str,
    source_type: str,
    connection: str,
) -> list[dict[str, Any]]:
    """Save a new data source.

    Args:
        n_clicks: Number of clicks on save button
        name: Data source name
        source_type: Data source type
        connection: Connection string

    Returns:
        Updated data sources list
    """
    # Placeholder for actual save logic
    return []
