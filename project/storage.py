"""
storage.py
Handles persistent storage for TaskFlow.
Supports multiple file formats: JSON and CSV.
Refactored to use a base Storage interface for extensibility.
"""

import json
import os
import csv


class Storage:
    """Abstract-style base storage class. Subclass for each format."""

    def load(self):
        raise NotImplementedError

    def save(self, tasks):
        raise NotImplementedError


class JSONStorage(Storage):
    """Manages reading and writing task data to a JSON file."""

    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath

    def load(self):
        """Load tasks from the JSON file.

        Returns:
            list: A list of task dictionaries, or an empty list if no file exists.

        Example:
            >>> storage = JSONStorage("tasks.json")
            >>> tasks = storage.load()
            >>> isinstance(tasks, list)
            True
        """
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load tasks file ({e}). Starting fresh.")
            return []

    def save(self, tasks):
        """Save the task list to the JSON file.

        Args:
            tasks (list): The list of task dictionaries to persist.

        Example:
            >>> storage = JSONStorage("tasks.json")
            >>> storage.save([{"id": 1, "title": "Test"}])
        """
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)


class CSVStorage(Storage):
    """Manages reading and writing task data to a CSV file."""

    FIELDS = ["id", "title", "description", "priority", "category",
              "due_date", "status", "created_at", "completed_at"]

    def __init__(self, filepath="tasks.csv"):
        self.filepath = filepath

    def load(self):
        """Load tasks from the CSV file.

        Returns:
            list: A list of task dictionaries, or an empty list if no file exists.

        Example:
            >>> storage = CSVStorage("tasks.csv")
            >>> tasks = storage.load()
            >>> isinstance(tasks, list)
            True
        """
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                tasks = []
                for row in reader:
                    row["id"] = int(row["id"])
                    tasks.append(row)
                return tasks
        except IOError as e:
            print(f"Warning: Could not load tasks file ({e}). Starting fresh.")
            return []

    def save(self, tasks):
        """Save the task list to the CSV file.

        Args:
            tasks (list): The list of task dictionaries to persist.

        Example:
            >>> storage = CSVStorage("tasks.csv")
            >>> storage.save([{"id": 1, "title": "Test"}])
        """
        with open(self.filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(tasks)


def get_storage(fmt="json"):
    """Factory function to return the correct storage instance.

    Args:
        fmt (str): Storage format — 'json' or 'csv'.

    Returns:
        Storage: An instance of JSONStorage or CSVStorage.

    Example:
        >>> storage = get_storage("json")
        >>> isinstance(storage, JSONStorage)
        True
    """
    if fmt == "csv":
        return CSVStorage()
    return JSONStorage()