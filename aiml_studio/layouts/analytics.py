"""Analytics dashboard page for AIML Studio.

This module provides a comprehensive analytics dashboard with key metrics,
charts, and visualizations for monitoring ML experiments and model performance.

Features:
    - Key performance metrics cards
    - Model performance charts
    - Experiment trend analysis
    - Interactive visualizations using Plotly
"""

from datetime import datetime, timedelta

import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html


def _generate_sample_data() -> dict[str, pd.DataFrame]:
    """Generate sample data for analytics visualizations.

    Returns:
        Dictionary containing DataFrames for different metrics.
    """
    # Generate sample time series data for model accuracy
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq="D")
    model_performance = pd.DataFrame(
        {
            "date": dates,
            "accuracy": [0.75 + i * 0.005 + (i % 3) * 0.01 for i in range(len(dates))],
            "loss": [0.5 - i * 0.01 + (i % 4) * 0.02 for i in range(len(dates))],
        }
    )

    # Generate sample model comparison data
    model_comparison = pd.DataFrame(
        {
            "model": ["Random Forest", "XGBoost", "Neural Network", "SVM", "Logistic Regression"],
            "accuracy": [0.92, 0.95, 0.94, 0.88, 0.85],
            "precision": [0.90, 0.93, 0.92, 0.86, 0.84],
            "recall": [0.91, 0.94, 0.93, 0.87, 0.83],
        }
    )

    return {"performance": model_performance, "comparison": model_comparison}


def _create_metric_card(title: str, value: str, description: str, icon: str, color: str) -> dmc.Card:
    """Create a metric card component.

    Args:
        title: The metric title
        value: The metric value to display
        description: Description or subtitle for the metric
        icon: Icon name for the card
        color: Color theme for the card

    Returns:
        A Mantine Card component displaying the metric.
    """
    return dmc.Card(
        children=[
            dmc.Group(
                children=[
                    dmc.ThemeIcon(
                        html.I(className=f"fas fa-{icon}"),
                        size="xl",
                        radius="md",
                        color=color,
                        variant="light",
                    ),
                    dmc.Stack(
                        children=[
                            dmc.Text(title, size="sm", c="dimmed"),
                            dmc.Title(value, order=3),
                            dmc.Text(description, size="xs", c="dimmed"),
                        ],
                        gap="xs",
                    ),
                ],
                justify="flex-start",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"padding": "20px"},
    )


def _create_performance_chart(data: pd.DataFrame) -> dcc.Graph:
    """Create a line chart showing model performance over time.

    Args:
        data: DataFrame with date, accuracy, and loss columns

    Returns:
        A Dash Graph component with the performance chart.
    """
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["date"],
            y=data["accuracy"],
            mode="lines+markers",
            name="Accuracy",
            line={"color": "#228be6", "width": 2},
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["date"],
            y=data["loss"],
            mode="lines+markers",
            name="Loss",
            line={"color": "#fa5252", "width": 2},
        )
    )

    fig.update_layout(
        title="Model Performance Trends",
        xaxis_title="Date",
        yaxis_title="Value",
        hovermode="x unified",
        template="plotly_white",
        height=400,
    )

    return dcc.Graph(figure=fig, config={"displayModeBar": False})


def _create_model_comparison_chart(data: pd.DataFrame) -> dcc.Graph:
    """Create a bar chart comparing different models.

    Args:
        data: DataFrame with model names and performance metrics

    Returns:
        A Dash Graph component with the comparison chart.
    """
    fig = px.bar(
        data,
        x="model",
        y=["accuracy", "precision", "recall"],
        title="Model Performance Comparison",
        labels={"value": "Score", "variable": "Metric"},
        barmode="group",
        color_discrete_sequence=["#228be6", "#40c057", "#fab005"],
    )

    fig.update_layout(
        xaxis_title="Model",
        yaxis_title="Score",
        template="plotly_white",
        height=400,
        legend={"title": "Metric", "orientation": "h", "y": -0.2},
    )

    return dcc.Graph(figure=fig, config={"displayModeBar": False})


# Generate sample data
sample_data = _generate_sample_data()

# Main layout for the analytics page
layout = dmc.Stack(
    children=[
        # Page header
        dmc.Title("Analytics Dashboard", order=1, style={"marginBottom": "10px"}),
        dmc.Text(
            "Monitor your ML experiments and model performance",
            size="sm",
            c="dimmed",
            style={"marginBottom": "30px"},
        ),
        # Metrics cards
        dmc.SimpleGrid(
            cols=4,
            spacing="lg",
            children=[
                _create_metric_card(
                    "Total Experiments",
                    "156",
                    "+12% from last month",
                    "flask",
                    "blue",
                ),
                _create_metric_card(
                    "Active Models",
                    "23",
                    "Currently deployed",
                    "robot",
                    "green",
                ),
                _create_metric_card(
                    "Avg Accuracy",
                    "94.2%",
                    "+2.1% improvement",
                    "chart-line",
                    "orange",
                ),
                _create_metric_card(
                    "Data Sources",
                    "8",
                    "Connected sources",
                    "database",
                    "violet",
                ),
            ],
            style={"marginBottom": "30px"},
        ),
        # Charts section
        dmc.SimpleGrid(
            cols=1,
            spacing="lg",
            children=[
                dmc.Card(
                    children=[_create_performance_chart(sample_data["performance"])],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "20px"},
                ),
                dmc.Card(
                    children=[_create_model_comparison_chart(sample_data["comparison"])],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"padding": "20px"},
                ),
            ],
        ),
    ],
    gap="md",
)
