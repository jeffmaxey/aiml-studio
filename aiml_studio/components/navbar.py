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
        style={"borderRadius": "8px"},
    )


def create_theme_toggle() -> dmc.Paper:
    """Create theme toggle switch with better styling.

    Returns:
        Paper containing theme toggle
    """
    return dmc.Paper(
        dmc.Group(
            [
                DashIconify(icon="tabler:sun", width=18, color="orange"),
                dmc.Switch(
                    id="theme-switch",
                    checked=False,
                    size="md",
                    color="blue",
                    onLabel=DashIconify(icon="tabler:moon", width=16),
                    offLabel=DashIconify(icon="tabler:sun", width=16),
                ),
                DashIconify(icon="tabler:moon", width=18, color="blue"),
            ],
            gap="xs",
            justify="center",
        ),
        p="sm",
        radius="md",
        withBorder=True,
    )


def create_rtl_toggle() -> dmc.Paper:
    """Create RTL toggle switch with better styling.

    Returns:
        Paper containing RTL toggle
    """
    return dmc.Paper(
        dmc.Group(
            [
                dmc.Text("LTR", size="sm", fw=600, c="dimmed"),
                dmc.Switch(id="rtl-switch", checked=False, size="md", color="blue"),
                dmc.Text("RTL", size="sm", fw=600, c="dimmed"),
            ],
            gap="xs",
            justify="center",
        ),
        p="sm",
        radius="md",
        withBorder=True,
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
        dmc.ScrollArea(
            dmc.Stack(
                [
                    # Core Section
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.ThemeIcon(
                                        DashIconify(icon="tabler:layout-dashboard", width=16),
                                        size="sm",
                                        radius="sm",
                                        variant="light",
                                        color="blue",
                                    ),
                                    dmc.Text("Core", size="xs", c="dimmed", fw=700, tt="uppercase"),
                                ],
                                gap="xs",
                            ),
                            *[create_nav_link(link["label"], link["icon"], link["href"]) for link in core_links],
                        ],
                        gap="xs",
                    ),
                    dmc.Divider(variant="dashed"),
                    # Admin Section
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.ThemeIcon(
                                        DashIconify(icon="tabler:shield-check", width=16),
                                        size="sm",
                                        radius="sm",
                                        variant="light",
                                        color="grape",
                                    ),
                                    dmc.Text("Admin", size="xs", c="dimmed", fw=700, tt="uppercase"),
                                ],
                                gap="xs",
                            ),
                            *[create_nav_link(link["label"], link["icon"], link["href"]) for link in admin_links],
                        ],
                        gap="xs",
                    ),
                    dmc.Divider(variant="dashed"),
                    # Appearance Section
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.ThemeIcon(
                                        DashIconify(icon="tabler:palette", width=16),
                                        size="sm",
                                        radius="sm",
                                        variant="light",
                                        color="pink",
                                    ),
                                    dmc.Text("Appearance", size="xs", c="dimmed", fw=700, tt="uppercase"),
                                ],
                                gap="xs",
                            ),
                            create_theme_toggle(),
                            create_rtl_toggle(),
                        ],
                        gap="sm",
                    ),
                    # Footer info
                    dmc.Stack(
                        [
                            dmc.Divider(variant="dashed"),
                            dmc.Paper(
                                dmc.Stack(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:info-circle", width=16, color="gray"),
                                                dmc.Text("Quick Tips", size="xs", fw=600),
                                            ],
                                            gap="xs",
                                        ),
                                        dmc.Text(
                                            "Press Ctrl+K for shortcuts",
                                            size="xs",
                                            c="dimmed",
                                        ),
                                    ],
                                    gap="xs",
                                ),
                                p="sm",
                                radius="md",
                                withBorder=True,
                                style={"background": "var(--mantine-color-blue-light)"},
                            ),
                        ],
                        gap="sm",
                    ),
                ],
                gap="lg",
                p="md",
            ),
            offsetScrollbars=True,
            type="auto",
        )
    ]

    return dmc.AppShellNavbar(navbar_content, id="navbar")
