<div align="center">

# Antigravity Config

A configuration framework for AI-assisted development environments.  
Rules, skills, and workflows that standardize how AI coding agents operate across projects.

<p>
  <a href="./README.md">English</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## What This Is

This repository provides a ready-to-use `.agent/` configuration directory for AI coding assistants (Gemini, Cursor, Windsurf, etc.). It acts as the brain and the law for your AI agent, giving it clear boundaries and specialized knowledge to use in your projects.

### The Three Pillars

- **Rules (The Constitution)** — The immutable laws of your project. The AI agent applies these automatically to every file it creates or edits (e.g., "always use strict TypeScript", "follow specific naming conventions"). You modify these in `GEMINI.md` or the `rules/` folder to adapt the agent to your team's preferences.
- **Skills (The Library)** — On-demand specialized knowledge. The agent reads these passively when working on specific topics, or you can explicitly tell it "Read the X skill before doing Y" to give it deep, domain-specific context (105+ skills across 10 categories available).
- **Workflows (The Standard Operating Procedures / SOPs)** — Step-by-step guides for executing complex tasks. This is the most interactive part: you invoke them explicitly using "Slash commands" (like `/deploy`, `/idea`, `/check-security`). Using a workflow ensures the AI agent never skips critical steps when performing multi-stage operations.

The goal is simple: clone once, install, and have a consistent, opinionated development environment where your AI assistant follows professional standards.

---

## 🤖 For AI Agents (How to Read This Repo)

**SYSTEM DIRECTIVE**: If you are an AI assistant analyzing or working within this workspace, follow these operating instructions:

1. **Start Here**: Your first step is ALWAYS to read `rules/PROTOCOL_ZERO.md` to understand the foundational philosophy.
2. **Skill Discovery**: Check `skills/INDEX.md` to find relevant knowledge before writing domain-specific code. If a skill matches the user's request, read its `SKILL.md` file unconditionally.
3. **Workflow Execution**: If you see the user typing a command like `/deploy` or `/idea`, immediately view the corresponding `.md` file in the `workflows/` directory and execute it step-by-step, exactly as written.

---

## Quick Start

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config && chmod +x install.sh && ./install.sh
```

The installer copies rules, skills, and workflows into your workspace's `.agent/` directory and sets up `GEMINI.md` as the global rules file.

---

## Repository Structure

```
antigravity-config/
├── GEMINI.md                  # Global rules template (customize for your needs)
├── install.sh                 # Installer script
│
├── rules/                     # Coding and architecture standards
│   ├── PROTOCOL_ZERO.md       # Core philosophy and principles
│   ├── ARCHITECTURE_STANDARDS.md
│   ├── CODE_STANDARDS.md
│   ├── QUALITY_GATES.md
│   ├── frontend/              # Frontend-specific rules
│   └── backend/               # Backend-specific rules
│
├── skills/                    # Domain knowledge (104+ skills)
│   ├── 1-core/                # Coding fundamentals, TDD, SDD
│   │   └── ...
│   ├── 2-ai/                  # AI agents, RAG, prompting
│   ├── 3-web/                 # Web development (Next.js, React, Tailwind)
│   ├── 4-automation/          # Testing, CI/CD, scraping
│   ├── 5-security/            # API security, pentesting
│   ├── 6-content/             # Technical writing, SEO, comics
│   ├── 7-meta/                # Skill creation and management
│   ├── 8-blockchain/          # Celo, EVM, DeFi
│   ├── 9-business/            # KPIs, market analysis
│   └── 10-tools/              # Docs, presentations, browser testing, Chrome DevTools MCP
│
├── workflows/                 # Agent command scripts
│   ├── deploy.md              # /deploy — production deployment
│   ├── idea.md                # /idea — evaluate project ideas
│   ├── status.md              # /status — project health check
│   ├── trello.md              # /trello — manage Trello boards
│   ├── issue.md               # /issue — research and create GitHub issues
│   └── help.md                # /help — list available commands
│
├── templates/                 # Project templates
├── research/                  # Decision log and key findings
└── docs/                      # Additional documentation
```

---

## Skills Reference

Skills are markdown files that give the AI agent domain-specific knowledge. Each skill contains instructions, patterns, and references the agent uses when working in that domain.

### 1-core — Fundamentals (10 skills)

Coding conventions, project structure standards, TypeScript patterns, TDD orchestration, and **Spec-Driven Development (SDD)** — a methodology for converting ideas into structured specifications before writing code.

### 2-ai — AI & Agents (21 skills)

Multi-agent orchestration (LangGraph, CrewAI), RAG systems, prompt engineering, voice AI development, and agent evaluation frameworks.

### 3-web — Web Development (23 skills)

Next.js App Router patterns, React best practices, Tailwind CSS architecture, Supabase integration, Vercel deployment, UI/UX design principles, and **UI prototyping** workflows.

### 4-automation — Testing & DevOps (10 skills)

Playwright browser testing, GitHub Actions workflows, deployment procedures, and web scraping with Firecrawl.

### 5-security — Security (5 skills)

API security best practices and penetration testing checklists.

### 6-content — Content Creation (7 skills)

Technical writing guidelines, SEO copywriting, documentation standards, and **AI comic generation** with NotebookLM.

### 7-meta — Skill Management (3 skills)

Tools for creating new skills, planning with files, and continuous improvement (Kaizen).

### 8-blockchain — Celo & EVM (19 skills)

Full Celo development stack: MiniPay integration, fee abstraction, stablecoin addresses, Celo Composer scaffolding, viem/wagmi libraries, Hardhat/Foundry tooling, cross-chain bridging, DeFi protocol integration, ERC-8004 agent trust protocol, and x402 HTTP payment protocol.

> See [skills/INDEX.md](./skills/INDEX.md) for the complete skill-by-skill breakdown.

---

## Rules Overview

The rules define how the AI agent writes and validates code. They are loaded into the agent's context and enforced automatically.

| Rule                        | Purpose                                                           |
| --------------------------- | ----------------------------------------------------------------- |
| `PROTOCOL_ZERO.md`          | Core philosophy: quality over speed, local as source of truth     |
| `ARCHITECTURE_STANDARDS.md` | Project structure, component organization, file naming            |
| `CODE_STANDARDS.md`         | TypeScript strict mode, import order, error handling, JSDoc       |
| `QUALITY_GATES.md`          | Pre-commit checks, build verification, accessibility, performance |

---

## Customization

`GEMINI.md` is the main configuration file. It aggregates all rules into a single document that the AI agent reads. Edit it to:

- Add or remove rules
- Change naming conventions
- Adjust quality thresholds
- Add workflow routing for your own commands

Sections marked with `<!-- CUSTOMIZE -->` are designed to be modified.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills, workflows, or rules.

```bash
git checkout -b feature/your-feature
git commit -m 'feat(skills): add new-skill-name'
git push origin feature/your-feature
```

---

## Research & Decision Log

| Document                                      | Purpose                                |
| --------------------------------------------- | -------------------------------------- |
| [KEY_FINDINGS.md](./research/KEY_FINDINGS.md) | Core principles and research findings  |
| [prompts/](./research/prompts/)               | Rule definition prompts and iterations |
| [rules/](./rules/)                            | The resulting standards documents      |

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Maintained by [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
