"""Application header component."""

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from aiml_studio.components.navbar import create_navbar_toggle
from aiml_studio.constants import APP_TITLE


def create_header() -> dmc.AppShellHeader:
    """Create the application header.

    Returns:
        Mantine AppShellHeader component
    """
    return dmc.AppShellHeader(
        dmc.Group(
            [
                # Left section with toggle and title
                dmc.Group(
                    [
                        create_navbar_toggle(),
                        dmc.Title(APP_TITLE, order=3),
                    ],
                    gap="md",
                ),
                # Right section with user menu
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
            justify="space-between",
            h="100%",
            px="md",
        ),
        id="header",
    )
