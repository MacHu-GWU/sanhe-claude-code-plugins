#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import tomllib
from pathlib import Path


def locate_pyproject_toml(dir_cwd: Path) -> Path | None:
    """
    Locate the pyproject.toml file by searching upwards in the directory tree.
    """
    for _ in range(10):
        if dir_cwd.joinpath("pyproject.toml").exists():
            return dir_cwd.joinpath("pyproject.toml")
        dir_cwd = dir_cwd.parent
    return None


def main():
    dir_here = Path.cwd()
    path_pyproject_toml = locate_pyproject_toml(dir_here)
    data = tomllib.loads(path_pyproject_toml.read_text(encoding="utf-8"))
    package_name = data["project"]["name"]
    package_version = data["project"]["version"]
    dir_project_root = path_pyproject_toml.parent
    dir_package = dir_project_root / package_name
    dir_venv = dir_project_root / ".venv"
    path_venv_bin_python = dir_venv / "bin" / "python"
    path_venv_bin_pip = dir_venv / "bin" / "pip"
    path_venv_bin_pytest = dir_venv / "bin" / "pytest"
    dir_unit_tests = dir_project_root / "tests"
    dir_docs_source = dir_project_root / "docs" / "source"
    path_sphinx_conf_py = dir_docs_source / "conf.py"
    path_makefile = dir_project_root / "Makefile"
    python_project_metadata = {
        "package_name": (package_name, "Package name from pyproject.toml"),
        "package_version": (package_version, "Package version"),
        "dir_package": (str(dir_package), "Main package directory"),
        "path_venv_bin_python": (str(path_venv_bin_python), "virtualenv Python interpreter"),
        "path_venv_bin_pip": (str(path_venv_bin_pip), "virtualenv Pip package manager"),
        "path_venv_bin_pytest": (str(path_venv_bin_pytest), "virtualenv Pytest test runner"),
        "dir_unit_tests": (str(dir_unit_tests), "Unit tests directory"),
        "dir_docs_source": (str(dir_docs_source), "Documentation source"),
        "path_sphinx_conf_py": (str(path_sphinx_conf_py), "Sphinx config file"),
        "path_makefile": (str(path_makefile), "Commands for environment, testing, docs, and releases"),
    }
    print("Python Project Structure:")
    for key, (path, description) in python_project_metadata.items():
        print(f"{key}")
        print(f"  Path: {path}")
        print(f"  Desc: {description}\n")


if __name__ == "__main__":
    main()
