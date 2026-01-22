"""Tests for the analytics layout."""

from aiml_studio.layouts import analytics


def test_analytics_layout_exists() -> None:
    """Test that the analytics layout is properly defined."""
    assert analytics.layout is not None


def test_analytics_sample_data_generation() -> None:
    """Test that sample data is generated correctly."""
    data = analytics._generate_sample_data()
    assert "performance" in data
    assert "comparison" in data
    assert len(data["performance"]) > 0
    assert len(data["comparison"]) > 0
