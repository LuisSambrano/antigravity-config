---
name: sdd-workflow
description: Spec-Driven Development methodology. Use when starting a new feature, project, or complex implementation. Transforms vague ideas into structured specifications before writing code.
---

# Spec-Driven Development (SDD)

> **"Specifications generate code. Code serves specifications."**

## When to Use

- Starting a **new feature** or **new project**
- Planning a **complex implementation** (>5 files, >200 lines)
- User asks to "build...", "create a...", "plan..."
- Before any large-scale code generation

## Core Philosophy

SDD **inverts** the traditional flow: instead of writing code and hoping it matches intent, you write a precise specification **first**, then generate code from it. The spec is the source of truth.

## The 5-Step Flow

```
Constitution → Specify → Clarify → Plan → Tasks → Implement
     ↑            |                    |
     └────────────┴── feedback loop ──┘
```

### Step 1: Constitution (One-time per Project)

Create `.specify/constitution.md` — the immutable principles governing the project.

**Template**: `templates/constitution-template.md`

Key questions:

- What are the quality standards?
- What architectural patterns are mandatory?
- What is the testing strategy?
- What constraints exist (stack, compliance, performance)?

### Step 2: Specify (Per Feature)

Create `specs/[feature-name]/spec.md` — **WHAT** and **WHY**, never HOW.

**Template**: `templates/spec-template.md`

Rules:

- ✅ Focus on user scenarios and acceptance criteria
- ✅ Mark ambiguities with `[NEEDS CLARIFICATION: question]`
- ✅ Prioritize user stories (P1, P2, P3)
- ❌ No tech stack, no code, no architecture

### Step 3: Clarify

Resolve every `[NEEDS CLARIFICATION]` marker before proceeding. Ask the user directly. Do NOT guess.

### Step 4: Plan (Per Feature)

Create `specs/[feature-name]/plan.md` — the technical translation.

**Template**: `templates/plan-template.md`

This is where tech stack, data models, API contracts, and architecture live. Run compliance gates:

- **Simplicity Gate**: ≤3 projects? No future-proofing?
- **Anti-Abstraction Gate**: Using framework directly? No unnecessary wrappers?
- **Test-First Gate**: Contracts defined? Tests written before code?

### Step 5: Tasks + Implement

Create `specs/[feature-name]/tasks.md` — granular, ordered, parallelizable.

**Template**: `templates/tasks-template.md`

Format: `[ID] [P?] [Story] Description`

- `[P]` = can run in parallel
- Organized by user story for independent delivery
- Tests FIRST, then models, then services, then endpoints

## File Structure Created by SDD

```
project/
└── .specify/
    ├── constitution.md          ← Project principles (one-time)
    ├── specs/
    │   └── 001-feature-name/
    │       ├── spec.md          ← Functional specification
    │       ├── plan.md          ← Technical plan
    │       ├── tasks.md         ← Task breakdown
    │       ├── data-model.md    ← Entity definitions
    │       └── contracts/       ← API specs
    └── templates/               ← Reusable templates
```

## Integration with Antigravity

SDD works alongside your existing tools:

- **PROTOCOL_ZERO**: SDD respects all Protocol Zero principles
- **QUALITY_GATES**: The Plan step enforces gates before code generation
- **Skills**: SDD uses existing skills (e.g., `tdd-orchestrator`, `react-patterns`) during implementation
- **Workflows**: After SDD planning, use `/deploy` to ship, `/status` to verify

## Anti-Patterns

- ❌ Jumping to code without a spec
- ❌ Mixing WHAT (spec) with HOW (plan)
- ❌ Guessing when something is ambiguous
- ❌ Over-engineering in the plan (keep it simple)
- ❌ Skipping the constitution for "small" projects

## References

- [github/spec-kit](https://github.com/github/spec-kit) — Original toolkit
- [spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) — Full methodology
