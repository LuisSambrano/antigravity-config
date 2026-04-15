---
name: nextjs
description: Next.js App Router rules and architecture.
---

# Next.js Protocol

## Routing
- Strictly use the `app/` router.
- Use `loading.tsx` and `error.tsx` for graceful degradation.

## Data Fetching
- Fetch data in Server Components (`async function Page()`).
- Avoid `useEffect` for data fetching; use SWR or React Query only for mutations or real-time polling on the client.

## Mutations
- Use Server Actions for all POST/PUT/DELETE operations.
