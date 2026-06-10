"""
task_manager.py
Core task management logic for TaskFlow.
"""

from datetime import datetime
from storage import Storage
from validator import validate_date, validate_title


class TaskManager:
    """Manages all task operations including CRUD and search."""

    def __init__(self, storage_path="tasks.json"):
        self.storage = Storage(storage_path)
        self.tasks = self.storage.load()

    def _next_id(self):
        """Generate the next available task ID."""
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def add_task(self, title, priority="medium", due_date=None, category="general", description=""):
        """Add a new task to the task list.

        Args:
            title (str): The title of the task.
            priority (str): Priority level — 'high', 'medium', or 'low'.
            due_date (str): Optional due date in YYYY-MM-DD format.
            category (str): Category label for the task.
            description (str): Optional detailed description.

        Returns:
            dict: The newly created task.
        """
        validate_title(title)
        if due_date:
            validate_date(due_date)

        task = {
            "id": self._next_id(),
            "title": title,
            "description": description,
            "priority": priority,
            "category": category,
            "due_date": due_date,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }

        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def list_tasks(self, priority_filter=None, category_filter=None, status_filter=None):
        """Retrieve tasks with optional filtering and sorting.

        Args:
            priority_filter (str): Optional priority to filter by.
            category_filter (str): Optional category to filter by.
            status_filter (str): Optional status to filter by.

        Returns:
            list: Filtered and sorted list of task dictionaries.
        """
        priority_order = {"high": 0, "medium": 1, "low": 2}
        results = list(self.tasks)

        if priority_filter:
            results = [t for t in results if t["priority"] == priority_filter]
        if category_filter:
            results = [t for t in results if t["category"] == category_filter]
        if status_filter:
            results = [t for t in results if t["status"] == status_filter]

        results.sort(key=lambda t: (t["status"], t["created_at"]))
        return results

    def complete_task(self, task_id):
        """Mark a task as completed.

        Args:
            task_id (int): The ID of the task to complete.

        Returns:
            bool: True if successful, False if task not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.storage.save(self.tasks)
                return True
        return False

    def delete_task(self, task_id):
        """Delete a task by ID.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if deleted, False if not found.
        """
        original_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < original_len:
            self.storage.save(self.tasks)
            return True
        return False

    def update_task(self, task_id, updates):
        """Update fields of an existing task.

        Args:
            task_id (int): The ID of the task to update.
            updates (dict): Dictionary of fields to update.

        Returns:
            bool: True if updated, False if not found.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                if "title" in updates:
                    validate_title(updates["title"])
                if "due_date" in updates and updates["due_date"]:
                    validate_date(updates["due_date"])
                task.update(updates)
                self.storage.save(self.tasks)
                return True
        return False

    def search_tasks(self, query):
        """Search tasks by keyword in title or description.

        Args:
            query (str): Keyword to search for.

        Returns:
            list: Tasks whose title or description contain the query.
        """
        query_lower = query.lower()
        return [
            found_task for found_task in self.tasks
            if query_lower in found_task.get("title", "").lower()
            or query_lower in found_task.get("description", "").lower()
        ]
    

    def get_overdue_tasks(self):
      """Return all pending tasks whose due date has passed."""
      from datetime import date
      today = date.today().strftime("%Y-%m-%d")
      return [
          t for t in self.tasks
          if t["status"] == "pending"
          and t["due_date"]
          and t["due_date"] < today
      ]
