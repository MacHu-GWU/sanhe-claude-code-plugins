# -*- coding: utf-8 -*-

import sys
import os
import urllib.request
import json
from pathlib import Path

# Detect OS
IS_WINDOWS = False
IS_MACOS = False
IS_LINUX = False

_platform = sys.platform
if _platform in ["win32", "cygwin"]:
    IS_WINDOWS = True
elif _platform == "darwin":
    IS_MACOS = True
elif _platform == "linux":
    IS_LINUX = True
else:
    raise RuntimeError(f"Unsupported platform: {_platform}")

dir_home = Path.home()

if IS_WINDOWS:
    filename = "yt-dlp.exe"
    path_yt_dlp = dir_home / "yt-dlp.exe"
elif IS_MACOS:
    filename = "yt-dlp_macos"
    path_yt_dlp = dir_home / "yt-dlp_macos"
elif IS_LINUX:
    filename = "yt-dlp_linux"
    path_yt_dlp = dir_home / "yt-dlp_linux"
else:
    raise RuntimeError("Unsupported operating system")


def get_latest_yt_dlp_release() -> str:
    """Get the latest yt-dlp release version from GitHub API."""
    api_url = "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"

    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())
        tag_name = data["tag_name"]
        return tag_name


def download_yt_dlp() -> Path:
    """Download the appropriate yt-dlp binary based on the OS."""
    # Get latest release version
    latest_version = get_latest_yt_dlp_release()
    print(f"Latest yt-dlp version: {latest_version}")

    # Determine download URL and local path based on OS
    download_url = f"https://github.com/yt-dlp/yt-dlp/releases/download/{latest_version}/{filename}"

    print(f"Downloading {filename} from {download_url}...")
    print(f"Saving to {path_yt_dlp}...")

    # Download the file
    urllib.request.urlretrieve(download_url, path_yt_dlp)

    # Set executable permissions for macOS and Linux
    if IS_MACOS or IS_LINUX:
        os.chmod(path_yt_dlp, 0o755)

    print(f"Successfully downloaded yt-dlp to {path_yt_dlp}")


def main():
    if path_yt_dlp.exists() is False:
        download_yt_dlp()


if __name__ == "__main__":
    main()
