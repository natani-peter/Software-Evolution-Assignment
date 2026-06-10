# Contributing to TaskFlow

Thank you for considering contributing to TaskFlow! This document outlines the process for contributing to this project.

---

## Code of Conduct

All contributors are expected to act respectfully and professionally. Harassment, discrimination, or harmful behaviour of any kind will not be tolerated.

---

## How to Contribute

### Reporting Bugs

If you find a bug, please open a GitHub Issue with the following information:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behaviour
- Actual behaviour
- Your operating system and Python version

### Suggesting Enhancements

Feature requests are welcome! Open a GitHub Issue labelled `enhancement` with:
- A clear description of the feature
- The problem it solves
- Any suggested implementation approach

### Submitting Pull Requests

1. **Fork the repository** and clone your fork locally.
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** with clear, descriptive commit messages.
4. **Run tests** before pushing:
   ```bash
   python -m pytest tests/
   ```
5. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** against the `main` branch. Include:
   - A summary of changes made
   - The issue number it closes (e.g., `Closes #12`)

---

## Commit Message Guidelines

Please use the following format for commit messages:

```
<type>: <short description>

[Optional longer description]
```

**Types:**
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation update
- `refactor` — Code restructuring
- `test` — Adding or updating tests
- `chore` — Maintenance or tooling

**Examples:**
- `feat: Added priority filtering to task list command`
- `fix: Resolved date validation error on task creation`
- `docs: Updated README with installation steps`

---

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/Software-Evolution-Assignment.git
cd Software-Evolution-Assignment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Style Guide

- Follow [PEP 8](https://pep8.org/) Python style conventions
- Use meaningful variable and function names
- Include docstrings for all functions and classes
- Keep functions small and focused on a single responsibility

---

Thank you for helping improve TaskFlow!
