# AIML Studio - Enhanced Architecture Documentation

## Overview

This document describes the enhanced architecture of AIML Studio with integrated managers and utilities.

## New Features

### 1. Header Controls
- **Navbar Toggle Button**: Top-left button to collapse/expand the navigation sidebar
- **Aside Toggle Button**: Top-right button to collapse/expand the aside panel

### 2. Navbar Appearance Controls
- **Theme Toggle**: Switch between light and dark modes (Sun/Moon icons)
- **RTL Toggle**: Switch between left-to-right (LTR) and right-to-left (RTL) text direction

### 3. Professional Stylesheet
A comprehensive CSS stylesheet (`assets/custom.css`) provides:
- Modern animations and transitions
- Enhanced scrollbar styling for light and dark modes
- Card hover effects
- Consistent button and icon interactions
- AG Grid table styling
- RTL support
- Print-friendly styles
- Responsive design utilities

## Architecture

### Managers

#### ApplicationManager (`managers/application_manager.py`)
Abstract base class for managing application-wide concerns:

**Responsibilities:**
- Application state management
- User session management
- Settings management
- Integration with logging and profiling utilities

**Key Methods:**
```python
# State Management
get_state(key, default=None)
set_state(key, value)
clear_state()

# Session Management
create_session(session_id, user_data)
get_session(session_id)
delete_session(session_id)

# Settings Management
get_setting(key, default=None)
set_setting(key, value)

# Utilities
get_logger()
get_profiler()
```

**Implementation:**
- `DefaultApplicationManager`: Production implementation with state tracking for theme, RTL mode, navbar/aside collapse states

#### DataManager (`managers/data_manager.py`)
Abstract base class for data operations:

**Responsibilities:**
- CRUD operations for all application entities
- Data storage and retrieval
- Search and filtering

**Key Methods:**
```python
# CRUD Operations
create(entity_type, entity_id, data) -> bool
retrieve(entity_type, entity_id) -> dict | None
update(entity_type, entity_id, data) -> bool
delete(entity_type, entity_id) -> bool

# Querying
list_all(entity_type) -> list[dict]
search(entity_type, filters) -> list[dict]
```

**Implementation:**
- `InMemoryDataManager`: Development/testing implementation using in-memory dictionaries
- Supports entity types: projects, data_sources, logs, users

### Utilities

#### Logger (`utilities/logger.py`)
Centralized logging utility:

**Features:**
- Consistent log formatting
- Console output with timestamps
- `LoggerMixin` class for easy integration
- Helper methods: `log_info()`, `log_warning()`, `log_error()`, `log_debug()`

**Usage:**
```python
from aiml_studio.utilities import get_logger

logger = get_logger(__name__)
logger.info("Application started")
```

#### Profiler (`utilities/profiler.py`)
Performance monitoring utility:

**Features:**
- Context manager for timing operations
- Statistical analysis (min, max, avg, total)
- Human-readable duration formatting
- Timestamp generation

**Usage:**
```python
from aiml_studio.utilities import Profiler

profiler = Profiler()

with profiler.profile("data_fetch"):
    # Your code here
    fetch_data()

stats = profiler.get_stats("data_fetch")
print(f"Average time: {stats['avg']:.4f}s")
```

## Integration

### In app.py

```python
from aiml_studio.managers import ApplicationManager, DataManager
from aiml_studio.managers.application_manager import DefaultApplicationManager
from aiml_studio.managers.data_manager import InMemoryDataManager

# Initialize managers
app_manager: ApplicationManager = DefaultApplicationManager()
data_manager: DataManager = InMemoryDataManager()

app_manager.initialize()
data_manager.initialize()

# Use in callbacks
@callback(...)
def toggle_theme(checked: bool) -> str:
    theme = "dark" if checked else "light"
    app_manager.set_state("theme", theme)
    return theme
```

### In Callbacks

Managers are globally accessible through the app module:
```python
from aiml_studio.app import app_manager, data_manager

# Use application manager
theme = app_manager.get_state("theme", "light")

# Use data manager
data_manager.create("projects", project_id, project_data)
projects = data_manager.list_all("projects")
```

## Callbacks

### Header Toggles

1. **Navbar Toggle** (`navbar-toggle-btn`):
   - Toggles the `appshell.navbar` collapsed state
   - Updates desktop collapse state

2. **Aside Toggle** (`aside-toggle-btn`):
   - Toggles the `appshell.aside` collapsed state
   - Updates desktop collapse state

### Appearance Controls

1. **Theme Switch** (`theme-switch`):
   - Updates `mantine-provider.forceColorScheme`
   - Stores preference in ApplicationManager state
   - Switches between "light" and "dark"

2. **RTL Switch** (`rtl-switch`):
   - Uses clientside callback for performance
   - Sets `dir` attribute on document root
   - Supports bidirectional text layouts

## Testing

Run the application:
```bash
uv run python -m aiml_studio.app
```

Navigate to http://localhost:8050

Test features:
1. Click navbar toggle button (top-left) - sidebar should collapse/expand
2. Click aside toggle button (top-right) - aside panel should collapse/expand
3. Toggle theme switch in navbar - UI should switch between light/dark
4. Toggle RTL switch in navbar - text direction should reverse

## Code Quality

All code follows:
- Type hints throughout
- Comprehensive docstrings
- PEP 8 style (enforced by ruff)
- Type safety (verified by mypy)
- Abstract base classes for extensibility
- Logging and error handling

## Future Enhancements

1. **Persistent Storage**: Replace InMemoryDataManager with database-backed implementation
2. **Authentication**: Integrate session management with real authentication
3. **Caching**: Add caching layer to DataManager
4. **Metrics**: Expand Profiler integration for performance monitoring
5. **Settings Persistence**: Save user preferences (theme, RTL) to backend
