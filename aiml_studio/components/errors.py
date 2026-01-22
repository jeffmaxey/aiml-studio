"""Error handling and display components."""

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_error_alert(error_message: str, title: str = "Error", show_icon: bool = True) -> dmc.Alert:
    """Create an error alert component.

    Args:
        error_message: The error message to display
        title: Alert title
        show_icon: Whether to show error icon

    Returns:
        Alert component with error styling
    """
    return dmc.Alert(
        error_message,
        title=title,
        color="red",
        icon=DashIconify(icon="tabler:alert-circle", width=20) if show_icon else None,
        withCloseButton=True,
    )


def create_warning_alert(warning_message: str, title: str = "Warning", show_icon: bool = True) -> dmc.Alert:
    """Create a warning alert component.

    Args:
        warning_message: The warning message to display
        title: Alert title
        show_icon: Whether to show warning icon

    Returns:
        Alert component with warning styling
    """
    return dmc.Alert(
        warning_message,
        title=title,
        color="yellow",
        icon=DashIconify(icon="tabler:alert-triangle", width=20) if show_icon else None,
        withCloseButton=True,
    )


def create_info_alert(info_message: str, title: str = "Info", show_icon: bool = True) -> dmc.Alert:
    """Create an info alert component.

    Args:
        info_message: The info message to display
        title: Alert title
        show_icon: Whether to show info icon

    Returns:
        Alert component with info styling
    """
    return dmc.Alert(
        info_message,
        title=title,
        color="blue",
        icon=DashIconify(icon="tabler:info-circle", width=20) if show_icon else None,
        withCloseButton=True,
    )


def create_success_alert(success_message: str, title: str = "Success", show_icon: bool = True) -> dmc.Alert:
    """Create a success alert component.

    Args:
        success_message: The success message to display
        title: Alert title
        show_icon: Whether to show success icon

    Returns:
        Alert component with success styling
    """
    return dmc.Alert(
        success_message,
        title=title,
        color="green",
        icon=DashIconify(icon="tabler:check", width=20) if show_icon else None,
        withCloseButton=True,
    )


def create_validation_error_list(errors: dict[str, str]) -> dmc.Alert:
    """Create an alert with a list of validation errors.

    Args:
        errors: Dictionary mapping field names to error messages

    Returns:
        Alert component with validation errors
    """
    error_items = [dmc.Text(f"• {field}: {msg}", size="sm") for field, msg in errors.items()]

    return dmc.Alert(
        dmc.Stack(error_items, gap="xs"),
        title="Please fix the following errors:",
        color="red",
        icon=DashIconify(icon="tabler:alert-circle", width=20),
        withCloseButton=True,
    )


def create_error_boundary(error_message: str = "Something went wrong") -> dmc.Paper:
    """Create an error boundary component for catastrophic errors.

    Args:
        error_message: Error message to display

    Returns:
        Paper component with error boundary styling
    """
    return dmc.Paper(
        dmc.Stack(
            [
                dmc.Center(
                    dmc.ThemeIcon(
                        DashIconify(icon="tabler:alert-octagon", width=60),
                        size=100,
                        radius="md",
                        variant="light",
                        color="red",
                    )
                ),
                dmc.Title("Oops! Something went wrong", order=3, ta="center"),
                dmc.Text(
                    error_message,
                    size="sm",
                    c="dimmed",
                    ta="center",
                ),
                dmc.Center(
                    dmc.Button(
                        "Reload Page",
                        leftSection=DashIconify(icon="tabler:refresh", width=18),
                        variant="light",
                        color="red",
                        id="error-reload-button",
                    )
                ),
            ],
            gap="lg",
            align="center",
        ),
        p="xl",
        radius="md",
        withBorder=True,
    )
