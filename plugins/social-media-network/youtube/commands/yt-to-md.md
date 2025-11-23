---
name: organize-youtube-video
description: Download, transcribe, and organize YouTube video into structured markdown with citations
args:
  - name: video_url
    description: YouTube video URL to process
---

Process YouTube video end-to-end and create a well-organized document:

## Workflow

Execute these three skills in sequence:

### 1. Download Audio
Use the `youtube-video-to-audio` skill to download audio from ${video_url}

### 2. Transcribe Audio
Use the `transcribe-audio-to-text` skill to transcribe the downloaded audio

### 3. Reorganize Transcript
Read the transcribed content and reorganize it into a well-structured markdown document with the following requirements:

**Structure & Formatting:**
- Detect the primary language of the transcript and use that language for output
- Add semantic paragraph breaks based on topic changes
- Create descriptive section headings (not present in original transcript)
- Fix obvious spelling, terminology, and grammatical errors
- Maintain all original information - do not add content not mentioned in the video

**Citation Enrichment (CRITICAL):**
- Identify all mentions of external sources, research, tools, products, or references
- For each external reference, perform web search to find the authoritative source
- Replace plain text mentions with markdown hyperlinks: `[Title](URL)`
- **Add spaces around hyperlinks** to ensure proper rendering: `text [link](url) text`
- Verify all links are valid and point to the correct source

**Language Handling:**
- Auto-detect source language (English, Chinese, etc.)
- Output in the same language as the source
- Maintain natural expression for the target language
- Adapt to cultural context where appropriate

**Quality Standards:**
- Ensure information accuracy
- Verify all hyperlinks work
- Maintain professional and readable tone
- Keep clear hierarchical structure

**Output Format:**
- Use proper markdown formatting
- Include a brief summary at the top
- Organize content with clear headers (##, ###)
- Use bullet points for lists
- Add hyperlinks with surrounding spaces

Save the final organized document to: `~/tmp/organized_transcript.md`

## Example Output Structure

```markdown
# [Video Title]

**Source:** [Original Video](${video_url})

## Summary
[2-3 sentence summary of the video content]

## [Section 1 Heading]
[Content with proper citations and [hyperlinks](url) ...]

## [Section 2 Heading]
[More content...]

## Key Takeaways
- Point 1
- Point 2
- Point 3
```

### 4. Display Output Location

After completing the reorganization and saving the document, print the absolute path of the final organized document in a clickable format.

**Format:** `file:///absolute/path/to/organized_transcript.md`

**Example output:**
```
✓ YouTube video processed successfully!
✓ Organized document saved to: file:///path/to/home/tmp/organized_transcript.md

Click the link above to open the document.
```

**Requirements:**
- Use absolute path (not relative path like `~/tmp/...`)
- Include `file://` protocol prefix for clickability
- Provide clear success message
- Make it easy for user to access the final document

---

**Note:** This command automates the complete workflow from video URL to organized markdown document. Each skill can also be run independently for partial workflows.
