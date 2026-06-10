"""
ui.py
Command-line interface display helpers for TaskFlow.
Provides colour-coded output and formatted task tables.
"""

# ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
GREY = "\033[90m"

PRIORITY_COLOURS = {
    "high": RED,
    "medium": YELLOW,
    "low": GREEN,
}

STATUS_COLOURS = {
    "pending": CYAN,
    "completed": GREY,
}


def print_header():
    """Print the application banner."""
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════╗")
    print(f"║       TaskFlow v1.0.0        ║")
    print(f"╚══════════════════════════════╝{RESET}\n")


def print_success(message):
    """Print a success message in green."""
    print(f"{GREEN}✔ {message}{RESET}")


def print_error(message):
    """Print an error message in red."""
    print(f"{RED}✘ {message}{RESET}")


def print_task_table(tasks):
    """Display a formatted table of tasks.

    Args:
        tasks (list): List of task dictionaries to display.
    """
    if not tasks:
        print(f"{GREY}No tasks found.{RESET}\n")
        return

    header = f"{'ID':<5} {'Title':<35} {'Priority':<10} {'Status':<12} {'Due Date':<12} {'Category'}"
    print(f"\n{BOLD}{header}{RESET}")
    print("-" * 90)

    for task in tasks:
        p_colour = PRIORITY_COLOURS.get(task["priority"], RESET)
        s_colour = STATUS_COLOURS.get(task["status"], RESET)
        due = task["due_date"] or "—"
        title = task["title"][:33] + ".." if len(task["title"]) > 35 else task["title"]

        print(
            f"{task['id']:<5} "
            f"{title:<35} "
            f"{p_colour}{task['priority']:<10}{RESET} "
            f"{s_colour}{task['status']:<12}{RESET} "
            f"{due:<12} "
            f"{task['category']}"
        )

    print()
