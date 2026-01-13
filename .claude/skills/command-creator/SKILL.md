---
description: Create custom slash commands for Claude Code
user-invocable: false
---

# Command Creator

Create custom slash commands following the official Claude Code documentation.

## Instructions

Before creating any slash command, read the reference documentation:
- `references/Slash-Commands.md` - Official slash command documentation

When creating multiple slash commands in sequence, reuse the same reference without re-reading.

## Key Points

- Project commands: `.claude/commands/`
- Personal commands: `~/.claude/commands/`
- Use frontmatter for metadata (allowed-tools, description, argument-hint, etc.)
- Use `$ARGUMENTS` for all args or `$1`, `$2` for positional args
- Use `!` prefix for bash execution
- Use `@` prefix for file references
