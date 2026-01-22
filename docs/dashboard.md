# Admin Dashboard

The AIML Studio admin dashboard provides a comprehensive web interface for managing machine learning projects, experiments, and data sources.

## Architecture

The dashboard is built using:

- **Dash**: Python framework for building analytical web applications
- **Dash Mantine Components**: Modern UI component library for beautiful interfaces
- **Dash AG Grid**: High-performance, feature-rich data tables
- **Plotly**: Interactive data visualization library

## Pages

### Analytics Dashboard

**URL**: `/` (default page)

The analytics dashboard provides an overview of your ML experiments and model performance:

- **Key Metrics Cards**:
  - Total experiments count
  - Active deployed models
  - Average model accuracy
  - Connected data sources

- **Performance Trends Chart**: 
  - Time series visualization of model accuracy and loss over the past 30 days
  - Interactive hover tooltips for detailed information

- **Model Comparison Chart**:
  - Bar chart comparing different models (Random Forest, XGBoost, Neural Network, SVM, Logistic Regression)
  - Metrics displayed: accuracy, precision, recall

**Implementation**: `aiml_studio/layouts/analytics.py`

### Data Sources Management

**URL**: `/data-sources`

Manage and monitor your data connections:

- **Summary Cards**:
  - Total sources count
  - Active connections
  - Disconnected sources
  - Error status count

- **Interactive Data Table** (AG Grid):
  - Filterable and sortable columns
  - Connection status with color coding:
    - 🟢 Connected (green)
    - ⚫ Disconnected (gray)
    - 🔴 Error (red)
  - Pagination (10 records per page)
  - Single row selection
  - Columns: ID, Name, Type, Status, Records, Last Sync

**Implementation**: `aiml_studio/layouts/data_sources.py`

### Projects Management

**URL**: `/projects`

Track and manage ML projects:

- **Summary Cards**:
  - Total projects
  - Active projects
  - In progress projects
  - Completed projects

- **Interactive Data Table** (AG Grid):
  - Project information with status color coding:
    - 🟢 Active (green)
    - 🔵 Completed (blue)
    - 🟡 In Progress (yellow)
    - ⚫ On Hold (gray)
  - Filter and search capabilities
  - Sortable columns
  - Pagination (10 records per page)
  - Columns: ID, Name, Owner, Status, Experiments, Best Accuracy, Created, Last Updated

**Implementation**: `aiml_studio/layouts/projects.py`

## Components

### Navigation Sidebar

Located on the left side of all pages, provides quick navigation between:

- Analytics Dashboard
- Data Sources
- Projects

**Implementation**: `aiml_studio/components/navigation.py`

## Running the Dashboard

### Development Mode

To run the dashboard in development mode with hot reloading:

```bash
python -m aiml_studio.app
```

The dashboard will be available at `http://localhost:8050`

### Production Mode

For production deployment, consider using a WSGI server like Gunicorn:

```bash
gunicorn aiml_studio.app:app.server -b 0.0.0.0:8050
```

## Code Structure

```
aiml_studio/
├── app.py                    # Main application entry point
├── components/               # Reusable UI components
│   ├── __init__.py
│   └── navigation.py        # Sidebar navigation
└── layouts/                 # Page layouts
    ├── __init__.py
    ├── analytics.py         # Analytics dashboard
    ├── data_sources.py      # Data sources management
    └── projects.py          # Projects management
```

## Best Practices

### Adding New Pages

1. Create a new layout file in `aiml_studio/layouts/`
2. Define a `layout` variable with your page content
3. Register the route in `aiml_studio/app.py` in the `display_page` callback

Example:

```python
# In aiml_studio/layouts/new_page.py
import dash_mantine_components as dmc

layout = dmc.Stack(
    children=[
        dmc.Title("New Page"),
        # Your content here
    ]
)

# In aiml_studio/app.py
from aiml_studio.layouts import new_page

@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname: str | None) -> Any:
    if pathname == "/new-page":
        return new_page.layout
    # ... existing routes
```

### Adding New Components

Create reusable components in `aiml_studio/components/`:

```python
import dash_mantine_components as dmc

def create_metric_card(title: str, value: str) -> dmc.Card:
    """Create a reusable metric card."""
    return dmc.Card(
        children=[
            dmc.Text(title, size="sm"),
            dmc.Title(value, order=2),
        ]
    )
```

### Styling Guidelines

- Use Mantine's built-in theming system
- Maintain consistent spacing with Mantine's `gap` and `spacing` props
- Use semantic colors from Mantine's palette
- Keep responsive design in mind with `SimpleGrid` and `Grid` components

## Testing

Tests are located in the `tests/` directory:

- `test_app.py`: Main application tests
- `test_navigation.py`: Navigation component tests
- `test_analytics.py`: Analytics page tests
- `test_data_sources.py`: Data sources page tests
- `test_projects.py`: Projects page tests

Run tests with:

```bash
pytest tests/
```

## Future Enhancements

Potential improvements for the dashboard:

1. **Authentication**: Add user authentication and role-based access control
2. **Real Data Integration**: Connect to actual databases and ML experiment tracking systems
3. **Real-time Updates**: Implement WebSocket for live data updates
4. **Export Features**: Add CSV/Excel export for data tables
5. **Advanced Filtering**: Implement complex filter combinations in AG Grid
6. **Custom Dashboards**: Allow users to create custom dashboard views
7. **Notifications**: Add alert system for model performance issues
8. **API Integration**: Expose REST API for programmatic access
