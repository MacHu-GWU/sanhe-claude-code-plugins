---
description: Manage tasks and stories using shai-tix CLI (kanban, tickets, planning)
argument-hint: your task management request
---

Use the `mini-kanban` agent skill to handle the following request:

$ARGUMENTS

**IMPORTANT**: Before doing anything else, run this command first to sync the database:
```bash
uvx --from shai-tix==0.1.3 shai-tix rebuild_index_db
```
