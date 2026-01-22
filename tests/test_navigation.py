"""Tests for the navigation component."""

from aiml_studio.components.navigation import create_sidebar


def test_create_sidebar() -> None:
    """Test that the sidebar component is created successfully."""
    sidebar = create_sidebar()
    assert sidebar is not None
