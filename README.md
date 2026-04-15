# Antigravity

Agentic configuration system. It enforces code standards, design consistency, and automation through skills and protocols for AI code generation (Gemini, Claude, Cursor).

<p>
  <a href="./readme.md">English</a> •
  <a href="./readme.es.md">Español</a>
</p>

---

## Technical Structure

```text
antigravity/
├── install.sh           # Bootstrap script (~/.gemini/antigravity)
├── docs/                # Knowledge base
├── rules/               # protocol.md (System constraints)
├── skills/              # Context triggers (React, Logic, UI)
└── workflows/           # Execution chains
```

## AI Agent Directives

1. **Read Protocols**: Parse `rules/protocol.md` before resolving tasks.
2. **Context First**: Autonomously load relevant `.md` from `skills/` based on the user's prompt (e.g. `skills/web/design-system` for UI tasks).
3. **DESIGN.md Integrity**: For any frontend work, the agent MUST locate and adhere to the `DESIGN.md` in the project root. If absent, fallback to minimal UI constraints.
4. **Clean Execution**: Commit directly using the Continuous Commit protocol once tests/lint pass.

---

## Installation

```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
chmod +x 01-antigravity/install.sh && ./01-antigravity/install.sh
```

## Security & Ethics
Contains no PII or proprietary code. MIT License.
