"""Tests for the data sources layout."""

from aiml_studio.layouts import data_sources


def test_data_sources_layout_exists() -> None:
    """Test that the data sources layout is properly defined."""
    assert data_sources.layout is not None


def test_data_sources_sample_data() -> None:
    """Test that sample data sources are generated correctly."""
    data = data_sources._generate_sample_data_sources()
    assert len(data) > 0
    assert "name" in data.columns
    assert "type" in data.columns
    assert "status" in data.columns


def test_data_sources_column_defs() -> None:
    """Test that column definitions are properly configured."""
    col_defs = data_sources._create_column_defs()
    assert len(col_defs) > 0
    assert all("field" in col for col in col_defs)
