# -*- coding: utf-8 -*-

"""
YouTube Audio Downloader

This module provides functionality to download audio from YouTube videos using yt-dlp.
It supports cross-platform operation (Windows, macOS, Linux) and includes automatic
yt-dlp binary management with built-in protection against overwriting existing files.

Key Features:
    - Download audio from YouTube videos as MP3 files
    - Automatic yt-dlp binary download and updates
    - Cross-platform support (Windows, macOS, Linux)
    - Customizable audio quality and bitrate
    - Default output location with overwrite capability
    - Custom output locations with overwrite protection
    - Automatic directory creation for custom paths

Default Behavior:
    - Output: ~/tmp/download_audio_result.mp3 (allows overwrite)
    - Quality: bestaudio[abr<=64]/worstaudio
    - Format: MP3
    - Bitrate: 64K

Custom Output:
    - Cannot overwrite existing files (raises FileExistsError)
    - Creates parent directories automatically

Example Usage:
    # Download with defaults (allows overwrite)
    $ python download_audio.py --video-url "https://www.youtube.com/watch?v=d6rZtgHcbWA"

    # Custom quality and bitrate
    $ python download_audio.py --video-url "https://youtu.be/xyz" --quality "bestaudio" --bitrate "128K"

    # Custom output location (cannot overwrite existing)
    $ python download_audio.py --video-url "https://youtu.be/xyz" --output "/path/to/audio.mp3"

Requirements:
    - ffmpeg installed at ~/ffmpeg
    - Internet connection for downloading yt-dlp and videos
    - yt-dlp will be automatically downloaded if not present

Platform Support:
    - Windows: Downloads yt-dlp.exe
    - macOS: Downloads yt-dlp_macos
    - Linux: Downloads yt-dlp_linux

Author: sanhe
Plugin: youtube@sanhe-claude-code-plugins
"""

import sys
import os
import json
import subprocess
import urllib.request
import argparse
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
dir_tmp = dir_home / "tmp"
try:
    dir_tmp.mkdir(exist_ok=True)
except Exception: # pragma: no cover
    pass
path_audio = dir_tmp / "download_audio_result.mp3"

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

path_ffmpeg = dir_home / "ffmpeg"


def get_latest_yt_dlp_release() -> str:
    """Get the latest yt-dlp release version from GitHub API."""
    api_url = "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"

    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())
        tag_name = data["tag_name"]
        return tag_name


def download_yt_dlp():
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


def download_audio(
    video_url: str,
    quality: str = "bestaudio[abr<=64]/worstaudio",
    audio_format: str = "mp3",
    bitrate: str = "64K",
    output_path: str = None,
):
    """
    Download audio from a YouTube video using yt-dlp.

    Args:
        video_url: YouTube video URL to download
        quality: yt-dlp quality selector (default: "bestaudio[abr<=64]/worstaudio")
        audio_format: Output audio format (default: "mp3")
        bitrate: Audio bitrate (default: "64K")
        output_path: Custom output path (default: ~/tmp/download_audio_result.mp3)

    Returns:
        Path to the downloaded audio file
    """
    output = output_path if output_path else str(path_audio)

    args = [
        f"{path_yt_dlp}",
        "-f",
        quality,
        "--extract-audio",
        "--audio-format",
        audio_format,
        "--audio-quality",
        bitrate,
        "-o",
        output,
        "--restrict-filenames",
        "--ffmpeg-location",
        f"{str(path_ffmpeg)}",
        video_url,
    ]
    result = subprocess.run(args, check=True, capture_output=True)
    return output


def main():
    """
    Main CLI entry point for downloading YouTube audio.

    This script downloads audio from YouTube videos using yt-dlp and ffmpeg.
    It automatically downloads yt-dlp if not present in the home directory.

    Example usage:
        # Use default output location (allows overwrite)
        python download_audio.py --video-url "https://www.youtube.com/watch?v=d6rZtgHcbWA"

        # Specify custom quality and bitrate
        python download_audio.py --video-url "https://youtu.be/xyz" --quality "bestaudio" --bitrate "128K"

        # Specify custom output location (cannot overwrite existing file)
        python download_audio.py --video-url "https://youtu.be/xyz" --output "/path/to/output.mp3"

    Requirements:
        - ffmpeg must be installed at ~/ffmpeg
        - yt-dlp will be automatically downloaded to home directory if not present

    Note:
        - Default location (~/tmp/download_audio_result.mp3) allows overwrite
        - Custom output locations cannot overwrite existing files
    """
    parser = argparse.ArgumentParser(
        description="Download audio from YouTube videos as MP3 files using yt-dlp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --video-url "https://www.youtube.com/watch?v=d6rZtgHcbWA"
  %(prog)s --video-url "https://youtu.be/xyz" --quality "bestaudio" --bitrate "128K"
  %(prog)s --video-url "https://youtu.be/xyz" --output "/custom/path/audio.mp3"

Quality options:
  bestaudio              - Best quality audio available
  bestaudio[abr<=64]     - Best audio with max 64kbps bitrate
  worstaudio             - Lowest quality audio (smallest file)
        """,
    )

    # Required arguments
    parser.add_argument(
        "--video-url",
        type=str,
        required=True,
        help="YouTube video URL to download (required)",
    )

    # Optional arguments for yt-dlp customization
    parser.add_argument(
        "--quality",
        type=str,
        default="bestaudio[abr<=64]/worstaudio",
        help='Quality selector for yt-dlp (default: "bestaudio[abr<=64]/worstaudio")',
    )

    parser.add_argument(
        "--audio-format",
        type=str,
        default="mp3",
        help="Output audio format: mp3, aac, wav, etc. (default: mp3)",
    )

    parser.add_argument(
        "--bitrate",
        type=str,
        default="64K",
        help="Audio bitrate: 64K, 128K, 192K, 320K, etc. (default: 64K)",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=f"Custom output file path (default: {path_audio}). Note: Default location allows overwrite, custom locations cannot overwrite existing files.",
    )

    args = parser.parse_args()

    # Ensure yt-dlp is downloaded
    if not path_yt_dlp.exists():
        print("yt-dlp not found, downloading...")
        download_yt_dlp()

    # Determine output path and check for existing files
    if args.output:
        path_output = Path(args.output).expanduser()
        # For custom locations, check if file already exists
        if (path_output != path_audio) and path_output.exists():
            raise FileExistsError(
                f"Output file already exists at {path_output}. "
                f"Please choose a different location or remove the existing file. "
                f"(Default location {path_audio} allows overwrite)"
            )
        # Ensure output directory exists
        path_output.parent.mkdir(parents=True, exist_ok=True)
        output_path_str = str(path_output)
    else:
        # Use default location (allows overwrite)
        path_audio.unlink(missing_ok=True)
        output_path_str = None

    # Download the audio
    output_file = download_audio(
        video_url=args.video_url,
        quality=args.quality,
        audio_format=args.audio_format,
        bitrate=args.bitrate,
        output_path=output_path_str,
    )

    print(f"✓ Audio successfully downloaded from {args.video_url}")
    print(f"✓ Saved to: {output_file}")


if __name__ == "__main__":
    main()
