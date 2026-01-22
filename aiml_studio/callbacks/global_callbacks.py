"""Global callbacks for persistence, notifications, and modals."""

from dash import Input, Output, State, callback, ctx, no_update


@callback(
    Output("user-preferences", "data"),
    [
        Input("theme-switch", "checked"),
        Input("rtl-switch", "checked"),
    ],
    State("user-preferences", "data"),
    prevent_initial_call=True,
)
def save_user_preferences(theme_checked: bool, rtl_checked: bool, current_prefs: dict) -> dict:
    """Save user preferences to localStorage.

    Args:
        theme_checked: Theme switch state (True for dark, False for light)
        rtl_checked: RTL switch state
        current_prefs: Current preferences data

    Returns:
        Updated preferences dictionary
    """
    if current_prefs is None:
        current_prefs = {}

    # Determine which input triggered the callback
    triggered = ctx.triggered_id

    if triggered == "theme-switch":
        current_prefs["theme"] = "dark" if theme_checked else "light"
    elif triggered == "rtl-switch":
        current_prefs["rtl"] = rtl_checked

    return current_prefs


@callback(
    [
        Output("theme-switch", "checked", allow_duplicate=True),
        Output("rtl-switch", "checked", allow_duplicate=True),
    ],
    Input("user-preferences", "data"),
    prevent_initial_call="initial_duplicate",
)
def restore_user_preferences(prefs: dict) -> tuple[bool, bool]:
    """Restore user preferences from localStorage on app load.

    Args:
        prefs: Stored preferences

    Returns:
        Tuple of (theme_checked, rtl_checked)
    """
    if not prefs:
        return False, False

    theme_checked = prefs.get("theme", "light") == "dark"
    rtl_checked = prefs.get("rtl", False)

    return theme_checked, rtl_checked


@callback(
    Output("mantine-provider", "forceColorScheme", allow_duplicate=True),
    Input("user-preferences", "data"),
    prevent_initial_call="initial_duplicate",
)
def apply_theme_preference(prefs: dict) -> str:
    """Apply theme preference from storage.

    Args:
        prefs: User preferences

    Returns:
        Theme name
    """
    if not prefs:
        return "light"

    return prefs.get("theme", "light")


@callback(
    Output("notification-output", "children"),
    Input("notification-trigger", "data"),
    State("notification-queue", "data"),
    prevent_initial_call=True,
)
def display_notification(trigger: int, queue: list) -> str:
    """Display notifications from the queue.

    Args:
        trigger: Trigger counter
        queue: List of notification dictionaries

    Returns:
        Empty string (side effect is notification display)
    """
    if not queue or len(queue) == 0:
        return no_update

    # This would integrate with dmc.notifications in a real implementation
    # For now, we just acknowledge the trigger
    return ""


@callback(
    Output("modal-output", "children"),
    Input("modal-states", "data"),
    prevent_initial_call=True,
)
def handle_modal_state_changes(modal_states: dict) -> str:
    """Handle modal state changes.

    Args:
        modal_states: Dictionary of modal states

    Returns:
        Empty string
    """
    # This callback handles modal state management
    # The actual modal opening/closing is handled by their individual callbacks
    return ""
