---
name: trello-ops
description: "Manage Trello boards, lists, and cards for project management. Use when the user asks to create, update, move, or query Trello cards, lists, or boards. Also use for: (1) organizing tasks on Trello boards, (2) moving cards between lists, (3) adding labels, members, or comments to cards, (4) querying board status, (5) syncing project progress with Trello, (6) any task management involving Trello."
---

---

```bash
# List boards
./scripts/trello-ops.sh get-boards

---

```bash
# Verify credentials are set (safe — only checks existence)
[ -n "$TRELLO_API_KEY" ] && echo "API Key: set" || echo "API Key: NOT SET"
[ -n "$TRELLO_TOKEN" ] && echo "Token: set" || echo "Token: NOT SET"
```

```bash
# ❌ NEVER — exposes credentials
echo $TRELLO_API_KEY
echo $TRELLO_TOKEN
printenv | grep TRELLO
```

```bash
# Add to ~/.zshrc
export TRELLO_API_KEY="your_api_key_here"
export TRELLO_TOKEN="your_token_here"
```

---

```bash
# From the skill directory
bash scripts/trello-ops.sh get-boards
```

```bash
# List all boards
bash scripts/trello-ops.sh get-boards

---

```json
{
  "mcpServers": {
    "trello": {
      "command": "npx",
      "args": ["-y", "@anthropic/trello-mcp-server"],
      "env": {
        "TRELLO_API_KEY": "${TRELLO_API_KEY}",
        "TRELLO_TOKEN": "${TRELLO_TOKEN}"
      }
    }
  }
}
```

---

```
Workspace (Organization)
└── Board
    ├── Lists (columns)
    │   └── Cards (tasks)
    │       ├── Labels
    │       ├── Members
    │       ├── Checklists
    │       ├── Comments
    │       ├── Attachments
    │       └── Due dates
    └── Labels (board-scoped)
```

---

---

---

# Trello Skill

Manage Trello boards, lists, cards, labels, and members via REST API or MCP.

## ⚠️ Tool Availability (READ FIRST)

**This skill supports multiple tool backends. Use whichever is available:**

1. **MCP Tools (mcp\_\_trello)** — Use if available in your tool set
2. **Helper Script (`trello-ops.sh`)** — Always available via Bash
3. **Direct `curl`** — Fallback for any operation

**If MCP tools are NOT available**, use the helper script:

# Create a card
./scripts/trello-ops.sh create-card <listId> "Card title" "Description"

# Move a card
./scripts/trello-ops.sh move-card <cardId> <targetListId>
```

**Do NOT report "MCP tools not available" as a blocker** — use the script or curl.

## 🔐 Security: API Credentials

**CRITICAL**: Never expose API keys or tokens in terminal output or context.

### Safe Commands (Always Use)

### Unsafe Commands (NEVER Use)

### Setup

1. Get API Key from https://trello.com/power-ups/admin
2. Generate Token from the API Key page (authorize your app)
3. Add to environment:

## Quick Start

### 1. Verify Setup

Expect: JSON array of your boards.

### 2. Common Operations

# List lists on a board
bash scripts/trello-ops.sh get-lists <boardId>

# List cards on a list
bash scripts/trello-ops.sh get-cards <listId>

# Create a card
bash scripts/trello-ops.sh create-card <listId> "Title" "Description"

# Move a card to another list
bash scripts/trello-ops.sh move-card <cardId> <targetListId>

# Archive a card
bash scripts/trello-ops.sh archive-card <cardId>

# Add a comment
bash scripts/trello-ops.sh add-comment <cardId> "Comment text"

# Add a label
bash scripts/trello-ops.sh add-label <cardId> <color>

# Show help
bash scripts/trello-ops.sh help
```

## Tool Selection

| Tool              | When to Use                            |
| ----------------- | -------------------------------------- |
| **MCP Server**    | Most operations — PREFERRED            |
| **Helper Script** | When MCP unavailable, quick operations |
| **Direct `curl`** | Custom or unsupported operations       |

### MCP Server Configuration

> **NOTE**: Multiple community MCP servers exist (Smithery, Composio). Use whichever is configured.

## Trello Data Model

### Key Concepts

- **Board** = Project or team workspace
- **List** = Column (e.g., "To Do", "In Progress", "Done")
- **Card** = Task or work item
- **Label** = Color-coded category tag

## Conventions

### Card Naming

Use conventional prefixes for clarity:

- `[FEAT]` — New feature
- `[BUG]` — Bug fix
- `[REFACTOR]` — Code refactoring
- `[DOCS]` — Documentation
- `[CHORE]` — Maintenance task

### Standard Board Lists

| List        | Purpose                      |
| ----------- | ---------------------------- |
| Backlog     | Unscheduled work             |
| To Do       | Scheduled for current sprint |
| In Progress | Currently being worked on    |
| In Review   | Code review / QA             |
| Done        | Completed work               |

### Labels (Color Convention)

| Color    | Meaning            |
| -------- | ------------------ |
| `green`  | Low priority       |
| `yellow` | Medium priority    |
| `orange` | High priority      |
| `red`    | Critical / Blocker |
| `purple` | Enhancement        |
| `blue`   | Technical debt     |

## Advanced: Direct API Usage

For operations not covered by the helper script, see [references/api-reference.md](references/api-reference.md) for:

- Full endpoint documentation
- Webhook configuration
- Batch operations
- Custom fields
- Power-Up integration

Base URL: `https://api.trello.com/1/`

Auth params: `?key=${TRELLO_API_KEY}&token=${TRELLO_TOKEN}`

## Reference

| Resource                                        | Purpose                          |
| ----------------------------------------------- | -------------------------------- |
| [api-reference.md](references/api-reference.md) | REST API endpoints and examples  |
| [scripts/trello-ops.sh](scripts/trello-ops.sh)  | CLI helper for common operations |

**External:** [Trello REST API Docs](https://developer.atlassian.com/cloud/trello/rest/)


