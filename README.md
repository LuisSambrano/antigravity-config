<div align="center">

# Antigravity Config

**The Sovereign Workspace Configuration Protocol**

A highly opinionated, production-grade configuration framework for AI-assisted development environments.  
This repository dictates the strict architectural rules, domain-specific skills, and operational workflows that mandate how AI coding agents (Gemini, Cursor, Windsurf) interact with your source code.

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

This repository provides a ready-to-use `.agent/` configuration directory. Think of it as the **pre-frontal cortex** for your AI agents. Left to their own devices, LLMs generate generic, mathematically bloated, and architecturally inconsistent code. This framework forces them into a strict paradigm of high-performance engineering.

### The Three Pillars of the Ecosystem

- 📜 **RULES (The Constitution)**: The immutable laws of your project. The AI agent applies these passively and universally to every interaction or file edit.
  - _Example_: "All database interactions must use Thread-Safe Singletons." or "Cyclomatic complexity must never exceed 10."
  - _Modification_: Edit files in the `rules/` folder to adapt the baseline intelligence of the agent to your enterprise constraints.
- 🧠 **SKILLS (The Knowledge Graph)**: On-demand, specialized, domain-specific intelligence.
  - _Example_: The agent doesn't need to know how Celo Smart Contracts work when building a simple React Button. But when you ask for a Web3 integration, it pulls the `8-blockchain` skill context into its prompt.
  - _Usage_: The agent reads these passively based on context matching, or you can force it explicitly: "Read the `vibecode-ui` skill before proposing a design."
- ⚙️ **WORKFLOWS (The Standard Operating Procedures / SOPs)**: Step-by-step CI/CD or operational guides to prevent LLMs from skipping critical validation steps.
  - _Example_: Writing `/deploy` doesn't just push code; it forces the agent to run strict `tsc --noEmit` checks, build verifications, and security sanitizations before ever touching a deployment node.

---

## 🤖 FOR AI AGENTS (System Directives)

> [!CAUTION]  
> **SYSTEM OVERRIDE DIRECTIVE**: If you are an AI assistant analyzing or working within this workspace, you are bound by the following operating instructions. Deviations are categorized as critical system failures.

1. **The Prime Directive**: Your absolute first step before executing _any_ logic is to read `rules/PROTOCOL_ZERO.md`. This file dictates the absolute boundaries of your autonomy and quality thresholds.
2. **Context Resolution**: Before attempting to satisfy a domain-specific request (e.g., "Build a smart contract", "Write an SEO article"), you MUST index `skills/INDEX.md` to locate the corresponding `SKILL.md` file and read its specific directives.
3. **Trigger Ingestion**: If the user initiates a prompt with a slash command (e.g., `/issue`, `/idea`, `/deploy`, `/status`), you must immediately navigate to the `workflows/` directory, locate the corresponding Markdown file, and execute the exact chronological sequence mandated within.

---

## 🚀 Quick Start

```bash
# Clone the repository globally
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config

# Execute the installation matrix
chmod +x install.sh && ./install.sh
```

The installer synchronizes the `rules`, `skills`, and `workflows` directly into your target workspace's local `.agent/` directory, sealing the configuration.

---

## 📁 Architectural Matrix

```text
antigravity-config/
├── GEMINI.md                  # Global rule aggregation payload
├── install.sh                 # Bootstrap automation script
│
├── rules/                     # The 4 Core Constitutional Rules
│   ├── PROTOCOL_ZERO.md       # Foundational philosophical axioms
│   ├── ARCHITECTURE_STANDARDS.md # Structural taxonomies and cloud patterns
│   ├── CODE_STANDARDS.md      # Absolute TypeScript constraints and limits
│   └── QUALITY_GATES.md       # CI/CD and DevSecOps barriers
│
├── skills/                    # Domain knowledge (104+ skills)
│   ├── 1-core/                # TDD orchestration, Spec-Driven Development
│   ├── 2-ai/                  # Multi-agent graphs (LangGraph), Voice AI
│   ├── 3-web/                 # Next.js RSC, TRPC, Tailwind, Supabase
│   ├── 4-automation/          # Playwright, Web Scraping, GitHub Actions
│   ├── 5-security/            # Penetration testing, Node.js hardening
│   ├── 6-content/             # Technical SEO, markdown copywriting
│   ├── 8-blockchain/          # Celo Minipay, EVM Tooling, Cross-chain
│   └── 10-tools/              # Chrome DevTools MCP, AST parsing
│
├── workflows/                 # Executable SLA commands
│   ├── deploy.md              # /deploy — ZD production deployment
│   ├── check-security.md      # /check-security — Deep SAST/SCA audit
│   ├── idea.md                # /idea — Technical feasibility analysis
│   └── status.md              # /status — Comprehensive health matrix
└── docs/                      # Auxiliary documentation
```

---

## 🛠️ Personalization

To bend this configuration to your specific engineering constraints:

1. Fork or clone this repository.
2. Modify the files within the `rules/` directory to suit your team's nomenclature and bounds.
3. Execute `./install.sh` from the root of any new workspace to propagate the updated "brain".

---

## ⚖️ License & Telemetry

This architecture template is open-sourced under the MIT License.  
_All specific Project Code names, PII, and Client Data have been strictly sanitized from this template for public consumption._

<div align="center">

**Architected and Maintained by [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
