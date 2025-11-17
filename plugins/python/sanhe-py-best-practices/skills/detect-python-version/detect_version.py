#!/usr/bin/env python3

import subprocess
from pathlib import Path


def main():
    dir_here = Path.cwd()
    path_venv_bin_python = dir_here.joinpath(".venv", "bin", "python")
    if path_venv_bin_python.exists():
        args = [
            f"{path_venv_bin_python}",
            "--version",
        ]
        res = subprocess.run(args, capture_output=True)
        text = res.stdout.decode("utf-8").strip()
        parts = text.split()[1].split(".")
        py_ver = f"{parts[0]}.{parts[1]}"
        print(py_ver)
        return


if __name__ == "__main__":
    main()
