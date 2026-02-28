---
description: Automates research on a given topic and creates a structured GitHub Issue
---

# /issue - Automated Research & Issue Generation

Use this workflow to trigger autonomous research on a specific topic. The agent will gather findings and publish them as a structured GitHub Issue for asynchronous tracking.

## Automated Execution Steps

1. **Topic Extraction**: Parse the user's command to identify the specific research objective.
2. **Web Reconnaissance**: Utilize the `search_web` tool to aggregate official documentation, technical specifications, implementation tradeoffs, and relevant context.
3. **Content Structuring**: Draft the issue payload using the standard research template:
   - **Context / Problem**: Rationale for the research.
   - **Objective**: The specific technical question to answer.
   - **Findings**: Bulleted list of technical discoveries.
   - **Conclusion / Solution**: Actionable recommendations.
4. **GitHub Integration**: Execute the `gh` CLI to publish the issue.
   - Command pattern: `gh issue create --title "[RESEARCH] <Topic>" --body "<Draft>" --label "research"`
5. **Confirmation**: Return the generated GitHub Issue URL to the user.

## Usage Context

- Exploring architectural pivots (e.g., "Research migrating from REST to GraphQL").
- Investigating third-party API capabilities before integration.
- Documenting technical debt or emerging vulnerabilities for future sprints.

## Usage Example

USER: `/issue Research Crypto Adoption Metrics in Venezuela 2024`

AGENT:

1. Executes web searches for relevant adoption data and stablecoin usage.
2. Aggregates findings into the markdown template.
3. Executes: `gh issue create --title "[RESEARCH] Crypto Adoption Metrics in Venezuela 2024" ...`
4. Reply: "Issue created successfully: https://github.com/LuisSambrano/puente-fintech-dapp/issues/15"
