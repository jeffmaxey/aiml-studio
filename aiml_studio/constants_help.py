"""Help text and tooltip constants for AIML Studio."""

from typing import Any

# Page-level help content
PAGE_HELP: dict[str, dict[str, Any]] = {
    "home": {
        "title": "Home Dashboard",
        "description": "View your AIML Studio dashboard with key metrics, recent activity, and quick actions.",
        "sections": [
            {
                "title": "Key Metrics",
                "content": "Monitor your project status, active models, data sources, and API usage in real-time.",
                "icon": "tabler:chart-line",
            },
            {
                "title": "Quick Actions",
                "content": "Create new projects, connect data sources, view analytics, or access documentation.",
                "icon": "tabler:bolt",
            },
            {
                "title": "Recent Activity",
                "content": "Track recent actions and changes across your workspace.",
                "icon": "tabler:history",
            },
        ],
    },
    "projects": {
        "title": "Projects Management",
        "description": "Create, manage, and monitor your machine learning projects.",
        "sections": [
            {
                "title": "Creating Projects",
                "content": "Click 'Create New Project' to start a new ML project. Provide a name, description, and tags.",
                "icon": "tabler:folder-plus",
            },
            {
                "title": "Project Status",
                "content": "Projects can be Active, Completed, or Inactive. Use filters to view specific statuses.",
                "icon": "tabler:status-change",
            },
            {
                "title": "Managing Projects",
                "content": "View, edit, or delete projects using the action buttons on each project card.",
                "icon": "tabler:settings",
            },
        ],
    },
    "data_sources": {
        "title": "Data Sources",
        "description": "Connect and manage your data sources for ML experiments.",
        "sections": [
            {
                "title": "Adding Data Sources",
                "content": "Click 'Add Data Source' to connect databases, file storage, or APIs.",
                "icon": "tabler:database-plus",
            },
            {
                "title": "Connection Testing",
                "content": "Test your data source connections to ensure they're working properly.",
                "icon": "tabler:plug-connected",
            },
            {
                "title": "Data Source Types",
                "content": "Supports PostgreSQL, MySQL, MongoDB, S3, API endpoints, and more.",
                "icon": "tabler:database",
            },
        ],
    },
    "analytics": {
        "title": "Analytics Dashboard",
        "description": "View performance metrics and analytics for your ML projects.",
        "sections": [
            {
                "title": "Performance Metrics",
                "content": "Monitor model accuracy, API response times, error rates, and system uptime.",
                "icon": "tabler:chart-bar",
            },
            {
                "title": "Time Ranges",
                "content": "Filter metrics by time range: 24 hours, 7 days, 30 days, or 90 days.",
                "icon": "tabler:calendar",
            },
            {
                "title": "Exporting Data",
                "content": "Export analytics data as CSV, JSON, or PDF for reporting.",
                "icon": "tabler:download",
            },
        ],
    },
    "settings": {
        "title": "Application Settings",
        "description": "Configure your AIML Studio preferences and settings.",
        "sections": [
            {
                "title": "User Preferences",
                "content": "Customize theme, language, notifications, and display settings.",
                "icon": "tabler:user-cog",
            },
            {
                "title": "API Configuration",
                "content": "Manage API keys, webhooks, and integration settings.",
                "icon": "tabler:api",
            },
            {
                "title": "Security Settings",
                "content": "Configure authentication, access controls, and security preferences.",
                "icon": "tabler:shield-lock",
            },
        ],
    },
    "logs": {
        "title": "Application Logs",
        "description": "View and search system logs and activity history.",
        "sections": [
            {
                "title": "Log Levels",
                "content": "Filter logs by severity: DEBUG, INFO, WARNING, ERROR, CRITICAL.",
                "icon": "tabler:list-details",
            },
            {
                "title": "Searching Logs",
                "content": "Use the search bar to find specific log entries or events.",
                "icon": "tabler:search",
            },
            {
                "title": "Exporting Logs",
                "content": "Export logs for external analysis or archiving.",
                "icon": "tabler:file-export",
            },
        ],
    },
    "help": {
        "title": "Help & Documentation",
        "description": "Access documentation, tutorials, and support resources.",
        "sections": [
            {
                "title": "Getting Started",
                "content": "Learn the basics of AIML Studio and create your first project.",
                "icon": "tabler:rocket",
            },
            {
                "title": "Documentation",
                "content": "Browse comprehensive documentation and API references.",
                "icon": "tabler:book",
            },
            {
                "title": "Support",
                "content": "Get help from our support team or community forums.",
                "icon": "tabler:headset",
            },
        ],
    },
}

# Component-level tooltips
TOOLTIPS: dict[str, str] = {
    # Navigation
    "navbar_toggle": "Toggle navigation sidebar",
    "aside_toggle": "Toggle aside panel",
    "theme_switch": "Switch between light and dark theme",
    "rtl_switch": "Toggle right-to-left text direction",
    # Header
    "search": "Search projects, data sources, and more (Ctrl+K)",
    "notifications": "View notifications and alerts",
    "user_menu": "Access user profile and settings",
    # Actions
    "refresh": "Refresh data",
    "filter": "Filter results",
    "export": "Export data",
    "edit": "Edit item",
    "delete": "Delete item",
    "view": "View details",
    "create": "Create new",
    "save": "Save changes",
    "cancel": "Cancel action",
    "close": "Close dialog",
    # Projects
    "project_create": "Create a new machine learning project",
    "project_status": "Current status of the project",
    "project_tags": "Project tags and categories",
    "project_view": "View project details and experiments",
    "project_edit": "Edit project information",
    "project_delete": "Delete project permanently",
    # Data Sources
    "data_source_add": "Add a new data source connection",
    "data_source_test": "Test connection to data source",
    "data_source_type": "Type of data source (database, API, file)",
    "data_source_status": "Connection status",
    # Analytics
    "analytics_timerange": "Select time range for metrics",
    "analytics_export": "Export analytics data",
    "analytics_refresh": "Refresh analytics data",
    # Settings
    "settings_save": "Save all settings changes",
    "settings_reset": "Reset to default settings",
    "settings_import": "Import settings from file",
    "settings_export": "Export settings to file",
    # Logs
    "logs_level": "Filter by log level",
    "logs_search": "Search log entries",
    "logs_clear": "Clear log history",
    "logs_download": "Download log file",
}

# Form field help text
FIELD_HELP: dict[str, str] = {
    # Project fields
    "project_name": "A unique name for your project (e.g., 'Customer Churn Prediction')",
    "project_description": "Brief description of your project goals and methodology",
    "project_tags": "Add tags to organize and categorize your project",
    "project_status": "Set the current status: Active, Completed, or Inactive",
    # Data source fields
    "data_source_name": "Descriptive name for this data source",
    "data_source_type": "Select the type of data source you want to connect",
    "data_source_host": "Hostname or IP address of the data source",
    "data_source_port": "Port number for the connection",
    "data_source_database": "Database or schema name",
    "data_source_username": "Username for authentication",
    "data_source_password": "Password for authentication (stored securely)",
    "data_source_connection_string": "Full connection string (alternative to individual fields)",
    # Settings fields
    "settings_theme": "Choose your preferred color theme",
    "settings_language": "Select your preferred language",
    "settings_notifications": "Enable or disable notifications",
    "settings_page_size": "Default number of items per page in tables",
    "settings_timezone": "Your local timezone for date/time display",
    # User fields
    "user_email": "Your email address for notifications and login",
    "user_name": "Your full name",
    "user_role": "User role determines access permissions",
    "user_password": "Must be at least 8 characters with letters and numbers",
}

# Keyboard shortcuts
KEYBOARD_SHORTCUTS: list[dict[str, Any]] = [
    {"keys": ["Ctrl", "K"], "description": "Open search"},
    {"keys": ["Ctrl", "B"], "description": "Toggle sidebar"},
    {"keys": ["Ctrl", "/"], "description": "Show keyboard shortcuts"},
    {"keys": ["Esc"], "description": "Close modal or dialog"},
    {"keys": ["Ctrl", "S"], "description": "Save changes"},
    {"keys": ["Ctrl", "N"], "description": "Create new item"},
    {"keys": ["?"], "description": "Show help"},
]

# Notification messages
NOTIFICATION_MESSAGES: dict[str, dict[str, str]] = {
    "project_created": {
        "title": "Project Created",
        "message": "Your project has been successfully created.",
        "type": "success",
    },
    "project_updated": {
        "title": "Project Updated",
        "message": "Your project has been successfully updated.",
        "type": "success",
    },
    "project_deleted": {
        "title": "Project Deleted",
        "message": "The project has been permanently deleted.",
        "type": "info",
    },
    "data_source_connected": {
        "title": "Data Source Connected",
        "message": "Successfully connected to the data source.",
        "type": "success",
    },
    "data_source_failed": {
        "title": "Connection Failed",
        "message": "Failed to connect to the data source. Please check your settings.",
        "type": "error",
    },
    "settings_saved": {
        "title": "Settings Saved",
        "message": "Your settings have been saved successfully.",
        "type": "success",
    },
    "error_occurred": {
        "title": "Error Occurred",
        "message": "An unexpected error occurred. Please try again.",
        "type": "error",
    },
    "changes_saved": {
        "title": "Changes Saved",
        "message": "All changes have been saved successfully.",
        "type": "success",
    },
}

# Empty state messages
EMPTY_STATE_MESSAGES: dict[str, dict[str, str]] = {
    "no_projects": {
        "title": "No Projects Yet",
        "message": "Create your first machine learning project to get started.",
        "icon": "tabler:folder-off",
        "action": "Create Project",
    },
    "no_data_sources": {
        "title": "No Data Sources",
        "message": "Connect your first data source to start analyzing data.",
        "icon": "tabler:database-off",
        "action": "Add Data Source",
    },
    "no_logs": {
        "title": "No Logs Available",
        "message": "No log entries found for the selected filters.",
        "icon": "tabler:file-off",
        "action": "Clear Filters",
    },
    "no_notifications": {
        "title": "No Notifications",
        "message": "You're all caught up! No new notifications.",
        "icon": "tabler:bell-off",
        "action": None,
    },
    "no_results": {
        "title": "No Results Found",
        "message": "Try adjusting your search or filters.",
        "icon": "tabler:search-off",
        "action": "Clear Search",
    },
}
