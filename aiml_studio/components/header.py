"""Application header component."""

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from aiml_studio.constants import APP_TITLE


def create_navbar_toggle() -> dmc.ActionIcon:
    """Create navbar toggle button.

    Returns:
        Mantine ActionIcon component for toggling navbar
    """
    return dmc.ActionIcon(
        DashIconify(icon="tabler:menu-2", width=22),
        variant="subtle",
        id="navbar-toggle-btn",
        size="lg",
        color="gray",
    )


def create_aside_toggle() -> dmc.ActionIcon:
    """Create aside toggle button.

    Returns:
        Mantine ActionIcon component for toggling aside
    """
    return dmc.ActionIcon(
        DashIconify(icon="tabler:layout-sidebar-right", width=22),
        variant="subtle",
        id="aside-toggle-btn",
        size="lg",
        color="gray",
    )


def create_logo_section() -> dmc.Group:
    """Create logo section with icon and title.

    Returns:
        Group containing logo and title
    """
    return dmc.Group(
        [
            dmc.ThemeIcon(
                DashIconify(icon="tabler:brain", width=28),
                size="lg",
                radius="md",
                variant="gradient",
                gradient={"from": "blue", "to": "cyan", "deg": 135},
            ),
            dmc.Stack(
                [
                    dmc.Title(APP_TITLE, order=3, style={"lineHeight": "1.2", "marginBottom": "0"}),
                    dmc.Text("ML Platform", size="xs", c="dimmed", fw=500),
                ],
                gap=0,
            ),
        ],
        gap="sm",
    )


def create_header() -> dmc.AppShellHeader:
    """Create the application header.

    Returns:
        Mantine AppShellHeader component
    """
    return dmc.AppShellHeader(
        dmc.Group(
            [
                # Left section with navbar toggle and logo
                dmc.Group(
                    [
                        create_navbar_toggle(),
                        create_logo_section(),
                    ],
                    gap="md",
                ),
                # Right section with search, notifications, and user menu
                dmc.Group(
                    [
                        # Search button/input
                        dmc.TextInput(
                            id="global-search-input",
                            placeholder="Search... (Ctrl+K)",
                            leftSection=DashIconify(icon="tabler:search", width=18),
                            rightSection=dmc.Badge("Ctrl+K", size="xs", variant="light", color="gray"),
                            style={"width": "300px"},
                            className="hide-mobile",
                        ),
                        dmc.ActionIcon(
                            DashIconify(icon="tabler:search", width=20),
                            variant="subtle",
                            size="lg",
                            color="gray",
                            id="mobile-search-btn",
                            className="hide-desktop",
                        ),
                        # Notifications
                        dmc.Indicator(
                            dmc.ActionIcon(
                                DashIconify(icon="tabler:bell", width=20),
                                variant="subtle",
                                size="lg",
                                color="gray",
                            ),
                            color="red",
                            size=8,
                            processing=True,
                        ),
                        dmc.Divider(orientation="vertical", style={"height": "24px"}),
                        # Aside toggle
                        create_aside_toggle(),
                        # User menu
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                    dmc.Group(
                                        [
                                            dmc.Avatar(
                                                DashIconify(icon="tabler:user", width=20),
                                                radius="xl",
                                                color="blue",
                                                variant="light",
                                            ),
                                            dmc.Stack(
                                                [
                                                    dmc.Text("Admin User", size="sm", fw=600),
                                                    dmc.Text("admin@aiml.studio", size="xs", c="dimmed"),
                                                ],
                                                gap=0,
                                                className="hide-mobile",
                                            ),
                                            DashIconify(icon="tabler:chevron-down", width=16, color="gray"),
                                        ],
                                        gap="sm",
                                        style={"cursor": "pointer"},
                                    )
                                ),
                                dmc.MenuDropdown([
                                    dmc.MenuItem(
                                        "Profile",
                                        leftSection=DashIconify(icon="tabler:user", width=16),
                                    ),
                                    dmc.MenuItem(
                                        "Settings",
                                        leftSection=DashIconify(icon="tabler:settings", width=16),
                                    ),
                                    dmc.MenuDivider(),
                                    dmc.MenuItem(
                                        "Documentation",
                                        leftSection=DashIconify(icon="tabler:book", width=16),
                                    ),
                                    dmc.MenuItem(
                                        "Keyboard Shortcuts",
                                        leftSection=DashIconify(icon="tabler:keyboard", width=16),
                                        rightSection=dmc.Text("Ctrl+K", size="xs", c="dimmed"),
                                    ),
                                    dmc.MenuDivider(),
                                    dmc.MenuItem(
                                        "Logout",
                                        leftSection=DashIconify(icon="tabler:logout", width=16),
                                        color="red",
                                    ),
                                ]),
                            ],
                            position="bottom-end",
                            width=240,
                        ),
                    ],
                    gap="sm",
                ),
            ],
            justify="space-between",
            h="100%",
            px="lg",
        ),
        id="header",
    )
