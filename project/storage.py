"""
storage.py
Handles persistent JSON-based storage for TaskFlow.
"""

import json
import os


class Storage:
    """Manages reading and writing task data to a JSON file."""

    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath

    def load(self):
        """Load tasks from the JSON file.

        Returns:
            list: A list of task dictionaries, or an empty list if no file exists.
        """
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, tasks):
        """Save the task list to the JSON file.

        Args:
            tasks (list): The list of task dictionaries to persist.
        """
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
