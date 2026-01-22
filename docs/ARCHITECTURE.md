# AIML Studio - Enhanced Architecture Documentation

## Overview

AIML Studio is a professional machine learning platform with a modern, intuitive UI/UX inspired by industry-leading platforms like MLflow. This document describes the enhanced architecture with integrated managers, utilities, and comprehensive UI/UX design system.

## UI/UX Design Philosophy

### Inspiration
The UI/UX design draws inspiration from:
- **MLflow**: Professional ML platform with clean, data-focused design
- **Dash Mantine Components v2**: Modern React-based UI framework
- **Material Design**: Consistent design language and interaction patterns

### Design Principles
1. **Professional & Clean**: Minimalist design with focus on data and functionality
2. **Consistent**: Unified design language across all pages and components
3. **Responsive**: Mobile-first approach with adaptive layouts
4. **Accessible**: WCAG 2.1 compliant with keyboard navigation support
5. **Performance**: Optimized animations and smooth interactions

## Enhanced Features

### 1. Professional Header
- **Logo & Branding**: Themed icon with gradient styling and subtitle
- **Search**: Quick search functionality (placeholder for future implementation)
- **Notifications**: Real-time notification indicator with pulse animation
- **User Menu**: Avatar with dropdown for profile, settings, and logout
- **Controls**: Navbar and aside panel toggles

### 2. Enhanced Navigation Sidebar
- **Section Organization**: 
  - Core: Home, Settings, Help, Logs
  - Admin: Analytics, Data Sources, Projects
  - Appearance: Theme and RTL toggles
- **Visual Hierarchy**: Section headers with themed icons
- **Active States**: Gradient background for active links
- **Quick Tips**: Contextual help panel at bottom
- **Smooth Animations**: Hover and transition effects

### 3. Professional Theme System
- **Color Palette**: MLflow-inspired color scheme
  - Primary: #0194E2 (MLflow blue)
  - Success: #00B388 (Professional green)
  - Warning: #FFB240 (Amber)
  - Error: #FF5252 (Clear red)
- **Typography**: Inter font family with optimized hierarchy
- **Spacing System**: Consistent 8px grid system
- **Shadow System**: Layered shadows for depth
- **Border Radius**: Consistent rounded corners (4px-16px)

### 4. Enhanced CSS Architecture
- **CSS Variables**: Design tokens for easy theming
- **Modern Animations**: fadeIn, slideIn, scaleIn with smooth easing
- **Status Indicators**: Colored dots with pulse animation
- **Professional Scrollbar**: Custom styled for light/dark modes
- **Responsive Utilities**: Mobile and desktop visibility classes
- **Print Styles**: Clean printing without UI chrome

### 5. Page-Specific Enhancements

#### Home Page
- **Welcome Banner**: Gradient text, illustration, action buttons
- **Key Metrics**: Live dashboard with trend indicators
- **Quick Actions**: Card-based navigation with themed icons
- **Recent Activity**: Table with user attribution

#### Analytics Dashboard
- **Timeframe Selector**: 24h, 7d, 30d, 90d options
- **Statistics Cards**: Trend indicators with status badges
- **Chart Placeholders**: Professional empty states
- **Detailed Metrics Table**: Sortable with last updated timestamps

#### Projects Page
- **View Toggle**: Card and table view options
- **Project Cards**: Status badges, icons, action buttons
- **Statistics Overview**: Total, active, completed, inactive counts
- **Create Modal**: Professional form with validation

#### Footer
- **System Status**: Live operational status indicator
- **Version Badge**: Current application version
- **Quick Links**: Documentation, API, GitHub
- **Social Icons**: Community engagement links

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
