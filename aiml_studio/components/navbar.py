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


def create_theme_toggle() -> dmc.Group:
    """Create theme toggle switch.

    Returns:
        Group containing theme toggle
    """
    return dmc.Group(
        [
            DashIconify(icon="tabler:sun", width=18),
            dmc.Switch(id="theme-switch", checked=False, size="md"),
            DashIconify(icon="tabler:moon", width=18),
        ],
        gap="xs",
        justify="center",
    )


def create_rtl_toggle() -> dmc.Group:
    """Create RTL toggle switch.

    Returns:
        Group containing RTL toggle
    """
    return dmc.Group(
        [
            dmc.Text("LTR", size="sm", fw=500),
            dmc.Switch(id="rtl-switch", checked=False, size="md"),
            dmc.Text("RTL", size="sm", fw=500),
        ],
        gap="xs",
        justify="center",
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
                dmc.Divider(my="sm"),
                # Theme Controls
                dmc.Stack(
                    [
                        dmc.Text("Appearance", size="xs", c="dimmed", fw=500, ml="xs", mb="xs"),
                        dmc.Paper(
                            [
                                dmc.Stack(
                                    [
                                        dmc.Text("Theme", size="sm", fw=500, ta="center"),
                                        create_theme_toggle(),
                                    ],
                                    gap="xs",
                                )
                            ],
                            p="sm",
                            radius="md",
                            withBorder=True,
                        ),
                        dmc.Paper(
                            [
                                dmc.Stack(
                                    [
                                        dmc.Text("Direction", size="sm", fw=500, ta="center"),
                                        create_rtl_toggle(),
                                    ],
                                    gap="xs",
                                )
                            ],
                            p="sm",
                            radius="md",
                            withBorder=True,
                        ),
                    ],
                    gap="sm",
                ),
            ],
            gap="xs",
            p="md",
        )
    ]

    return dmc.AppShellNavbar(navbar_content, id="navbar")
