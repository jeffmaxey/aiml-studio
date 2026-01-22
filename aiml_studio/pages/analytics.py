"""Analytics dashboard page."""

import dash

from aiml_studio.layouts.analytics import create_analytics_layout

dash.register_page(__name__, path="/analytics", title="Analytics - AIML Studio")

layout = create_analytics_layout()
