# Quick Reference Guide - UI Enhancement Features

## Quick Imports

```python
# Managers
from aiml_studio.managers import (
    BrowserPersistenceManager,
    LRUCacheManager,
    cached,
)

# Components
from aiml_studio.components import (
    # Notifications
    create_notification,
    create_inline_alert,
    create_notification_bell,
    
    # Modals
    create_modal,
    create_confirm_modal,
    create_alert_modal,
    create_form_modal,
    create_drawer,
    
    # Tooltips & Help
    create_tooltip,
    create_help_icon,
    create_info_icon,
    create_label_with_help,
    create_help_text,
    create_help_section,
)

# Constants
from aiml_studio.constants_help import (
    TOOLTIPS,
    FIELD_HELP,
    PAGE_HELP,
    NOTIFICATION_MESSAGES,
    KEYBOARD_SHORTCUTS,
)
```

## Common Patterns

### 1. Add Tooltip to Button

```python
create_tooltip(
    dmc.Button("Click me", id="my-btn"),
    label=TOOLTIPS.get("action_name", "Description here"),
)
```

### 2. Form Field with Help

```python
dmc.Stack([
    create_label_with_help(
        label="Field Name",
        help_text=FIELD_HELP["field_key"],
        required=True,
    ),
    dmc.TextInput(id="field-input"),
])
```

### 3. Confirmation Modal

```python
create_confirm_modal(
    modal_id="delete-modal",
    title="Delete Item",
    message="Are you sure?",
    confirm_label="Delete",
    confirm_color="red",
    icon="tabler:trash",
)
```

### 4. Success Notification

```python
create_notification(
    title="Success",
    message="Operation completed!",
    notification_type="success",
    auto_close=5000,
)
```

### 5. Inline Alert

```python
create_inline_alert(
    title="Warning",
    message="Please review these settings.",
    alert_type="warning",
    dismissible=True,
)
```

### 6. Cache Expensive Function

```python
@cached(cache_manager, ttl=3600)
def expensive_operation(param):
    # Your code here
    return result
```

### 7. Page Help Section

```python
help_data = PAGE_HELP.get("page_name", {})
create_help_content_section(help_data.get("sections", []))
```

## Component Props Quick Reference

### Tooltip
- `label`: Text to display
- `position`: "top", "right", "bottom", "left"
- `with_arrow`: True/False
- `multiline`: True/False (for long text)
- `width`: Fixed width in pixels

### Modal
- `size`: "xs", "sm", "md", "lg", "xl", "full"
- `centered`: True/False
- `closeOnEscape`: True/False
- `closeOnClickOutside`: True/False
- `withCloseButton`: True/False

### Alert
- `alert_type`: "success", "error", "info", "warning"
- `variant`: "light", "filled", "outline"
- `dismissible`: True/False
- `icon`: Icon identifier (optional)

### Notification
- `notification_type`: "success", "error", "info", "warning"
- `auto_close`: milliseconds or False
- `action`: Button configuration (optional)

## Color Mapping

| Type    | Color  | Use Case        |
|---------|--------|-----------------|
| success | green  | Success states  |
| error   | red    | Errors          |
| info    | blue   | Information     |
| warning | yellow | Warnings        |

## Icon Conventions

| Purpose        | Icon                  |
|----------------|-----------------------|
| Help           | tabler:help-circle    |
| Info           | tabler:info-circle    |
| Success        | tabler:check-circle   |
| Error          | tabler:x-circle       |
| Warning        | tabler:alert-triangle |
| Delete         | tabler:trash          |
| Edit           | tabler:edit           |
| View           | tabler:eye            |
| Refresh        | tabler:refresh        |
| Filter         | tabler:filter         |

## Callback Patterns

### Save Preferences

```python
@callback(
    Output("user-preferences", "data"),
    Input("some-input", "value"),
    State("user-preferences", "data"),
)
def save_preference(value, prefs):
    prefs = prefs or {}
    prefs["setting_name"] = value
    return prefs
```

### Show Notification

```python
@callback(
    Output("notification-trigger", "data"),
    Input("save-btn", "n_clicks"),
)
def show_notification(n_clicks):
    if n_clicks:
        # Trigger notification display
        return n_clicks
    return no_update
```

### Open Modal

```python
@callback(
    Output("modal-id", "opened"),
    Input("open-modal-btn", "n_clicks"),
    prevent_initial_call=True,
)
def open_modal(n_clicks):
    return True
```

### Close Modal

```python
@callback(
    Output("modal-id", "opened"),
    [Input("cancel-btn", "n_clicks"), Input("confirm-btn", "n_clicks")],
    prevent_initial_call=True,
)
def close_modal(cancel, confirm):
    return False
```

## TTL Guidelines

| Data Type              | Recommended TTL |
|------------------------|-----------------|
| User profile           | 1 hour          |
| Analytics data         | 15 minutes      |
| Configuration          | 24 hours        |
| Search results         | 5 minutes       |
| API responses          | 30 minutes      |
| Static content         | 7 days          |

## Accessibility Checklist

- [ ] All interactive elements have tooltips
- [ ] Form fields have help text
- [ ] Modals can be closed with Escape key
- [ ] Color contrast meets WCAG 2.1 AA
- [ ] Screen reader labels are present
- [ ] Keyboard navigation works
- [ ] Focus indicators are visible

## Performance Tips

1. **Cache aggressively**: Cache expensive operations
2. **Set appropriate TTLs**: Don't cache forever
3. **Use memory storage**: For temporary UI state
4. **Limit notification queue**: Max 3-5 visible
5. **Lazy load help content**: Load on demand
6. **Minimize modal content**: Keep modals focused

## Common Mistakes

❌ **Don't**: Hardcode tooltip text
```python
create_tooltip(button, label="Refresh")
```

✅ **Do**: Use constants
```python
create_tooltip(button, label=TOOLTIPS["refresh"])
```

---

❌ **Don't**: Skip help text for complex fields
```python
dmc.TextInput(label="Regex Pattern")
```

✅ **Do**: Provide context
```python
create_label_with_help(
    "Regex Pattern",
    FIELD_HELP["regex_pattern"],
)
```

---

❌ **Don't**: Cache without TTL
```python
cache_manager.set("key", value)  # Uses default TTL
```

✅ **Do**: Set explicit TTL
```python
cache_manager.set("key", value, ttl=300)
```

---

❌ **Don't**: Show too many notifications
```python
# Showing 10 notifications at once
```

✅ **Do**: Limit and prioritize
```python
# Use notification queue limit (max 3)
```

## Testing Checklist

### Persistence
- [ ] Save and reload preferences
- [ ] Clear storage works
- [ ] Different storage types work

### Caching
- [ ] Cache hits increase over time
- [ ] Expired entries are removed
- [ ] LRU eviction works

### Notifications
- [ ] All types display correctly
- [ ] Auto-close timing works
- [ ] Dismiss button works

### Modals
- [ ] Open/close works
- [ ] Escape key closes
- [ ] Click outside closes (when enabled)

### Tooltips
- [ ] Appear on hover
- [ ] Position correctly
- [ ] Arrows point to element

### Help Text
- [ ] Icons display popover
- [ ] Content is accurate
- [ ] Keyboard shortcuts work

## Debugging

### Enable Debug Logging

```python
import logging
logging.getLogger("aiml_studio").setLevel(logging.DEBUG)
```

### Check Cache Stats

```python
stats = cache_manager.get_stats()
print(f"Hit rate: {stats['hits'] / (stats['hits'] + stats['misses']):.2%}")
```

### Inspect Stored Data

```python
prefs = persistence_manager.get_all("local")
print(f"Stored preferences: {prefs}")
```

## Need Help?

- **Documentation**: `docs/FEATURES_DOCUMENTATION.md`
- **Examples**: Check `layouts/home.py` and `layouts/projects.py`
- **Constants**: See `constants_help.py` for all pre-defined text
- **Components**: Browse `components/` directory for available components

## Contributing

When adding new features:

1. Add constants to `constants_help.py`
2. Use existing component factories
3. Follow naming conventions
4. Add tooltips and help text
5. Write tests
6. Update documentation

---

*Last updated: 2024-01-22*
