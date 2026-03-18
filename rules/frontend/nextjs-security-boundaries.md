# Next.js Security Boundaries

**Version**: 1.0.0
**Status**: MANDATORY
**Level**: 1 (Security Critical)

## Purpose

These rules govern the Server/Client boundary in Next.js App Router.
Violating these patterns causes real security incidents — affiliate URLs
in client HTML, auth emails in browser bundles, service keys in responses.

---

## 1. NEXT_PUBLIC_ Prefix Rules

`NEXT_PUBLIC_` bakes the value into the JavaScript bundle at build time.
It is visible in browser devtools, HTML source, and network traces.

```
NEVER NEXT_PUBLIC_:          ALWAYS USE PLAIN:
─────────────────────────    ─────────────────────────
ADMIN_EMAIL                  ADMIN_EMAIL
SERVICE_ROLE_KEY             SUPABASE_SERVICE_ROLE_KEY
RESEND_API_KEY               RESEND_API_KEY
Any affiliate URL            (never in env at all — DB only)
Any secret key or token      Any secret key or token

SAFE AS NEXT_PUBLIC_:
─────────────────────────────────
NEXT_PUBLIC_SUPABASE_URL     (public anon endpoint)
NEXT_PUBLIC_SUPABASE_ANON_KEY (designed to be public)
NEXT_PUBLIC_SITE_URL         (just a URL, no secret)
```

**Middleware/proxy.ts runs in Edge runtime** and has access to ALL env vars
including non-NEXT_PUBLIC_ ones. Use `process.env.ADMIN_EMAIL` there directly.

```typescript
// ❌ CRITICAL VIOLATION — proxy.ts
user.email !== process.env.NEXT_PUBLIC_ADMIN_EMAIL  // undefined in production

// ✅ CORRECT
user.email !== process.env.ADMIN_EMAIL
```

---

## 2. Server → Client Prop Boundary

When a Server Component passes props to a Client Component (`'use client'`),
Next.js serializes ALL props into an inline `<script>` tag in the HTML.
Every value in those props is readable in the browser source.

```typescript
// ❌ CRITICAL — passes affiliate_url to client via props
async function GearEditPage({ params }) {
  const gear = await supabase.from('gear_items').select('*').eq('id', id).single()
  return <GearEditor initialData={gear} />  // affiliate_url lands in HTML
}

// ✅ CORRECT — exclude sensitive fields at query level
async function GearEditPage({ params }) {
  const gear = await supabase
    .from('gear_items')
    .select('id, name, brand, slug, go_slug, ...')  // no affiliate_url
    .eq('id', id).single()
  return <GearEditor initialData={gear} has_affiliate_url={!!gear.affiliate_url} />
}
```

**Rule**: Never pass a full DB row `*` to a Client Component.
Always explicit-select and exclude sensitive columns.

---

## 3. Affiliate URL Handling

`affiliate_url` is a special field — it is the raw monetization link.
Exposing it to clients lets anyone bypass the click tracking, copy the
raw affiliate link, and strip commission.

```
NEVER expose affiliate_url in:        ALWAYS use:
─────────────────────────────────    ──────────────────────────────
Client component props               /go/{go_slug} redirect route
JSON-LD structured data              /go/{go_slug} in offers.url
API response bodies                  Boolean has_affiliate_url
href attributes on <a> tags          href="/go/{go_slug}"
Fallback when go_slug is null        Return null — no CTA at all
```

```typescript
// ❌ VIOLATION — JSON-LD exposes raw URL in page source
const jsonLd = { offers: { url: item.affiliate_url } }

// ✅ CORRECT
const jsonLd = {
  offers: {
    url: item.go_slug
      ? `${process.env.NEXT_PUBLIC_SITE_URL}/go/${item.go_slug}`
      : undefined
  }
}
```

---

## 4. Server Actions for Admin Writes

All write operations from admin UI must go through Server Actions.
This keeps sensitive fields (affiliate_url) server-side at all times.

```typescript
// ❌ VIOLATION — Client component calls Supabase directly with service role
'use client'
import { createAdminClient } from '@/lib/supabase/admin'
async function save() {
  await createAdminClient().from('gear_items').upsert(formData)  // service key in client
}

// ✅ CORRECT — Server Action handles write, client never touches supabase/admin
'use server'
export async function upsertGearAction(data: GearFormData) {
  // affiliate_url: strip empty string to avoid overwriting existing value
  const payload = { ...data }
  if (!payload.affiliate_url) delete payload.affiliate_url
  await createAdminClient().from('gear_items').upsert(payload)
}
```

---

## 5. Rate Limiting on Public API Routes

Every route that accepts POST from the public internet needs rate limiting.
No exceptions for contact forms, newsletter signups, or auth endpoints.

```typescript
// Minimal in-memory rate limiter for Edge/Node API routes
const rateLimitMap = new Map<string, { count: number; reset: number }>()

function checkRateLimit(ip: string, limit: number, windowMs: number): boolean {
  const now = Date.now()
  const entry = rateLimitMap.get(ip)
  if (!entry || now > entry.reset) {
    rateLimitMap.set(ip, { count: 1, reset: now + windowMs })
    return true
  }
  if (entry.count >= limit) return false
  entry.count++
  return true
}
```

Public routes and their limits:
- `/api/newsletter/subscribe` → 3 req/hour per IP
- `/api/contact` → 5 req/day per IP
- `/api/admin/auth` → 10 req/hour per IP

---

## 6. Hardcoded Domain Audit Checklist

Before every commit, grep for hardcoded domains in email/URL fields:

```bash
grep -rn 'your-old-domain.com\|placeholder.dev\|example.co' app/ --include='*.ts' --include='*.tsx'
```

All domains in `from:`, `to:`, `sitemap`, `robots`, `canonical` must come
from environment variables:

```typescript
// ❌ VIOLATION
from: 'noreply@old-domain.co'
sitemap: 'https://old-domain.co/sitemap.xml'

// ✅ CORRECT
from: process.env.RESEND_FROM_EMAIL || 'hello@luissambrano.dev'
sitemap: `${process.env.NEXT_PUBLIC_SITE_URL || 'https://luissambrano.dev'}/sitemap.xml`
```