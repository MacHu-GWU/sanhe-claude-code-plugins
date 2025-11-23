# -*- coding: utf-8 -*-

"""
Example usage::

    python /Users/sanhehu/Documents/GitHub/sanhe-claude-code-plugins/plugins/social-media-network/youtube/skills/audio-transcription-cleanup/scripts/audio_transcription_cleanup.py --transcript-file /Users/sanhehu/tmp/download_audio_result.txt
"""

import subprocess
import argparse
from pathlib import Path

dir_home = Path.home()
path_cleaned_transcript = dir_home / "tmp" / "cleaned_transcript.md"

prompt = """
## Task
Transform the messy voice transcription text provided below into a well-formatted, human-readable document while preserving ALL original meaning and content.

## Key Principles
- **Preserve original meaning**: Do not summarize or omit information
- **Fix transcription artifacts**: Remove filler words, false starts, and repetitions
- **Improve readability**: Organize into proper paragraphs with clear structure
- **Handle multi-speaker content**: Clearly attribute dialogue when multiple speakers are present
- **Enhance document structure**: Add semantic paragraphing and descriptive headings

## Processing Instructions

### Step 1: Analyze the Input
Examine the transcription to identify:
- **Primary language**: Determine the dominant language of the transcription
- **Number of speakers**: Single vs. multi-speaker content
- **Main topics or themes**: Identify distinct topics for sectioning
- **Transcription quality issues**: Filler words, repetitions, false starts, obvious errors

### Step 2: Text Cleanup Operations

1. **Remove verbal artifacts**:
   - Filler words: "um", "uh", "like", "you know", "呃", "啊", "那个", "就是说", "嗯", "然后"
   - False starts and self-corrections
   - Unnecessary repetitions

2. **Fix errors and improve accuracy**:
   - **Correct obvious noun errors**: Fix misrecognized names, places, technical terms
   - **Fix spelling mistakes**: Correct typos and transcription errors
   - **Fix grammar errors**: Subject-verb agreement, tense consistency, word order
   - **Clarify ambiguous terms**: Use context to determine correct words when transcription is unclear

3. **Organize content structure**:
   - **Semantic paragraphing**: Group related ideas into logical paragraphs based on meaning
   - **Add section headings**: Create descriptive headings that summarize each section's content
   - Convert spoken fragments into complete sentences
   - Create logical flow between sections

4. **For multi-speaker content**:
   - Use clear speaker labels (Speaker A, B, or actual names if identified)
   - Format as dialogue or meeting notes
   - Preserve conversational context

### Step 3: Language and Formatting

**Language Selection Rules** (in priority order):
1. If user explicitly specifies output language → use that language
2. Otherwise → use the primary language of the original transcription
3. Preserve technical terms and proper nouns in their original language/form

**For single-speaker content**:
```markdown
# [Main Topic Title]

## [Section 1 Heading]

[Cleaned paragraph 1 content...]

[Cleaned paragraph 2 content...]

## [Section 2 Heading]

[Cleaned content...]
```

**For multi-speaker content** - Option 1 (Dialogue format):
```markdown
# [Meeting/Discussion Title]

## [Topic 1]

**Speaker A:** [清理后的对话内容]

**Speaker B:** [清理后的对话内容]

## [Topic 2]

**Speaker A:** [清理后的对话内容]
```

**For multi-speaker content** - Option 2 (Meeting notes format):
```markdown
# [Meeting Title]

## [Discussion Topic 1]

Speaker A mentioned that [cleaned content]...

Speaker B responded by explaining [cleaned content]...

## [Discussion Topic 2]

The group discussed [cleaned content]...
```

## Important Constraints
- **NEVER summarize**: Include all information from original transcription
- **NEVER add new substantive information**: Only reorganize and clarify existing content
- **NEVER change the speaker's meaning or intent**
- **DO add section headings**: These are structural additions that help readability
- **Preserve technical terms and specific names** exactly as intended (fix transcription errors only)

## Heading Guidelines
- Section headings should be **concise and descriptive** (3-8 words typically)
- Headings should reflect the **actual content** of each section
- Use appropriate heading levels (H1 for main title, H2 for major sections, H3 for subsections)
- Headings are added to **improve navigation**, not to interpret or editorialize

## Language Support
This skill works with transcriptions in any language:
- **Chinese** (Mandarin, Cantonese, etc.)
- **English**
- **Mixed language** content (preserve code-switching naturally)
- **Other languages** (apply language-appropriate grammar rules)

## OUTPUT INSTRUCTIONS

**CRITICAL**: Your response must contain ONLY the cleaned markdown document. 

**DO NOT include**:
- Any explanations before the document
- Any explanations after the document
- Any meta-commentary about the cleaning process
- Any acknowledgments like "Here is the cleaned version"
- Any markdown code fences (no ```markdown blocks)
- Any introductory or concluding remarks

**START your response immediately with the H1 title** (# [Title]) and **END immediately after the last content paragraph**.

Your entire response = the cleaned document itself, nothing more.

## INPUT TRANSCRIPTION:
""".strip()


def cleanup_transcript(path_transcript: Path):
    """
    Clean up audio transcription and save to file.

    Args:
        path_transcript: Path to the raw transcript file
    """
    # Read transcript content
    content = path_transcript.read_text(encoding="utf-8")

    # Call Claude CLI to process the transcript
    args = [
        "claude",
        "--append-system-prompt",
        prompt,
        "--print",
        content,
    ]

    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Claude CLI failed: {result.stderr}")

    # Save the cleaned output
    cleaned_transcript = result.stdout
    return cleaned_transcript


def main():
    """
    Main CLI entry point for cleaning up audio transcriptions.

    This script transforms messy voice transcription text into well-formatted,
    human-readable markdown documents while preserving the original meaning.

    Example usage:
        python audio_transcription_cleanup.py --transcript-file "/path/to/transcript.txt"

    What it does:
        - Removes filler words and verbal artifacts (um, uh, like, etc.)
        - Fixes obvious spelling and grammar errors
        - Adds semantic paragraph breaks and section headings
        - Preserves all original information (no summarization)
        - Maintains the speaker's meaning and intent

    Requirements:
        - Transcript file must exist
        - Claude CLI must be installed and accessible
    """
    parser = argparse.ArgumentParser(
        description="Clean up audio transcriptions into well-formatted markdown documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --transcript-file "~/tmp/transcript.txt"

Cleanup Operations:
  - Remove verbal artifacts: um, uh, like, you know, 呃, 啊, 那个
  - Fix spelling and grammar errors
  - Add semantic paragraphs and section headings
  - Convert spoken fragments into complete sentences
  - Preserve all original information

Language Support:
  - auto: Auto-detect from source (default)
  - en: English output
  - zh: Chinese output

Note:
  This script uses Claude CLI to perform intelligent transcript cleanup.
  All original information is preserved - no summarization occurs.
        """,
    )

    parser.add_argument(
        "--transcript-file",
        type=str,
        help=f"Path to the transcript file to clean up",
    )

    args = parser.parse_args()

    # Convert to Path objects and expand user home directory
    path_transcript = Path(args.transcript_file).expanduser()

    # Clean up the transcript
    cleaned_transcript = cleanup_transcript(
        path_transcript=path_transcript,
    )
    print(cleaned_transcript)


if __name__ == "__main__":
    main()
