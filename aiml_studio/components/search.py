"""Search functionality components and utilities."""

from typing import Any

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_search_modal() -> dmc.Modal:
    """Create a global search modal with command palette functionality.

    Returns:
        Modal component for global search
    """
    return dmc.Modal(
        id="global-search-modal",
        title=dmc.Group(
            [
                DashIconify(icon="tabler:search", width=20),
                "Search",
                dmc.Badge("Ctrl+K", size="xs", variant="light", color="gray", ml="auto"),
            ],
            gap="sm",
        ),
        size="lg",
        centered=True,
        children=[
            dmc.Stack(
                [
                    dmc.TextInput(
                        id="modal-search-input",
                        placeholder="Type to search...",
                        leftSection=DashIconify(icon="tabler:search", width=18),
                        size="md",
                    ),
                    dmc.Divider(),
                    dmc.ScrollArea(
                        id="search-results-container",
                        h=400,
                        children=[
                            dmc.Stack(
                                [
                                    dmc.Text("Recent Searches", size="sm", fw=600, c="dimmed"),
                                    create_search_result_item(
                                        "Projects",
                                        "View all projects",
                                        "tabler:folder",
                                        "/projects",
                                    ),
                                    create_search_result_item(
                                        "Analytics Dashboard",
                                        "View analytics and metrics",
                                        "tabler:chart-bar",
                                        "/analytics",
                                    ),
                                    create_search_result_item(
                                        "Data Sources",
                                        "Manage data connections",
                                        "tabler:database",
                                        "/data-sources",
                                    ),
                                ],
                                gap="xs",
                            )
                        ],
                    ),
                ],
                gap="md",
            )
        ],
    )


def create_search_result_item(title: str, description: str, icon: str, href: str) -> dmc.Paper:
    """Create a search result item.

    Args:
        title: Result title
        description: Result description
        icon: Icon identifier
        href: Link to navigate to

    Returns:
        Paper component with search result
    """
    return dmc.Paper(
        dmc.Anchor(
            dmc.Group(
                [
                    dmc.ThemeIcon(
                        DashIconify(icon=icon, width=20),
                        size="lg",
                        radius="md",
                        variant="light",
                        color="blue",
                    ),
                    dmc.Stack(
                        [
                            dmc.Text(title, size="sm", fw=600),
                            dmc.Text(description, size="xs", c="dimmed"),
                        ],
                        gap=2,
                    ),
                    dmc.ActionIcon(
                        DashIconify(icon="tabler:arrow-right", width=16),
                        variant="subtle",
                        size="sm",
                        ml="auto",
                    ),
                ],
                gap="md",
            ),
            href=href,
            style={"textDecoration": "none"},
        ),
        p="md",
        radius="md",
        withBorder=True,
        className="search-result-item",
        style={
            "cursor": "pointer",
            "transition": "all 0.2s ease",
            ":hover": {"backgroundColor": "var(--mantine-color-gray-0)"},
        },
    )


def filter_search_results(query: str, all_items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter search results based on query.

    Args:
        query: Search query string
        all_items: List of all searchable items

    Returns:
        Filtered list of items matching the query
    """
    if not query:
        return all_items

    query = query.lower()
    filtered = []

    for item in all_items:
        title = item.get("title", "").lower()
        description = item.get("description", "").lower()
        tags = " ".join(item.get("tags", [])).lower()

        if query in title or query in description or query in tags:
            filtered.append(item)

    return filtered
