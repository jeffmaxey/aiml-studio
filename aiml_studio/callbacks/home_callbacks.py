"""Home page callbacks."""

from typing import Any

from dash import Input, Output, callback


@callback(
    Output({"type": "action-card", "index": Input("_pages_location", "pathname")}, "n_clicks"),
    Input({"type": "action-card", "index": Input("_pages_location", "pathname")}, "n_clicks"),
    prevent_initial_call=True,
)
def navigate_to_action(n_clicks: int) -> Any:
    """Navigate to action page when card is clicked.

    Args:
        n_clicks: Number of clicks on the card

    Returns:
        Navigation action
    """
    # This would typically use dcc.Location or similar for navigation
    # For now, this is a placeholder
    return None
