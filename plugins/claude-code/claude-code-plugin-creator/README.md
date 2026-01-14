# claude-code-plugin-creator

A Claude Code plugin for creating Claude Code plugins. Build Agent Skills and Slash Commands with guided workflows and best practices.

## Quick Start

```
/build-skill create a PDF editor skill that can rotate and merge PDFs
/build-command create a /deploy command that runs deployment scripts
/build-skill-and-command create a skill and command for managing database migrations
```

## Features

- **Agent Skill Creation**: Full-featured skill development with scripts, references, and assets
- **Slash Command Creation**: Custom commands following official Claude Code patterns
- **Combined Workflow**: Create both a skill and its command wrapper in one step
- **Built-in Validation**: Automatic validation and packaging of skills

## Available Commands

| Command | Description |
|---------|-------------|
| `/build-skill` | Create or update an Agent Skill |
| `/build-command` | Create or update a Slash Command |
| `/build-skill-and-command` | Create both a Skill and Command wrapper together |

## Skill Creation Workflow

The plugin guides you through a structured process:

1. **Understand** - Gather requirements and usage examples
2. **Plan** - Identify scripts, references, and assets needed
3. **Initialize** - Generate skill directory structure
4. **Edit** - Implement resources and write SKILL.md
5. **Package** - Validate and create distributable .skill file
6. **Iterate** - Refine based on real usage

## Skill Structure

```
skill-name/
├── SKILL.md              # Required - Instructions and metadata
├── scripts/              # Executable code (Python/Bash)
├── references/           # Documentation loaded as needed
└── assets/               # Templates, images, fonts for output
```

## Included Tools

- `init_skill.py` - Initialize new skill directories
- `package_skill.py` - Validate and package skills for distribution
- `quick_validate.py` - Quick validation checks

## Links

- [Agent Skills Guide](https://code.claude.com/docs/en/skills)
- [Slash Commands Reference](https://code.claude.com/docs/en/slash-commands)
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference)
