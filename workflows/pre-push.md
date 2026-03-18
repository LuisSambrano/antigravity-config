---
description: Mandatory pre-push security and quality gate. Run before reporting any phase complete.
---
# /pre-push — Security & Quality Gate

Run this workflow before every `git push` and before reporting any task or phase as done.

## Automated Execution Steps

1. **Build Gate**
   ```bash
   npm run build
   ```
   Zero errors required. No exceptions.

2. **Environment Variable Security Scan**
   ```bash
   grep -rn 'NEXT_PUBLIC_ADMIN_EMAIL\|NEXT_PUBLIC_SERVICE_ROLE\|NEXT_PUBLIC_RESEND_API' 
     app/ proxy.ts 2>/dev/null
   ```
   Expected: zero matches. Any match is a CRITICAL violation — remove NEXT_PUBLIC_ prefix.

3. **Sensitive Field Exposure Scan**
   ```bash
   grep -rn 'affiliate_url' components/ app/ --include='*.ts' --include='*.tsx' | 
     grep -v '//\|server\|action\|SECURITY\|has_affiliate\|exclude'
   ```
   Expected: zero unintentional client-side matches.

4. **Hardcoded Domain Scan**
   ```bash
   grep -rn "from:.*'[^']*@" app/ --include='*.ts' | grep -v 'process\.env'
   grep -rn 'https://[a-z-]*\.(co|cc)/' app/ --include='*.ts' --include='*.tsx'
   ```
   Expected: zero matches. Replace with environment variables.

5. **TypeScript Strict Check**
   ```bash
   npx tsc --noEmit
   ```
   Zero errors required.

6. **Git Status Verification**
   ```bash
   git status --short
   git log --oneline -3
   ```
   All work committed. Working tree clean before push.

## Output Format

```
🔒 Pre-push Gate — [Project Name]
──────────────────────────────────
✅ Build:           0 errors
✅ NEXT_PUBLIC_:    0 violations
✅ affiliate_url:   0 client exposures
✅ Hardcoded domains: 0 matches
✅ TypeScript:      0 errors
✅ Git:             clean, 3 commits ready

🚀 Safe to push.
```

Or if a check fails:

```
❌ Pre-push Gate FAILED — [Project Name]

❌ NEXT_PUBLIC_ violation found:
   proxy.ts:47 — process.env.NEXT_PUBLIC_ADMIN_EMAIL
   → Fix: change to process.env.ADMIN_EMAIL

Push blocked. Fix violations before proceeding.
```

## Usage

```
/pre-push
```

Invoke before every push. Invoke before reporting any phase complete.
This workflow is NOT optional — it is a gate, not a suggestion.