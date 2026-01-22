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
                # Left section with copyright
                dmc.Text(
                    f"© 2024 {APP_TITLE} v{APP_VERSION}",
                    size="sm",
                    c="dimmed",
                ),
                # Right section with links
                dmc.Group(
                    [
                        dmc.Anchor(
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:book", width=16),
                                    dmc.Text("Docs", size="sm"),
                                ],
                                gap="xs",
                            ),
                            href="/help",
                            underline=False,
                        ),
                        dmc.Anchor(
                            dmc.Group(
                                [
                                    DashIconify(icon="tabler:brand-github", width=16),
                                    dmc.Text("GitHub", size="sm"),
                                ],
                                gap="xs",
                            ),
                            href="https://github.com/jeffmaxey/aiml-studio",
                            target="_blank",
                            underline=False,
                        ),
                    ],
                    gap="md",
                ),
            ],
            justify="space-between",
            h="100%",
            px="md",
        ),
        id="footer",
    )
