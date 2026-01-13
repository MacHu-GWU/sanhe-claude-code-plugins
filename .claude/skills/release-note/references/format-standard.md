# Release Note Format Standard

This document defines the standardized format for release notes in the sanhe-claude-code-plugins repository.

## Overview

All release entries follow a hierarchical structure:
```
plugin -> category -> feature_name
```

## Entry Format

Each entry uses the `@` symbol as separator:

```
{plugin_name}@{category}@{feature_name}
```

### Components

| Component | Description | Examples |
|-----------|-------------|----------|
| `plugin_name` | Name of the plugin (directory name) | `sanhe-py-best-practices`, `mini-kanban`, `youtube`, `tell-me-a-joke` |
| `category` | Type of the feature | `skills`, `slash-commands`, `agents`, `hooks` |
| `feature_name` | Specific feature identifier | `detect-python-version`, `yt-to-md`, `mini-kanban` |

### Valid Categories

- `skills` - Reusable agent skills for domain-specific problems
- `slash-commands` - User-invocable slash commands
- `agents` - Custom subagents for specialized tasks
- `hooks` - Automation hooks

## Change Types

Each release section groups entries by change type:

| Type | Description | Use When |
|------|-------------|----------|
| **Add** | New additions | New plugin, skill, command, agent, or hook |
| **Update** | Modifications to existing features | Behavior change, enhancement, improvement |
| **Fix** | Bug fixes | Correcting errors or unexpected behavior |
| **Remove** | Deletions | Deprecating or removing features |

## RST Template Structure

```rst
x.y.z (YYYY-MM-DD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Add**

- {plugin}@{category}@{feature}: {brief description}

**Update**

- {plugin}@{category}@{feature}: {what changed}

**Fix**

- {plugin}@{category}@{feature}: {what was fixed}

**Remove**

- {plugin}@{category}@{feature}: {reason for removal}
```

## Entry Guidelines

1. **One feature per line** - Each entry represents a single feature change
2. **Brief description** - Optional but recommended, use colon `:` to separate
3. **Alphabetical order** - Within each change type, sort by plugin name
4. **Omit empty sections** - Only include change type headers that have entries

## Examples

### Adding a new skill
```
- sanhe-py-best-practices@skills@python-test-strategy: pytest unit testing patterns
```

### Adding a new slash command
```
- youtube@slash-commands@yt-to-md: YouTube video to markdown converter
```

### Updating an existing feature
```
- mini-kanban@skills@mini-kanban: improved task filtering logic
```

### Fixing a bug
```
- tell-me-a-joke@slash-commands@tell-me-a-joke: fixed encoding issue with non-ASCII characters
```

### Removing a feature
```
- youtube@skills@legacy-downloader: replaced by youtube-video-to-audio
```
