"""Form validation utilities for AIML Studio."""

import re
from typing import Any


def validate_required(value: Any, field_name: str = "Field") -> tuple[bool, str]:
    """Validate that a field is not empty.

    Args:
        value: Field value to validate
        field_name: Name of the field for error messages

    Returns:
        Tuple of (is_valid, error_message)
    """
    if value is None or value == "" or (isinstance(value, str) and value.strip() == ""):
        return False, f"{field_name} is required"
    return True, ""


def validate_email(email: str) -> tuple[bool, str]:
    """Validate email format.

    Args:
        email: Email address to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not email:
        return False, "Email is required"

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"

    return True, ""


def validate_min_length(value: str, min_length: int, field_name: str = "Field") -> tuple[bool, str]:
    """Validate minimum string length.

    Args:
        value: String value to validate
        min_length: Minimum required length
        field_name: Name of the field for error messages

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not value or len(value) < min_length:
        return False, f"{field_name} must be at least {min_length} characters long"
    return True, ""


def validate_max_length(value: str, max_length: int, field_name: str = "Field") -> tuple[bool, str]:
    """Validate maximum string length.

    Args:
        value: String value to validate
        max_length: Maximum allowed length
        field_name: Name of the field for error messages

    Returns:
        Tuple of (is_valid, error_message)
    """
    if value and len(value) > max_length:
        return False, f"{field_name} must not exceed {max_length} characters"
    return True, ""


def validate_numeric_range(
    value: float | int | None, min_value: float | None = None, max_value: float | None = None, field_name: str = "Value"
) -> tuple[bool, str]:
    """Validate numeric value is within range.

    Args:
        value: Numeric value to validate
        min_value: Minimum allowed value (optional)
        max_value: Maximum allowed value (optional)
        field_name: Name of the field for error messages

    Returns:
        Tuple of (is_valid, error_message)
    """
    if value is None:
        return False, f"{field_name} is required"

    try:
        num_value = float(value)
    except (ValueError, TypeError):
        return False, f"{field_name} must be a number"

    if min_value is not None and num_value < min_value:
        return False, f"{field_name} must be at least {min_value}"

    if max_value is not None and num_value > max_value:
        return False, f"{field_name} must not exceed {max_value}"

    return True, ""


def validate_pattern(value: str, pattern: str, field_name: str = "Field", error_msg: str | None = None) -> tuple[bool, str]:
    """Validate value matches a regex pattern.

    Args:
        value: String value to validate
        pattern: Regex pattern to match
        field_name: Name of the field for error messages
        error_msg: Custom error message (optional)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not value:
        return False, f"{field_name} is required"

    if not re.match(pattern, value):
        msg = error_msg or f"{field_name} format is invalid"
        return False, msg

    return True, ""


def validate_form(
    form_data: dict[str, Any], validation_rules: dict[str, list[tuple]]
) -> tuple[bool, dict[str, str]]:
    """Validate entire form based on rules.

    Args:
        form_data: Dictionary of form field values
        validation_rules: Dictionary mapping field names to list of validation tuples
            Each tuple is (validator_function, args_dict)

    Returns:
        Tuple of (all_valid, errors_dict)
        where errors_dict maps field names to error messages

    Example:
        >>> form_data = {"name": "John", "email": "invalid"}
        >>> rules = {
        ...     "name": [(validate_required, {"field_name": "Name"})],
        ...     "email": [(validate_required, {"field_name": "Email"}),
        ...               (validate_email, {})]
        ... }
        >>> is_valid, errors = validate_form(form_data, rules)
    """
    errors: dict[str, str] = {}
    all_valid = True

    for field_name, validators in validation_rules.items():
        field_value = form_data.get(field_name)

        for validator_func, validator_args in validators:
            is_valid, error_msg = validator_func(field_value, **validator_args)
            if not is_valid:
                errors[field_name] = error_msg
                all_valid = False
                break  # Stop at first error for this field

    return all_valid, errors


def create_error_message(field_name: str, error_type: str) -> str:
    """Create a user-friendly error message with recovery suggestions.

    Args:
        field_name: Name of the field with error
        error_type: Type of error (required, invalid, too_short, etc.)

    Returns:
        Formatted error message with suggestions
    """
    error_messages = {
        "required": f"{field_name} is required. Please provide a value.",
        "invalid": f"{field_name} format is invalid. Please check your input.",
        "too_short": f"{field_name} is too short. Please provide more characters.",
        "too_long": f"{field_name} is too long. Please reduce the length.",
        "out_of_range": f"{field_name} is out of valid range. Please check the limits.",
        "duplicate": f"{field_name} already exists. Please choose a different value.",
    }

    return error_messages.get(error_type, f"{field_name} is invalid")
