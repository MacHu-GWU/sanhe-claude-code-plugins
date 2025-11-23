---
name: enrich-citations
description: Add authoritative source links for all facts, citations, and references in markdown documents
---

Enrich a markdown document with authoritative citation links using the `enrich-citations` skill.

## Input

The command accepts a file path as argument:

```
/enrich-citations $ARGUMENTS
```

Where `$ARGUMENTS` is the path to the markdown document to enrich.

## Workflow

### 1. Run the enrich-citations Script

Execute the `enrich-citations` skill script to process the document:

The script will:
- Read the markdown document from the specified path
- Identify all references (tools, research, products, organizations, people, standards)
- Perform web searches to find authoritative sources
- Add markdown hyperlinks with proper spacing: `[Reference](URL)`
- Verify all URLs are valid and accessible
- Save the enriched document to `~/tmp/citation_enriched.md`

### 2. Display Output Location

After the script completes, it will automatically print the absolute path in a clickable format:

```
✓ Citation enrichment completed successfully!
✓ Enriched document saved to: file:///Users/sanhehu/tmp/citation_enriched.md

Click the link above to open the document.
```

## Usage Examples

**Enrich a cleaned transcript:**
```bash
/enrich-citations ~/tmp/cleaned_transcript.md
```

**Enrich any markdown document:**
```bash
/enrich-citations /Users/sanhehu/Documents/article.md
```

**Complete workflow after /yt-to-md:**
```bash
# Step 1: Create organized transcript
/yt-to-md https://www.youtube.com/watch?v=xyz

# Step 2: Optionally enrich with citations
/enrich-citations ~/tmp/cleaned_transcript.md
```

---

**Note:** This command uses the `enrich-citations` skill script which leverages Claude CLI with web search to automatically find and verify authoritative sources for all references in the document.
