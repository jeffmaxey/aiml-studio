"""Notification components for displaying alerts, toasts, and messages."""

from typing import Any, Literal

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_notification_provider() -> dmc.NotificationProvider:
    """Create the notification provider component.

    This should be placed at the root of the application to enable notifications.

    Returns:
        NotificationProvider component
    """
    return dmc.NotificationProvider(
        html.Div(id="notification-container"),
        position="top-right",
        autoClose=5000,
        limit=3,
    )


def create_notification(
    title: str,
    message: str,
    notification_type: Literal["success", "error", "info", "warning"] = "info",
    icon: str | None = None,
    auto_close: int | bool = 5000,
    action: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create a notification configuration.

    Args:
        title: Notification title
        message: Notification message
        notification_type: Type of notification (success, error, info, warning)
        icon: Icon identifier (auto-selected if None)
        auto_close: Auto-close time in ms or False to disable
        action: Optional action button configuration

    Returns:
        Notification configuration dictionary
    """
    # Auto-select icon based on type if not provided
    if icon is None:
        icon_map = {
            "success": "tabler:check-circle",
            "error": "tabler:x-circle",
            "info": "tabler:info-circle",
            "warning": "tabler:alert-triangle",
        }
        icon = icon_map.get(notification_type, "tabler:bell")

    # Map notification type to Mantine color
    color_map = {
        "success": "green",
        "error": "red",
        "info": "blue",
        "warning": "yellow",
    }
    color = color_map.get(notification_type, "blue")

    notification_config = {
        "id": f"notification-{notification_type}",
        "title": title,
        "message": message,
        "color": color,
        "icon": DashIconify(icon=icon, width=20),
        "autoClose": auto_close,
        "withBorder": True,
    }

    if action:
        notification_config["action"] = action

    return notification_config


def create_inline_alert(
    title: str,
    message: str,
    alert_type: Literal["success", "error", "info", "warning"] = "info",
    icon: str | None = None,
    dismissible: bool = True,
    variant: Literal["light", "filled", "outline"] = "light",
) -> dmc.Alert:
    """Create an inline alert component.

    Args:
        title: Alert title
        message: Alert message
        alert_type: Type of alert (success, error, info, warning)
        icon: Icon identifier (auto-selected if None)
        dismissible: Whether the alert can be dismissed
        variant: Alert variant style

    Returns:
        Mantine Alert component
    """
    # Auto-select icon based on type if not provided
    if icon is None:
        icon_map = {
            "success": "tabler:check",
            "error": "tabler:x",
            "info": "tabler:info-circle",
            "warning": "tabler:alert-triangle",
        }
        icon = icon_map.get(alert_type, "tabler:info-circle")

    # Map alert type to Mantine color
    color_map = {
        "success": "green",
        "error": "red",
        "info": "blue",
        "warning": "yellow",
    }
    color = color_map.get(alert_type, "blue")

    return dmc.Alert(
        message,
        title=title,
        color=color,
        icon=DashIconify(icon=icon, width=20),
        withCloseButton=dismissible,
        variant=variant,
        radius="md",
        id={"type": "alert", "variant": alert_type},
    )


def create_notification_manager() -> html.Div:
    """Create a notification manager component with store for managing notifications.

    Returns:
        Div containing notification manager components
    """
    from dash import dcc

    return html.Div(
        [
            # Store for notification queue
            dcc.Store(id="notification-queue", data=[], storage_type="memory"),
            # Store for notification trigger
            dcc.Store(id="notification-trigger", data=0, storage_type="memory"),
            # Hidden div for triggering notifications
            html.Div(id="notification-output", style={"display": "none"}),
        ]
    )


def create_toast_notification(
    message: str,
    notification_type: Literal["success", "error", "info", "warning"] = "info",
    duration: int = 3000,
) -> dict[str, Any]:
    """Create a simple toast notification.

    Args:
        message: Toast message
        notification_type: Type of notification
        duration: Duration in milliseconds

    Returns:
        Toast notification configuration
    """
    return {
        "message": message,
        "type": notification_type,
        "duration": duration,
        "timestamp": None,  # Will be set when displayed
    }


def create_notification_bell(unread_count: int = 0) -> dmc.Indicator:
    """Create a notification bell with unread count indicator.

    Args:
        unread_count: Number of unread notifications

    Returns:
        Indicator with bell icon
    """
    return dmc.Indicator(
        dmc.ActionIcon(
            DashIconify(icon="tabler:bell", width=20),
            variant="subtle",
            size="lg",
            id="notification-bell",
        ),
        label=str(unread_count) if unread_count > 0 else None,
        disabled=unread_count == 0,
        size=16,
        color="red",
        processing=unread_count > 0,
    )


def create_notification_list(notifications: list[dict[str, Any]]) -> dmc.Stack:
    """Create a list of notifications for display in a dropdown or panel.

    Args:
        notifications: List of notification dictionaries

    Returns:
        Stack containing notification items
    """
    if not notifications:
        return dmc.Stack(
            [
                dmc.Center(
                    dmc.Stack(
                        [
                            DashIconify(icon="tabler:bell-off", width=40, color="gray"),
                            dmc.Text("No notifications", size="sm", c="dimmed"),
                        ],
                        gap="xs",
                        align="center",
                    ),
                    h=200,
                )
            ],
            gap="md",
        )

    notification_items = []
    for notif in notifications:
        notification_items.append(
            dmc.Paper(
                dmc.Group(
                    [
                        dmc.ThemeIcon(
                            DashIconify(icon=notif.get("icon", "tabler:bell"), width=20),
                            color=notif.get("color", "blue"),
                            variant="light",
                            size="lg",
                        ),
                        dmc.Stack(
                            [
                                dmc.Text(notif.get("title", "Notification"), size="sm", fw=600),
                                dmc.Text(notif.get("message", ""), size="xs", c="dimmed"),
                                dmc.Text(notif.get("time", "Just now"), size="xs", c="dimmed", fs="italic"),
                            ],
                            gap=2,
                        ),
                    ],
                    align="flex-start",
                ),
                p="sm",
                withBorder=True,
                radius="md",
                style={"cursor": "pointer"},
                className="notification-item",
            )
        )

    return dmc.Stack(notification_items, gap="xs")
