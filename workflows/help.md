---
description: List all available workflows and their purposes
---

# 🆘 /help - Agent Command Menu

Use this command to review available operational workflows and automated skills.

## 🔴 Core Workflows (On-Demand)

| Command               | Definition               | Usage Context                                                                |
| :-------------------- | :----------------------- | :--------------------------------------------------------------------------- |
| **`/status`**         | **Health Check**         | Run upon starting a session to review git, linting, and build integrity.     |
| **`/deploy`**         | **Production Release**   | Trigger deployment pipelines (e.g., Vercel) after security validation.       |
| **`/idea`**           | **Feasibility Analysis** | Evaluate the technical viability of a new concept against the current stack. |
| **`/trello`**         | **Task Management**      | Interface with Trello boards, lists, and sprint management.                  |
| **`/check-security`** | **Security Audit**       | Execute an OWASP Top 10 vulnerability scan on specific components.           |
| **`/issue`**          | **Automated Research**   | Autonomous web research and GitHub issue generation.                         |

## 🧠 Automated Skills (Context-Aware)

> _Skills do not require explicit invocation. The agent activates them based on context._

| Skill                             | Domain   | Activation Trigger                                                   |
| :-------------------------------- | :------- | :------------------------------------------------------------------- |
| **`spec-driven-dev`**             | Core     | Planning complex architectural features from scratch.                |
| **`browser-testing`**             | Tools    | Visual validation, screenshots, or cross-browser debugging required. |
| **`ui-prototyping`**              | Web      | Pre-code UI/UX wireframing requests.                                 |
| **`api-security-best-practices`** | Security | Writing or modifying backend API routes.                             |
| + 90 more skills                  | Various  | Refer to the complete [INDEX.md](../skills/INDEX.md) directory.      |

---

> **Execution Directive:** Simply input the slash command (e.g., `/status`) to initiate the workflow. For skills, state the objective, and the agent will load the optimal toolkit.
