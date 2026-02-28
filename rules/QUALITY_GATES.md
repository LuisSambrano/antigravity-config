# ✅ Antigravity Quality Gates

**Version**: 1.0.0
**Status**: MANDATORY
**Level**: 1 (Quality Assurance - Transversal)

---

## 🎯 Purpose

This document dictates the **mandatory quality gates** automatically enforced throughout the development lifecycle. These gates unify all localized QA workflows into automated checklists.

**Origin**: Condenses `auto-qa.md` and auxiliary quality workflows.

---

## 🚦 Quality Gates (By Lifecycle Stage)

### 1. Pre-Code Gate (Initialization Phase)

**Trigger**: Prior to the creation or modification of any source code file.

**Automated Validations**:

#### Workspace Architecture

- [ ] ✅ Project root contains the `.agent/` directory.
- [ ] ✅ `.agent/rules/architecture.md` exists.
- [ ] ✅ Bilingual README configuration (`README.md`, `README.es.md`) exists.
- [ ] ✅ `.gitignore` array is fully configured.

#### TypeScript Compiler

- [ ] ✅ `tsconfig.json` exists.
- [ ] ✅ `"strict": true` is explicitly enabled.
- [ ] ✅ `"noUncheckedIndexedAccess": true` is explicitly enabled.

#### ESLint Linter

- [ ] ✅ `.eslintrc.json` or `eslint.config.js` exists.
- [ ] ✅ Strict TypeScript rulesets are active.

**Failure Action**: Automatically provision missing configuration files.

---

### 2. During-Code Gate (Active Development Phase)

**Trigger**: Actively evaluated during code generation or manual modification.

**Automated Enforcements**:

#### Naming Conventions

- ✅ Components: `PascalCase.tsx`
- ✅ Utilities: `camelCase.ts`
- ✅ Hooks: `use*.ts`
- ✅ Types: `*.types.ts`
- ✅ Variables: `camelCase`
- ✅ Constants: `SCREAMING_SNAKE_CASE`
- ✅ Functions: `camelCase` (verb-led definitions)
- ✅ Booleans: `is*`, `has*`, `can*`

#### Import Topology

```typescript
// 1. React Runtime
import React from "react";

// 2. Vendor Dependencies (e.g., node_modules)
import { motion } from "framer-motion";

// 3. Internal Application Aliases
import { Button } from "@/components/ui/button";

// 4. Type Declarations
import type { User } from "@/types/user.types";

// 5. CSS Stylesheets
import "./styles.css";
```

#### TypeScript Integrity

- ✅ The `any` type is strictly forbidden.
- ✅ `interface` used for public object topologies.
- ✅ `type` used for unions.
- ✅ Generics are contextually descriptive.

#### Error Handling Paradigms

- ✅ `try-catch` structures mandatory for all asynchronous operations.
- ✅ Error logging must include systemic context.
- ✅ Failures are returned as objects (No `throw` operations in production payloads).

#### Comment Syntax

- ✅ Comments document "WHY", never "WHAT".
- ✅ JSDoc formatting is mandatory for public/exported functions.
- ✅ Code syntax is strictly English; complex architectural annotations are localized (Spanish).

**Failure Action**: Trigger local block or warn developer prior to save operations.

---

### 3. Post-Code Gate (Compilation Phase)

**Trigger**: Immediately following file ingestion/modification.

**Automated Validations**:

#### TypeScript Type Integrity Check

```bash
# turbo execution
tsc --noEmit
```

**Assertion**: 0 type errors.

#### ESLint Diagnostics

```bash
# turbo execution
npx eslint . --ext .ts,.tsx --max-warnings 0
```

**Assertion**: 0 errors, 0 warnings.

#### Build Verification

```bash
# turbo execution
npm run build
```

**Assertion**: Success without compilation errors.

**Failure Action**: Hard-block Git commit operations. Propagate critical errors to the user.

---

### 4. Pre-Commit Gate (Version Control Phase)

**Trigger**: Intercepts `git commit` operations.

**Automated Validations**:

#### Git Staging Diagnostics

```bash
# turbo execution
git status
```

**Required State**:

- [ ] ✅ `.env` configurations absent from the staging area.
- [ ] ✅ Hardcoded secrets completely absent.
- [ ] ✅ Asset sizes > 10MB absent from the staging area.
- [ ] ✅ `.gitignore` effectively blocking `node_modules/`, `.env*`, and `.DS_Store`.

#### Conventional Commits Formatting

```bash
# Mandatory structural pattern
<type>(<scope>): <description>

# Validated types
feat, fix, refactor, style, docs, test, chore
```

**Formatting Examples**:

- ✅ `feat(auth): implement SSR authentication`
- ✅ `fix(ui): correct dark mode contrast ratios`
- ❌ `updated auth stuff`
- ❌ `fix bug`

#### Production Code Integrity

- [ ] ✅ `console.log` statements stripped from production code.
- [ ] ✅ Zero `TODO` annotations lacking GitHub issue association.
- [ ] ✅ Zero orphaned or commented-out code blocks lacking clear justification.
- [ ] ✅ Zero unused imports.

**Failure Action**: Abort Git commit. Output required rectifications.

---

### 5. Pre-Deploy Gate (CI/CD Pipeline Phase)

**Trigger**: Actively evaluated prior to production/staging deployment.

**Automated Validations**:

#### Testing Architecture

```bash
# turbo execution
npm run test
```

**Assertion**: 100% test pass rate.

#### Cloud Environment Verification

- [ ] ✅ `.env.example` is fully synchronized with required dependencies.
- [ ] ✅ Required variables are thoroughly documented.
- [ ] ✅ Zero secrets leaked into `.env.example`.

#### Database Schemas (If Applicable)

- [ ] ✅ Forward migrations verified and applied.
- [ ] ✅ RLS policies heavily audited for gaps.
- [ ] ✅ Data indexing validated for high-frequency queries.

#### Security Baseline

- [ ] ✅ Outdated dependencies pruned (`npm audit`).
- [ ] ✅ Zero critical CVE vulnerabilities remaining.
- [ ] ✅ HTTPS rigidly configured across all routes.

**Failure Action**: Hard-block deployment pipeline. Route issue to engineer.

---

### 6. Pre-Delivery Gate (Agent Output Phase)

**Trigger**: Fired immediately prior to invoking the `notify_user` system tool.

**Automated Validations**:

#### Full System Summary Execute

```bash
tsc --noEmit && \
npx eslint . --ext .ts,.tsx --max-warnings 0 && \
npm run build
```

#### Content Quality Assertions (If Generating Text)

**For Article/Documentation Targets**:

- [ ] ⚠️ Total word count ≥ 800 boundaries.
- [ ] ⚠️ Linear Heading Topology: H1 → H2 → H3 (No structural jumps).
- [ ] ⚠️ Syntax highlighting injected on all code blocks.
- [ ] ⚠️ Hyperlinks are descriptive, validated, and resolving.

**For UI Component Targets**:

- [ ] ⚠️ Viewport responsiveness verified across 4 matrices (375px, 768px, 1024px, 1440px).
- [ ] ⚠️ Dark mode color inversions functionally operate.
- [ ] ⚠️ End-to-end Accessibility parameters met (Alt Text, ARIA bounds, minimum 4.5:1 contrast, keyboard navigation flow).

#### Performance Benchmarks

**Core Web Vitals Thresholds**:

- [ ] ✅ LCP (Largest Contentful Paint) < 2.5s
- [ ] ✅ FID (First Input Delay) < 100ms
- [ ] ✅ CLS (Cumulative Layout Shift) < 0.1

**Lighthouse Benchmarks**:

- [ ] ✅ Performance ≥ 90
- [ ] ✅ Accessibility ≥ 95
- [ ] ✅ Best Practices ≥ 90
- [ ] ✅ SEO ≥ 95

#### Git Hygiene Confirmation

```bash
# turbo execution
git status
```

**Required State**:

- [ ] ✅ Working tree clean (all necessary changes fully committed).
- [ ] ✅ Branch aligned with remote origin.

**Action**: Aggregates data and autonomously generates the QA status payload.

---

## 📊 Autogenerated QA Reporting Schema

### Format Template

```markdown
## 🔍 Quality Assurance Report

**Timestamp**: 2026-02-03  
**Target Repository**: venezuela-news-app  
**Active Branch**: feature/new-carousel

---

### ✅ Optimal Integrity (X/Y checks passed)

- TypeScript: 0 errors
- ESLint: 0 errors, 0 warnings
- Build Compilation: Success
- Git Status: Clean
- Commit Nomenclature: ✅
- Accessibility Score: 98/100
- Performance Score: 95/100

---

### ⚠️ Attention Required (X non-fatal items)

- **SEO**: Meta description data missing on the `/about` route.
- **Performance**: High-resolution image asset on `/home` bypasses WebP optimization bounds (1.2MB).
- **Content Density**: Article payload word count registers at 650 (Target: 800+).

---

### ❌ Fatal Breaches (X critical violations)

- **Security Override**: Stray `.env` configuration file detected within the Git staging tree.
- **TypeScript Core**: 3 distinct type violations mapped to `components/ArticleCard.tsx`.

---

### 📝 Actionable Recommendations

1. **Optimize Image Assets**: Throttle homepage hero asset to WebP parameters and enforce late/lazy loading.
2. **Expand Data Density**: Append >150 words of targeted content to clear article validation matrix.
3. **Patch SEO Routing**: Inject meta description tags to address the `/about` page degradation.
4. **Isolate Env Variables**: Promptly unstage the `.env` file and append the target to `.gitignore` rules.

---

### 🎯 Iterative Next Steps

1. Remediate Critical/Fatal Breaches (❌).
2. Triage and integrate Warning advisories (⚠️).
3. Re-trigger automated QA cycle.
4. Advance to Delivery state.
```

---

## 🚨 Severity Threat Matrices

### Critical Severity (❌) - Blocks Deployment/Delivery

- Failed Build compilations.
- Fatal TypeScript routing errors.
- ESLint terminal state errors.
- Exposed hardcoded security secrets.
- Overriding or disabling production Database RLS.
- Lighthouse Performance metrics dropping < 70 points.

**Automated Action**: Total procedure halt. Refusal to proceed without resolution.

### High Severity (⚠️) - Demands Immediate Triage

- Active ESLint warnings.
- Lighthouse metric degradation < 90 points.
- Lighthouse Accessibility degradation < 95 points.
- Monolithic functional drift (functions spanning > 50 lines).
- Missing critical HTML alt text/ARIA structures.

**Automated Action**: Flag issues directly to engineer. Resolve proactively prior to delivery whenever technically feasible.

### Medium Severity (📝) - Advisory Recommendations

- Hanging TODO strings lacking issue topology.
- Variable nomenclature that degrades self-documenting parameters.
- Opportunities for micro-refactoring or localized component logic cleaning.

**Automated Action**: Push to next viable sprint. Log in advisory parameters.

---

## 📚 Core References

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Level 0
- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Level 1
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Level 1
