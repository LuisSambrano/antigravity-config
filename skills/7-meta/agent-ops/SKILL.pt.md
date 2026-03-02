---
name: agent-ops
description: Meta-skill proactively used to clean, organize, and enforce structural standards within the .agent directory and antigravity-config. Triggers when the user asks to "organize", "clean", or "structure" the agent ecosystem.
version: "1.0.0"
category: "7-meta"
---

---

---

# 🧹 Agent Ops: Workspace Organizer

## What is this Skill?

`agent-ops` is the designated structural custodian of the Antigravity ecosystem. It operates primarily within the `.agent` directory (local) or `antigravity-config` (upstream template).

This skill teaches the agent how to audit the file tree, identify loose files, detect naming convention violations, and automatically reorganize them following the `agent-workspace-standards.md` policy.

## ⚡ SKILL TYPE: PROACTIVE / MAINTENANCE

Activate this sequence automatically when the user issues commands like:

- _"Organize this folder..."_
- _"Clean up the loose files in the agent..."_
- _"Enforce the workspace rules here..."_

## 🛠️ Execution Matrix: `enforce_structure()`

When activated, you must perform the following autonomous steps using your terminal/bash capabilities:

### Step 1: Root Audit

List all files in the root of the targeted `.agent` directory.
Identify any files that are NOT: `README.md`, `INDEX.md`, `install.sh`, `.env`, `.gitignore`.

### Step 2: Categorization & Routing

Using standard `mv` commands, route the orphaned files to their corresponding domain based on the Global Rules:

1. **Move Community/Standard Docs to `/docs`**

   ```bash
   mkdir -p docs
   mv CODE_OF_CONDUCT.md docs/ 2>/dev/null
   mv CONTRIBUTING.md docs/ 2>/dev/null
   mv SECURITY.md docs/ 2>/dev/null
   mv CHANGELOG.md docs/ 2>/dev/null
   mv GEMINI.md docs/ 2>/dev/null
   ```

2. **Move Loose Scripts to `/scripts`**

   ```bash
   mkdir -p scripts
   mv *.py scripts/ 2>/dev/null
   mv *.sh scripts/ 2>/dev/null
   # Exclude install.sh intentionally
   mv scripts/install.sh ./ 2>/dev/null
   ```

3. **Move Orphaned Rules to `/rules`**
   ```bash
   mkdir -p rules
   # If any ad-hoc rules were dumped in root
   ```

### Step 3: Naming Convention Sweep

Review the subdirectories. If you spot CamelCase or spaces, alert the user and propose a `mv` rename to strict `kebab-case`.

### Step 4: Trash Collection

Delete empty temporary files, failed script artifacts (`test.py`, `output.txt`), or `.DS_Store` cache fragments.

### Autonomous Conclusion

Once the `mv` sequences are complete, print a visual tree (`ls -la` or `tree` if available) to the user via the `notify_user` block, demonstrating the newly enforced state.


