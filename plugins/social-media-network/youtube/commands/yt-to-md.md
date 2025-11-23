---
name: yt-to-md
description: Download, transcribe, and organize YouTube video into structured markdown document
---

Process YouTube video $ARGUMENTS end-to-end and create a well-organized document:

## Workflow

Execute these skills in sequence:

### 1. Download Audio
Use the `youtube-video-to-audio` agent skill to download audio from the provided YouTube URL.

### 2. Transcribe Audio
Use the `transcribe-audio-to-text` agent skill to transcribe the downloaded audio file.

### 3. Clean Up Transcription
Use the `audio-transcription-cleanup` agent skill to transform the raw transcription into a well-structured markdown document.

This step will:
- Detect the primary language and use it for output
- Add semantic paragraph breaks based on topic changes
- Create descriptive section headings
- Fix obvious spelling, terminology, and grammatical errors
- Remove filler words and verbal artifacts
- Maintain all original information from the video

**Output Format:**
```markdown
# [Video Title]

## [Section 1 Heading]

[Cleaned paragraph content...]

[More cleaned content...]

## [Section 2 Heading]

[Content continues...]

## Key Takeaways

- Point 1
- Point 2
- Point 3
```

Save the cleaned document to: `~/tmp/organized_transcript.md`

### 4. Display Output Location

After completing the cleanup and saving the document, print the absolute path of the final organized document in a clickable format.

**Format:** `file:///absolute/path/to/organized_transcript.md`

**Example output:**
```
✓ YouTube video processed successfully!
✓ Organized document saved to: file:///Users/sanhehu/tmp/organized_transcript.md

Click the link above to open the document.
```

**Requirements:**
- Use absolute path (not relative path like `~/tmp/...`)
- Include `file://` protocol prefix for clickability
- Provide clear success message
- Make it easy for user to access the final document

**Note:** This command automates the core workflow from video URL to organized markdown document. Citation enrichment is optional and left to the user's discretion. Each skill can also be run independently for partial workflows.
