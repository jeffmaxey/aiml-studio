"""Help page layout."""

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_help_layout() -> html.Div:
    """Create the help page layout.

    Returns:
        Help page layout component
    """
    faq_items = [
        {
            "question": "How do I create a new project?",
            "answer": "Navigate to the Projects page and click the 'Create New Project' button. Fill in the project details and click 'Save'.",
        },
        {
            "question": "How do I connect to a data source?",
            "answer": "Go to the Data Sources page, click 'Add Data Source', select your database type, and enter the connection details.",
        },
        {
            "question": "How do I view analytics?",
            "answer": "Access the Analytics dashboard from the main navigation menu to view key metrics and performance data.",
        },
        {
            "question": "Can I change the theme?",
            "answer": "Yes! Go to Settings and toggle between Light and Dark themes using the Theme Mode selector.",
        },
    ]

    return html.Div([
        dmc.Stack(
            [
                dmc.Title("Help & Documentation", order=2, mb="md"),
                # Getting started
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                DashIconify(icon="tabler:rocket", width=24),
                                dmc.Title("Getting Started", order=4),
                            ],
                            gap="sm",
                            mb="md",
                        ),
                        dmc.Text(
                            "Welcome to AIML Studio! This platform helps you run predictive analytics "
                            "and machine learning experiments. Here's how to get started:",
                            mb="md",
                        ),
                        dmc.List(
                            [
                                dmc.ListItem("Configure your settings in the Settings page"),
                                dmc.ListItem("Connect to your data sources"),
                                dmc.ListItem("Create your first project"),
                                dmc.ListItem("Start analyzing your data"),
                            ],
                            spacing="sm",
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
                # Documentation sections
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                DashIconify(icon="tabler:book", width=24),
                                dmc.Title("Documentation", order=4),
                            ],
                            gap="sm",
                            mb="md",
                        ),
                        dmc.SimpleGrid(
                            cols={"base": 1, "sm": 2},
                            spacing="md",
                            children=[
                                dmc.Paper(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:database", width=20),
                                                dmc.Text("Data Sources", fw=500),
                                            ],
                                            gap="xs",
                                            mb="xs",
                                        ),
                                        dmc.Text(
                                            "Learn how to connect and manage various data sources.",
                                            size="sm",
                                            c="dimmed",
                                        ),
                                    ],
                                    p="md",
                                    withBorder=True,
                                    radius="sm",
                                    style={"cursor": "pointer"},
                                ),
                                dmc.Paper(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:folder", width=20),
                                                dmc.Text("Projects", fw=500),
                                            ],
                                            gap="xs",
                                            mb="xs",
                                        ),
                                        dmc.Text(
                                            "Understand project structure and management.",
                                            size="sm",
                                            c="dimmed",
                                        ),
                                    ],
                                    p="md",
                                    withBorder=True,
                                    radius="sm",
                                    style={"cursor": "pointer"},
                                ),
                                dmc.Paper(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:chart-bar", width=20),
                                                dmc.Text("Analytics", fw=500),
                                            ],
                                            gap="xs",
                                            mb="xs",
                                        ),
                                        dmc.Text(
                                            "Explore analytics features and visualizations.",
                                            size="sm",
                                            c="dimmed",
                                        ),
                                    ],
                                    p="md",
                                    withBorder=True,
                                    radius="sm",
                                    style={"cursor": "pointer"},
                                ),
                                dmc.Paper(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:settings", width=20),
                                                dmc.Text("Configuration", fw=500),
                                            ],
                                            gap="xs",
                                            mb="xs",
                                        ),
                                        dmc.Text(
                                            "Configure application settings and preferences.",
                                            size="sm",
                                            c="dimmed",
                                        ),
                                    ],
                                    p="md",
                                    withBorder=True,
                                    radius="sm",
                                    style={"cursor": "pointer"},
                                ),
                            ],
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
                # FAQ
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                DashIconify(icon="tabler:help", width=24),
                                dmc.Title("Frequently Asked Questions", order=4),
                            ],
                            gap="sm",
                            mb="md",
                        ),
                        dmc.Accordion(
                            children=[
                                dmc.AccordionItem(
                                    [
                                        dmc.AccordionControl(item["question"]),
                                        dmc.AccordionPanel(item["answer"]),
                                    ],
                                    value=str(i),
                                )
                                for i, item in enumerate(faq_items)
                            ],
                            value="0",
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
                # Support
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                DashIconify(icon="tabler:mail", width=24),
                                dmc.Title("Contact Support", order=4),
                            ],
                            gap="sm",
                            mb="md",
                        ),
                        dmc.Text("Need help? Get in touch with our support team:", mb="md"),
                        dmc.Stack(
                            [
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:mail", width=20),
                                        dmc.Text("Email: support@aiml-studio.com"),
                                    ],
                                    gap="xs",
                                ),
                                dmc.Group(
                                    [
                                        DashIconify(icon="tabler:brand-github", width=20),
                                        dmc.Anchor(
                                            "GitHub Issues",
                                            href="https://github.com/jeffmaxey/aiml-studio/issues",
                                            target="_blank",
                                        ),
                                    ],
                                    gap="xs",
                                ),
                            ],
                            gap="sm",
                        ),
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    p="lg",
                ),
            ],
            gap="lg",
        )
    ])
