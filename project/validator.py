"""
validator.py
Input validation functions for TaskFlow.
"""

from datetime import datetime


def validate_date(date_str):
    """Validate that a date string is in YYYY-MM-DD format.

    Args:
        date_str (str): The date string to validate.

    Raises:
        ValueError: If the date format is invalid.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"Invalid date format '{date_str}'. Expected format: YYYY-MM-DD (e.g. 2026-06-15)"
        )


def validate_title(title):
    """Validate that a task title is non-empty and within character limits.

    Args:
        title (str): The title to validate.

    Raises:
        ValueError: If the title is empty or exceeds 100 characters.
    """
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    if len(title.strip()) > 100:
        raise ValueError("Task title must be 100 characters or fewer.")


def validate_priority(priority):
    """Validate that priority is one of the accepted values.

    Args:
        priority (str): The priority string to validate.

    Raises:
        ValueError: If the priority is not valid.
    """
    valid = {"high", "medium", "low"}
    if priority not in valid:
        raise ValueError(f"Priority must be one of: {', '.join(valid)}. Got '{priority}'.")
