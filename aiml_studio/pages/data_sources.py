"""Data sources page."""

import dash

from aiml_studio.layouts.data_sources import create_data_sources_layout

dash.register_page(__name__, path="/data-sources", title="Data Sources - AIML Studio")

layout = create_data_sources_layout()
