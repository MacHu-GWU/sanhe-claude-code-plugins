---
name: python-test-strategy
description: Python testing patterns with organized test file structure, coverage goals, and public API testing
---

# python-test-strategy

Comprehensive testing strategy for Python projects with organized test structure, code coverage standards, and public API testing patterns.

## Use This Skill When You Need To

- Set up test file organization matching your project structure
- Understand test naming conventions and directory layouts
- Configure code coverage reporting and goals
- Test public API interfaces with `api.py` imports
- Run individual module tests or entire package coverage

## Key Concepts

**Test Organization**: Each source file has a corresponding test file with structured naming conventions.

**Coverage Goals**: Target 95%+ code coverage for implementation files.

**Public API Testing**: Use `api.py` to expose all public interfaces and test them in `tests/test_api.py`.

## Quick Reference

- 📋 **Unit Test Organization**: See [Unit Testing Guide](./reference/unit-testing.md)
- 🗂️ **Directory Structure**: See [Test Structure Reference](./reference/test-structure.md)
- ▶️ **Running Tests**: See [Running Tests Guide](./reference/running-tests.md)
- 📊 **Coverage Configuration**: See [Coverage Reference](./reference/coverage.md)
- 🔌 **Public API Testing**: See [Public API Guide](./reference/public-api.md)

## Quick Start Example

For a project named `learn_claude_code`:

- Source: `learn_claude_code/math/operations/calculator.py`
- Test: `tests/math/operations/test_math_operations_calculator.py`
- Run test: `.venv/bin/python tests/math/operations/test_math_operations_calculator.py`
- Run all tests: `.venv/bin/python tests/all.py`

## Utility Script: locate_test_file.py

The included `scripts/locate_test_file.py` utility helps identify where test files should be placed for a given source file. This is useful for IDE integrations, pre-commit hooks, and development workflows.

**Usage:**
```bash
python scripts/locate_test_file.py /absolute/path/to/source/file.py
```

**Example:**
```bash
python scripts/locate_test_file.py /Users/dev/project/learn_claude_code/math/operations/calculator.py
# Output: /Users/dev/project/tests/math/operations/test_math_operations_calculator.py
```

**Verbose mode (shows calculation details):**
```bash
python scripts/locate_test_file.py -v /Users/dev/project/learn_claude_code/utils/helpers.py
# Output:
# Project root:     /Users/dev/project
# Source file:      /Users/dev/project/learn_claude_code/utils/helpers.py
# Relative source:  learn_claude_code/utils/helpers.py
# Test file:        /Users/dev/project/tests/utils/test_utils_helpers.py
```

See the reference guides for comprehensive details on each aspect of the testing strategy.
