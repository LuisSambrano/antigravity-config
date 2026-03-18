# Pre-Push Security Checklist

**Version**: 1.0.0
**Status**: MANDATORY
**Level**: 0 (Blocks push if failed)

## Purpose

Mandatory checks before ANY `git push`. These are the patterns that
cause production incidents. Run this before reporting a phase as complete.

---

## The 60-Second Check

Run all at once from project root:

```bash
# 1. Build must pass
npm run build

# 2. No NEXT_PUBLIC_ on server-only values
grep -rn 'NEXT_PUBLIC_ADMIN_EMAIL\|NEXT_PUBLIC_SERVICE_ROLE\|NEXT_PUBLIC_RESEND' 
  app/ proxy.ts --include='*.ts' --include='*.tsx'
# Expected output: NOTHING. Any match = CRITICAL VIOLATION.

# 3. No affiliate_url in client-facing code
grep -rn 'affiliate_url' 
  components/ app/ --include='*.ts' --include='*.tsx' | 
  grep -v 'server\|action\|SECURITY\|exclude\|has_affiliate'
# Expected: only server actions and comments. Any client component match = VIOLATION.

# 4. No hardcoded domains in email/sitemap fields
grep -rn 'from:.*@.*\.\(co\|cc\|io\|dev\)' 
  app/ --include='*.ts' | grep -v 'process\.env'
# Expected: NOTHING. Any match = replace with env var.

# 5. TypeScript clean
npx tsc --noEmit
```

---

## Gate Criteria

| Check | Pass | Fail → Action |
|-------|------|---------------|
| `npm run build` | 0 errors | Fix before push — no exceptions |
| NEXT_PUBLIC_ scan | 0 matches | Remove NEXT_PUBLIC_ prefix, use server-only var |
| affiliate_url scan | 0 client matches | Move to server action or exclude from select |
| hardcoded domains | 0 matches | Replace with `process.env.X \|\| 'fallback'` |
| TypeScript | 0 errors | Fix type errors |

---

## Per-Phase Security Additions

### Adding a new API route (POST)
- [ ] Rate limiting implemented
- [ ] Input validated (shape + types)
- [ ] No sensitive data in response body

### Adding a new admin Client Component
- [ ] Does not import from `lib/supabase/admin`
- [ ] Does not receive `affiliate_url`, `service_role_key`, or raw DB rows as props
- [ ] Writes go through a Server Action in `actions.ts`

### Adding a new gear/article field
- [ ] If sensitive: excluded from `select()` in server pages
- [ ] If sensitive: not in `initialData` prop to client editors
- [ ] If sensitive: handled via dedicated server action

### Modifying email sending
- [ ] `from:` uses `process.env.RESEND_FROM_EMAIL`
- [ ] `to:` uses `process.env.RESEND_NOTIFY_EMAIL` or `ADMIN_EMAIL`
- [ ] No hardcoded email addresses or domains
- [ ] Batch logic if sending to multiple recipients (max 100/request)

---

## How Antigravity Uses This

Before invoking `notify_user` or reporting a phase complete:

1. Run the 60-Second Check above
2. If any check fails → fix it, do not report done
3. If all pass → commit with descriptive message, push, then report

```markdown
✅ Pre-push checklist passed:
- Build: 0 errors
- NEXT_PUBLIC_ scan: 0 violations
- affiliate_url scan: 0 client exposures
- Domain scan: 0 hardcoded values
- TypeScript: 0 errors
```