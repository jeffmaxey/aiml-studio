"""Loading states and progress indicator components."""

from typing import Any

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_skeleton_loader(height: int = 100, radius: str = "md") -> dmc.Skeleton:
    """Create a skeleton loader for content placeholders.

    Args:
        height: Height of the skeleton in pixels
        radius: Border radius (xs, sm, md, lg, xl)

    Returns:
        Skeleton component
    """
    return dmc.Skeleton(height=height, radius=radius, animate=True)


def create_skeleton_card() -> dmc.Card:
    """Create a skeleton loader card that mimics a content card.

    Returns:
        Card with skeleton elements
    """
    return dmc.Card(
        [
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Skeleton(height=40, width=40, radius="md"),
                            dmc.Stack(
                                [
                                    dmc.Skeleton(height=12, width="60%"),
                                    dmc.Skeleton(height=10, width="40%"),
                                ],
                                gap="xs",
                            ),
                        ],
                        gap="md",
                    ),
                    dmc.Skeleton(height=60, radius="sm"),
                    dmc.Group(
                        [
                            dmc.Skeleton(height=30, width=80, radius="sm"),
                            dmc.Skeleton(height=30, width=80, radius="sm"),
                        ],
                        gap="sm",
                    ),
                ],
                gap="md",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="lg",
        p="lg",
    )


def create_table_skeleton(rows: int = 5) -> dmc.Stack:
    """Create a skeleton loader for tables.

    Args:
        rows: Number of skeleton rows to display

    Returns:
        Stack of skeleton rows
    """
    skeleton_rows = []
    # Header row
    skeleton_rows.append(
        dmc.Group(
            [
                dmc.Skeleton(height=20, width="25%"),
                dmc.Skeleton(height=20, width="25%"),
                dmc.Skeleton(height=20, width="25%"),
                dmc.Skeleton(height=20, width="25%"),
            ],
            gap="md",
            mb="md",
        )
    )

    # Data rows
    for _ in range(rows):
        skeleton_rows.append(
            dmc.Group(
                [
                    dmc.Skeleton(height=16, width="25%"),
                    dmc.Skeleton(height=16, width="25%"),
                    dmc.Skeleton(height=16, width="25%"),
                    dmc.Skeleton(height=16, width="25%"),
                ],
                gap="md",
                mb="sm",
            )
        )

    return dmc.Stack(skeleton_rows, gap="xs")


def create_spinner(size: str = "md", color: str = "blue") -> dmc.Loader:
    """Create a spinner/loader component.

    Args:
        size: Size of the spinner (xs, sm, md, lg, xl)
        color: Color of the spinner

    Returns:
        Loader component
    """
    return dmc.Loader(size=size, color=color, type="dots")


def create_centered_spinner(message: str | None = None, size: str = "lg") -> dmc.Center:
    """Create a centered spinner with optional message.

    Args:
        message: Optional loading message to display
        size: Size of the spinner

    Returns:
        Centered loader with message
    """
    content = [create_spinner(size=size)]

    if message:
        content.append(dmc.Text(message, size="sm", c="dimmed", mt="md"))

    return dmc.Center(dmc.Stack(content, align="center", gap="md"), style={"minHeight": "200px"})


def create_progress_bar(value: float, label: str | None = None, color: str = "blue") -> dmc.Progress:
    """Create a progress bar.

    Args:
        value: Progress value (0-100)
        label: Optional label to display
        color: Color of the progress bar

    Returns:
        Progress component
    """
    return dmc.Progress(
        value=value,
        label=label if label else f"{value:.0f}%",
        size="lg",
        radius="sm",
        color=color,
        striped=True,
        animate=True,
    )


def create_loading_overlay(visible: bool = True, message: str | None = None) -> dmc.LoadingOverlay:
    """Create a loading overlay that covers content.

    Args:
        visible: Whether the overlay is visible
        message: Optional loading message

    Returns:
        LoadingOverlay component
    """
    loader_props = {
        "type": "dots",
        "size": "xl",
    }

    return dmc.LoadingOverlay(
        visible=visible,
        overlayProps={"radius": "sm", "blur": 2},
        loaderProps=loader_props,
    )


def create_inline_loader(text: str = "Loading...", size: str = "sm") -> dmc.Group:
    """Create an inline loader with text.

    Args:
        text: Loading text to display
        size: Size of the loader

    Returns:
        Group with loader and text
    """
    return dmc.Group(
        [
            dmc.Loader(size=size, type="dots"),
            dmc.Text(text, size="sm", c="dimmed"),
        ],
        gap="sm",
    )


def create_step_progress(active_step: int, steps: list[str]) -> dmc.Stepper:
    """Create a step-by-step progress indicator.

    Args:
        active_step: Currently active step index (0-based)
        steps: List of step labels

    Returns:
        Stepper component
    """
    step_items = [dmc.StepperStep(label=step) for step in steps]

    return dmc.Stepper(
        active=active_step,
        children=step_items,
        size="sm",
    )


def create_loading_state_wrapper(
    children: list, is_loading: bool, skeleton_component: Any | None = None
) -> html.Div:
    """Wrap content with loading state.

    Shows skeleton or spinner while loading, content when loaded.

    Args:
        children: Content to display when loaded
        is_loading: Whether content is currently loading
        skeleton_component: Optional custom skeleton component

    Returns:
        Div with conditional loading state
    """
    if is_loading:
        return html.Div(skeleton_component if skeleton_component else create_centered_spinner("Loading data..."))
    return html.Div(children)


def create_pulse_indicator(color: str = "blue", size: int = 12) -> html.Div:
    """Create a pulsing dot indicator for live/active status.

    Args:
        color: Color of the pulse indicator
        size: Size of the indicator in pixels

    Returns:
        Div with pulsing animation
    """
    return html.Div(
        style={
            "width": f"{size}px",
            "height": f"{size}px",
            "borderRadius": "50%",
            "backgroundColor": f"var(--mantine-color-{color}-6)",
            "animation": "pulse-dot 2s ease-in-out infinite",
        }
    )
