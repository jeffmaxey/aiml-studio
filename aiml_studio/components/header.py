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
        DashIconify(icon="tabler:menu-2", width=20),
        variant="subtle",
        id="navbar-toggle-btn",
        size="lg",
    )


def create_aside_toggle() -> dmc.ActionIcon:
    """Create aside toggle button.

    Returns:
        Mantine ActionIcon component for toggling aside
    """
    return dmc.ActionIcon(
        DashIconify(icon="tabler:layout-sidebar-right", width=20),
        variant="subtle",
        id="aside-toggle-btn",
        size="lg",
    )


def create_header() -> dmc.AppShellHeader:
    """Create the application header.

    Returns:
        Mantine AppShellHeader component
    """
    return dmc.AppShellHeader(
        dmc.Group(
            [
                # Left section with navbar toggle and title
                dmc.Group(
                    [
                        create_navbar_toggle(),
                        dmc.Title(APP_TITLE, order=3),
                    ],
                    gap="md",
                ),
                # Right section with aside toggle and user menu
                dmc.Group(
                    [
                        create_aside_toggle(),
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                    dmc.ActionIcon(
                                        DashIconify(icon="tabler:user", width=20),
                                        variant="subtle",
                                        size="lg",
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
                                        "Logout",
                                        leftSection=DashIconify(icon="tabler:logout", width=16),
                                        color="red",
                                    ),
                                ]),
                            ],
                            position="bottom-end",
                            width=200,
                        ),
                    ],
                    gap="sm",
                ),
            ],
            justify="space-between",
            h="100%",
            px="md",
        ),
        id="header",
    )
