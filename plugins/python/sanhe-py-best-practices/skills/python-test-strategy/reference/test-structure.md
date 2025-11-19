# Package Test Directory Structure

Each Python package (directory containing `__init__.py`) has a corresponding test directory in `tests/`. Each test directory contains an `all.py` file that runs code coverage tests for all modules in that package.

## Directory Structure Pattern

The test directory structure mirrors your source directory:

```
Source:  <project>/<subpackage>/
Tests:   tests/<subpackage>/
```

## Purpose of `all.py` Files

Each test directory includes an `all.py` file that:
- Runs coverage tests for all modules in that package
- Generates HTML coverage reports for the package
- Enables hierarchical testing (test individual packages or entire project)

**Examples:**
- `tests/all.py` - Run all tests for entire project
- `tests/math/all.py` - Run all tests for math package
- `tests/math/operations/all.py` - Run all tests for operations subpackage

## Finding the Right Test Location

Use the `locate_test_file.py` script to determine where a test file should be placed for any source file:

```bash
python scripts/locate_test_file.py /absolute/path/to/source/file.py
```

This handles the naming convention automatically. See the SKILL.md for usage examples.
