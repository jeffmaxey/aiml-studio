"""Help page."""

import dash

from aiml_studio.layouts.help import create_help_layout

dash.register_page(__name__, path="/help", title="Help - AIML Studio")

layout = create_help_layout()
