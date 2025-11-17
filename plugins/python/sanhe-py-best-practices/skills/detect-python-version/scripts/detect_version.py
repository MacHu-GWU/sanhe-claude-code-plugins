#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path


def locate_git_repo(dir_cwd: Path) -> Path | None:
    """
    Locate the git repository root directory by searching for the .git folder.
    """
    for _ in range(10):
        if dir_cwd.joinpath(".git").exists():
            return dir_cwd
        dir_cwd = dir_cwd.parent
    return None


def locate_pyproject_toml(dir_cwd: Path) -> Path | None:
    """
    Locate the pyproject.toml file by searching upwards in the directory tree.
    """
    for _ in range(10):
        if dir_cwd.joinpath("pyproject.toml").exists():
            return dir_cwd.joinpath("pyproject.toml")
        dir_cwd = dir_cwd.parent
    return None


def locate_venv_bin_python(dir_cwd: Path) -> Path | None:
    """
    Locate the virtual environment directory by searching for the .venv folder.
    """
    for _ in range(10):
        path_venv_bin_python = dir_cwd.joinpath(".venv", "bin", "python")
        if path_venv_bin_python.exists():
            return path_venv_bin_python
        dir_cwd = dir_cwd.parent
    return None


def get_python_version(path_venv_bin_python: Path) -> tuple[int, int, int]:
    """
    Get the Python version of the specified python executable.
    """
    args = [
        f"{path_venv_bin_python}",
        "--version",
    ]
    res = subprocess.run(args, capture_output=True)
    text = res.stdout.decode("utf-8").strip()
    parts = text.split()[1].split(".")
    return int(parts[0]), int(parts[1]), int(parts[2])


def main():
    dir_here = Path.cwd()
    path_venv_bin_python = locate_venv_bin_python(dir_here)
    if path_venv_bin_python is not None:
        major, minor, micro = get_python_version(path_venv_bin_python)
        py_ver = f"{major}.{minor}"
        print(py_ver)
        return


if __name__ == "__main__":
    main()
