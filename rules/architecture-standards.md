# 🏗️ Architecture and System Design Standards

**Version**: 2.1.0
**Status**: Standard
**Scope**: Project Structure and Patterns

---

## 🎯 Purpose

This document defines the required directory structures, naming conventions, and architectural patterns for all projects. Maintaining these standards ensures consistency, security, and long-term maintainability across the ecosystem.

---

## 📁 Project Structure (App Router)

### Core Directory Layout

```text
project/
├── .agent/              # Agent configuration and controls
│   ├── rules/           # Local project rules
│   ├── workflows/       # Automated task sequences
│   └── templates/       # Code generation templates
├── app/                 # Next.js App Router (Routing and Pages)
│   ├── (auth)/          # Auth-related route groups
│   ├── (dashboard)/     # Feature-related route groups
│   ├── api/             # API Route Handlers
│   ├── layout.tsx       # Root layout
│   └── error.tsx        # Global error boundary
├── components/          # React components
│   ├── ui/              # Base UI primitives (e.g., shadcn/ui)
│   ├── features/        # Feature-specific components
│   └── layouts/         # Shared layout components
├── lib/                 # Core infrastructure and shared logic
│   ├── api/             # Data fetching and API clients
│   ├── supabase/        # Database initialization and clients
│   ├── utils/           # Utility functions
│   └── hooks/           # Custom React hooks
├── server/              # Server-only logic and services
│   ├── actions/         # Next.js Server Actions
│   ├── services/        # Business logic services
│   └── dtos/            # Data Transfer Object schemas
├── types/               # Shared TypeScript definitions
├── .env.example         # Template for environment variables
└── README.md            # Project documentation
```

---

## 🏷️ Naming Conventions

### File Naming

| Category             | Convention                 | Example                     |
| :------------------- | :------------------------- | :-------------------------- |
| **React Components** | `PascalCase.tsx`           | `UserAvatar.tsx`            |
| **Next.js Routing**  | `page.tsx`, `layout.tsx`   | `app/dashboard/page.tsx`    |
| **Route Handlers**   | `route.ts`                 | `app/api/users/route.ts`    |
| **Pure Utilities**   | `camelCase.ts`             | `formatCurrency.ts`         |
| **React Hooks**      | `use*.ts`                  | `useAuthStatus.ts`          |
| **Types/Interfaces** | `*.types.ts`               | `user.types.ts`             |
| **Data Mappers**     | `*.dto.ts`                 | `user.dto.ts`               |
| **Test Files**       | `*.test.ts` or `*.spec.ts` | `formatCurrency.test.ts`    |

### Code Syntax

| Type                 | Convention                     | Example                                 |
| :------------------- | :----------------------------- | :-------------------------------------- |
| **Variables**        | `camelCase`                    | `const userCount = 10;`                 |
| **Constants**        | `SCREAMING_SNAKE_CASE`         | `const MAX_TIMEOUT = 5000;`             |
| **Functions**        | `camelCase` (Verbs)            | `function fetchData() {}`               |
| **Interfaces/Types** | `PascalCase`                   | `interface UserSettings {}`             |
| **Enums**            | `PascalCase`                   | `enum Status { Active, Inactive }`      |
| **Predicates**       | `is*`, `has*`, `can*`          | `const isValid = true;`                 |

---

## 🏛️ Architectural Patterns

### 1. Database and Service Access
External resources (Databases, Third-party APIs) should be accessed via connection-pooled singletons to optimize resource usage in serverless environments.

```typescript
// Example: Supabase Server Singleton
import { createClient, SupabaseClient } from "@supabase/supabase-js";
import type { Database } from "@/types/database.types";

const globalForSupabase = globalThis as unknown as {
  supabaseClient: SupabaseClient<Database> | undefined;
};

export function getSupabaseClient(): SupabaseClient<Database> {
  if (!globalForSupabase.supabaseClient) {
    globalForSupabase.supabaseClient = createClient<Database>(
      process.env.NEXT_PUBLIC_SUPABASE_URL!,
      process.env.SUPABASE_SERVICE_ROLE_KEY!
    );
  }
  return globalForSupabase.supabaseClient;
}
```

### 2. React Server Components (RSC)
Favor Server Components as the default for data fetching and layout structure. Use Client Components (`'use client'`) only for interactivity or browser-specific APIs.

**Use Client Components for**:
- State management (`useState`, `useReducer`, Context).
- Lifecycle methods (`useEffect`).
- Event listeners (`onClick`, etc.).
- Browser-only APIs (`localStorage`, `window`).

**Use Server Components for**:
- Direct database or secure API access.
- Sensitive information handling (API keys).
- Static or Edge-cached content.

### 3. Business Logic Isolation
Isolate UI components from complex business logic. Use Server Actions for data mutations and Custom Hooks for client-side state orchestration.

### 4. Component Composition
Promote component reusability and avoid deeply nested prop drilling by using composition patterns (passing components as props or `children`).

### 5. Runtime Optimization
Select the appropriate runtime based on the workload. Use the `edge` runtime for middleware and global read operations, and the `nodejs` runtime for complex computations or specific Node.js dependencies.

---

## 🔐 Environment Variables

- **Public**: Use `NEXT_PUBLIC_` prefix for variables that need to be accessible in the browser bundle (e.g., public keys, feature flags).
- **Private**: All other variables are kept server-side only. Do not commit sensitive values to version control. Reference them in `.env.example` with placeholder values.
