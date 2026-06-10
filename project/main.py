#!/usr/bin/env python3
"""
TaskFlow - A Simple Command-Line Task Manager
Entry point for the application.
"""

import argparse
import sys
from task_manager import TaskManager
from ui import print_header, print_task_table, print_success, print_error


def main():
    """Main entry point for the TaskFlow application."""
    print_header()

    parser = argparse.ArgumentParser(
        description="TaskFlow - Manage your tasks from the command line",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--title", required=True, help="Task title")
    add_parser.add_argument("--priority", choices=["high", "medium", "low"],
                            default="medium", help="Task priority")
    add_parser.add_argument("--due", help="Due date (YYYY-MM-DD)")
    add_parser.add_argument("--category", default="general", help="Task category")
    add_parser.add_argument("--description", default="", help="Task description")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--priority", choices=["high", "medium", "low"],
                             help="Filter by priority")
    list_parser.add_argument("--category", help="Filter by category")
    list_parser.add_argument("--status", choices=["pending", "completed"],
                              help="Filter by status")

    # Complete task command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("--id", type=int, required=True, help="Task ID")

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("--id", type=int, required=True, help="Task ID")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search tasks by keyword")
    search_parser.add_argument("--query", required=True, help="Search keyword")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("--id", type=int, required=True, help="Task ID")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--priority", choices=["high", "medium", "low"])
    update_parser.add_argument("--due", help="New due date (YYYY-MM-DD)")
    update_parser.add_argument("--category", help="New category")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(
            title=args.title,
            priority=args.priority,
            due_date=args.due,
            category=args.category,
            description=args.description
        )
        print_success(f"Task added successfully (ID: {task['id']})")

    elif args.command == "list":
        tasks = manager.list_tasks(
            priority_filter=args.priority,
            category_filter=args.category,
            status_filter=args.status
        )
        print_task_table(tasks)

    elif args.command == "complete":
        success = manager.complete_task(args.id)
        if success:
            print_success(f"Task {args.id} marked as complete.")
        else:
            print_error(f"Task with ID {args.id} not found.")

    elif args.command == "delete":
        success = manager.delete_task(args.id)
        if success:
            print_success(f"Task {args.id} deleted.")
        else:
            print_error(f"Task with ID {args.id} not found.")

    elif args.command == "search":
        results = manager.search_tasks(args.query)
        if results:
            print_task_table(results)
        else:
            print(f"No tasks found matching '{args.query}'.")

    elif args.command == "update":
        updates = {}
        if args.title:
            updates["title"] = args.title
        if args.priority:
            updates["priority"] = args.priority
        if args.due:
            updates["due_date"] = args.due
        if args.category:
            updates["category"] = args.category
        success = manager.update_task(args.id, updates)
        if success:
            print_success(f"Task {args.id} updated successfully.")
        else:
            print_error(f"Task with ID {args.id} not found.")


if __name__ == "__main__":
    main()
