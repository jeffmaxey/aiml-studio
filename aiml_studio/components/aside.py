"""Application aside panel component."""

import dash_mantine_components as dmc
from dash import html


def create_aside() -> dmc.AppShellAside:
    """Create the application aside panel.

    Returns:
        Mantine AppShellAside component
    """
    return dmc.AppShellAside(
        dmc.Stack(
            [
                dmc.Title("Contextual Info", order=5, mb="md"),
                dmc.Text(
                    "This panel can be used for contextual information, notifications, or additional controls.",
                    size="sm",
                    c="dimmed",
                ),
            ],
            p="md",
        ),
        id="aside",
    )
