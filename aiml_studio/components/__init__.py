"""Reusable UI components for AIML Studio."""

from aiml_studio.components.aside import create_aside
from aiml_studio.components.errors import (
    create_error_alert,
    create_error_boundary,
    create_info_alert,
    create_success_alert,
    create_validation_error_list,
    create_warning_alert,
)
from aiml_studio.components.footer import create_footer
from aiml_studio.components.header import create_header
from aiml_studio.components.modals import (
    create_alert_modal,
    create_confirm_modal,
    create_drawer,
    create_form_modal,
    create_modal,
    create_modal_manager,
)
from aiml_studio.components.navbar import create_navbar
from aiml_studio.components.notifications import (
    create_inline_alert,
    create_notification,
    create_notification_bell,
    create_notification_list,
    create_notification_manager,
    create_notification_provider,
    create_toast_notification,
)
from aiml_studio.components.search import create_search_modal, create_search_result_item, filter_search_results
from aiml_studio.components.tables import (
    create_ag_grid,
    create_data_sources_grid,
    create_logs_grid,
    create_projects_grid,
)
from aiml_studio.components.tooltips import (
    create_contextual_help_button,
    create_field_description,
    create_help_content_section,
    create_help_drawer_trigger,
    create_help_icon,
    create_help_section,
    create_help_text,
    create_info_icon,
    create_keyboard_shortcut,
    create_label_with_help,
    create_popover_help,
    create_tooltip,
)

__all__ = [
    "create_ag_grid",
    "create_aside",
    "create_data_sources_grid",
    "create_footer",
    "create_header",
    "create_logs_grid",
    "create_navbar",
    "create_projects_grid",
    # Modals
    "create_modal",
    "create_confirm_modal",
    "create_alert_modal",
    "create_form_modal",
    "create_drawer",
    "create_modal_manager",
    # Notifications
    "create_notification_provider",
    "create_notification",
    "create_inline_alert",
    "create_toast_notification",
    "create_notification_bell",
    "create_notification_list",
    "create_notification_manager",
    # Tooltips and Help
    "create_tooltip",
    "create_help_icon",
    "create_info_icon",
    "create_help_text",
    "create_label_with_help",
    "create_popover_help",
    "create_contextual_help_button",
    "create_help_drawer_trigger",
    "create_help_section",
    "create_help_content_section",
    "create_keyboard_shortcut",
    "create_field_description",
    # Search
    "create_search_modal",
    "create_search_result_item",
    "filter_search_results",
    # Error Handling
    "create_error_alert",
    "create_warning_alert",
    "create_info_alert",
    "create_success_alert",
    "create_validation_error_list",
    "create_error_boundary",
]
