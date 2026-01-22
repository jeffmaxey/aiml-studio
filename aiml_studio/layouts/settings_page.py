"""Settings page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_settings_layout() -> html.Div:
    """Create the settings page layout.

    Returns:
        Settings page layout component
    """
    return html.Div(
        [
            dmc.Stack(
                [
                    dmc.Title("Application Settings", order=2, mb="md"),
                    # Appearance settings
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:palette", width=24),
                                    dmc.Title("Appearance", order=4),
                                ],
                                gap="sm",
                                mb="md",
                            ),
                            dmc.Stack(
                                [
                                    dmc.Group(
                                        [
                                            dmc.Text("Theme Mode:", fw=500),
                                            dmc.SegmentedControl(
                                                id="theme-toggle",
                                                value="light",
                                                data=[
                                                    {"label": "Light", "value": "light"},
                                                    {"label": "Dark", "value": "dark"},
                                                ],
                                            ),
                                        ],
                                        justify="space-between",
                                    ),
                                ],
                                gap="md",
                            ),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="lg",
                    ),
                    # User preferences
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:user-cog", width=24),
                                    dmc.Title("User Preferences", order=4),
                                ],
                                gap="sm",
                                mb="md",
                            ),
                            dmc.Stack(
                                [
                                    dmc.TextInput(
                                        label="Display Name",
                                        placeholder="Enter your name",
                                        id="display-name-input",
                                    ),
                                    dmc.TextInput(
                                        label="Email",
                                        placeholder="your.email@example.com",
                                        id="email-input",
                                    ),
                                    dmc.Select(
                                        label="Default Page Size",
                                        placeholder="Select page size",
                                        id="page-size-select",
                                        data=[
                                            {"label": "10 items", "value": "10"},
                                            {"label": "20 items", "value": "20"},
                                            {"label": "50 items", "value": "50"},
                                            {"label": "100 items", "value": "100"},
                                        ],
                                        value="20",
                                    ),
                                ],
                                gap="md",
                            ),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="lg",
                    ),
                    # Notification settings
                    dmc.Card(
                        [
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:bell", width=24),
                                    dmc.Title("Notifications", order=4),
                                ],
                                gap="sm",
                                mb="md",
                            ),
                            dmc.Stack(
                                [
                                    dmc.Switch(
                                        id="email-notifications-switch",
                                        label="Email Notifications",
                                        checked=True,
                                    ),
                                    dmc.Switch(
                                        id="browser-notifications-switch",
                                        label="Browser Notifications",
                                        checked=False,
                                    ),
                                    dmc.Switch(
                                        id="activity-alerts-switch",
                                        label="Activity Alerts",
                                        checked=True,
                                    ),
                                ],
                                gap="md",
                            ),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        p="lg",
                    ),
                    # Save button
                    dmc.Group(
                        [
                            dmc.Button(
                                "Save Settings",
                                leftSection=DashIconify(icon="tabler:device-floppy", width=20),
                                id="save-settings-button",
                            ),
                            dmc.Button(
                                "Reset to Defaults",
                                variant="outline",
                                leftSection=DashIconify(icon="tabler:refresh", width=20),
                                id="reset-settings-button",
                            ),
                        ],
                        justify="flex-end",
                    ),
                ],
                gap="lg",
            )
        ]
    )
