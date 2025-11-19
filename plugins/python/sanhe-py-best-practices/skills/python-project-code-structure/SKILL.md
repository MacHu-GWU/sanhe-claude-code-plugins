---
name: python-project-code-structure
description: Detects and displays Python project structure and important paths
---

# python-project-code-structure

**Use this skill when you need to:**

- Understand the directory structure of a Python project
- Find important paths (package location, tests, docs, venv, tools)
- Get package name and version from pyproject.toml
- Locate project root and configuration files

**What it does:**

Runs `scripts/detect_python_project_metadata.py` to automatically detect and display all critical paths in your Python project, including:

- Package name and version
- Virtual environment paths (Python, pip, pytest)
- Tests and documentation directories
- Configuration files (Sphinx, Makefile)
