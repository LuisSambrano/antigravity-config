---
description: Manage Trello boards, lists, and cards via the API
---

# /trello - Project Management Integration

Use this workflow to interface directly with Trello boards, querying status, creating cards, and syncing project progress without leaving the IDE.

## Prerequisites

- `TRELLO_API_KEY` and `TRELLO_TOKEN` must be configured in the environment.
- Unconfigured states should direct the user to the Trello Admin portal.

## Automated Commands

### Overview & Discovery

- **`/trello status`**: Aggregates and displays active boards, filtering out closed boards, presenting a summary table with column distributions.
- **`/trello boards`**: Lists all available boards with their respective IDs and URLs.
- **`/trello lists <boardId>`**: Retrieves and structures all lists within a designated board by position.
- **`/trello cards <listId>`**: Aggregates all cards within a list, displaying labels, due dates, and member assignments.

### Mutations & Creation

- **`/trello create card <listId> "<name>" "[desc]"`**: Provisions a new card within a list. Returns the canonical URL.
- **`/trello create board "<name>" "[desc]"`**: Initializes a new Trello board. Returns the canonical URL.
- **`/trello move <cardId> <targetListId>`**: Reassigns a card to a different list (e.g., moving from 'In Progress' to 'Done').

### Search & Synchronization

- **`/trello search "<query>"`**: Executes a global search across all boards and cards, returning formatted markdown links.
- **`/trello sync`**: Cross-references the active project state (e.g., local `task.md`) with a specified board, proposing state updates and card movements. Executes approved mutations.

## Usage Example

USER: `/trello status`

AGENT:

```text
📋 Active Boards Overview:

| Board          | Lists | Cards | URL                          |
|----------------|-------|-------|------------------------------|
| Client MVP     | 5     | 12    | https://trello.com/b/abc123  |
| Antigravity    | 4     | 8     | https://trello.com/b/def456  |
```
