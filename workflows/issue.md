---
description: Automates research on a topic and creates a GitHub Issue with the findings.
---

# /issue Workflow

This workflow is triggered when the user types `/issue [topic]`. It automates the process of researching a topic and creating a GitHub Issue with the findings.

## Trigger

- User command: `/issue [topic]`

## Steps

1.  **Extract Topic**: Identify the specific topic or question the user wants to research from the command.
2.  **Research**: Use `search_web` to gather relevant information, official documentation, and context about the topic. Look for technical details, pros/cons, and implementation options.
3.  **Draft Content**: Prepare the issue body using the `research_ticket.md` template structure:
    - **Contexto / Problema**: Briefly explain why this research is needed.
    - **Objetivo**: State what needs to be answered or solved.
    - **Hallazgos**: List key findings from the research.
    - **Conclusión / Solución**: Summarize the recommendation or next steps.
4.  **Create Issue**: Use the `gh` CLI to create the issue.
    - Command: `gh issue create --title "[RESEARCH] [Topic]" --body "[Draft Content]" --label "research"`
    - **Critical**: Ensure the content is properly formatted in Markdown.
5.  **Notify User**: Inform the user that the issue has been created and provide the link.

## Example

**User:** `/issue investigar adopción cripto en Venezuela`

**Agent Action:**

1.  Search web for "adopción cripto Venezuela 2024 data", "uso stablecoins Venezuela", etc.
2.  Draft issue body with stats, sources, and summary.
3.  Run: `gh issue create --title "[RESEARCH] Adopción Cripto en Venezuela" --body "..." --label "research"`
4.  Reply: "Issue creado: https://github.com/LuisSambrano/puente-fintech-dapp/issues/14"
