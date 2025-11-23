---
name: enrich-citations
description: Add authoritative source links for all facts, citations, and references in markdown content
---

Process markdown content and enrich it with authoritative citation links:

<input_markdown_content>
$ARGUMENTS
</input_markdown_content>

## Input Processing

The command accepts ARGUMENTS which can be either:

1. **Absolute file path**: If the ARGUMENTS starts with `/`, treat it as a file path
   - Read the markdown content from the specified file
   - Example: `/enrich-citations /Users/sanhehu/Documents/article.md`

2. **Inline content**: If ARGUMENTS is not an absolute path, treat it as inline markdown text
   - Process the text directly
   - Example: `/enrich-citations This article mentions React and TypeScript frameworks.`

## Workflow

### 1. Load Content

- If absolute path provided: Read content from file
- If inline content provided: Use the provided text directly

### 2. Enrich Citations

Use the `enrich-citations` agent skill to process the markdown content:

**Identify all references:**
- External sources and research papers
- Tools, software, frameworks, libraries
- Products and services
- Organizations and institutions
- Technical concepts and standards
- People and experts

**For each identified reference:**
1. Perform web search to find the authoritative source
2. Verify the URL is current and accessible
3. Replace plain text with markdown hyperlinks: `[Reference](URL)`
4. **Add spaces around hyperlinks**: `text [link](url) text`

**Citation priority:**
- Official sources (project homepages, official documentation)
- Primary sources (original research papers, publications)
- Authoritative organizations (standards bodies, academic institutions)
- Reputable publications (tech blogs, news sites)
- Community resources (GitHub, Stack Overflow)
- General references (Wikipedia as last resort)

**Quality requirements:**
- Verify all links are valid and working
- Ensure proper markdown formatting with spaces
- Preserve all original content (only add hyperlinks)
- Maintain document structure and meaning

### 3. Save Output

Save the enriched document to: `~/tmp/citation_enriched.md`

**Example enrichment:**

Input:
```markdown
# Introduction to Modern JavaScript

JavaScript has evolved significantly with ES6 introducing features like arrow functions.
TypeScript adds static typing to JavaScript and is developed by Microsoft.
```

Output:
```markdown
# Introduction to Modern JavaScript

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) has evolved significantly with [ES6](https://www.ecma-international.org/ecma-262/6.0/) introducing features like arrow functions.
[TypeScript](https://www.typescriptlang.org/) adds static typing to JavaScript and is developed by [Microsoft](https://www.microsoft.com/) .
```

### 4. Display Output Location

After completing the enrichment and saving the document, print the absolute path in a clickable format.

**Format:** `file:///absolute/path/to/citation_enriched.md`

**Example output:**
```
✓ Citation enrichment completed successfully!
✓ Enriched document saved to: file:///Users/sanhehu/tmp/citation_enriched.md

Click the link above to open the document.
```

**Requirements:**
- Use absolute path (not relative path like `~/tmp/...`)
- Include `file://` protocol prefix for clickability
- Provide clear success message
- Make it easy for user to access the enriched document

---

## Usage Examples

**Enrich an existing file:**
```bash
/enrich-citations /Users/sanhehu/Documents/article.md
```

**Enrich inline content:**
```bash
/enrich-citations This article discusses React, Next.js, and Vercel deployment.
```

---

**Note:** This command makes citation enrichment quick and accessible. It automatically performs web searches to find authoritative sources and adds verified hyperlinks to the document.
