# Omni-Architect Protocol

**Context**: Global rules for Agentic AI development. Everything boils down to this single file.

## 1. Local Authority
- The local codebase is the ultimate source of truth.
- Do not mutate remote states unless local tests pass.

## 2. Code Quality & Formatting
- **Quality**: Zero tolerance for broken types or lint.
- **Tone**: CommStyle applies. Be direct, no pleasantries, no marketing.
- **Language**: Code is 100% US English. Communication with user can be Spanish.

## 3. Architecture & Security
- **Web**: React/Next.js default. Server components where possible.
- **Security**: Parameterize queries, use RLS (Row Level Security), no hardcoded API keys.
- **Performance**: Optimize images, lazy-load heavy components, avoid N+1 queries.

## 4. UI/UX Standard
- **The Protocol**: All UI generation must defer to the `DESIGN.md` in the workspace root.
- **Fallback**: If no `DESIGN.md` exists, use minimalist glassmorphism, readable contrast, and smooth transitions (scale 0.98 on tap).

## 5. Workflow Automation
- Agents must autonomously verify actions via `npm run lint` or `npm run build` before considering a task done.
- If stuck, debug root causes instead of applying band-aid fixes.
