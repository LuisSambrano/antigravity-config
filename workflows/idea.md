---
description: Evaluate technical feasibility of product ideas and technologies
---

# /idea - Feasibility Evaluation

Use this workflow to assess the technical viability of new features, libraries, or product concepts within the current stack.

## Automated Execution Steps

1. **Research & Analysis**
   - Define the core concept and technical requirements.
   - Identify underlying technologies and dependencies.
   - Assess required infrastructure resources.

2. **Feasibility Assessment**
   - Stack Compatibility: Evaluate integration with Next.js, Supabase, Vercel.
   - Effort Estimation: Approximate implementation time.
   - Risk Analysis: Identify security, performance, or architectural risks.

3. **Verdict Generation**
   - ✅ YES: Provide an actionable implementation plan.
   - ⚠️ PARTIAL: Specify supported vs. unsupported components.
   - ❌ NO: State blocking reasons and propose viable alternatives.

## Usage Context

- Evaluating a new technology trend or library.
- Assessing if a requested feature aligns with the current architecture.
- Determining implementation cost before committing development time.

## Usage Example

USER: `/idea Implement passkey authentication`

AGENT:

```text
🔍 Researching WebAuthn passkeys...

## Analysis

**Concept**: Passwordless authentication via device biometrics.

**Stack Compatibility**:
- Next.js ✅ Supported
- Supabase ⚠️ Indirect support via workarounds
- Vercel ✅ Supported

## Verdict: ⚠️ PARTIAL

**Supported Implementation**:
- Integrate WebAuthn via `@simplewebauthn`.
- Deploy as a secondary MFA method.

**Unsupported Strategy**:
- Exclusive passkey authentication (due to device compatibility limits).

**Estimated Effort**: 4-6 hours

**Recommended Alternative**: Magic links (Native Supabase support).
```

## Prerequisites

- ❌ Do not self-research before invoking.
- ❌ Deep technical context is not required from the user.
- Provide the core idea; the agent handles the technical assessment.
