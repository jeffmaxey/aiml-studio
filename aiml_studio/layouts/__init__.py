"""Layout modules for AIML Studio pages."""

from aiml_studio.layouts.analytics import create_analytics_layout
from aiml_studio.layouts.appshell import create_appshell
from aiml_studio.layouts.data_sources import create_data_sources_layout
from aiml_studio.layouts.help import create_help_layout
from aiml_studio.layouts.home import create_home_layout
from aiml_studio.layouts.logs import create_logs_layout
from aiml_studio.layouts.projects import create_projects_layout
from aiml_studio.layouts.settings_page import create_settings_layout

__all__ = [
    "create_appshell",
    "create_home_layout",
    "create_settings_layout",
    "create_help_layout",
    "create_logs_layout",
    "create_analytics_layout",
    "create_data_sources_layout",
    "create_projects_layout",
]
