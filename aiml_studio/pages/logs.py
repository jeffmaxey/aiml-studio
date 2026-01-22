"""Logs page."""

import dash

from aiml_studio.layouts.logs import create_logs_layout

dash.register_page(__name__, path="/logs", title="Logs - AIML Studio")

layout = create_logs_layout()
