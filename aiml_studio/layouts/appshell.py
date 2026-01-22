"""Global AppShell layout container."""

import dash_mantine_components as dmc
from dash import html

from aiml_studio.components import create_aside, create_footer, create_header, create_navbar
from aiml_studio.constants import FOOTER_HEIGHT, HEADER_HEIGHT, NAVBAR_WIDTH


def create_appshell(page_content: html.Div) -> dmc.MantineProvider:
    """Create the main AppShell layout.

    Args:
        page_content: The main page content to display

    Returns:
        MantineProvider with AppShell layout
    """
    return dmc.MantineProvider(
        dmc.AppShell(
            [
                create_header(),
                create_navbar(opened=True),
                create_aside(),
                dmc.AppShellMain(page_content, id="main-content"),
                create_footer(),
            ],
            header={"height": HEADER_HEIGHT},
            navbar={"width": NAVBAR_WIDTH, "breakpoint": "sm", "collapsed": {"mobile": True}},
            aside={"width": 0, "breakpoint": "md", "collapsed": {"desktop": True, "mobile": True}},
            footer={"height": FOOTER_HEIGHT},
            padding="md",
            id="appshell",
        ),
        id="mantine-provider",
    )
