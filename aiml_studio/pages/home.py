"""Home page."""

import dash

from aiml_studio.layouts.home import create_home_layout

dash.register_page(__name__, path="/", title="Home - AIML Studio")

layout = create_home_layout()
