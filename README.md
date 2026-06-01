# Antigravity

Agent configuration system. Installs skills, workflows, and rules into any AI coding agent that reads markdown files from a context directory.

Tested with: Google Gemini CLI, Claude Code, Cursor.

[English](./readme.md) · [Español](./readme.es.md)

---

## Structure

```
antigravity/
├── install.sh           # Installer — copies config into the active agent directory
├── AGENT.md             # Global agent rules (copy of template/agent-instructions.md)
├── rules/               # Core protocol — loaded by agent on every session
├── skills/              # Domain modules — loaded by agent based on task context
└── workflows/           # Slash commands — invoked explicitly by the user
```

## How It Works

The installer detects which agent is active based on the `--target` flag and copies the relevant files into the agent's configuration directory. The agent then reads these files at session start or on-demand.

Agents must:
1. Read `rules/protocol.md` before resolving any task.
2. Autonomously load relevant skills from `skills/` based on the user's prompt.
3. Adhere to `DESIGN.md` in the project root for any frontend work. If absent, use the fallback defined in `rules/protocol.md`.
4. Follow the GitOps Continuous Commit protocol after completing tasks.

## Installation

```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
cd 01-antigravity
chmod +x install.sh

# Gemini CLI  →  ~/.gemini/
./install.sh --target gemini

# Claude Code  →  project root CLAUDE.md + .claude/
./install.sh --target claude

# Cursor  →  .cursor/rules/
./install.sh --target cursor
```

## License

MIT. No PII or proprietary code.
