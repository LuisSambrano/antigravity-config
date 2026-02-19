---
description: Manage Trello boards, lists, and cards from the agent
---

# /trello Workflow

This workflow is triggered when the user types `/trello <action>`. It provides quick access to common Trello operations.

## Trigger

- User command: `/trello <action> [args]`

## Prerequisites

- `TRELLO_API_KEY` and `TRELLO_TOKEN` must be set in environment
- If not set, guide user to https://trello.com/power-ups/admin

## Actions

### `/trello status`

Show an overview of the user's active boards.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh get-boards`
2. Filter out closed boards
3. For each active board, optionally fetch lists to show column counts
4. Present a summary table to the user

### `/trello boards`

List all boards with their IDs for reference.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh get-boards`
2. Format as a clean table: Name | ID | URL

### `/trello lists <boardId>`

Show all lists on a specific board.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh get-lists <boardId>`
2. Format as a table: Name | ID | Position

### `/trello cards <listId>`

Show all cards on a specific list.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh get-cards <listId>`
2. Format as a table: Name | Labels | Due | Members | URL

### `/trello create card <listId> <name> [desc]`

Create a new card on a list.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh create-card <listId> "<name>" "<desc>"`
2. Confirm creation and show the card URL

### `/trello create board <name> [desc]`

Create a new board.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh create-board "<name>" "<desc>"`
2. Confirm creation and show the board URL

### `/trello move <cardId> <targetListId>`

Move a card to another list.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh move-card <cardId> <targetListId>`
2. Confirm the move

### `/trello search <query>`

Search across boards and cards.

1. Run: `bash ~/.agent/skills/10-tools/trello-skill/scripts/trello-ops.sh search "<query>"`
2. Format results as a table with links

### `/trello sync`

Sync project progress with a Trello board.

1. Ask user which board to sync with (or use the most recently referenced board)
2. Fetch the board's lists and cards
3. Compare with local project state (task.md or similar)
4. Suggest card updates or movements based on progress
5. Execute approved changes

## Example

**User:** `/trello status`

**Agent Action:**

1. Fetch boards: `bash scripts/trello-ops.sh get-boards`
2. Present:

```
📋 Tus Boards Activos:
| Board          | Lists | Cards | URL                          |
|----------------|-------|-------|------------------------------|
| Puente MVP     | 5     | 12    | https://trello.com/b/abc123  |
| Antigravity    | 4     | 8     | https://trello.com/b/def456  |
```
