# 🌌 PROTOCOL ZERO: Antigravity Philosophy

**Version**: 1.0.0
**Status**: IMMUTABLE
**Level**: 0 (Foundational)

---

## 🎯 Purpose

This document defines the **fundamental principles** and **non-negotiable values** of the Antigravity ecosystem. All technical, architectural, and operational decisions must align with these principles.

---

## 🧬 Core Principles

### 1. Playground is the Source of Truth

**Philosophy**: The local environment (`~/playground`) is the origin of all truth. GitHub is merely a cloud mirror.

**Implications**:

- ✅ All changes originate locally.
- ✅ Synchronization is strictly unidirectional: `Local → GitHub`.
- ✅ Local directory names are authoritative.
- ✅ GitHub adapts to the local environment, never the reverse.
- ❌ Never edit directly in the GitHub Web UI (except in extreme emergencies).
- ❌ Never rename local directories to match remote inconsistencies.

**Example**:

```bash
# ✅ CORRECT
cd ~/playground/repos/LuisSambrano/my-project
# Make local changes
git push origin main

# ❌ INCORRECT
# Editing via GitHub Web UI
# Running pull to sync local environment
```

---

### 2. Quality Over Speed

**Philosophy**: Never sacrifice quality for velocity. Broken code is never committed or pushed.

**Implications**:

- ✅ All tests must pass prior to commit.
- ✅ The build process must succeed prior to push.
- ✅ Zero linting errors prior to commit.
- ✅ TypeScript strict mode is mandatory.
- ✅ Mandatory code review (including self or agent-driven reviews).
- ❌ "I'll fix it later" is an unacceptable paradigm.
- ❌ Commits containing TODOs without associated issue tracking are forbidden.
- ❌ Commented-out code without documented justification is forbidden.

**Pre-Commit Checklist**:

```bash
npm run build  # ✅ Must succeed
npm run lint   # ✅ 0 errors
tsc --noEmit   # ✅ 0 type errors
```

---

### 3. Documentation as Code

**Philosophy**: Comprehensive documentation is mandatory. Documentation holds equal weight to the codebase itself.

**Implications**:

- ✅ Bilingual/Trilingual READMEs (EN + ES + PT) are mandatory.
- ✅ System architecture must be visualized via Mermaid diagrams.
- ✅ Inline comments must explain "WHY" the code exists, not "WHAT" it does.
- ✅ `CHANGELOG.md` must be updated on every release.
- ✅ Public APIs must be fully documented using JSDoc.
- ❌ Repositories without a README are unacceptable.
- ❌ Undocumented public functions are strictly forbidden.
- ❌ Undocumented breaking changes are strictly forbidden.

**Example**:

```typescript
/**
 * Fetches user data from Supabase with caching.
 *
 * Uses a 5-minute cache to reduce API calls and improve performance.
 * Cache is invalidated on user updates via Supabase realtime.
 *
 * @param userId - The UUID of the specified user.
 * @returns The User object, or null if not found.
 * @throws {Error} If the Supabase client is uninitialized.
 */
export async function fetchUser(userId: string): Promise<User | null> {
  // Implementation
}
```

---

### 4. Autonomy with Accountability

**Philosophy**: Agents (human or AI) possess decision-making freedom, provided they adhere to the protocol and maintain absolute transparency.

**Implications**:

- ✅ Freedom to select implementation strategies.
- ✅ Strict obligation to adhere to architectural standards.
- ✅ Total transparency regarding automated or manual actions.
- ✅ Mandatory documentation of non-obvious engineering decisions.
- ✅ Obligation to request clarification when confronted with ambiguity.
- ❌ Deviating from protocol without documented justification is forbidden.
- ❌ "Silent" or undocumented architectural shifts are unacceptable.
- ❌ Proceeding on critical assumptions without user verification is forbidden.

**Transparency Example**:

```markdown
## Decision: Implement Zustand overriding Context API

**Rationale**: The global state complexity (>5 slices) rendered Context API
inefficient due to predictable excessive re-renders. Zustand provides superior
performance metrics and developer ergonomics for this specific use case.

**Considered Alternatives**:

- Context API: Discarded due to performance constraints.
- Redux Toolkit: Evaluated as excessive overhead for current scope.
- Jotai: Evaluated as less mature compared to Zustand for this architecture.

**Date**: 2026-02-03
**Author**: Luis Sambrano / Antigravity Agent
```

---

### 5. Continuous Improvement (Kaizen)

**Philosophy**: Every session must leave the codebase demonstrably better than its prior state. Incremental refactoring is a constant requirement.

**Implications**:

- ✅ Refactor adjacent technical debt when interacting with legacy code.
- ✅ Enhance test coverage upon bug discovery.
- ✅ Synchronize documentation actively when altering APIs.
- ✅ Document new technical insights via TIL (Today I Learned) logs.
- ✅ Actively seek to simplify unnecessary complexity.
- ❌ "If it works, don't touch it" is an unacceptable paradigm.
- ❌ Degrading overall code quality is strictly forbidden.
- ❌ Ignoring identified code smells is an unacceptable practice.

**The Boy Scout Rule**:

> "Always leave the codebase cleaner than you found it."

---

## 🔒 Non-Negotiable Values

### 1. Security First

**Mandatory Requirements**:

- ✅ Row Level Security (RLS) enforcement on all Supabase tables.
- ✅ Strict input validation (Zero-trust client model).
- ✅ Output sanitization (XSS prevention).
- ✅ Environment variables are mandatory for all sensitive application secrets.
- ✅ HTTPS enforcement in production environments.
- ❌ Hardcoded secrets are a critical violation.
- ❌ SQL injection vulnerabilities are a critical violation.
- ❌ Authentication endpoints lacking rate limiting are unacceptable.

**RLS Enforcement Example**:

```sql
-- ✅ CORRECT: RLS Enabled and Managed
ALTER TABLE articles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only read published articles"
ON articles FOR SELECT
USING (status = 'published' OR auth.uid() = author_id);

-- ❌ INCORRECT: RLS Disabled
-- Tables lacking policies default to unrestricted access, causing critical data leaks.
```

---

### 2. Accessibility (A11y)

**Mandatory Requirements**:

- ✅ WCAG 2.1 AA compliance (Absolute minimum baseline).
- ✅ Appropriate color contrast ratios (4.5:1 text, 3:1 UI components).
- ✅ 100% functional keyboard navigation.
- ✅ Full Screen Reader compatibility.
- ✅ Strategic deployment of ARIA attributes.
- ❌ Visual elements lacking alternative text definitions are forbidden.
- ❌ Interactive elements without descriptive labels are forbidden.
- ❌ Form inputs lacking explicit association labels are forbidden.

**Implementation Example**:

```tsx
// ✅ CORRECT: Accessible Implementation
<button
  aria-label="Close dialog modal"
  onClick={handleClose}
>
  <X className="h-4 w-4" aria-hidden="true" />
</button>

// ❌ INCORRECT: Inaccessible Implementation
<button onClick={handleClose}>
  <X className="h-4 w-4" />
</button>
```

---

### 3. Performance Excellence

**Mandatory Requirements**:

- ✅ Core Web Vitals must consistently pass.
  - LCP (Largest Contentful Paint): < 2.5s
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1
- ✅ Lighthouse Performance Score: > 90.
- ✅ Optimized bundle sizes via strategic code splitting.
- ✅ Comprehensive image optimization (WebP targeting, lazy loading defaults).
- ❌ Initial load bundles exceeding 500KB without documented justification.
- ❌ Deployment of unoptimized media assets.
- ❌ Predictable, preventable component re-renders.

**Implementation Example**:

```tsx
// ✅ CORRECT: Strategic Lazy Loading
import dynamic from "next/dynamic";

const HeavyDataChart = dynamic(() => import("./HeavyDataChart"), {
  loading: () => <ChartSkeleton />,
  ssr: false,
});

// ❌ INCORRECT: Monolithic Initial Bundle
import { HeavyDataChart } from "./HeavyDataChart";
```

---

### 4. Code Maintainability

**Mandatory Requirements**:

- ✅ Self-documenting code via hyper-descriptive naming conventions.
- ✅ Strict function size limits (< 50 lines per function block).
- ✅ Architectural Separation of Concerns (UI layer isolated from business logic).
- ✅ DRY principles (Don't Repeat Yourself).
- ✅ Uniform consistency in naming, structural patterns, and export methods.
- ❌ Functions exceeding 100 lines.
- ❌ Embedding complex business logic within presentational UI components.
- ❌ Copy-pasting architectural blocks without abstraction.

**Implementation Example**:

```typescript
// ✅ CORRECT: Self-Documenting Naming
function calculateDiscountedPrice(
  originalPrice: number,
  discountPercentage: number,
): number {
  const discountAmount = originalPrice * (discountPercentage / 100);
  return originalPrice - discountAmount;
}

// ❌ INCORRECT: Cryptic Variable References
function calc(p: number, d: number): number {
  return p - p * (d / 100);
}
```

---

### 5. Infinite Scalability

**Mandatory Requirements**:

- ✅ Modular architecture built on isolated feature silos.
- ✅ Explicit demarcation between frontend consumption and backend resolution.
- ✅ Strict API versioning patterns (e.g., v1, v2).
- ✅ Optimized, deliberate database indexing.
- ✅ Strategic, multi-layered caching implementations.
- ❌ Tightly coupled monoliths hindering independent feature deployments.
- ❌ N+1 query structures.
- ❌ Retrieving macro datasets without server-side pagination enforcement.

**Architectural Example**:

```typescript
// ✅ CORRECT: Feature-Driven Modularity
app/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── api/
│   └── articles/
│       ├── components/
│       ├── hooks/
│       └── api/

// ❌ INCORRECT: Generic Type Grouping
app/
├── components/
│   ├── LoginForm.tsx
│   ├── ArticleCard.tsx
│   └── UserProfile.tsx
```

---

## 🚨 Protocol Violations

### Critical Severity (Blocks Deployment)

- Submitting code blocks failing unit or integration tests.
- Committing parameters that result in a failed build sequence.
- Detecting hardcoded secrets within the repository or staging area.
- Introducing identified security vulnerabilities to the codebase.
- Disabling Row Level Security (RLS) in production environments.

### High Severity (Immediate Rectification Required)

- Unresolved linter errors or warnings.
- Unresolved TypeScript compilation errors.
- Lighthouse Performance score falling below 70.
- Lighthouse Accessibility score falling below 90.
- Code duplication ratios exceeding a 10% threshold.

### Medium Severity (Rectification Required Upcoming Sprint)

- Outdated or misleading inline comments.
- Hanging TODO notes lacking associated issue tracking tags.
- Functions approaching or slightly exceeding the 50-line maximum.
- Insufficient public API documentation.

### Low Severity (Backlog/Nice to Have)

- Opportunities for variable nomenclature optimization.
- Non-critical, aesthetic refactoring possibilities.
- Minor computational optimizations.

---

## 📚 Core References

- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Level 1
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Level 1
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Level 1
- [Workflows](../workflows/) - Level 2
