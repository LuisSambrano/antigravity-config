# 🌌 PROTOCOL ZERO: Antigravity Prime Directive

**Version**: 2.0.0
**Status**: IMMUTABLE
**Level**: 0 (Foundational Doctrine)

---

## 🎯 Purpose

This document enshrines the **unalterable foundational doctrines** and **engineering axioms** of the Antigravity ecosystem. All architectural design, code synthesis, and operational deployment pipelines must derive logically from these axioms.

---

## 🧬 Core Engineering Axioms

### 1. The Local Workspace as the Single Source of Truth (SSOT)

**Philosophy**: The local developer machine (`~/playground`) acts as the absolute Authoritative State. Remote VCS (GitHub) is strictly a passive, downstream artifact mirror.

**Implications**:

- ✅ **Strict Unidirectionality**: State mutations flow exclusively from `Local → Remote`.
- ✅ **Immutable Local Authority**: Directory structures, configurations, and environment variables declared locally supersede any remote drift.
- ❌ **Prohibition of Remote Mutations**: Modifications via GitHub Web UI or remote interventions are classified as critical system violations.
- ❌ **Rebasing Remote Drift**: Remote repositories must be force-pushed to match local state if an unauthorized remote mutation occurs.

---

### 2. Quality as a Gatekeeper (Zero-Defect Tolerance)

**Philosophy**: Velocity is a byproduct of quality, not its replacement. Defective, unoptimized, or untested code is fundamentally blocked from ingestion.

**Implications**:

- ✅ **Automated Gate Enforcement**: Passing CI/CD pipelines is the minimum valid threshold for commit rights.
- ✅ **Strict Concurrency**: Zero TypeScript errors (`tsc --noEmit`), zero ESLint warnings, and flawless builds are non-negotiable compilation requirements.
- ✅ **Defensive Programming**: All IO operations and asynchronous pipelines must handle failure gracefully via isolated error boundaries.
- ❌ **Technical Debt Acceptance**: "Fixing it post-deployment" is an invalid operational paradigm.
- ❌ **Bypassing Gates**: Using `--no-verify` or `// @ts-ignore` without explicit, documented architectural justification is a critical violation.

---

### 3. Documentation as Executable Context

**Philosophy**: Code executes logic; documentation defines intent. Abstract intent must be as rigidly maintained as the execution environments.

**Implications**:

- ✅ **Bilingual Synchronization**: Core architectural documentation must exist flawlessly in English (System Primary) and Spanish (Human Primary).
- ✅ **Architectural Visualization**: Complex system flows must be mapped via code-generated graphs (Mermaid.js).
- ✅ **Teleological Commenting**: Inline annotations explain the _business logic ("Why")_, never the _syntax ("What")_.
- ❌ **Undocumented Mutations**: Publishing API updates or breaking changes without immediate `CHANGELOG.md` and type-definition updates is forbidden.

---

### 4. Autonomous Execution with Absolute Telemetry

**Philosophy**: AI Agents and human operators exercise extreme autonomy in implementation details, bound strictly by total transparency and adherence to Protocol Zero.

**Implications**:

- ✅ **Design Freedom**: Operators may select novel libraries or design patterns if they mathematically or architecturally outperform existing constraints.
- ✅ **Decision Logging**: Every non-trivial architectural pivot (e.g., migrating from Context to Zustand) requires an explicit Architecture Decision Record (ADR) appended to the issue/PR.
- ✅ **Predictable Staging**: Agents must clarify assumptions prior to executing destructive or systemic changes.
- ❌ **Shadow Implementations**: Introducing unapproved paradigms or deviating from the `.agent/rules/` bounds without logged consensus is a critical failure.

---

### 5. Architectural Kaizen (Continuous Iteration)

**Philosophy**: Codebases tend toward entropy. Every interaction must apply negative pressure on technical debt, leaving the requested module measurably superior.

**Implications**:

- ✅ **The Boy Scout Axiom**: Refactor adjacent legacy code, elevate test coverage, and modernize types whenever modifying a module.
- ✅ **Complexity Reduction**: Actively seek out and compress cyclomatic complexity strings.
- ❌ **Stagnation Tolerance**: Preserving poorly written code simply because "it currently executes" is an invalid engineering stance.

---

## 🔒 Enterprise Posture Standards

### 1. Zero-Trust Security Architecture

**Mandatory Enforcement**:

- ✅ **Data Sovereignty**: Row Level Security (RLS) is strictly enforced on all relational databases (Supabase/Postgres). Default state is `DENY ALL`.
- ✅ **Edge Validation**: 100% of ingress payloads must be structurally validated against strict schemas (e.g., Zod) prior to application logic parsing.
- ✅ **Cryptographic Hygiene**: Environment secrets (`.env`) manage all keys. Hardcoded tokens trigger immediate rollback.
- ✅ **Sanitized Egress**: Output contexts must be stripped of executable payloads to neutralize XSS vectors.

---

### 2. Extreme Accessibility (A11y)

**Mandatory Enforcement**:

- ✅ **WCAG 2.1 AA Baseline**: Accessibility is a core operational metric, not a post-launch enhancement.
- ✅ **Screen Reader Matrix**: ARIA tagging, focus-trapping in modals, and logical DOM flows are required.
- ✅ **Contrast Topologies**: 4.5:1 minimum contrast for text; 3:1 for interactive UI boundaries.
- ❌ **Semantic Violence**: Using a `<div>` when a `<button>` or `<nav>` is semantically required is an architectural failure.

---

### 3. High-Fidelity Performance Metrics

**Mandatory Enforcement**:

- ✅ **Core Web Vitals Thresholds**:
  - Largest Contentful Paint (LCP): < 2.5s (Target: < 1.5s via Edge Caching)
  - First Input Delay (FID): < 100ms
  - Cumulative Layout Shift (CLS): 0.00
  - Time to First Byte (TTFB): < 200ms
- ✅ **Bundle Optimization**: Initial JavaScript payloads must be aggressively code-split. Dynamic imports (`next/dynamic`) are mandatory for heavy charting or secondary UI renders.
- ✅ **Asset Delivery**: Media assets are strictly deferred, lazy-loaded, and served in next-gen formats (WebP/AVIF).

---

### 4. Cyclomatic Code Maintainability

**Mandatory Enforcement**:

- ✅ **SOLID Principles**: Single Responsibility architectures isolate UI from business logic completely via Custom Hooks or Services.
- ✅ **Complexity Bounds**: Logic sequences exceeding 50 lines or reaching a cyclomatic complexity index of > 10 must be abstracted and decoupled.
- ✅ **DRY Architecture**: Reusable logic is extracted into `/lib/utils` or `/hooks`; copy-pasting code arrays > 5 lines is forbidden.

---

### 5. Cloud-Native Scalability

**Mandatory Enforcement**:

- ✅ **Stateless Isolation**: Applications must be designed as stateless entities capable of infinite horizontal replication at the Edge.
- ✅ **Data Optimization**: N+1 database queries are strictly prohibited. Joined macros and indexed pagination are mandatory for array resolutions.
- ✅ **Multi-Layer Caching**: Intensive database aggregates must be buffered by Redis or Next.js aggressive Data Cache (ISR) methodologies.
