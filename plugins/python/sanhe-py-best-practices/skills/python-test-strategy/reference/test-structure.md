# Package Test Directory Structure

Each Python package (directory containing `__init__.py`) has a corresponding test directory in `tests/`. Each test directory contains an `all.py` file that runs code coverage tests for all modules in that package.

## Directory Structure Pattern

**Pattern:**
```
Package: <project>/<subpackage>/
Test directory: tests/<subpackage>/
Coverage runner: tests/<subpackage>/all.py
```

**Example:**

| Package | Test Directory | Coverage Runner |
|---------|----------------|-----------------|
| `learn_claude_code/math/operations/` | `tests/math/operations/` | `tests/math/operations/all.py` |
| `learn_claude_code/utils/` | `tests/utils/` | `tests/utils/all.py` |
| `learn_claude_code/` | `tests/learn_claude_code/` | `tests/learn_claude_code/all.py` |

## Full Project Structure Example

```
learn_claude_code/
├── __init__.py
├── math/
│   ├── __init__.py
│   └── operations/
│       ├── __init__.py
│       └── calculator.py
└── utils/
    ├── __init__.py
    └── helpers.py

tests/
├── all.py                    (run all tests for entire project)
├── learn_claude_code/
│   └── all.py               (run all tests for learn_claude_code package)
├── math/
│   ├── all.py               (run all tests for math package)
│   └── operations/
│       ├── all.py           (run all tests for operations package)
│       └── test_math_operations_calculator.py
└── utils/
    ├── all.py               (run all tests for utils package)
    └── test_utils_helpers.py
```

## Root Level Tests

The main `tests/all.py` at the project root runs code coverage tests for all modules across all packages in your entire project.

## Purpose of `all.py` Files

- **Package coverage**: Each `all.py` runs coverage tests for its specific package
- **Hierarchical testing**: Tests can be run at any level (package, subpackage, or whole project)
- **Development workflow**: Test individual packages during development; run full suite before committing

## Coverage Tools Integration

The `all.py` files integrate with your `.coveragerc` configuration to generate HTML coverage reports for their respective packages or the entire project.
