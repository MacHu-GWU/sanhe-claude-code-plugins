# -*- coding: utf-8 -*-

import subprocess
import argparse
from pathlib import Path

dir_home = Path.home()
default_audio_path = dir_home / "tmp" / "download_audio_result.mp3"


def transcribe_audio(path_audio: Path):
    """
    Transcribe an audio file to text using audinota.

    Args:
        path_audio: Path to the audio file to transcribe

    Raises:
        subprocess.CalledProcessError: If audinota transcription fails
    """
    path_audinota = (
        dir_home
        / "Documents"
        / "GitHub"
        / "audinota-project"
        / ".venv"
        / "bin"
        / "audinota"
    )

    if not path_audinota.exists():
        raise FileNotFoundError(f"audinota not found at {path_audinota}")

    if not path_audio.exists():
        raise FileNotFoundError(f"Audio file not found at {path_audio}")

    args = [
        str(path_audinota),
        "transcribe",
        "--input",
        str(path_audio),
    ]

    print(f"Transcribing audio file: {path_audio}")
    subprocess.run(args, check=True)
    print(f"✓ Transcription completed successfully")


def main():
    """
    Main CLI entry point for transcribing audio files to text.

    This script uses audinota to transcribe audio files to text.
    By default, it transcribes the audio file downloaded by the youtube-video-to-audio skill.

    Example usage:
        python transcribe_audio.py
        python transcribe_audio.py --audio-file-path "/path/to/audio.mp3"

    Requirements:
        - audinota must be installed at ~/Documents/GitHub/audinota-project/.venv/bin/audinota
        - Audio file must exist at the specified path
    """
    parser = argparse.ArgumentParser(
        description="Transcribe audio files to text using audinota",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --audio-file-path "/path/to/audio.mp3"
  %(prog)s --audio-file-path "~/Music/podcast.mp3"

Notes:
  - The default audio file path is the output of youtube-video-to-audio skill
  - Requires audinota to be installed at ~/Documents/GitHub/audinota-project/.venv/bin/audinota
        """,
    )

    parser.add_argument(
        "--audio-file-path",
        type=str,
        default=str(default_audio_path),
        help=f"Path to the audio file to transcribe (default: {default_audio_path})",
    )

    args = parser.parse_args()

    # Convert to Path object and expand user home directory
    audio_path = Path(args.audio_file_path).expanduser()

    # Transcribe the audio
    transcribe_audio(path_audio=audio_path)


if __name__ == "__main__":
    main()
