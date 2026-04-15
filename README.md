# 🌌 Antigravity Config

**Workspace Configuration Framework for Agentic Software Engineering**

A standardized configuration framework to define architectural constraints, specialized skills, and operational workflows for AI coding agents (Gemini, Claude, Cursor, Windsurf).

<p>
  <a href="./readme.md">English</a> •
  <a href="./readme.es.md">Español</a> •
  <a href="./readme.pt.md">Português</a>
</p>

---

## 🎯 Overview

This repository provides a standardized configuration structure for AI development environments. It ensures code consistency and adherence to architectural standards through three main components:

### Core Components

1. **Rules**: Global architectural constraints applied universally to all agent interactions.
   - *Example*: Enforcing thread-safe patterns or complexity limits.
   - *Location*: `rules/`
2. **Skills**: Specialized knowledge modules for specific domains.
   - *Concept*: Contextual information (e.g., `8-blockchain`) loaded only when relevant to the task.
   - *Format*: Standardized `SKILL.md` files organized by category.
3. **Workflows**: Automated procedures for multi-step tasks.
   - *Mechanics*: Pre-defined sequences for operations like `/deploy` or security audits.

---

## 🌐 Trilingual Support

Main documentation is available in English, Spanish, and Portuguese. Technical skill instructions (`skill.md`) are maintained in English for cross-LLM precision and token efficiency.

---

## 🏗️ Directory Standards

This repository enforces **lowercase kebab-case** for file and directory names to ensure compatibility with CLI tools.

```text
antigravity-config/
├── install.sh           # Installation script
├── docs/                # Project documentation
├── scripts/             # Internal utilities and scripts
├── template/            # Templates for new components
├── rules/               # Global architectural rules
├── skills/              # Domain knowledge (100+ Skills)
└── workflows/           # Automated operational sequences
```

---

## 🛡️ Workspace Maintenance

The `7-meta/agent-ops` skill automates workspace organization:
- Enforces naming conventions.
- Removes unauthorized or temporary files.
- Organizes scattered files into `/scripts` or `/docs`.

---

## 🤖 Guidelines for AI Agents

> [!IMPORTANT]
> Support instructions for AI agents operating within this workspace:

1. **Initialization**: Read `rules/protocol-zero.md` before executing any task.
2. **Context Selection**: Reference `skills/index.md` to identify and load relevant domain skills.
3. **Workflow Execution**: For commands (e.g., `/deploy`), follow the sequence defined in the corresponding `workflows/` file.
4. **Organization**: Store logs and temporary scripts in `/docs` or `/scripts`. Never add orphan files to the root directory.

---

## 🚀 Quick Start (Installation)

1. Clone this repository anywhere:
```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
```

2. Run the bootstrap installer (this configures everything in `~/.gemini/antigravity`):
```bash
chmod +x 01-antigravity/install.sh && ./01-antigravity/install.sh --minimal
```

*Optionally use `--full` to link all 100+ skills.*

---

## 🔒 Security

This architecture template is open-sourced under the MIT License and strictly maintains zero Personal Identifiable Information (PII) or proprietary API keys.

<div align="center">

**Architected and Maintained by [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
