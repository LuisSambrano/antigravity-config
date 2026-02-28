# 🏗️ Antigravity Architecture Standards

**Version**: 1.0.0
**Status**: MANDATORY
**Level**: 1 (Architecture)

---

## 🎯 Purpose

This document dictates the **mandatory directory structure**, **naming conventions**, and **architectural patterns** required across all Antigravity projects.

---

## 📁 Mandatory Directory Structure

### For Next.js (App Router) Projects

```text
project/
├── .agent/                          # ← MANDATORY: Agent workspace
│   ├── rules/                       # Project-specific directives
│   │   ├── architecture.md
│   │   ├── workspace-standards.md
│   │   ├── nextjs-strict.md         # Framework constraints
│   │   ├── ui-ux-luxury.md          # UI/UX constraints
│   │   └── supabase-security.md     # Backend constraints
│   ├── workflows/                   # Project-specific workflows
│   │   ├── auto-qa.md
│   │   ├── deploy.md
│   │   └── create-component.md
│   └── templates/                   # Code gen templates
│       ├── component-template.tsx
│       └── api-route-template.ts
├── app/                             # Next.js App Router root
│   ├── (auth)/                      # Route Group: Authentication
│   │   ├── login/
│   │   ├── register/
│   │   └── layout.tsx
│   ├── (dashboard)/                 # Route Group: Dashboard
│   │   ├── profile/
│   │   ├── settings/
│   │   └── layout.tsx
│   ├── (public)/                    # Route Group: Public-facing
│   │   ├── about/
│   │   ├── contact/
│   │   └── layout.tsx
│   ├── api/                         # Backend API routes
│   │   ├── auth/
│   │   ├── users/
│   │   └── articles/
│   ├── layout.tsx                   # Root layout
│   ├── page.tsx                     # Home page
│   ├── error.tsx                    # Error boundary
│   ├── loading.tsx                  # Loading UI
│   └── not-found.tsx                # 404 page
├── components/                      # React Components
│   ├── ui/                          # Primitive UI (e.g., shadcn/ui)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── input.tsx
│   ├── features/                    # Domain-specific components
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   └── RegisterForm.tsx
│   │   └── articles/
│   │       ├── ArticleCard.tsx
│   │       └── ArticleList.tsx
│   └── layouts/                     # Reusable structural layouts
│       ├── Header.tsx
│       ├── Footer.tsx
│       └── Sidebar.tsx
├── lib/                             # Shared utilities and configurations
│   ├── supabase/                    # Supabase client singletons
│   │   ├── client.ts                # Browser client
│   │   ├── server.ts                # Server client
│   │   └── middleware.ts            # Auth middleware
│   ├── utils/                       # Generic utilities
│   │   ├── cn.ts                    # Class name merger
│   │   ├── date.ts                  # Date formatting
│   │   └── validation.ts            # Schema validation
│   ├── hooks/                       # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useArticles.ts
│   │   └── useDebounce.ts
│   └── constants/                   # Static configurations
│       ├── routes.ts
│       └── config.ts
├── types/                           # Global TypeScript declarations
│   ├── database.types.ts            # Supabase generated typings
│   ├── user.types.ts
│   └── article.types.ts
├── public/                          # Static assets
│   ├── images/
│   ├── icons/
│   └── fonts/
├── .env.local                       # Local secrets (DO NOT COMMIT)
├── .env.example                     # Environment template (COMMIT)
├── .gitignore
├── next.config.ts                   # Next.js compiler configuration
├── tailwind.config.ts               # Tailwind CSS configuration
├── tsconfig.json                    # TypeScript compiler configuration
├── package.json
├── README.md                        # ← MANDATORY (English core)
├── README.es.md                     # ← MANDATORY (Spanish translation)
└── CHANGELOG.md                     # Version history
```

---

## 🏷️ Naming Conventions

### File Level

| Type                 | Convention                 | Example                  |
| :------------------- | :------------------------- | :----------------------- |
| **React Components** | `PascalCase.tsx`           | `ArticleCard.tsx`        |
| **Next.js Routing**  | `page.tsx`, `layout.tsx`   | `app/about/page.tsx`     |
| **API Routes**       | `route.ts`                 | `app/api/users/route.ts` |
| **Utilities**        | `camelCase.ts`             | `formatDate.ts`          |
| **Hooks**            | `use*.ts`                  | `useAuth.ts`             |
| **Types**            | `*.types.ts`               | `user.types.ts`          |
| **Constants**        | `*.constants.ts`           | `routes.constants.ts`    |
| **Config**           | `*.config.ts`              | `next.config.ts`         |
| **Tests**            | `*.test.ts` or `*.spec.ts` | `ArticleCard.test.tsx`   |

### Directory Level

| Type                 | Convention     | Example                               |
| :------------------- | :------------- | :------------------------------------ |
| **Next.js Routes**   | `kebab-case`   | `app/user-profile/`                   |
| **Route Groups**     | `(kebab-case)` | `app/(dashboard)/`                    |
| **Component Groups** | `PascalCase`   | `components/ArticleList/`             |
| **Utilities**        | `camelCase`    | `lib/utils/`                          |
| **Features**         | `kebab-case`   | `components/features/article-editor/` |

### Syntax Level

| Type             | Convention                   | Example                                        |
| :--------------- | :--------------------------- | :--------------------------------------------- |
| **Variables**    | `camelCase`                  | `const userName = 'Luis';`                     |
| **Constants**    | `SCREAMING_SNAKE_CASE`       | `const MAX_RETRIES = 3;`                       |
| **Functions**    | `camelCase` (verb-led)       | `function fetchUser() {}`                      |
| **Components**   | `PascalCase`                 | `function ArticleCard() {}`                    |
| **Classes**      | `PascalCase`                 | `class UserService {}`                         |
| **Interfaces**   | `PascalCase` (No 'I' prefix) | `interface User {}`                            |
| **Types**        | `PascalCase`                 | `type ArticleStatus = 'draft' \| 'published';` |
| **Enums**        | `PascalCase`                 | `enum Role { Admin, User }`                    |
| **Private Refs** | `_prefix`                    | `const _internalCache = {};`                   |
| **Booleans**     | `is*`, `has*`, `can*`        | `const isLoading = true;`                      |
| **Handlers**     | `handle*`                    | `const handleClick = () => {};`                |
| **Callbacks**    | `on*`                        | `const onSuccess = () => {};`                  |

---

## 🏛️ Mandatory Architectural Patterns

### 1. Singleton for Remote Clients (Supabase, APIs)

**Problem**: Instantiating multiple clients causes memory leaks and pipeline exhaustion.

**Solution**: Strictly enforce the Singleton pattern.

```typescript
// ✅ CORRECT: lib/supabase/client.ts
import { createClient, SupabaseClient } from "@supabase/supabase-js";
import type { Database } from "@/types/database.types";

let supabaseClient: SupabaseClient<Database> | null = null;

export function getSupabaseClient(): SupabaseClient<Database> {
  if (!supabaseClient) {
    const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
    const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

    supabaseClient = createClient<Database>(supabaseUrl, supabaseKey);
  }

  return supabaseClient;
}
```

```typescript
// ❌ INCORRECT: Creating new instances per call
import { createClient } from "@supabase/supabase-js";

// This exhausts connection pools
export const supabase = createClient(url, key);
```

---

### 2. Server Components strictly by Default

**Philosophy**: Assume Next.js Server Components. Explicitly opt-in to Client Components only when browser APIS or client-side interactivity is unavoidable.

**When to use Client Components (`'use client'`)**:

- ✅ Required React hooks (`useState`, `useEffect`, `useContext`).
- ✅ Required event listeners (`onClick`, `onChange`).
- ✅ Access to browser APIs (`window`, `localStorage`).
- ✅ Client-only libraries (e.g., framer-motion, react-hot-toast).

**When to use Server Components**:

- ✅ Direct data fetching.
- ✅ Direct backend access (databases, file systems).
- ✅ Static content derivation.
- ✅ Critical SEO paths.

```tsx
// ✅ CORRECT: Server Component (Default)
// app/articles/page.tsx
import { getSupabaseServer } from "@/lib/supabase/server";
import { ArticleCard } from "@/components/features/articles/ArticleCard";

export default async function ArticlesPage() {
  const supabase = getSupabaseServer();
  const { data: articles } = await supabase
    .from("articles")
    .select("*")
    .eq("status", "published");

  return (
    <div>
      {articles?.map((article) => (
        <ArticleCard key={article.id} article={article} />
      ))}
    </div>
  );
}
```

---

### 3. Separation of Concerns (UI vs. Logic)

**Philosophy**: UI components must remain "dumb." Business logic must be outsourced to hooks, services, or Server Actions.

```tsx
// ✅ CORRECT: Logic isolated in a custom hook
// lib/hooks/useArticles.ts
export function useArticles() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    async function fetchArticles() {
      try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
          .from("articles")
          .select("*")
          .eq("status", "published");

        if (error) throw error;
        setArticles(data);
      } catch (err) {
        setError(err as Error);
      } finally {
        setIsLoading(false);
      }
    }

    fetchArticles();
  }, []);

  return { articles, isLoading, error };
}

// components/features/articles/ArticleList.tsx
("use client");

import { useArticles } from "@/lib/hooks/useArticles";
import { ArticleCard } from "./ArticleCard";

export function ArticleList() {
  const { articles, isLoading, error } = useArticles();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {articles.map((article) => (
        <ArticleCard key={article.id} article={article} />
      ))}
    </div>
  );
}
```

---

### 4. Composition Over Inheritance

**Philosophy**: Construct complex UIs by composing smaller, focused components. Avoid deeply nested inheritance structures.

```tsx
// ✅ CORRECT: Composition pattern
interface CardProps {
  children: React.ReactNode;
  variant?: "default" | "outlined" | "elevated";
}

export function Card({ children, variant = "default" }: CardProps) {
  return (
    <div className={cn("rounded-lg", variantStyles[variant])}>{children}</div>
  );
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-b">{children}</div>;
}

export function CardContent({ children }: { children: React.ReactNode }) {
  return <div className="p-4">{children}</div>;
}

// Consumption Context
<Card variant="elevated">
  <CardHeader>
    <h2>Title</h2>
  </CardHeader>
  <CardContent>
    <p>Content</p>
  </CardContent>
</Card>;
```

---

### 5. Error Boundaries

**Philosophy**: Implement localized error boundaries to prevent application-wide catastrophic failures. Isolate by feature segment.

```tsx
// ✅ CORRECT: Feature-level Error Boundary
// app/(dashboard)/articles/error.tsx
"use client";

export default function ArticlesError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <h2 className="text-2xl font-bold mb-4">Error loading articles</h2>
      <p className="text-muted-foreground mb-4">{error.message}</p>
      <button onClick={reset} className="btn-primary">
        Try again
      </button>
    </div>
  );
}
```

---

## 🗂️ Feature-Driven Organization

**Philosophy**: Group architectural elements by domain feature, not by technical file type.

```text
// ✅ CORRECT: Organized by Domain Feature
components/
└── features/
    ├── auth/
    │   ├── LoginForm.tsx
    │   ├── RegisterForm.tsx
    │   ├── useAuth.ts
    │   └── auth.types.ts
    └── articles/
        ├── ArticleCard.tsx
        ├── ArticleList.tsx
        ├── useArticles.ts
        └── article.types.ts

// ❌ INCORRECT: Organized by Technical Type
components/
├── forms/
│   ├── LoginForm.tsx
│   └── ArticleForm.tsx
├── hooks/
│   ├── useAuth.ts
│   └── useArticles.ts
```

---

## 📦 Barrel Exports

**Philosophy**: Utilize `index.ts` files to cleanly expose public interfaces and simplify consumption paths.

```typescript
// ✅ CORRECT: components/ui/index.ts
export { Button } from "./button";
export { Card, CardHeader, CardContent } from "./card";
export { Dialog } from "./dialog";

// Usage Context
import { Button, Card, Dialog } from "@/components/ui";
```

---

## 🔐 Environment Variables

**Mandatory Structure**:

```bash
# .env.example (COMMIT ALLOWED)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```

```bash
# .env.local (DO NOT COMMIT)
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGc...
```

**Conventions**:

- ✅ Use `NEXT_PUBLIC_*` strictly for variables required client-side.
- ✅ Omit prefixes for secure, server-only variables.
- ✅ Maintain `.env.example` with dummy values for repository cloning.
- ❌ Hardcoding secrets within the file system is strictly forbidden.

---

## 📚 Core References

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Level 0
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Level 2
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Level 3
