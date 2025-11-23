# -*- coding: utf-8 -*-

import subprocess
import argparse
from pathlib import Path

dir_home = Path.home()
default_audio_path = dir_home / "tmp" / "download_audio_result.mp3"
default_transcript_path = dir_home / "tmp" / "download_audio_result.txt"


def transcribe_audio(path_audio: Path, path_output: Path = None):
    """
    Transcribe an audio file to text using audinota.

    Args:
        path_audio: Path to the audio file to transcribe
        path_output: Path to save the transcript (optional, audinota will use default if not specified)

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

    # Add output argument if specified
    if path_output:
        args.extend(["--output", str(path_output)])

    print(f"Transcribing audio file: {path_audio}")
    subprocess.run(args, check=True)

    output_location = path_output if path_output else "default location"
    print(f"✓ Transcription completed successfully")
    print(f"✓ Saved to: {output_location}")


def main():
    """
    Main CLI entry point for transcribing audio files to text.

    This script uses audinota to transcribe audio files to text.
    By default, it transcribes the audio file downloaded by the youtube-video-to-audio skill.

    Example usage:
        # Use default paths (allows overwrite)
        python transcribe_audio.py

        # Specify custom audio file with default output
        python transcribe_audio.py --audio-file-path "/path/to/audio.mp3"

        # Specify both custom audio and output (cannot overwrite existing file)
        python transcribe_audio.py --audio-file-path "/path/to/audio.mp3" --output "~/Documents/transcript.txt"

    Requirements:
        - audinota must be installed at ~/Documents/GitHub/audinota-project/.venv/bin/audinota
        - Audio file must exist at the specified path

    Note:
        - Default location (~/tmp/download_audio_result.txt) allows overwrite
        - Custom output locations cannot overwrite existing files
    """
    parser = argparse.ArgumentParser(
        description="Transcribe audio files to text using audinota",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --audio-file-path "/path/to/audio.mp3"
  %(prog)s --audio-file-path "~/Music/podcast.mp3" --output "~/Documents/transcript.txt"

Notes:
  - The default audio file path is the output of youtube-video-to-audio skill
  - Default output location (~/tmp/download_audio_result.txt) allows overwrite
  - Custom output locations cannot overwrite existing files
  - Requires audinota to be installed at ~/Documents/GitHub/audinota-project/.venv/bin/audinota
        """,
    )

    parser.add_argument(
        "--audio-file-path",
        type=str,
        default=str(default_audio_path),
        help=f"Path to the audio file to transcribe (default: {default_audio_path})",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=f"Output file path for transcript (default: {default_transcript_path}). Note: Default location allows overwrite, custom locations cannot overwrite existing files.",
    )

    args = parser.parse_args()

    # Convert to Path object and expand user home directory
    audio_path = Path(args.audio_file_path).expanduser()

    # Determine output path and check for existing files
    if args.output:
        path_output = Path(args.output).expanduser()
        # For custom locations, check if file already exists
        if path_output.exists():
            raise FileExistsError(
                f"Output file already exists at {path_output}. "
                f"Please choose a different location or remove the existing file. "
                f"(Default location {default_transcript_path} allows overwrite)"
            )
        # Ensure output directory exists
        path_output.parent.mkdir(parents=True, exist_ok=True)
    else:
        # Use default location (allows overwrite)
        path_output = default_transcript_path
        path_output.unlink(missing_ok=True)

    # Transcribe the audio
    transcribe_audio(path_audio=audio_path, path_output=path_output)


if __name__ == "__main__":
    main()
