"""Tests for the projects layout."""

from aiml_studio.layouts import projects


def test_projects_layout_exists() -> None:
    """Test that the projects layout is properly defined."""
    assert projects.layout is not None


def test_projects_sample_data() -> None:
    """Test that sample projects are generated correctly."""
    data = projects._generate_sample_projects()
    assert len(data) > 0
    assert "name" in data.columns
    assert "owner" in data.columns
    assert "status" in data.columns


def test_projects_column_defs() -> None:
    """Test that column definitions are properly configured."""
    col_defs = projects._create_column_defs()
    assert len(col_defs) > 0
    assert all("field" in col for col in col_defs)
