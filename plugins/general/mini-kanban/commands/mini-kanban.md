---
description: Manage tasks and stories using shai-tix CLI (kanban, tickets, planning)
argument-hint: your task management request
---

Use the `mini-kanban` agent skill to handle the following request:

$ARGUMENTS

**IMPORTANT**: Before doing anything else:
1. Sync the database: `uvx --from shai-tix==0.1.3 shai-tix rebuild_index_db`
2. Get command list: `uvx --from shai-tix==0.1.3 shai-tix -h`
3. Check specific command usage: `uvx --from shai-tix==0.1.3 shai-tix <subcommand> -h`
