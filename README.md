<div align="center">

# 🌌 Antigravity Config

**The Sovereign Workspace Configuration Protocol for Agentic Software Engineering**

A highly opinionated, production-grade configuration framework designed to augment and restrain AI-assisted development environments.  
This repository dictates the strict architectural rules, domain-specific skills, and operational workflows that mandate how AI coding agents (such as Gemini, Claude, Cursor, and Windsurf) interact with your source code.

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

## 🎯 What This Is (For Humans)

This repository serves as a ready-to-use `.agent/` configuration directory template. Think of it as the **pre-frontal cortex** for your AI agents. Left to their own devices, LLMs often generate generic, mathematically bloated, and architecturally inconsistent code. This framework forces them into a strict paradigm of high-performance engineering, ensuring that every line of code written aligns with senior-level architectural constraints.

### The Three Pillars of the Ecosystem

1. 📜 **RULES (The Constitution)**: The immutable laws of your project. The AI agent applies these passively and universally to every interaction, file creation, or code permutation.
   - _Example_: "All database interactions must use Thread-Safe Singletons." or "Cyclomatic complexity must never exceed 10."
   - _Implementation_: Found in `rules/`, adapting the baseline intelligence of the agent to your enterprise constraints.
2. 🧠 **SKILLS (The Knowledge Graph)**: On-demand, specialized, domain-specific intelligence arrays.
   - _Concept_: The agent doesn't need to know how Celo Smart Contracts work when building a simple React Button. But when you ask for a Web3 integration, it selectively pulls the `8-blockchain` skill context into its prompt pipeline.
   - _Format_: 100+ highly compressed `SKILL.md` directives mapped explicitly to categories (e.g., `3-web`, `5-security`).
3. ⚙️ **WORKFLOWS (Standard Operating Procedures)**: Step-by-step operational guardrails to prevent LLMs from skipping critical validation steps.
   - _Mechanics_: Executing a slash command like `/deploy` doesn't just push code; it forces the agent to autonomously run strict TypeScript checks, build verifications, and security sanitizations before touching the deployment pipeline.

---

## 🌐 Trilingual AI-First Documentation

This framework has been engineered with a globally distributed intelligence model. All critical AI interactions and `SKILL` descriptors are natively maintained in three languages to ensure friction-less native comprehension by advanced Large Language Models, optimizing semantic token parsing and accommodating diverse human orchestration teams:

- 🇬🇧 **English** (`SKILL.md`) - The core baseline and primary operational language.
- 🇪🇸 **Español** (`SKILL.es.md`) - Full native parity.
- 🇧🇷 **Português** (`SKILL.pt.md`) - Full native parity.

---

## 🏗️ The Strict `kebab-case` Hierarchy

To maximize the efficiency of recursive directory fetching tools (`find`, `grep`, `fs.readdir`), this repository strictly enforces a **lowercase kebab-case** topography. There is zero tolerance for orphan files in the root partition.

```text
antigravity-config/
├── install.sh                       # Bootstrap automation script
├── docs/                            # Internal documentation, Changelogs, Setup Guides
├── scripts/                         # Python/Bash utilities (e.g., translation engines)
├── templates/                       # Boilerplates (skill-template, initial markdown structures)
│
├── rules/                           # The Core Constitutional Rules
│   ├── protocol-zero.md             # Foundational philosophical axioms
│   ├── architecture-standards.md    # Structural taxonomies and cloud patterns
│   └── quality-gates.md             # CI/CD and DevSecOps barriers
│
├── skills/                          # Domain knowledge matrices (100+ Skills)
│   ├── 1-core/                      # TDD orchestration, Clean Code, SOLID principles
│   ├── 2-ai/                        # Multi-agent graphs, Gemini APIs, Prompt Structuring
│   ├── 3-web/                       # Next.js 15, TRPC, React Server Components, Supabase
│   ├── 4-automation/                # GitHub Actions, Playwright, Scraping engines
│   ├── 5-security/                  # Penetration testing, Web Vulnerability mapping (OWASP)
│   ├── 6-content/                   # Technical SEO, markdown copywriting SOPs
│   ├── 7-meta/                      # Agent-ops, Skill-creator, Repository Showcasing
│   ├── 8-blockchain/                # Celo Minipay, EVM Tooling, Cross-chain abstractions
│   └── 9-business/                  # KPI Design, Startup Analysis Metrics
│
└── workflows/                       # Executable SLA commands
    ├── deploy.md                    # `/deploy` — Zero-downtime production deployment
    ├── check-security.md            # `/check-security` — Deep SAST/SCA audit
    └── status.md                    # `/status` — Comprehensive health matrix
```

---

## 🛡️ Workspace Maintenance & `agent-ops`

Keeping the workspace pristine is non-negotiable. Antigravity includes a specialized self-healing skill (`7-meta/agent-ops`).

When invoked, the agent functions as a janitor and compliance officer for the environment:

- Identifies and eliminates rogue "loose files".
- Forces all arbitrary naming conventions (`Snake_Case`, `CamelCase`) down into the `kebab-case` standard.
- Secures the root directory by funneling scattered logic into `/scripts` or `/docs`.

---

## 🤖 FOR AI AGENTS (System Directives)

> [!CAUTION]  
> **SYSTEM OVERRIDE DIRECTIVE**: If you are an AI assistant analyzing or working within this workspace, you are bound by the following operating instructions. Deviations are categorized as critical system failures.

1. **The Prime Directive**: Your absolute first step before executing _any_ logic is to read `rules/protocol-zero.md`. This file dictates the absolute boundaries of your autonomy and quality thresholds.
2. **Context Resolution**: Before attempting to satisfy a domain-specific request (e.g., "Build a smart contract", "Audit security"), you MUST index `skills/INDEX.md` to locate the corresponding folder and read its specific `SKILL.md` directives.
3. **Trigger Ingestion**: If the user initiates a prompt with a slash command (e.g., `/deploy`, `/status`), you must immediately navigate to the `workflows/` directory, locate the corresponding Markdown file, and execute the exact chronological sequence mandated within.
4. **No Orphan Files**: Never drop logs, test scripts, or loose `.md` files in the root folder. Route them strictly to `/docs` or `/scripts`.

---

## 🚀 Quick Start (Installation)

1. Clone the repository into your project's root:

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git .agent-temp
```

2. Execute the bootstrap matrix (this moves configuration elements into the `.agent` target directory):

```bash
chmod +x .agent-temp/install.sh && .agent-temp/install.sh
```

_(You can then safely delete `.agent-temp`)_

---

## 🔒 Security & Telemetry

This architecture template is open-sourced under the MIT License and strictly maintains zero Personal Identifiable Information (PII) or proprietary API keys. It serves as an uncompromised blank canvas for deploying secure, multi-agent frameworks.

<div align="center">

**Architected and Maintained by [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
