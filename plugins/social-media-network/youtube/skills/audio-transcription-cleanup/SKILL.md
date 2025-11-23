---
name: audio-transcription-cleanup
description: This skill transforms messy voice transcription text into well-formatted, human-readable documents while preserving the original meaning and content.
---

## Key Principles
- **Preserve original meaning**: Do not summarize or omit information
- **Fix transcription artifacts**: Remove filler words, false starts, and repetitions
- **Improve readability**: Organize into proper paragraphs with clear structure
- **Handle multi-speaker content**: Clearly attribute dialogue when multiple speakers are present
- **Enhance document structure**: Add semantic paragraphing and descriptive headings

## When to Use This Skill
Use this skill when the user asks to:
- Clean up voice transcription text
- Format audio/meeting transcripts
- Make transcribed content more readable
- Organize messy spoken-language text
- Polish voice-to-text output

## Processing Instructions

### Step 1: Analyze the Input
First, examine the transcription to identify:
- **Primary language**: Determine the dominant language of the transcription
- **Number of speakers**: Single vs. multi-speaker content
- **Main topics or themes**: Identify distinct topics for sectioning
- **Transcription quality issues**: Filler words, repetitions, false starts, obvious errors

### Step 2: Text Cleanup Operations
Apply the following transformations:

1. **Remove verbal artifacts**:
   - Filler words: "um", "uh", "like", "you know", "呃", "啊", "那个", "就是说", "嗯"
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
   - Use clear speaker labels (Speaker A, B, or actual names if known)
   - Format as dialogue or meeting notes
   - Preserve conversational context

### Step 3: Language and Formatting Guidelines

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

**For multi-speaker content**:
```markdown
# [Meeting/Discussion Title]

## [Topic 1]

**Speaker A:** [清理后的对话内容]

**Speaker B:** [清理后的对话内容]

## [Topic 2]

**Speaker A:** [清理后的对话内容]
```

Or use meeting notes format:
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
- **ADD section headings**: These are structural additions that help readability (not new content)
- **Preserve technical terms and specific names** exactly as intended (fix transcription errors)

## Heading Guidelines
- Section headings should be **concise and descriptive** (3-8 words typically)
- Headings should reflect the **actual content** of each section
- Use appropriate heading levels (H1 for main title, H2 for major sections, H3 for subsections)
- Headings are added to **improve navigation**, not to interpret or editorialize

## Output Format
Create a `.md` (Markdown) file with the cleaned transcription, using appropriate formatting for readability.

## Language Support
This skill works with transcriptions in any language:
- **Chinese** (Mandarin, Cantonese, etc.)
- **English**
- **Mixed language** content (preserve code-switching naturally)
- **Other languages** (apply language-appropriate grammar rules)
