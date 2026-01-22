"""Modal components for dialogs, confirmations, and forms."""

from typing import Any, Literal

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_modal(
    modal_id: str,
    title: str,
    children: list[Any] | Any,
    size: Literal["xs", "sm", "md", "lg", "xl", "full"] = "md",
    opened: bool = False,
    with_close_button: bool = True,
    close_on_escape: bool = True,
    close_on_click_outside: bool = True,
    centered: bool = True,
    overlayProps: dict[str, Any] | None = None,
) -> dmc.Modal:
    """Create a reusable modal component.

    Args:
        modal_id: Unique modal identifier
        title: Modal title
        children: Modal content
        size: Modal size
        opened: Whether modal is initially opened
        with_close_button: Show close button
        close_on_escape: Close on Escape key
        close_on_click_outside: Close when clicking outside
        centered: Center modal vertically
        overlayProps: Overlay styling properties

    Returns:
        Mantine Modal component
    """
    if overlayProps is None:
        overlayProps = {"backgroundOpacity": 0.55, "blur": 3}

    return dmc.Modal(
        title=title,
        id=modal_id,
        size=size,
        opened=opened,
        withCloseButton=with_close_button,
        closeOnEscape=close_on_escape,
        closeOnClickOutside=close_on_click_outside,
        centered=centered,
        overlayProps=overlayProps,
        children=children,
    )


def create_confirm_modal(
    modal_id: str,
    title: str,
    message: str,
    confirm_label: str = "Confirm",
    cancel_label: str = "Cancel",
    confirm_color: str = "blue",
    icon: str | None = None,
    opened: bool = False,
) -> dmc.Modal:
    """Create a confirmation modal dialog.

    Args:
        modal_id: Unique modal identifier
        title: Modal title
        message: Confirmation message
        confirm_label: Confirm button label
        cancel_label: Cancel button label
        confirm_color: Confirm button color
        icon: Optional icon identifier
        opened: Whether modal is initially opened

    Returns:
        Mantine Modal component
    """
    content = [
        dmc.Stack(
            [
                dmc.Group(
                    [
                        icon
                        and dmc.ThemeIcon(
                            DashIconify(icon=icon, width=24),
                            size="xl",
                            radius="md",
                            variant="light",
                            color=confirm_color,
                        ),
                        dmc.Text(message, size="sm"),
                    ],
                    gap="md",
                ),
                dmc.Group(
                    [
                        dmc.Button(
                            cancel_label,
                            variant="subtle",
                            color="gray",
                            id={"type": "modal-button", "action": "cancel", "modal": modal_id},
                        ),
                        dmc.Button(
                            confirm_label,
                            color=confirm_color,
                            id={"type": "modal-button", "action": "confirm", "modal": modal_id},
                        ),
                    ],
                    justify="flex-end",
                    gap="xs",
                ),
            ],
            gap="lg",
        )
    ]

    return create_modal(
        modal_id=modal_id,
        title=title,
        children=content,
        size="sm",
        opened=opened,
    )


def create_alert_modal(
    modal_id: str,
    title: str,
    message: str,
    alert_type: Literal["success", "error", "info", "warning"] = "info",
    button_label: str = "OK",
    opened: bool = False,
) -> dmc.Modal:
    """Create an alert modal dialog.

    Args:
        modal_id: Unique modal identifier
        title: Modal title
        message: Alert message
        alert_type: Type of alert
        button_label: Button label
        opened: Whether modal is initially opened

    Returns:
        Mantine Modal component
    """
    # Map alert type to icon and color
    type_config = {
        "success": {"icon": "tabler:check-circle", "color": "green"},
        "error": {"icon": "tabler:x-circle", "color": "red"},
        "info": {"icon": "tabler:info-circle", "color": "blue"},
        "warning": {"icon": "tabler:alert-triangle", "color": "yellow"},
    }

    config = type_config.get(alert_type, type_config["info"])

    content = [
        dmc.Stack(
            [
                dmc.Center(
                    dmc.ThemeIcon(
                        DashIconify(icon=config["icon"], width=48),
                        size=80,
                        radius="xl",
                        variant="light",
                        color=config["color"],
                    )
                ),
                dmc.Text(message, size="sm", ta="center"),
                dmc.Button(
                    button_label,
                    fullWidth=True,
                    color=config["color"],
                    id={"type": "modal-button", "action": "close", "modal": modal_id},
                ),
            ],
            gap="lg",
            align="center",
        )
    ]

    return create_modal(
        modal_id=modal_id,
        title=title,
        children=content,
        size="xs",
        opened=opened,
    )


def create_form_modal(
    modal_id: str,
    title: str,
    form_fields: list[Any],
    submit_label: str = "Submit",
    cancel_label: str = "Cancel",
    submit_color: str = "blue",
    opened: bool = False,
) -> dmc.Modal:
    """Create a form modal dialog.

    Args:
        modal_id: Unique modal identifier
        title: Modal title
        form_fields: List of form field components
        submit_label: Submit button label
        cancel_label: Cancel button label
        submit_color: Submit button color
        opened: Whether modal is initially opened

    Returns:
        Mantine Modal component
    """
    content = [
        dmc.Stack(
            [
                dmc.Stack(form_fields, gap="md"),
                dmc.Group(
                    [
                        dmc.Button(
                            cancel_label,
                            variant="subtle",
                            color="gray",
                            id={"type": "modal-button", "action": "cancel", "modal": modal_id},
                        ),
                        dmc.Button(
                            submit_label,
                            color=submit_color,
                            id={"type": "modal-button", "action": "submit", "modal": modal_id},
                        ),
                    ],
                    justify="flex-end",
                    gap="xs",
                ),
            ],
            gap="lg",
        )
    ]

    return create_modal(
        modal_id=modal_id,
        title=title,
        children=content,
        size="md",
        opened=opened,
    )


def create_drawer(
    drawer_id: str,
    title: str,
    children: list[Any] | Any,
    position: Literal["left", "right", "top", "bottom"] = "right",
    size: str | int = "md",
    opened: bool = False,
    with_close_button: bool = True,
    close_on_escape: bool = True,
    close_on_click_outside: bool = True,
    overlayProps: dict[str, Any] | None = None,
) -> dmc.Drawer:
    """Create a drawer component (side panel).

    Args:
        drawer_id: Unique drawer identifier
        title: Drawer title
        children: Drawer content
        position: Drawer position
        size: Drawer size
        opened: Whether drawer is initially opened
        with_close_button: Show close button
        close_on_escape: Close on Escape key
        close_on_click_outside: Close when clicking outside
        overlayProps: Overlay styling properties

    Returns:
        Mantine Drawer component
    """
    if overlayProps is None:
        overlayProps = {"backgroundOpacity": 0.55, "blur": 3}

    return dmc.Drawer(
        title=title,
        id=drawer_id,
        position=position,
        size=size,
        opened=opened,
        withCloseButton=with_close_button,
        closeOnEscape=close_on_escape,
        closeOnClickOutside=close_on_click_outside,
        overlayProps=overlayProps,
        children=children,
    )


def create_modal_manager() -> html.Div:
    """Create a modal manager component with stores for managing modal states.

    Returns:
        Div containing modal manager components
    """
    from dash import dcc

    return html.Div(
        [
            # Store for modal states
            dcc.Store(id="modal-states", data={}, storage_type="memory"),
            # Hidden div for modal outputs
            html.Div(id="modal-output", style={"display": "none"}),
        ]
    )
