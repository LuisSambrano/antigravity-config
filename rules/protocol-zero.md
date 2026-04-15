# 🌌 Core Engineering Principles (Protocol Zero)

**Version**: 2.1.0
**Status**: Active
**Scope**: Standards and Best Practices

---

## 🎯 Purpose

This document defines the foundational standards for development within the Antigravity ecosystem. These principles ensure consistency, quality, and security across all architectural designs, code synthesis, and deployment pipelines.

---

## ⚙️ Core Principles

### 1. Local Workspace as Source of Truth
The local development environment is the primary authority for the project state. Remote repositories (e.g., GitHub) serve as mirrors of this local state.
- **Workflow**: Mutations flow from `Local → Remote`.
- **Consistency**: Local configurations and structures supersede remote state.
- **Integrity**: Remote repositories must be kept in sync with the established local state.

### 2. Quality-First Development
Code quality is prioritized over delivery speed. All contributions must meet established verification thresholds before being integrated.
- **Verification**: Passing automated CI/CD pipelines is a prerequisite for all merges.
- **Standards**: Zero tolerance for types/lint errors or failing builds in production branches.
- **Reliability**: All operations must include proper error handling and graceful degradation.

### 3. Documentation of Intent
Code defines logic, while documentation and comments define intent. Both must be maintained with the same level of rigor.
- **Bilingual Context**: Technical documentation is maintained in English (system) and human-facing docs in Spanish.
- **Logic Explanation**: Comments should explain the "Why" (business logic) rather than the "What" (syntax).
- **Tracability**: Significant architectural changes must be documented (e.g., via ADRs) and reflected in the CHANGELOG.

### 4. Transparency and Standards Adherence
Developers have implementation autonomy but must operate within established architectural bounds and maintain full transparency.
- **Innovation**: New libraries or patterns are encouraged if they provide measurable improvements over existing solutions.
- **Consensus**: Systemic changes or deviations from standard rules require documentation and peer review.
- **Predictability**: Potential destructive or high-impact changes must be clearly communicated before execution.

### 5. Continuous Improvement
Every modification should aim to reduce technical debt and improve the overall quality of the module.
- **Refactoring**: Improving adjacent legacy code and increasing test coverage is encouraged during feature development.
- **Simplification**: Continuously seek to reduce code complexity and improve maintainability.

---

## 🛡️ Technical Standards

### 1. Security
- **Data Privacy**: Row Level Security (RLS) is required for all database interactions. Default access is restricted.
- **Input Validation**: All ingress data must be validated against strict schemas (e.g., Zod).
- **Key Management**: Secrets must be managed via environment variables; never hardcoded.

### 2. Accessibility (A11y)
- **Compliance**: Follow WCAG 2.1 AA standards as a baseline for all user interfaces.
- **Semantics**: Use correct HTML semantic elements and ARIA attributes where necessary.
- **Visuals**: Maintain standard contrast ratios for readability.

### 3. Performance
- **Web Vitals**: Aim for high performance metrics (LCP < 2.5s, minimal CLS and TTFB).
- **Optimization**: Use code-splitting, lazy loading, and next-gen asset formats (WebP/AVIF).
- **Efficiency**: Aggressively optimize bundles and database queries (avoid N+1).

### 4. Maintainability
- **Design Patterns**: Follow SOLID principles and separate UI from business logic.
- **Complexity Limits**: Abstract complex logic into reusable functions, hooks, or services.
- **Code Reuse**: Follow DRY (Don't Repeat Yourself) principles to minimize redundancy.

### 5. Scalability
- **Statelessness**: Design applications to be stateless and capable of horizontal scaling.
- **Caching**: Implement multi-layer caching (Edge, CDN, Redis) for data-intensive operations.
