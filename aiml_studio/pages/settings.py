"""Settings page."""

import dash

from aiml_studio.layouts.settings_page import create_settings_layout

dash.register_page(__name__, path="/settings", title="Settings - AIML Studio")

layout = create_settings_layout()
