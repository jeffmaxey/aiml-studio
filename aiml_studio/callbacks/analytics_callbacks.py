"""Analytics page callbacks."""

from dash import Input, Output, State, callback

from aiml_studio.utilities import create_download_link, export_to_csv, export_to_json, generate_export_filename


@callback(
    Output("download-analytics-data", "data"),
    Input("export-analytics-csv", "n_clicks"),
    Input("export-analytics-json", "n_clicks"),
    State("metrics-summary-grid", "rowData"),
    prevent_initial_call=True,
)
def export_analytics_data(
    csv_clicks: int | None, json_clicks: int | None, row_data: list[dict] | None
) -> dict[str, str] | None:
    """Export analytics data to CSV or JSON.

    Args:
        csv_clicks: Number of clicks on CSV export button
        json_clicks: Number of clicks on JSON export button
        row_data: Current data from the metrics grid

    Returns:
        Download data dictionary or None
    """
    if not row_data:
        return None

    # Determine which export format was requested
    from dash import ctx

    if not ctx.triggered:
        return None

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_id == "export-analytics-csv":
        csv_data = export_to_csv(row_data)
        filename = generate_export_filename("analytics_metrics", "csv")
        return create_download_link(csv_data, filename, "text/csv")

    if triggered_id == "export-analytics-json":
        json_data = export_to_json(row_data)
        filename = generate_export_filename("analytics_metrics", "json")
        return create_download_link(json_data, filename, "application/json")

    return None
