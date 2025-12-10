# -*- coding: utf-8 -*-

"""
Example usage::

    # Use default output location (allows overwrite)
    python /Users/sanhehu/Documents/GitHub/sanhe-claude-code-plugins/plugins/social-media-network/youtube/skills/enrich-citations/scripts/enrich_citations.py --document-file /Users/sanhehu/tmp/cleaned_transcript.md

    # Specify custom output location (cannot overwrite existing file)
    python /Users/sanhehu/Documents/GitHub/sanhe-claude-code-plugins/plugins/social-media-network/youtube/skills/enrich-citations/scripts/enrich_citations.py --document-file /Users/sanhehu/tmp/cleaned_transcript.md --output ~/Documents/enriched_document.md
"""

import subprocess
import argparse
from pathlib import Path

dir_home = Path.home()
path_enriched_document = dir_home / "tmp" / "citation_enriched.md"

prompt = """
## Task
Enhance the markdown document provided below by finding and adding authoritative source links for all mentioned facts, citations, tools, products, research, and references.

## Key Principles
- **Find authoritative sources**: Search for the original, most credible source for each reference
- **Verify accuracy**: Ensure links point to the correct, current information
- **Preserve content**: Only add hyperlinks, don't change the document's text or meaning
- **Proper formatting**: Use markdown hyperlink syntax with spaces for proper rendering

## Processing Instructions

### Step 1: Identify References

Read through the entire markdown document and identify all mentions of:

1. **External sources and research**:
   - Academic papers, studies, reports
   - Books, articles, blog posts
   - Research findings or statistics

2. **Tools and software**:
   - Applications, frameworks, libraries
   - Programming languages, platforms
   - Development tools, services

3. **Products and services**:
   - Commercial products
   - SaaS platforms
   - Hardware or software products

4. **Organizations and institutions**:
   - Companies, universities
   - Standards bodies, foundations
   - Government agencies

5. **Technical concepts and standards**:
   - Specifications (RFC, W3C, etc.)
   - APIs, protocols
   - Industry standards

6. **People and experts**:
   - Authors, researchers
   - Industry leaders
   - Subject matter experts

### Step 2: Web Search for Sources

For **each identified reference**:

1. **Search for the authoritative source**:
   - Use web search to find the official or most credible source
   - Prioritize: official websites > documentation > reputable publications
   - For academic references: search for DOI, arXiv, official publication

2. **Verify the source**:
   - Ensure the URL is current and accessible
   - Check that content matches the reference
   - Confirm it's the most authoritative source available

3. **Select the best link**:
   - Official documentation or homepage for tools/products
   - Original publication for research/articles
   - Wikipedia for general concepts (if no better source exists)
   - GitHub repository for open source projects

### Step 3: Add Hyperlinks

Replace plain text references with markdown hyperlinks:

**Format:** `[Reference Text](URL)`

**Critical formatting requirements:**
- **Add spaces around hyperlinks**: `text [link](url) text` (not `text[link](url)text`)
- Use descriptive link text (the actual reference name, not "click here")
- Maintain the original sentence structure
- Preserve all other content unchanged

**Examples:**

Before:
```
According to the 2023 Stack Overflow Survey, JavaScript is the most popular language.
```

After:
```
According to the [2023 Stack Overflow Survey](https://survey.stackoverflow.co/2023/) , JavaScript is the most popular language.
```

Before (Chinese):
```
文章提到了GPT-4的能力提升
```

After (Chinese):
```
文章提到了 [GPT-4](https://openai.com/gpt-4) 的能力提升
```

### Step 4: Quality Assurance

Before finalizing:

1. **Verify all links**:
   - Test that URLs are valid and accessible
   - Check for broken links or redirects
   - Ensure HTTPS when available

2. **Check formatting**:
   - Confirm spaces around hyperlinks
   - Verify markdown syntax is correct
   - Ensure links render properly

3. **Review accuracy**:
   - Links point to correct resources
   - No duplicate or conflicting sources
   - All identified references are addressed

## Important Constraints

- **NEVER change the document content**: Only add hyperlinks to existing text
- **NEVER add new information**: Don't insert citations not mentioned in the original
- **NEVER remove existing content**: Preserve all original text
- **NEVER summarize or paraphrase**: Keep exact wording
- **DO add spaces around hyperlinks**: Essential for proper rendering
- **DO verify all sources**: Ensure accuracy and accessibility

## Source Priority Guidelines

When multiple sources exist, prioritize in this order:

1. **Official sources**: Project homepages, official documentation
2. **Primary sources**: Original research papers, first publications
3. **Authoritative organizations**: Standards bodies, academic institutions
4. **Reputable publications**: Well-known tech blogs, news sites
5. **Community resources**: GitHub, Stack Overflow (for code/tools)
6. **General references**: Wikipedia, encyclopedias (as last resort)

## Language Support

This skill works with documents in any language:
- Respect the document's primary language
- Use appropriate sources for the language/region
- Maintain original text while adding hyperlinks
- For multilingual documents, find sources matching each language section when appropriate

## OUTPUT INSTRUCTIONS

**CRITICAL**: Your response must contain ONLY the enhanced markdown document with citations added.

**DO NOT include**:
- Any explanations before the document
- Any explanations after the document
- Any meta-commentary about the enrichment process
- Any acknowledgments like "Here is the enriched version"
- Any markdown code fences (no ```markdown blocks)
- Any introductory or concluding remarks

**START your response immediately with the first line of the document** and **END immediately after the last line**.

Your entire response = the enriched document itself, nothing more.

## INPUT DOCUMENT:
""".strip()


def enrich_citations(path_document: Path):
    """
    Enrich markdown document with authoritative citation links.

    Args:
        path_document: Path to the markdown document file
    """
    # Read document content
    content = path_document.read_text(encoding="utf-8")

    # Call Claude CLI to process the document
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

    # Return the enriched document
    enriched_document = result.stdout
    return enriched_document


def main():
    """
    Main CLI entry point for enriching citations in markdown documents.

    This script enhances markdown documents by finding and adding authoritative
    source links for all mentioned facts, citations, and references.

    Example usage:
        python enrich_citations.py --document-file "/path/to/document.md"

    What it does:
        - Identifies all references (tools, research, products, people, etc.)
        - Performs web search to find authoritative sources
        - Adds markdown hyperlinks with proper spacing
        - Verifies all URLs are valid and current
        - Preserves all original content (only adds links)

    Requirements:
        - Document file must exist
        - Claude CLI must be installed and accessible
        - Internet connection required for web searches
    """
    parser = argparse.ArgumentParser(
        description="Enrich markdown documents with authoritative citation links",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default output location (allows overwrite)
  %(prog)s --document-file "~/tmp/cleaned_transcript.md"

  # Specify custom output location (cannot overwrite existing file)
  %(prog)s --document-file "~/tmp/cleaned_transcript.md" --output "~/Documents/enriched.md"

Citation Enrichment:
  - Identifies facts, tools, products, research, and references
  - Web search to find authoritative sources
  - Adds markdown hyperlinks: [Title](URL)
  - Verifies all links are valid and current
  - Maintains proper spacing around hyperlinks
  - Preserves original document content

Output Behavior:
  - Default location (~/tmp/citation_enriched.md): Allows overwrite
  - Custom location: Cannot overwrite existing files (will raise error)

Note:
  This script uses Claude CLI with web search to perform intelligent citation enrichment.
  All original content is preserved - only hyperlinks are added.
        """,
    )

    parser.add_argument(
        "--document-file",
        type=str,
        required=True,
        help=f"Path to the markdown document to enrich (required)",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=f"Output file path for enriched document (default: {path_enriched_document}). Note: Default location allows overwrite, custom locations cannot overwrite existing files.",
    )

    args = parser.parse_args()

    # Convert to Path objects and expand user home directory
    path_document = Path(args.document_file).expanduser()

    # Determine output path
    if args.output:
        path_output = Path(args.output).expanduser()
        # For custom locations, check if file already exists
        if (path_output != path_enriched_document) and path_output.exists():
            raise FileExistsError(
                f"Output file already exists at {path_output}. "
                f"Please choose a different location or remove the existing file. "
                f"(Default location {path_enriched_document} allows overwrite)"
            )
    else:
        # Use default location (allows overwrite)
        path_output = path_enriched_document

    # Ensure output directory exists
    path_output.parent.mkdir(parents=True, exist_ok=True)

    # Enrich citations in the document
    enriched_document = enrich_citations(
        path_document=path_document,
    )

    # Save to output file
    path_output.write_text(enriched_document, encoding="utf-8")

    # Print success message with clickable file path
    absolute_path = path_output.resolve()
    print(f"✓ Citation enrichment completed successfully!")
    print(f"✓ Enriched document saved to: file://{absolute_path}")
    print(f"\nClick the link above to open the document.")


if __name__ == "__main__":
    main()
