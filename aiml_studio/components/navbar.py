"""Responsive collapsible navbar component."""

from typing import Any

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from aiml_studio.constants import NAV_LINKS


def create_nav_link(label: str, icon: str, href: str) -> dmc.NavLink:
    """Create a navigation link with icon.

    Args:
        label: Link label text
        icon: Icon identifier for dash_iconify
        href: Link URL

    Returns:
        Mantine NavLink component
    """
    return dmc.NavLink(
        label=label,
        href=href,
        leftSection=DashIconify(icon=icon, width=20),
        variant="subtle",
        active="exact",
    )


def create_navbar(opened: bool = True) -> dmc.AppShellNavbar:
    """Create the application navbar.

    Args:
        opened: Whether the navbar is opened or collapsed

    Returns:
        Mantine AppShellNavbar component
    """
    # Group navigation links by section
    core_links = [link for link in NAV_LINKS if link["section"] == "core"]
    admin_links = [link for link in NAV_LINKS if link["section"] == "admin"]

    navbar_content: list[Any] = [
        dmc.Stack(
            [
                # Core Section
                dmc.Text("Core", size="xs", c="dimmed", fw=500, ml="xs", mb="xs"),
                *[create_nav_link(link["label"], link["icon"], link["href"]) for link in core_links],
                dmc.Divider(my="sm"),
                # Admin Section
                dmc.Text("Admin", size="xs", c="dimmed", fw=500, ml="xs", mb="xs"),
                *[create_nav_link(link["label"], link["icon"], link["href"]) for link in admin_links],
            ],
            gap="xs",
            p="md",
        )
    ]

    return dmc.AppShellNavbar(navbar_content, id="navbar")


def create_navbar_toggle() -> dmc.ActionIcon:
    """Create navbar toggle button.

    Returns:
        Mantine ActionIcon component for toggling navbar
    """
    return dmc.ActionIcon(
        DashIconify(icon="tabler:menu-2", width=20),
        variant="subtle",
        id="navbar-toggle",
        size="lg",
    )
