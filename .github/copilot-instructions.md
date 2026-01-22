# GitHub Copilot Instructions for AIML Studio

## Project Overview

AIML Studio is a production-ready multipage Dash application for running predictive analytics and machine learning experiments. The application uses dash-mantine-components v2, dash_iconify, and dash_ag_grid for a modern, responsive UI.

## Architecture

### Package Structure

```
aiml_studio/
├── app.py                      # Main Dash application with pages support
├── constants.py                # Centralized constants (colors, nav links, sizes)
├── settings.py                 # Environment-based configuration
├── managers/                   # Application & data management
│   ├── application_manager.py  # State, sessions, utilities management
│   └── data_manager.py         # CRUD operations for all entities
├── utilities/                  # Logging & profiling utilities
│   ├── logger.py               # Centralized logging
│   └── profiler.py             # Performance monitoring
├── components/                 # Reusable UI components
│   ├── navbar.py               # Navigation with theme/RTL controls
│   ├── header.py               # Header with toggle buttons
│   ├── footer.py               # Application footer
│   ├── aside.py                # Aside panel
│   └── tables.py               # AG Grid table factories
├── layouts/                    # Page-specific layouts
│   ├── appshell.py             # Main AppShell container
│   ├── home.py                 # Home page layout
│   ├── settings_page.py        # Settings page layout
│   ├── help.py                 # Help page layout
│   ├── logs.py                 # Logs page layout
│   ├── analytics.py            # Analytics dashboard layout
│   ├── data_sources.py         # Data sources page layout
│   └── projects.py             # Projects page layout
├── pages/                      # Dash pages registry
│   ├── home.py                 # Home page registration
│   ├── settings.py             # Settings page registration
│   ├── help.py                 # Help page registration
│   ├── logs.py                 # Logs page registration
│   ├── analytics.py            # Analytics page registration
│   ├── data_sources.py         # Data sources page registration
│   └── projects.py             # Projects page registration
├── callbacks/                  # Page-specific callbacks
│   ├── home_callbacks.py
│   ├── settings_callbacks.py
│   ├── help_callbacks.py
│   ├── logs_callbacks.py
│   ├── analytics_callbacks.py
│   ├── data_sources_callbacks.py
│   └── projects_callbacks.py
├── styles/                     # Theme configuration
│   └── theme.py                # Mantine theme setup
└── assets/                     # Static assets
    └── custom.css              # Professional stylesheet
```

## Coding Standards

### Python Style

- **PEP 8 Compliance**: Follow PEP 8 style guidelines strictly
- **Type Hints**: All functions must include type hints for parameters and return values
- **Docstrings**: Use Google-style docstrings for all functions, classes, and modules
- **Line Length**: Maximum 100 characters per line
- **Imports**: Organize imports in three groups (standard library, third-party, local)

### Type Annotations

```python
from typing import Any

def create_component(data: dict[str, Any], config: dict[str, str] | None = None) -> dmc.Component:
    """Create a reusable component.
    
    Args:
        data: Component data dictionary
        config: Optional configuration dictionary
        
    Returns:
        Mantine component instance
    """
    pass
```

### Docstring Format

```python
def example_function(param1: str, param2: int) -> bool:
    """Brief description of function.
    
    Longer description if needed. Explain what the function does,
    any side effects, and important behavior.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input is provided
        
    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
    pass
```

## Component Development

### UI Components (dash-mantine-components v2)

**ALWAYS use dash-mantine-components v2 for ALL UI elements:**

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Use Mantine components for layout
dmc.Stack(children=[...])
dmc.Group(children=[...])
dmc.Paper(children=[...])
dmc.Card(children=[...])

# Use Mantine components for forms
dmc.TextInput(id="input-id", label="Label")
dmc.Select(id="select-id", data=options)
dmc.Switch(id="switch-id", label="Toggle")

# Use DashIconify for all icons
DashIconify(icon="tabler:home", width=20)
```

### Tables (dash_ag_grid)

**ALWAYS use dash_ag_grid for ALL tables:**

```python
import dash_ag_grid as dag

# Use the factory function from components/tables.py
from aiml_studio.components.tables import create_ag_grid

table = create_ag_grid(
    grid_id="my-grid",
    column_defs=[
        {"field": "name", "headerName": "Name"},
        {"field": "value", "headerName": "Value"},
    ],
    row_data=data,
    pagination=True,
    page_size=20,
)
```

### Layout Patterns

**Use consistent layout patterns:**

```python
# Page layout structure
def create_page_layout() -> dmc.Container:
    """Create page layout."""
    return dmc.Container(
        [
            dmc.Title("Page Title", order=2),
            dmc.Space(h="md"),
            dmc.Stack(
                [
                    # Page content sections
                    create_section_one(),
                    create_section_two(),
                ],
                gap="lg",
            ),
        ],
        size="xl",
        py="md",
    )
```

## Callbacks

### Callback Organization

- One callback file per page in `callbacks/` directory
- Import callbacks in `app.py` to register them
- Use `prevent_initial_call=True` for interactive callbacks
- Use clientside callbacks for simple DOM manipulations

### Callback Pattern

```python
from dash import Input, Output, State, callback

@callback(
    Output("output-id", "property"),
    Input("input-id", "property"),
    State("state-id", "property"),
    prevent_initial_call=True,
)
def callback_name(input_value: Any, state_value: Any) -> Any:
    """Brief description of callback.
    
    Args:
        input_value: Description
        state_value: Description
        
    Returns:
        Updated output value
    """
    # Callback logic
    return result
```

### Clientside Callbacks

Use for performance-critical operations:

```python
from dash import clientside_callback, Input, Output

clientside_callback(
    """
    function(value) {
        // JavaScript code
        return value;
    }
    """,
    Output("output-id", "property"),
    Input("input-id", "property"),
)
```

## Manager Integration

### ApplicationManager

Use for application-wide state management:

```python
from aiml_studio.app import app_manager

# Get/set application state
theme = app_manager.get_state("theme", "light")
app_manager.set_state("theme", "dark")

# Session management
app_manager.create_session(session_id, user_data)
session = app_manager.get_session(session_id)

# Settings
app_manager.set_setting("default_page_size", 20)
```

### DataManager

Use for all CRUD operations:

```python
from aiml_studio.app import data_manager

# Create
data_manager.create("projects", project_id, project_data)

# Read
project = data_manager.retrieve("projects", project_id)
all_projects = data_manager.list_all("projects")

# Update
data_manager.update("projects", project_id, updated_data)

# Delete
data_manager.delete("projects", project_id)

# Search
results = data_manager.search("projects", {"status": "active"})
```

## Styling

### CSS Classes

Use the professional stylesheet in `assets/custom.css`:

- Modern animations and transitions
- Enhanced scrollbar styling
- Card hover effects
- RTL support
- Responsive utilities

### Theme Configuration

Configure themes in `styles/theme.py`:

```python
# Light/Dark mode support
forceColorScheme="light"  # or "dark"

# Mantine theme customization
theme = {
    "colorScheme": "light",
    "primaryColor": "blue",
    # Additional theme settings
}
```

## Testing

### Manual Testing

```bash
# Start the application
uv run python -m aiml_studio.app

# Navigate to http://localhost:8050
# Test all features:
# - Navbar toggle (top-left)
# - Aside toggle (top-right)
# - Theme switch (navbar)
# - RTL toggle (navbar)
# - All page navigation
```

### Code Quality

```bash
# Format code
uv run ruff format aiml_studio/

# Lint code
uv run ruff check aiml_studio/

# Type check
uv run mypy aiml_studio/

# Run tests
uv run pytest tests/
```

## Common Patterns

### Creating a New Page

1. **Create layout** in `layouts/new_page.py`:
```python
import dash_mantine_components as dmc

def create_new_page_layout() -> dmc.Container:
    """Create new page layout."""
    return dmc.Container([
        dmc.Title("New Page", order=2),
        # Page content
    ])
```

2. **Register page** in `pages/new_page.py`:
```python
import dash
from aiml_studio.layouts.new_page import create_new_page_layout

dash.register_page(
    __name__,
    path="/new-page",
    title="New Page - AIML Studio",
    name="New Page",
)

layout = create_new_page_layout()
```

3. **Add callbacks** in `callbacks/new_page_callbacks.py`:
```python
from dash import Input, Output, callback

@callback(
    Output("output-id", "children"),
    Input("input-id", "value"),
)
def update_content(value: str) -> str:
    """Update page content."""
    return f"Value: {value}"
```

4. **Import callbacks** in `app.py`:
```python
from aiml_studio.callbacks import new_page_callbacks  # noqa: F401
```

5. **Add navigation link** in `constants.py`:
```python
NAV_LINKS = [
    # ...
    {"label": "New Page", "icon": "tabler:new", "href": "/new-page", "section": "core"},
]
```

### Creating a Reusable Component

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

def create_metric_card(title: str, value: str, icon: str, color: str = "blue") -> dmc.Card:
    """Create a metric display card.
    
    Args:
        title: Card title
        value: Metric value
        icon: Icon identifier
        color: Mantine color name
        
    Returns:
        Styled metric card component
    """
    return dmc.Card(
        [
            dmc.Group(
                [
                    DashIconify(icon=icon, width=30, color=color),
                    dmc.Stack(
                        [
                            dmc.Text(title, size="sm", c="dimmed"),
                            dmc.Title(value, order=3),
                        ],
                        gap=0,
                    ),
                ],
                justify="space-between",
            ),
        ],
        withBorder=True,
        radius="md",
        p="lg",
    )
```

## Best Practices

### Do's ✅

- Use type hints for all function parameters and returns
- Write comprehensive docstrings
- Use dash-mantine-components v2 for ALL UI
- Use dash_ag_grid for ALL tables
- Use dash_iconify for ALL icons
- Organize code by feature/page
- Use managers for state and data operations
- Test all features before committing
- Follow PEP 8 style guidelines
- Use descriptive variable names

### Don'ts ❌

- Don't use plain HTML/Dash core components (use Mantine instead)
- Don't use DataTable (use dash_ag_grid instead)
- Don't hardcode values (use constants.py)
- Don't write code without type hints
- Don't skip docstrings
- Don't create global state outside managers
- Don't mix UI and business logic
- Don't commit without testing
- Don't ignore linting errors

## Security

- Never commit secrets or API keys
- Validate all user inputs
- Use parameterized queries (when applicable)
- Log security events through utilities/logger.py
- Follow principle of least privilege

## Performance

- Use clientside callbacks for simple operations
- Profile with utilities/profiler.py
- Lazy load large datasets
- Use pagination in tables
- Minimize callback chains

## Documentation

- Keep docs/ARCHITECTURE.md updated
- Document all new features in PR descriptions
- Include usage examples in docstrings
- Update README.md for user-facing changes
- Add screenshots for UI changes

## Git Workflow

- Create feature branches from main
- Write clear commit messages
- Keep commits focused and atomic
- Test before pushing
- Update documentation in same commit as code

## Resources

- [Dash Documentation](https://dash.plotly.com/)
- [Dash Mantine Components](https://www.dash-mantine-components.com/)
- [AG Grid for Dash](https://dashaggrid.pythonanywhere.com/)
- [Dash Iconify](https://github.com/snehilvj/dash-iconify)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## Getting Help

- Check docs/ARCHITECTURE.md for architecture details
- Review existing code for patterns
- Test locally before committing
- Ask for clarification on requirements
