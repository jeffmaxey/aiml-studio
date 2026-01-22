"""Projects page."""

import dash

from aiml_studio.layouts.projects import create_projects_layout

dash.register_page(__name__, path="/projects", title="Projects - AIML Studio")

layout = create_projects_layout()
