"""Tests for the main Dash application."""

from aiml_studio.app import app


def test_app_initialization() -> None:
    """Test that the Dash app initializes correctly."""
    assert app is not None
    assert app.title == "AIML Studio - Admin Dashboard"


def test_app_layout() -> None:
    """Test that the app layout is properly configured."""
    assert app.layout is not None
