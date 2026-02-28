---
description: Comprehensive project health, CI/CD, and quality status report
---

# /status - Project Status Report

Use this workflow to generate an overview of the project's current health, codebase quality, and repository state.

## Automated Execution Steps

1. **Codebase Quality Check**
   - TypeScript compilation status (errors/warnings)
   - ESLint validation
   - Build execution status

2. **Version Control Audit**
   - Pending working tree changes (uncommitted)
   - Current active branch
   - Synchronization state with remote repository (GitHub)

3. **Performance & Standards Review**
   - Accessibility (a11y) score
   - Core Web Vitals / Navigation performance
   - SEO metadata (if applicable)

4. **Summary Generation**
   - ✅ Optimal elements (Passed checks)
   - ⚠️ Attention required (Warnings/Degradations)
   - 📝 Actionable recommendations

## Usage Context

- Resuming work on a project after a context switch or downtime.
- Auditing the project state before a major refactor or deployment.
- Generating a stakeholder report on technical debt.

## Usage Example

USER: `/status`

AGENT:

```text
📊 Project Status: venezuela-news-app

## ✅ Optimal (5/7)
- TypeScript: 0 errors
- ESLint: 0 errors
- Build: Successful
- Git: Synced with origin/main
- Accessibility: 95/100

## ⚠️ Attention Required (2 items)
- Performance: 78/100 (Oversized hero asset)
- SEO: Missing meta description on `/about`

## 📝 Recommendations
1. Convert hero image to WebP format.
2. Inject meta description tags in `/about` route.

## 🔄 Last Commit
`feat(carousel): add auto-play functionality` (2 days ago)
```
