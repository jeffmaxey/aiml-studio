"""Tooltip and help text components for providing contextual information."""

from typing import Any, Literal

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_tooltip(
    children: Any,
    label: str,
    position: Literal["top", "right", "bottom", "left"] = "top",
    with_arrow: bool = True,
    multiline: bool = False,
    color: str = "dark",
    transition_props: dict[str, Any] | None = None,
) -> dmc.Tooltip:
    """Create a tooltip component.

    Args:
        children: Element to attach tooltip to
        label: Tooltip text
        position: Tooltip position relative to element
        with_arrow: Show arrow pointing to element
        multiline: Allow multiline text
        color: Tooltip background color
        transition_props: Transition animation properties

    Returns:
        Mantine Tooltip component
    """
    if transition_props is None:
        transition_props = {"transition": "fade", "duration": 200}

    return dmc.Tooltip(
        label=label,
        position=position,
        withArrow=with_arrow,
        multiline=multiline,
        color=color,
        transitionProps=transition_props,
        children=children,
    )


def create_help_icon(
    tooltip_text: str,
    icon: str = "tabler:help-circle",
    size: int = 16,
    color: str = "gray",
) -> dmc.Tooltip:
    """Create a help icon with tooltip.

    Args:
        tooltip_text: Help text to display
        icon: Icon identifier
        size: Icon size
        color: Icon color

    Returns:
        Tooltip containing help icon
    """
    return create_tooltip(
        children=DashIconify(icon=icon, width=size, color=color, style={"cursor": "help"}),
        label=tooltip_text,
        multiline=True,
    )


def create_info_icon(
    tooltip_text: str,
    icon: str = "tabler:info-circle",
    size: int = 16,
    color: str = "blue",
) -> dmc.Tooltip:
    """Create an info icon with tooltip.

    Args:
        tooltip_text: Information text to display
        icon: Icon identifier
        size: Icon size
        color: Icon color

    Returns:
        Tooltip containing info icon
    """
    return create_tooltip(
        children=DashIconify(icon=icon, width=size, color=color, style={"cursor": "help"}),
        label=tooltip_text,
        multiline=True,
    )


def create_help_text(
    text: str,
    size: Literal["xs", "sm", "md", "lg"] = "xs",
    color: str = "dimmed",
    icon: str | None = "tabler:info-circle",
) -> dmc.Group:
    """Create help text with optional icon.

    Args:
        text: Help text content
        size: Text size
        color: Text color
        icon: Optional icon identifier

    Returns:
        Group containing help text
    """
    children = []

    if icon:
        children.append(DashIconify(icon=icon, width=14, color=color))

    children.append(dmc.Text(text, size=size, c=color))

    return dmc.Group(children, gap="xs", align="center")


def create_label_with_help(
    label: str,
    help_text: str,
    required: bool = False,
) -> dmc.Group:
    """Create a form label with help icon.

    Args:
        label: Label text
        help_text: Help text to display in tooltip
        required: Show required indicator

    Returns:
        Group containing label and help icon
    """
    label_text = f"{label} *" if required else label

    return dmc.Group(
        [
            dmc.Text(label_text, size="sm", fw=500),
            create_help_icon(help_text),
        ],
        gap="xs",
        align="center",
    )


def create_popover_help(
    children: Any,
    help_title: str,
    help_content: str | list[Any],
    width: int = 320,
    position: Literal["top", "right", "bottom", "left"] = "right",
) -> dmc.Popover:
    """Create a popover with help content.

    Args:
        children: Element to attach popover to (usually help icon)
        help_title: Popover title
        help_content: Help content (text or components)
        width: Popover width
        position: Popover position

    Returns:
        Mantine Popover component
    """
    if isinstance(help_content, str):
        help_content = dmc.Text(help_content, size="sm")

    return dmc.Popover(
        [
            dmc.PopoverTarget(children),
            dmc.PopoverDropdown(
                dmc.Stack(
                    [
                        dmc.Text(help_title, size="sm", fw=600),
                        help_content,
                    ],
                    gap="xs",
                )
            ),
        ],
        width=width,
        position=position,
        withArrow=True,
        shadow="md",
    )


def create_contextual_help_button(button_text: str = "Help") -> dmc.Button:
    """Create a contextual help button.

    Args:
        button_text: Button label

    Returns:
        Help button component
    """
    return dmc.Button(
        button_text,
        leftSection=DashIconify(icon="tabler:help-circle", width=16),
        variant="light",
        color="blue",
        size="xs",
        id="contextual-help-button",
    )


def create_help_drawer_trigger() -> dmc.ActionIcon:
    """Create a help drawer trigger button.

    Returns:
        ActionIcon that opens help drawer
    """
    return dmc.ActionIcon(
        DashIconify(icon="tabler:help-circle", width=20),
        variant="subtle",
        size="lg",
        color="blue",
        id="help-drawer-trigger",
    )


def create_help_section(
    title: str,
    content: str | list[Any],
    icon: str = "tabler:info-circle",
    collapsible: bool = False,
) -> dmc.Paper:
    """Create a help section component.

    Args:
        title: Section title
        content: Help content (text or components)
        icon: Section icon
        collapsible: Make section collapsible

    Returns:
        Paper containing help section
    """
    if isinstance(content, str):
        content = dmc.Text(content, size="sm")

    header = dmc.Group(
        [
            dmc.ThemeIcon(
                DashIconify(icon=icon, width=20),
                size="lg",
                radius="md",
                variant="light",
                color="blue",
            ),
            dmc.Text(title, size="sm", fw=600),
        ],
        gap="sm",
    )

    if collapsible:
        section_content = dmc.Accordion(
            dmc.AccordionItem(
                [
                    dmc.AccordionControl(header),
                    dmc.AccordionPanel(content),
                ],
                value=title,
            ),
            variant="contained",
        )
    else:
        section_content = dmc.Stack([header, content], gap="sm")

    return dmc.Paper(
        section_content,
        p="md",
        radius="md",
        withBorder=True,
    )


def create_keyboard_shortcut(
    keys: list[str],
    description: str,
) -> dmc.Group:
    """Create a keyboard shortcut display component.

    Args:
        keys: List of keyboard keys (e.g., ["Ctrl", "K"])
        description: Description of the shortcut

    Returns:
        Group containing shortcut display
    """
    key_badges = [dmc.Kbd(key) for key in keys]

    return dmc.Group(
        [
            dmc.Group(key_badges, gap="xs"),
            dmc.Text(description, size="sm", c="dimmed"),
        ],
        justify="space-between",
        style={"width": "100%"},
    )


def create_help_content_section(
    sections: list[dict[str, Any]],
) -> dmc.Stack:
    """Create a complete help content section with multiple topics.

    Args:
        sections: List of section dictionaries with title, content, icon

    Returns:
        Stack containing help sections
    """
    help_sections = []

    for section in sections:
        help_sections.append(
            create_help_section(
                title=section.get("title", "Help"),
                content=section.get("content", ""),
                icon=section.get("icon", "tabler:info-circle"),
                collapsible=section.get("collapsible", False),
            )
        )

    return dmc.Stack(help_sections, gap="md")


def create_field_description(
    description: str,
    type: Literal["help", "error", "warning", "info"] = "help",
) -> dmc.Text:
    """Create a field description/help text.

    Args:
        description: Description text
        type: Type of description (affects color)

    Returns:
        Text component
    """
    color_map = {
        "help": "dimmed",
        "error": "red",
        "warning": "yellow",
        "info": "blue",
    }

    return dmc.Text(
        description,
        size="xs",
        c=color_map.get(type, "dimmed"),
        mt=4,
    )
