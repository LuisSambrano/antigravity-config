# Contributing to Antigravity Config

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🌐 Language

- **Code**: English (Variables, Comments, Commits)
- **Documentation**: Mandatory Trilingual Support
  - `README.md` (English - Primary/Source of Truth)
  - `README.es.md` (Spanish)
  - `README.pt.md` (Portuguese)
- **Quality**: Documentation must be "Senior Level" with proper SEO, clear value propositions, and professional structure.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Commit: `git commit -m 'feat: add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📦 Adding a New Skill

### Step 1: Choose the Right Category

| Category       | For Skills Related To            |
| -------------- | -------------------------------- |
| `1-core`       | Essential, always-loaded skills  |
| `2-ai`         | AI agents, prompting, RAG, voice |
| `3-web`        | Frontend, backend, platforms     |
| `4-automation` | Testing, CI/CD, scraping         |
| `5-security`   | Security practices               |
| `6-content`    | Writing, SEO, documentation      |
| `7-meta`       | Skills about creating skills     |

### Step 2: Create Skill Folder

```bash
mkdir skills/2-ai/agents/my-new-skill
```

### Step 3: Add SKILL.md

Every skill **MUST** have a `SKILL.md` file with this structure:

```markdown
---
name: my-new-skill
version: 1.0.0
description: "One-line description (max 80 chars)"
category: 2-ai/agents
tags: [tag1, tag2, tag3]
author: YourGitHubUsername
license: MIT
---

# My New Skill

## When to Use

Describe when this skill should be activated.

## Instructions

Step-by-step instructions for the AI agent.

## Examples

Code examples or usage patterns.

## Resources

- [Link to docs](https://example.com)
```

### Step 4: Update INDEX.md

Add your skill to `skills/INDEX.md` in the appropriate section.

### Step 5: Submit PR

Submit a pull request with:

- Clear description of what the skill does
- Why it's useful
- Example use cases

## 📝 Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]
```

### Types

| Type       | Description                |
| ---------- | -------------------------- |
| `feat`     | New feature or skill       |
| `fix`      | Bug fix                    |
| `docs`     | Documentation only         |
| `style`    | Formatting, no code change |
| `refactor` | Code restructuring         |
| `test`     | Adding tests               |
| `chore`    | Maintenance                |

### Examples

```bash
feat(skills): add langgraph skill for multi-agent orchestration
fix(install): correct symlink path on macOS
docs(readme): add portuguese translation
```

## 🔍 Code Review Process

1. All PRs require at least 1 review
2. Automated checks must pass:
   - SKILL.md exists in skill folders
   - Valid YAML frontmatter
   - No broken links
3. Maintainer will merge once approved

## 💬 Questions?

- Open an [issue](https://github.com/LuisSambrano/antigravity-config/issues)
- Tag with `question` label

---

Thank you for contributing! 🚀
