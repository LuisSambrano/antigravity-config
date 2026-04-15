---
name: react
description: Modern React 18/19 patterns and practices.
---

# React Master Protocol

## Architecture
- Use Server Components by default in Next.js.
- Isolate client state inside `use client` boundary components at the deepest possible tree level.

## State Management
- Prefer Zustand for global state. Avoid Redux.
- Keep component state flat.

## Patterns
- Separate logic from UI via custom hooks (`use...`).
- Strictly adhere to exhaustive deps in `useEffect`.
