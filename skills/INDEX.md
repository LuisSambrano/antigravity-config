# Antigravity Skills Index
116 unique skills across 10 categories. Zero duplicates.

---

| Category     | Skills | Domain                                        |
| ------------ | ------ | --------------------------------------------- |
| 1-core       | 10     | Fundamentals, quality, TDD, SDD               |
| 10-tools     | 8      | Docs, presentations, Linear, browser, Trello  |
| 2-ai         | 10     | Agents, RAG, prompting, voice, CMS AI         |
| 3-web        | 32     | Frontend, backend, platforms, prototyping     |
| 4-automation | 13     | Testing, CI/CD, n8n, Docker, scraping         |
| 5-security   | 5      | API security, PCI, pentesting, compliance     |
| 6-content    | 7      | Writing, SEO, social, email, comics           |
| 7-meta       | 5      | Agent-ops, skill creation, kaizen             |
| 8-blockchain | 24     | Celo, EVM, DeFi, wallets, stablecoins         |
| 9-business   | 2      | KPIs, market analysis                         |

---

## Rules (`rules/`)

| File                                         | Purpose                                                  |
|----------------------------------------------|----------------------------------------------------------|
| `protocol-zero.md`                           | Foundational doctrine. Level 0, immutable.              |
| `quality-gates.md`                           | CI/CD gates + AI Terminal Gate with security scans.     |
| `architecture-standards.md`                  | Project structure, naming, SOLID principles.            |
| `code-standards.md`                          | TypeScript strict, complexity bounds, error handling.   |
| `workspace-standards.md`                     | Atomic commits, bilingual docs, UI luxury mandates.     |
| `content-standards.md`                       | Content and documentation standards.                    |
| `pre-push-checklist.md`                      | 60-second security gate. Run before every push.         |
| `frontend/nextjs-strict.md`                  | App Router, Server Components, data fetching patterns.  |
| `frontend/nextjs-security-boundaries.md`     | NEXT_PUBLIC_, Server/Client boundary, sensitive fields. |
| `frontend/ui-ux-luxury.md`                   | Glassmorphism, micro-animations, premium threshold.     |
| `backend/supabase-security.md`               | RLS, SSR Auth, schema conventions.                      |

---

## Workflows (`workflows/`)

| Command           | Description                                              |
|-------------------|----------------------------------------------------------|
| `/pre-push`       | Security & quality gate. MANDATORY before every push.   |
| `/check-security` | Full SAST/SCA audit. Run before production deploys.     |
| `/deploy`         | Deploy to Vercel with quality + security checks.        |
| `/status`         | Project health report.                                   |
| `/idea`           | Feasibility evaluation of features or technologies.     |
| `/issue`          | Research + GitHub Issue creation.                       |
| `/til`            | Today I Learned — learning log.                         |
| `/trello`         | Trello board management.                                 |
| `/help`           | List all available workflows.                           |

---

## Changelog

- **v2.1** (2026-03-17): Added `pre-push-checklist.md`, `nextjs-security-boundaries.md`, `/pre-push` workflow. Security Gate Addendum added to `quality-gates.md`. Removed 14 duplicate skill directories.
- **v2.0** (2026-03-09): Global symlink architecture established.
- **v1.0** (2026-03-07): Initial public release.