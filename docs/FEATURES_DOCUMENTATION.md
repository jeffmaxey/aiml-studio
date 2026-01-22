# AIML Studio - Persistence, Caching, Notifications, Modals, and Help System

## Overview

This document provides comprehensive documentation for the persistence, caching, notifications, modals, alerts, tooltips, and help text features implemented in AIML Studio.

## Table of Contents

1. [Persistence System](#persistence-system)
2. [Caching System](#caching-system)
3. [Notification System](#notification-system)
4. [Modal System](#modal-system)
5. [Alert System](#alert-system)
6. [Tooltip System](#tooltip-system)
7. [Help Text System](#help-text-system)
8. [Usage Examples](#usage-examples)

---

## Persistence System

### Overview

The persistence system provides browser-based storage for user preferences and application state using Dash's `dcc.Store` components.

### Components

#### BrowserPersistenceManager

**Location**: `aiml_studio/managers/persistence_manager.py`

**Features**:
- localStorage equivalent for persistent data
- sessionStorage equivalent for temporary session data
- In-memory storage for transient data
- JSON serialization/deserialization
- Type-safe storage operations

**Usage**:

```python
from aiml_studio.managers import BrowserPersistenceManager

# Initialize
persistence_manager = BrowserPersistenceManager()
persistence_manager.initialize()

# Save data
persistence_manager.save("theme", "dark", storage_type="local")

# Load data
theme = persistence_manager.load("theme", storage_type="local", default="light")

# Delete data
persistence_manager.delete("theme", storage_type="local")

# Clear all data
persistence_manager.clear(storage_type="local")
```

### Storage Types

- **local**: Persists across browser sessions (equivalent to localStorage)
- **session**: Persists only for the current browser session (equivalent to sessionStorage)
- **memory**: In-memory only, lost on page refresh

### User Preferences

User preferences are automatically saved and restored:

- Theme selection (light/dark)
- RTL text direction
- Sidebar collapse state
- Custom display settings

**Implementation**: See `aiml_studio/callbacks/global_callbacks.py`

---

## Caching System

### Overview

The caching system provides LRU (Least Recently Used) caching with TTL (Time-To-Live) support for expensive operations.

### Components

#### LRUCacheManager

**Location**: `aiml_studio/managers/cache_manager.py`

**Features**:
- LRU eviction policy
- Configurable TTL per cache entry
- Cache statistics (hits, misses, evictions)
- Maximum cache size limit
- Automatic expiration

**Usage**:

```python
from aiml_studio.managers import LRUCacheManager

# Initialize with max_size and default TTL
cache_manager = LRUCacheManager(max_size=100, default_ttl=3600)
cache_manager.initialize()

# Set value with custom TTL (600 seconds)
cache_manager.set("user_data", user_data, ttl=600)

# Get value
data = cache_manager.get("user_data", default=None)

# Check if key exists
if cache_manager.has_key("user_data"):
    # Use cached data
    pass

# Get statistics
stats = cache_manager.get_stats()
print(f"Hits: {stats['hits']}, Misses: {stats['misses']}")
```

#### Cache Decorator

**Usage**:

```python
from aiml_studio.managers import cached, cache_manager

@cached(cache_manager, ttl=300, key_prefix="api")
def expensive_api_call(param1, param2):
    """This function's results will be cached for 5 minutes."""
    # Expensive operation
    return result
```

### Cache Statistics

- **hits**: Number of successful cache retrievals
- **misses**: Number of cache misses
- **sets**: Number of cache writes
- **evictions**: Number of LRU evictions

---

## Notification System

### Overview

The notification system provides toast notifications, inline alerts, and notification management.

### Components

#### NotificationProvider

**Location**: `aiml_studio/components/notifications.py`

**Features**:
- Toast notifications (top-right by default)
- Auto-close with configurable duration
- Notification queue with limit
- Multiple notification types

**Types**:
- `success`: Green, check icon
- `error`: Red, X icon
- `info`: Blue, info icon
- `warning`: Yellow, warning icon

#### Creating Notifications

```python
from aiml_studio.components import create_notification

# Create a success notification
notification = create_notification(
    title="Success",
    message="Your project has been created successfully.",
    notification_type="success",
    auto_close=5000,  # 5 seconds
)

# Create a persistent notification (no auto-close)
notification = create_notification(
    title="Important",
    message="Please review these settings.",
    notification_type="info",
    auto_close=False,
)

# Create notification with action button
notification = create_notification(
    title="Update Available",
    message="A new version is available.",
    notification_type="info",
    action={"label": "Update Now", "onClick": "handleUpdate"},
)
```

#### Inline Alerts

```python
from aiml_studio.components import create_inline_alert

# Create an inline alert
alert = create_inline_alert(
    title="Welcome",
    message="This is your first time here. Let's get started!",
    alert_type="info",
    dismissible=True,
    variant="light",  # or "filled" or "outline"
)
```

#### Notification Bell

```python
from aiml_studio.components import create_notification_bell

# Create notification bell with unread count
bell = create_notification_bell(unread_count=5)
```

### Constants

**Location**: `aiml_studio/constants_help.py`

Pre-defined notification messages:

```python
NOTIFICATION_MESSAGES = {
    "project_created": {
        "title": "Project Created",
        "message": "Your project has been successfully created.",
        "type": "success",
    },
    # ... more messages
}
```

---

## Modal System

### Overview

The modal system provides reusable dialog components for confirmations, alerts, and forms.

### Components

**Location**: `aiml_studio/components/modals.py`

#### Basic Modal

```python
from aiml_studio.components import create_modal

modal = create_modal(
    modal_id="my-modal",
    title="Modal Title",
    children=[
        dmc.Text("Modal content goes here"),
        dmc.Button("Close", id="close-modal-btn"),
    ],
    size="md",  # xs, sm, md, lg, xl, full
    opened=False,  # Initially closed
)
```

#### Confirmation Modal

```python
from aiml_studio.components import create_confirm_modal

modal = create_confirm_modal(
    modal_id="delete-confirm",
    title="Delete Project",
    message="Are you sure you want to delete this project? This action cannot be undone.",
    confirm_label="Delete",
    cancel_label="Cancel",
    confirm_color="red",
    icon="tabler:trash",
)
```

#### Alert Modal

```python
from aiml_studio.components import create_alert_modal

modal = create_alert_modal(
    modal_id="success-alert",
    title="Success",
    message="Your changes have been saved successfully.",
    alert_type="success",  # success, error, info, warning
    button_label="OK",
)
```

#### Form Modal

```python
from aiml_studio.components import create_form_modal

form_fields = [
    dmc.TextInput(label="Name", id="name-input"),
    dmc.TextInput(label="Email", id="email-input"),
]

modal = create_form_modal(
    modal_id="edit-form",
    title="Edit User",
    form_fields=form_fields,
    submit_label="Save",
    cancel_label="Cancel",
)
```

#### Drawer (Side Panel)

```python
from aiml_studio.components import create_drawer

drawer = create_drawer(
    drawer_id="help-drawer",
    title="Help & Documentation",
    children=[dmc.Text("Help content here")],
    position="right",  # left, right, top, bottom
    size="md",
)
```

### Modal Properties

- **size**: xs, sm, md, lg, xl, full
- **centered**: Vertically center the modal
- **closeOnEscape**: Close when Escape key is pressed
- **closeOnClickOutside**: Close when clicking outside
- **withCloseButton**: Show close button
- **overlayProps**: Customize overlay appearance

---

## Alert System

### Overview

Inline alerts for displaying contextual messages within pages.

### Components

#### Inline Alert

```python
from aiml_studio.components import create_inline_alert

# Success alert
alert = create_inline_alert(
    title="Success",
    message="Operation completed successfully.",
    alert_type="success",
    dismissible=True,
)

# Error alert
alert = create_inline_alert(
    title="Error",
    message="An error occurred. Please try again.",
    alert_type="error",
    dismissible=True,
    variant="filled",
)

# Info alert
alert = create_inline_alert(
    title="Information",
    message="Please note this important information.",
    alert_type="info",
    variant="outline",
)
```

### Alert Types and Colors

| Type      | Color  | Icon               | Use Case           |
|-----------|--------|--------------------|--------------------|
| success   | Green  | check              | Success messages   |
| error     | Red    | x                  | Error messages     |
| info      | Blue   | info-circle        | Information        |
| warning   | Yellow | alert-triangle     | Warnings           |

### Variants

- **light**: Light background (default)
- **filled**: Solid color background
- **outline**: Border only

---

## Tooltip System

### Overview

Tooltips provide contextual information on hover for UI elements.

### Components

**Location**: `aiml_studio/components/tooltips.py`

#### Basic Tooltip

```python
from aiml_studio.components import create_tooltip

tooltip = create_tooltip(
    children=dmc.Button("Hover me"),
    label="This is a helpful tooltip",
    position="top",  # top, right, bottom, left
    with_arrow=True,
)
```

#### Help Icon

```python
from aiml_studio.components import create_help_icon

help_icon = create_help_icon(
    tooltip_text="This field accepts email addresses in the format: name@example.com",
)
```

#### Info Icon

```python
from aiml_studio.components import create_info_icon

info_icon = create_info_icon(
    tooltip_text="Additional information about this feature.",
    color="blue",
)
```

#### Label with Help

```python
from aiml_studio.components import create_label_with_help

label = create_label_with_help(
    label="Email Address",
    help_text="Enter your email address for notifications",
    required=True,  # Shows asterisk
)
```

#### Popover Help

```python
from aiml_studio.components import create_popover_help

popover = create_popover_help(
    children=dmc.ActionIcon(DashIconify(icon="tabler:help")),
    help_title="How to Use This Feature",
    help_content="Detailed instructions go here...",
    width=320,
)
```

### Tooltip Constants

**Location**: `aiml_studio/constants_help.py`

```python
TOOLTIPS = {
    "refresh": "Refresh data",
    "filter": "Filter results",
    "export": "Export data",
    "project_create": "Create a new machine learning project",
    # ... more tooltips
}
```

**Usage**:

```python
from aiml_studio.constants_help import TOOLTIPS

tooltip = create_tooltip(
    children=button,
    label=TOOLTIPS.get("refresh", "Refresh"),
)
```

---

## Help Text System

### Overview

Comprehensive help text and contextual assistance throughout the application.

### Components

#### Help Text

```python
from aiml_studio.components import create_help_text

help_text = create_help_text(
    text="Enter a unique name for your project",
    size="xs",
    icon="tabler:info-circle",
)
```

#### Field Description

```python
from aiml_studio.components import create_field_description

description = create_field_description(
    description="Must be at least 8 characters",
    type="help",  # help, error, warning, info
)
```

#### Help Section

```python
from aiml_studio.components import create_help_section

section = create_help_section(
    title="Getting Started",
    content="Follow these steps to create your first project...",
    icon="tabler:rocket",
    collapsible=False,
)
```

#### Help Content Section

```python
from aiml_studio.components import create_help_content_section

sections = [
    {
        "title": "Creating Projects",
        "content": "Click 'Create New Project' to start...",
        "icon": "tabler:folder-plus",
    },
    {
        "title": "Managing Data",
        "content": "Connect data sources from the Data Sources page...",
        "icon": "tabler:database",
    },
]

help_content = create_help_content_section(sections)
```

#### Keyboard Shortcuts

```python
from aiml_studio.components import create_keyboard_shortcut

shortcut = create_keyboard_shortcut(
    keys=["Ctrl", "K"],
    description="Open search",
)
```

### Help Constants

**Location**: `aiml_studio/constants_help.py`

#### Page Help

```python
PAGE_HELP = {
    "home": {
        "title": "Home Dashboard",
        "description": "View your AIML Studio dashboard...",
        "sections": [
            {
                "title": "Key Metrics",
                "content": "Monitor your project status...",
                "icon": "tabler:chart-line",
            },
        ],
    },
}
```

#### Field Help

```python
FIELD_HELP = {
    "project_name": "A unique name for your project (e.g., 'Customer Churn Prediction')",
    "project_description": "Brief description of your project goals and methodology",
    # ... more field help
}
```

#### Keyboard Shortcuts

```python
KEYBOARD_SHORTCUTS = [
    {"keys": ["Ctrl", "K"], "description": "Open search"},
    {"keys": ["Ctrl", "B"], "description": "Toggle sidebar"},
    {"keys": ["Esc"], "description": "Close modal or dialog"},
]
```

---

## Usage Examples

### Example 1: Form with Help Text

```python
import dash_mantine_components as dmc
from aiml_studio.components import create_label_with_help, create_field_description
from aiml_studio.constants_help import FIELD_HELP

form = dmc.Stack([
    create_label_with_help(
        label="Project Name",
        help_text=FIELD_HELP["project_name"],
        required=True,
    ),
    dmc.TextInput(
        id="project-name-input",
        placeholder="Enter project name",
    ),
    create_field_description(
        description="This name will be displayed in project lists",
        type="help",
    ),
])
```

### Example 2: Button with Tooltip and Confirmation Modal

```python
from aiml_studio.components import create_tooltip, create_confirm_modal

layout = html.Div([
    create_tooltip(
        dmc.Button(
            "Delete Project",
            color="red",
            id="delete-btn",
        ),
        label="Permanently delete this project",
    ),
    create_confirm_modal(
        modal_id="delete-confirm",
        title="Confirm Deletion",
        message="Are you sure? This action cannot be undone.",
        confirm_label="Delete",
        confirm_color="red",
        icon="tabler:trash",
    ),
])
```

### Example 3: Page with Help Section

```python
from aiml_studio.components import create_help_section, create_help_icon
from aiml_studio.constants_help import PAGE_HELP

page_help = PAGE_HELP.get("projects", {})

layout = dmc.Stack([
    dmc.Group([
        dmc.Title("Projects", order=2),
        create_help_icon(page_help.get("description", "")),
    ]),
    # ... page content ...
    create_help_content_section(page_help.get("sections", [])),
])
```

### Example 4: Notification on Success

```python
from aiml_studio.components import create_notification
from aiml_studio.constants_help import NOTIFICATION_MESSAGES

@callback(
    Output("notification-trigger", "data"),
    Input("save-btn", "n_clicks"),
)
def save_data(n_clicks):
    if n_clicks:
        # Save logic here
        msg = NOTIFICATION_MESSAGES["changes_saved"]
        # Trigger notification
        return n_clicks
    return no_update
```

### Example 5: Cached Function

```python
from aiml_studio.managers import cached, cache_manager

@cached(cache_manager, ttl=3600, key_prefix="analytics")
def get_analytics_data(start_date, end_date):
    """Fetch analytics data - cached for 1 hour."""
    # Expensive database query
    return data
```

---

## Best Practices

### Persistence

1. **Use appropriate storage types**:
   - `local` for user preferences
   - `session` for temporary workflow state
   - `memory` for transient UI state

2. **Keep stored data minimal**: Only store what's necessary

3. **Validate data on load**: Always provide defaults

### Caching

1. **Cache expensive operations**: Database queries, API calls, computations

2. **Set appropriate TTLs**: 
   - Short TTL (5-15 min) for frequently changing data
   - Medium TTL (30-60 min) for relatively static data
   - Long TTL (1-24 hours) for rarely changing data

3. **Monitor cache statistics**: Track hit rates and evictions

### Notifications

1. **Use appropriate types**: Match notification type to message severity

2. **Keep messages concise**: Clear and actionable

3. **Set reasonable auto-close times**:
   - Success: 3-5 seconds
   - Info: 5-7 seconds
   - Warning: 7-10 seconds
   - Error: 10+ seconds or manual dismiss

### Modals

1. **Use sparingly**: Don't overuse modals; they interrupt workflow

2. **Provide clear actions**: Always have clear confirm/cancel buttons

3. **Size appropriately**: Match modal size to content

### Tooltips

1. **Be concise**: Keep tooltip text short and helpful

2. **Use consistently**: Apply to all interactive elements

3. **Position wisely**: Default to top, adjust for edge cases

### Help Text

1. **Provide context**: Explain why, not just what

2. **Include examples**: Show expected formats

3. **Progressive disclosure**: Use popovers for detailed help

---

## Testing

### Manual Testing Checklist

- [ ] Persistence: Verify preferences persist across page refreshes
- [ ] Caching: Check cache hit/miss rates
- [ ] Notifications: Test all notification types and auto-close
- [ ] Modals: Verify keyboard shortcuts (Escape to close)
- [ ] Alerts: Test dismissible alerts
- [ ] Tooltips: Check positioning on all screen sizes
- [ ] Help Text: Verify help icons display correct content

### Automated Testing

```python
# Example test for persistence
def test_persistence_save_and_load():
    manager = BrowserPersistenceManager()
    manager.initialize()
    
    # Save
    assert manager.save("test_key", "test_value", "memory")
    
    # Load
    value = manager.load("test_key", "memory")
    assert value == "test_value"
    
    # Delete
    assert manager.delete("test_key", "memory")
    
    # Verify deleted
    value = manager.load("test_key", "memory", default="default")
    assert value == "default"
```

---

## Troubleshooting

### Common Issues

**Issue**: Tooltips not appearing
- **Solution**: Ensure Mantine Provider is wrapping the component

**Issue**: Modals not closing on Escape
- **Solution**: Check `closeOnEscape=True` prop

**Issue**: Cache not working
- **Solution**: Verify cache_manager is initialized

**Issue**: Preferences not persisting
- **Solution**: Check browser localStorage is enabled

---

## Future Enhancements

- [ ] Add notification sound options
- [ ] Implement notification grouping
- [ ] Add modal animations customization
- [ ] Create help video integration
- [ ] Add A/B testing for tooltips
- [ ] Implement user feedback collection
- [ ] Add analytics for help usage

---

## Resources

- [Dash Mantine Components - Notifications](https://www.dash-mantine-components.com/components/notifications)
- [Dash Mantine Components - Modals](https://www.dash-mantine-components.com/components/modal)
- [Dash Mantine Components - Tooltips](https://www.dash-mantine-components.com/components/tooltip)
- [LRU Cache Algorithm](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))

---

## Contributing

When adding new features that use these systems:

1. Update constants in `constants_help.py`
2. Add help text and tooltips to all interactive elements
3. Use appropriate notification types
4. Provide confirmation modals for destructive actions
5. Test across different screen sizes
6. Update this documentation

---

## License

This implementation is part of AIML Studio and follows the project's license terms.
