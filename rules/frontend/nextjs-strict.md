# Next.js Strict Engineering Standards

These rules are MANDATORY for all Antigravity properties and client projects.

## 1. App Router Architecture

- **Grouped Routes**: Always use route groups to organize feature logic without affecting URLs.
  - `app/(marketing)/` -> Public pages.
  - `app/(dashboard)/` -> Protected app pages.
  - `app/(auth)/` -> Login/Signup flows.
- **Colocation**: Components that are specific to a page MUST live in a `_components` folder inside that route.
  - `app/(dashboard)/settings/_components/profile-form.tsx`

## 2. Server Components Strategy

- **Default by Design**: All components are Server Components unless explicitly strictly needed.
- **Leaf Interactivity**: Push `use client` down to the leaves of the component tree (buttons, inputs, interactive charts).
  - ❌ BAD: Adding `use client` to `page.tsx`.
  - ✅ GOOD: Importing `<InteractiveButton />` into a Server Page.

## 3. Data Fetching

- **Direct Fetching**: Fetch data directly in Server Components using `await`.
- **No API Routes**: Do NOT create `app/api/users/route.ts` just to fetch data for the frontend. Use Server Actions or Direct Fetch.
- **Supabase**: Use the correctly typed client for the context (Server Client vs Browser Client).

## 4. Performance

- **Images**: All images must use `next/image`.
- **Fonts**: `next/font` with `variable` strategy to prevent CLS.
- **Suspense**: Use `loading.tsx` or `<Suspense>` boundaries for granular loading states.
