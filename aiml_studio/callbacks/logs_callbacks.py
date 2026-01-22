"""Logs page callbacks."""

from typing import Any

from dash import Input, Output, callback


@callback(
    Output("logs-grid", "rowData"),
    Input("refresh-logs-button", "n_clicks"),
    prevent_initial_call=True,
)
def refresh_logs(n_clicks: int) -> list[dict[str, Any]]:
    """Refresh logs data.

    Args:
        n_clicks: Number of clicks on refresh button

    Returns:
        Updated logs data
    """
    # Placeholder for actual log fetching logic
    return [
        {"timestamp": "2024-01-22 10:30:15", "level": "INFO", "message": "Application started successfully"},
        {"timestamp": "2024-01-22 10:30:20", "level": "INFO", "message": "User authenticated: admin@example.com"},
    ]


@callback(
    Output("logs-grid", "rowData", allow_duplicate=True),
    Input("clear-logs-button", "n_clicks"),
    prevent_initial_call=True,
)
def clear_logs(n_clicks: int) -> list[dict[str, Any]]:
    """Clear all logs.

    Args:
        n_clicks: Number of clicks on clear button

    Returns:
        Empty logs data
    """
    return []
