---
name: web-vitals
description: Performance optimization and SEO requirements.
---

# Web Performance & SEO Protocol

## Rendering
- Optimize LCP (Largest Contentful Paint) < 2.5s.
- Always use Next.js `<Image>` component.
- Prioritize static rendering or ISR over SSR when content updates are infrequent.

## SEO
- Generate dynamic `metadata` objects in Next.js `layout.tsx` or `page.tsx`.
- Include standard `robots.txt` and `sitemap.xml` components.
- Enforce semantic HTML (`<main>`, `<article>`, `<nav>`, `<h1>` to `<h6>`).
