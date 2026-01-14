---
description: Create both an Agent Skill and a Slash Command wrapper in one workflow
argument-hint: <describe the skill and command you want to create>
---

# Build Skill and Command

Create both an Agent Skill and its corresponding Slash Command wrapper in a single workflow.

## Workflow

Execute these steps in order:

### Step 1: Create the Agent Skill

Use the `skill-creator` agent skill to create the Agent Skill based on the request below. Follow all skill creation best practices including understanding requirements, planning resources, initializing, editing, and packaging.

### Step 2: Create the Slash Command Wrapper

After the skill is created, use the `command-creator` agent skill to create a simple Slash Command that wraps the newly created skill. The command should:

- Be placed in `.claude/commands/` with a name matching the skill
- Have a description that reflects what the skill does
- Include an appropriate argument-hint
- Simply delegate to the skill with `$ARGUMENTS`

## Request

$ARGUMENTS
