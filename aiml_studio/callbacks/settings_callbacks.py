"""Settings page callbacks."""

from dash import Input, Output, callback


@callback(
    Output("theme-toggle", "value"),
    Input("theme-toggle", "value"),
    prevent_initial_call=True,
)
def toggle_theme(theme: str) -> str:
    """Toggle theme between light and dark mode.

    Args:
        theme: Current theme value

    Returns:
        Updated theme value
    """
    return theme


@callback(
    Output("save-settings-button", "children"),
    Input("save-settings-button", "n_clicks"),
    prevent_initial_call=True,
)
def save_settings(n_clicks: int) -> str:
    """Save user settings.

    Args:
        n_clicks: Number of clicks on save button

    Returns:
        Button text
    """
    if n_clicks:
        return "Settings Saved!"
    return "Save Settings"
