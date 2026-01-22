"""Application footer component."""

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from aiml_studio.constants import APP_TITLE, APP_VERSION


def create_footer() -> dmc.AppShellFooter:
    """Create the application footer.

    Returns:
        Mantine AppShellFooter component
    """
    return dmc.AppShellFooter(
        dmc.Group(
            [
                # Left section with copyright and status
                dmc.Group(
                    [
                        dmc.Text(
                            f"© 2024 {APP_TITLE}",
                            size="sm",
                            c="dimmed",
                            fw=500,
                        ),
                        dmc.Badge(
                            f"v{APP_VERSION}",
                            size="sm",
                            variant="dot",
                            color="blue",
                        ),
                        dmc.Group(
                            [
                                dmc.Box(className="status-dot success"),
                                dmc.Text("All Systems Operational", size="xs", c="dimmed", fw=500),
                            ],
                            gap="xs",
                            className="hide-mobile",
                        ),
                    ],
                    gap="md",
                ),
                # Right section with links
                dmc.Group(
                    [
                        dmc.Anchor(
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:book", width=16),
                                    dmc.Text("Docs", size="sm", fw=500),
                                ],
                                gap="xs",
                            ),
                            href="/help",
                            underline=False,
                            c="dimmed",
                        ),
                        dmc.Anchor(
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:api", width=16),
                                    dmc.Text("API", size="sm", fw=500),
                                ],
                                gap="xs",
                            ),
                            href="/help#api",
                            underline=False,
                            c="dimmed",
                        ),
                        dmc.Anchor(
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:brand-github", width=16),
                                    dmc.Text("GitHub", size="sm", fw=500),
                                ],
                                gap="xs",
                            ),
                            href="https://github.com/jeffmaxey/aiml-studio",
                            target="_blank",
                            underline=False,
                            c="dimmed",
                        ),
                        dmc.Divider(orientation="vertical", style={"height": "20px"}),
                        dmc.Group(
                            [
                                dmc.ActionIcon(
                                    DashIconify(icon="tabler:brand-twitter", width=16),
                                    variant="subtle",
                                    size="sm",
                                    color="gray",
                                ),
                                dmc.ActionIcon(
                                    DashIconify(icon="tabler:brand-discord", width=16),
                                    variant="subtle",
                                    size="sm",
                                    color="gray",
                                ),
                            ],
                            gap="xs",
                        ),
                    ],
                    gap="md",
                ),
            ],
            justify="space-between",
            h="100%",
            px="lg",
        ),
        id="footer",
    )
