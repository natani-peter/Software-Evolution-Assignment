# TaskFlow — Simple Task Manager

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

## Project Description

TaskFlow is a lightweight command-line task manager built in Python. It allows users to create, update, prioritise, and track tasks with due dates and categories. The project was created as part of a Software Evolution assignment to demonstrate version control, branching, issue tracking, and collaborative development practices using GitHub.

Key features include:
- Create, read, update, and delete (CRUD) tasks
- Assign priorities (High, Medium, Low)
- Set due dates and categories
- Filter and search tasks
- Mark tasks as complete
- Persistent JSON-based storage

---

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Software-Evolution-Assignment.git
   cd Software-Evolution-Assignment
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## Usage Instructions

### Adding a Task
```bash
python main.py add --title "Buy groceries" --priority high --due 2026-06-15 --category personal
```

### Listing All Tasks
```bash
python main.py list
```

### Completing a Task
```bash
python main.py complete --id 1
```

### Deleting a Task
```bash
python main.py delete --id 1
```

### Searching Tasks
```bash
python main.py search --query "groceries"
```

### Filtering by Priority
```bash
python main.py list --priority high
```

---

## Project Structure

```
Software-Evolution-Assignment/
├── main.py              # Entry point
├── task_manager.py      # Core task management logic
├── storage.py           # JSON persistence layer
├── ui.py                # Command-line interface helpers
├── validator.py         # Input validation module
├── requirements.txt     # Python dependencies
├── tasks.json           # Task data storage (auto-generated)
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## Merge Conflict Resolution

During the development of this project, a merge conflict occurred when merging the `feature-ui` and `feature-enhancement` branches into `main`. Both branches had modified the `task_manager.py` file — specifically the `list_tasks()` method:

- **feature-ui** added a colour-coded output format using the `colorama` library.
- **feature-enhancement** added sorting and filtering parameters to the same method.

**Resolution Process:**
1. When `feature-enhancement` was merged into `main` first (via Pull Request), it succeeded cleanly.
2. When `feature-ui` was subsequently merged, Git detected a conflict in `task_manager.py` around the `list_tasks()` method.
3. The conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) were inspected in the file.
4. The resolution combined both changes: the sorting/filtering logic from `feature-enhancement` was preserved, and the colour-coded display formatting from `feature-ui` was applied on top.
5. The resolved file was staged (`git add task_manager.py`) and the merge was committed.
6. The fix was documented in the Pull Request description before closing.

---

## Contributors

| Name | Role |
|------|------|
|NATANI PETER| Lead Developer |

---

## License

This project is licensed under the MIT License. See the license file for details.
