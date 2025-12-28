# mini-kanban

A Claude Code plugin for file-based task management. Manage your project's kanban board using natural language through the `/mini-kanban` slash command.

## Quick Start

```
/mini-kanban create a story for user authentication with 3 tasks
/mini-kanban show me pending tickets
/mini-kanban work on task #3
```

## Features

- **Story & Task Management**: Create, update, and track stories (epics) and tasks
- **Natural Language**: Just describe what you want in plain English
- **File-Based Storage**: All data stored in `.tix/` directory as human-readable files
- **Git-Friendly**: Track task changes alongside your code

## Usage Examples

### Planning Work

```
/mini-kanban create a story "API Refactoring" with tasks for error handling, validation, and testing
```

### Checking Status

```
/mini-kanban what tasks are in progress?
/mini-kanban list stories that are blocked
```

### Working on Tickets

```
/mini-kanban get details for task #5
/mini-kanban mark story 2 as completed with report "All endpoints migrated"
```

### Searching

```
/mini-kanban search tasks about "authentication"
/mini-kanban find all TODO items from last week
```

## How It Works

This plugin uses [shai-tix](https://pypi.org/project/shai-tix/) as the underlying CLI tool. All task data is stored in a `.tix/` directory at your git repository root:

```
your-project/
├── .git/
├── .tix/                    # Task management data
│   ├── index.sqlite         # Search index
│   └── stories/
│       └── story-.../
│           ├── metadata.json
│           ├── description.md
│           ├── report.md
│           └── tasks/
│               └── task-.../
├── src/
└── ...
```

## Status Values

| Status | Description |
|--------|-------------|
| `TODO` | Not started |
| `IN_PROGRESS` | Currently being worked on |
| `COMPLETED` | Finished |
| `BLOCKED` | Blocked by dependencies |
| `CANCELED` | Canceled |

## Requirements

- Python 3.8+ (for shai-tix CLI via uvx)
- No manual installation needed - the plugin uses `uvx` to run shai-tix

## Links

- [shai-tix on PyPI](https://pypi.org/project/shai-tix/)
- [shai-tix Documentation](https://shai-tix.readthedocs.io/)
