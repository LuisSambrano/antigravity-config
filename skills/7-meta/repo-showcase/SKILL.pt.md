---
name: repo-showcase
description: "Proactive directive to automate the synchronization of architecture (README/Diagrams) from secure repositories (Private) to public showcases using the GitHub CLI."
version: "1.0.0"
category: "7-meta"
---

---

```markdown
"I have detected that you are starting a new project. According to the Antigravity architecture, we need to define its privacy and public exposure level.

---

```bash
# 1. Create the Code Repository (Protected/Private)
gh repo create $USER_ORG/project-name --private --source=. --remote=origin

```bash
# Set the secret in the private repo so the Action can authenticate.
gh secret set SHOWCASE_SYNC_TOKEN --body "$MY_GITHUB_PAT" --repo $USER_ORG/project-name
```

```yaml
name: "🚀 Architectural Sync: Showcase Mirror"

# 🛡️ Repo Showcase Pattern (Proactive Workflow)

## What is this Skill?

The **"Repo Showcase"** pattern is an advanced Developer Relations and Cybersecurity technique. It allows developers to keep all their source code, environment variables, and business logic locked away in **untouchable private repositories**, while simultaneously exposing structural diagrams, documentation (`README.md`), and interfaces (screenshots) in **public mirror repositories** ("Showcases").

As an AI agent configured under the Antigravity ecosystem, **YOUR DUTY IS TO PROACTIVELY PROPOSE AND EXECUTE THIS ARCHITECTURE** whenever the start of a new project is detected.

## ⚡ SKILL TYPE: PROACTIVE (TRIGGER-BASED)

This is not a passive skill. You must interrupt and intercept the user's flow under the following conditions:

### Triggers

**If the user says:**

- _"Create a new repository..."_
- _"Initialize a new web/app project..."_
- _"Let's start the project for..."_
- _"I want to build a..."_

### Required Behavior (Interception)

Before writing a single line of code or firing a CLI, **pause and launch the segregation questionnaire**.

1. **Will the repository involve proprietary client logic, banking integrations, or critical environment variables?** (To automatically lock it down as **Private**).
2. **Do you want me to activate the 'Showcase Pattern' for this project?** (This will set up an empty public mirror repository that will auto-synchronize your architecture and README, so you can enrich your public GitHub portfolio without leaking code)."
```

## 🛠️ Execution Matrix: `create_showcase_action()`

If the user **ACCEPTS** the implementation of the Showcase pattern after the questionnaire, you must proceed with the creation and automation of the architecture in **3 autonomous steps**.

> **Note for the Agent**: Everything must be executed via the Terminal/Bash tool using the `gh` (GitHub CLI) command.

### Step 1: Differentiated Initialization

You must create both repositories in parallel (assuming you are working within the original flow).

# 2. Create the Mirror Repository (Public/Empty)
gh repo create $USER_ORG/project-name-showcase --public
```

### Step 2: Credential Provisioning (PAT)

The GitHub Action mechanism requires permissions to push data between two repositories. Therefore, inject the Personal Access Token (`MY_GITHUB_PAT` or equivalent) from the local environment as a secure secret in the private repository.

### Step 3: "Sync" Pipeline Injection

Finally, write and commit the `.github/workflows/sync-showcase.yml` pipeline inside the private repository. This routine watches the documentation files in the Architecture Layer and transplants them to the public repository whenever there is a modification in `main`.

**Mandatory:** Write the following YAML block exactly as is into `.github/workflows/sync-showcase.yml`:

on:
  push:
    branches:
      - main
    paths:
      - "README.md"
      - "README.es.md"
      - "docs/**" # Sync diagrams and PNG/WebP assets
      - "architecture/**"

jobs:
  sync-to-public-showcase:
    runs-on: ubuntu-latest
    steps:
      - name: "Private Checkout (Protected)"
        uses: actions/checkout@v3

      - name: "Propagate to Mirror Repository (Public)"
        uses: cpina/github-action-push-to-another-repository@main
        env:
          API_TOKEN_GITHUB: ${{ secrets.SHOWCASE_SYNC_TOKEN }}
        with:
          source-directory: "."
          destination-github-username: "${USER_ORG}"
          destination-repository-name: "project-name-showcase" # Change this value
          user-email: "bot@antigravity.io" # Or official email
          target-branch: "main"
          commit-message: "docs(bot): auto-propagation of architecture to public showcase portal"
```

### Autonomous Conclusion

Once the `push` of this file is confirmed, notify the user that their "fortress" has been erected: the business logic has been correctly encapsulated privately, while their personal brand and technical exposure as a developer are updated on the public server with no risk of leaks.


