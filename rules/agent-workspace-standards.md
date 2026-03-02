# 🛠️ Agent Workspace Standards (.agent)

**Version**: 1.0.0
**Status**: ACTIVE
**Level**: 1 (Core Ecosystem Parameters)

---

## 🎯 Purpose

These directives govern the structural integrity, naming conventions, and file organization of the `.agent` directory (and its base template repository `antigravity-config`). Deep compliance is mandatory to maintain indexation speed, token efficiency, and AI parser compatibility.

---

## 📁 Directory Architecture Rules

The `.agent` workspace must strictly adhere to the following unified directory tree. **No loose files are permitted in the root directory** other than the standard OS files (`.env`, `.gitignore`) and the mandatory `install.sh` / `INDEX.md`.

### Core Directories

- **`/rules`**: Global behavioral and architectural instructions (Markdown).
- **`/workflows`**: Step-by-step procedural playbooks.
- **`/skills`**: Tooling configurations, grouped by numbered categories (e.g., `1-core`).
- **`/docs`**: General project documentation, architectural diagrams, and standard MDs (Contributing, Security).
- **`/scripts`**: Executable bash/python scripts. _Never place scripts inside skill folders directly_.
- **`/templates`**: Boilerplates and configuration templates.
- **`/resources`**: Static assets, prompt libraries, or contextual txt/pdf references.

---

## 🛑 Strict Naming Conventions

### "Kebab-Case" Only

All directories and files within the ecosystem MUST utilize ultra-concise `kebab-case` entirely in English.

- ✅ `bug-hunter`
- ❌ `Bug_Hunter_Skill`
- ✅ `agent-ops`
- ❌ `agent_operations_skill`

### Redependency Ban

Never append redundant suffixes if the parent directory already provides the context.

- ✅ `/skills/7-meta/repo-showcase/SKILL.md`
- ❌ `/skills/7-meta/repo-showcase-skill/repo-showcase-skill.md`

---

## 🧹 Zero Loose Files Policy

Whenever the agent is prompted to "create a file", "save this script", or "write down this rule", the agent must proactively route the file to its corresponding subfolder.

1. **Scripts (`*.sh`, `*.py`, `*.js`)** -> `/.agent/scripts`
2. **Rules (`*.md`)** -> `/.agent/rules`
3. **Drafts / Research** -> `/.agent/research`
4. **General Docs** -> `/.agent/docs`

Any execution, script, or test that generates temporary logs or files must clean up after itself. If a script (e.g., `translate.py`) fails, the agent must execute `rm translate.py` immediately to prevent root clutter.
