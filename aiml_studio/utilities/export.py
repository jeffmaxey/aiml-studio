"""Data export utilities for AIML Studio."""

import csv
import io
import json
from datetime import datetime
from typing import Any


def export_to_csv(data: list[dict[str, Any]], columns: list[str] | None = None) -> str:
    """Export data to CSV format.

    Args:
        data: List of dictionaries containing the data
        columns: Optional list of column names to include (defaults to all keys)

    Returns:
        CSV formatted string
    """
    if not data:
        return ""

    # Use provided columns or extract from first row
    fieldnames = columns or list(data[0].keys())

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(data)

    return output.getvalue()


def export_to_json(data: list[dict[str, Any]], pretty: bool = True) -> str:
    """Export data to JSON format.

    Args:
        data: List of dictionaries containing the data
        pretty: Whether to format JSON with indentation

    Returns:
        JSON formatted string
    """
    if pretty:
        return json.dumps(data, indent=2, default=str)
    return json.dumps(data, default=str)


def create_download_link(data: str, filename: str, file_type: str = "text/csv") -> dict[str, str]:
    """Create a download link data dictionary for dcc.Download component.

    Args:
        data: The file content as string
        filename: Name for the downloaded file
        file_type: MIME type for the file

    Returns:
        Dictionary with content, filename, and type for dcc.Download
    """
    return {"content": data, "filename": filename, "type": file_type}


def generate_export_filename(prefix: str, extension: str) -> str:
    """Generate a timestamped filename for exports.

    Args:
        prefix: Prefix for the filename (e.g., 'projects', 'analytics')
        extension: File extension (e.g., 'csv', 'json')

    Returns:
        Formatted filename with timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"
