"""Reusable dash_ag_grid table components."""

from typing import Any

import dash_ag_grid as dag

from aiml_studio.constants import DEFAULT_TABLE_PAGE_SIZE


def create_ag_grid(
    grid_id: str,
    column_defs: list[dict[str, Any]],
    row_data: list[dict[str, Any]] | None = None,
    pagination: bool = True,
    page_size: int = DEFAULT_TABLE_PAGE_SIZE,
    **kwargs: Any,
) -> dag.AgGrid:
    """Create a configured AG Grid table.

    Args:
        grid_id: Unique identifier for the grid
        column_defs: Column definitions for the grid
        row_data: Initial row data (optional)
        pagination: Whether to enable pagination
        page_size: Number of rows per page
        **kwargs: Additional AG Grid options

    Returns:
        Configured AgGrid component
    """
    default_col_def = {
        "flex": 1,
        "minWidth": 100,
        "sortable": True,
        "filter": True,
        "resizable": True,
    }

    dash_grid_options = {
        "pagination": pagination,
        "paginationPageSize": page_size,
        "animateRows": True,
        "rowSelection": "single",
    }

    # Merge any custom grid options
    if "dashGridOptions" in kwargs:
        dash_grid_options.update(kwargs.pop("dashGridOptions"))

    return dag.AgGrid(
        id=grid_id,
        columnDefs=column_defs,
        rowData=row_data or [],
        defaultColDef=default_col_def,
        dashGridOptions=dash_grid_options,
        **kwargs,
    )


def create_logs_grid() -> dag.AgGrid:
    """Create a configured grid for logs display.

    Returns:
        AgGrid component configured for logs
    """
    column_defs = [
        {"field": "timestamp", "headerName": "Timestamp", "width": 200},
        {"field": "level", "headerName": "Level", "width": 120},
        {"field": "message", "headerName": "Message", "flex": 1},
    ]

    return create_ag_grid(
        grid_id="logs-grid",
        column_defs=column_defs,
        row_data=[],
    )


def create_data_sources_grid() -> dag.AgGrid:
    """Create a configured grid for data sources display.

    Returns:
        AgGrid component configured for data sources
    """
    column_defs = [
        {"field": "name", "headerName": "Name", "width": 200},
        {"field": "type", "headerName": "Type", "width": 150},
        {"field": "status", "headerName": "Status", "width": 120},
        {"field": "connection", "headerName": "Connection String", "flex": 1},
    ]

    return create_ag_grid(
        grid_id="data-sources-grid",
        column_defs=column_defs,
        row_data=[],
    )


def create_projects_grid() -> dag.AgGrid:
    """Create a configured grid for projects display.

    Returns:
        AgGrid component configured for projects
    """
    column_defs = [
        {"field": "name", "headerName": "Project Name", "width": 200},
        {"field": "status", "headerName": "Status", "width": 120},
        {"field": "created", "headerName": "Created", "width": 150},
        {"field": "modified", "headerName": "Last Modified", "width": 150},
        {"field": "description", "headerName": "Description", "flex": 1},
    ]

    return create_ag_grid(
        grid_id="projects-grid",
        column_defs=column_defs,
        row_data=[],
    )
