#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Locate the test file path for a given Python source file.

This utility calculates where a test file should be placed for a given Python
source file, following the Python test strategy naming convention:

    Source: git-repo/<package_name>/<subpackage>/<module>.py
    Test:   tests/<subpackage>/test_<subpackage>_<module>.py

Given an absolute path to a source file, this script:

1. Finds the project root (by locating pyproject.toml)
2. Determines the relative path from project root to source file
3. Calculates the correct test file path using naming convention
4. Prints the absolute test file path

This is useful for:

- IDE integrations that need to jump from source to test file
- Build tools that generate test files in the correct location
- Pre-commit hooks that validate tests exist for changed source files
- Development workflows that automate test file creation

Examples:

    Given source file:
    /Users/dev/project/learn_claude_code/math/operations/calculator.py

    The script outputs:
    /Users/dev/project/tests/math/operations/test_math_operations_calculator.py

    Another example:
    Given source file:
    /Users/dev/project/learn_claude_code/utils/helpers.py

    The script outputs:
    /Users/dev/project/tests/utils/test_utils_helpers.py
"""

import argparse
import sys
from pathlib import Path


def locate_pyproject_toml(dir_cwd: Path) -> Path | None:
    """
    Locate the pyproject.toml file by searching upwards in the directory tree.

    Searches up to 10 levels up from the starting directory to find the
    pyproject.toml file, which indicates the project root.

    Args:
        dir_cwd: Starting directory for search

    Returns:
        Path to pyproject.toml if found, None otherwise
    """
    for _ in range(10):
        pyproject = dir_cwd / "pyproject.toml"
        if pyproject.exists():
            return pyproject
        dir_cwd = dir_cwd.parent
    return None


def calculate_test_file_path(
    source_file_path: Path,
    project_root: Path,
) -> Path:
    """
    Calculate the test file path for a given source file.

    Applies the naming convention:
        tests/<subpackage>/test_<subpackage>_<module>.py

    For example:
        Source: learn_claude_code/math/operations/calculator.py
        Test:   tests/math/operations/test_math_operations_calculator.py

    Args:
        source_file_path: Absolute path to the source file
        project_root: Absolute path to the project root

    Returns:
        Absolute path where the test file should be located

    Raises:
        ValueError: If source file is not within the project
    """
    # Get relative path from project root
    try:
        relative_source = source_file_path.relative_to(project_root)
    except ValueError:
        raise ValueError(
            f"Source file {source_file_path} is not within project root {project_root}"
        )

    # Get all path parts: ['package_name', 'subpackage', 'module.py']
    parts = relative_source.parts
    skip_first = 1  # Skip the project/package name (first directory)

    # Extract subdirectory and module name
    # parts[1:-1] are subdirectories, parts[-1] is the module filename
    subdirs = parts[skip_first:-1]
    module_filename = parts[-1].replace(".py", "")

    # Build test filename
    if subdirs:
        # Has subdirectories: test_<subdir1>_<subdir2>_<module>.py
        test_filename = f"test_{'_'.join(subdirs)}_{module_filename}.py"
        test_dir = project_root / "tests" / Path(*subdirs)
    else:
        # Root level: test_<module>.py
        test_filename = f"test_{module_filename}.py"
        test_dir = project_root / "tests"

    return test_dir / test_filename


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Calculate test file path for a given Python source file",
        epilog="""
Examples:
  %(prog)s /path/to/project/learn_claude_code/math/calculator.py
    → /path/to/project/tests/math/test_math_calculator.py

  %(prog)s /path/to/project/learn_claude_code/math/operations/calculator.py
    → /path/to/project/tests/math/operations/test_math_operations_calculator.py

This script is useful for:
  • IDE integrations (jump from source to test)
  • Pre-commit hooks (verify tests exist)
  • Build tools (generate test files)
  • Development workflows
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "source_file",
        type=str,
        help="Absolute path to the Python source file",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed information about the calculation",
    )

    args = parser.parse_args()

    # Convert to Path
    source_path = Path(args.source_file)

    # Don't check existence of source file for flexibility, this function
    # is just to calculate the test path.

    # Find project root
    pyproject = locate_pyproject_toml(source_path.parent)
    if not pyproject:
        print(
            "Error: Could not locate pyproject.toml (project root not found)",
            file=sys.stderr,
        )
        sys.exit(1)

    project_root = pyproject.parent

    # Calculate test file path
    try:
        test_path = calculate_test_file_path(source_path, project_root)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Output results
    if args.verbose:
        print(f"Project root:     {project_root}")
        print(f"Source file:      {source_path}")
        rel_source = source_path.relative_to(project_root)
        print(f"Relative source:  {rel_source}")
        print(f"Test file:        {test_path}")
    else:
        # Just print the test path
        print(test_path)


if __name__ == "__main__":
    main()
