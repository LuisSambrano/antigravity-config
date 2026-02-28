# 🏗️ Enterprise Architecture Standards

**Version**: 2.0.0
**Status**: MANDATORY
**Level**: 1 (Architecture & System Design)

---

## 🎯 Purpose

This document enforces the **inflexible directory topologies**, **naming taxonomies**, and **cloud-native architectural patterns** required across all Antigravity properties. Deviations from these doctrines require explicit, documented Architecture Decision Records (ADRs).

---

## 📁 System Topology (App Router Hierarchy)

### Mandatory Directory Scaffolding

```text
project/
├── .agent/                          # ← MANDATORY: AI/Operator Control Plane
│   ├── rules/                       # Bounded Context Directives
│   ├── workflows/                   # Immutable Execution Sequences
│   └── templates/                   # Code Generation ASTs
├── app/                             # Next.js App Router (Routing Plane)
│   ├── (auth)/                      # Route Segments: Auth Domain
│   ├── (dashboard)/                 # Route Segments: Internal Domain
│   ├── api/                         # Edge/Node API Handlers
│   ├── layout.tsx                   # Root HTML Scaffolding
│   └── error.tsx                    # Top-Level React Error Boundary
├── components/                      # Presentation Layer (Dumb Components)
│   ├── ui/                          # Design System Primitives (e.g., shadcn/ui)
│   ├── features/                    # Domain-Bounded Components (e.g., Auth, Feed)
│   └── layouts/                     # Macro-Layout Shells
├── lib/                             # Core Infrastructure & Business Logic
│   ├── api/                         # Data Access Objects (DAOs) / Fetch Wrappers
│   ├── supabase/                    # Thread-safe Database Singletons
│   ├── utils/                       # Pure Functional Utilities
│   └── hooks/                       # Custom State Orchestration Hooks
├── server/                          # Server-Side Only Logic (Data Layer)
│   ├── actions/                     # Next.js Server Actions (Mutations)
│   ├── services/                    # Business Logic Services
│   └── dtos/                        # Data Transfer Object Mappers
├── types/                           # Transversal TypeScript Interfaces (Domain Models)
├── .env.local                       # Cryptographically Secure Local Overrides
├── .env.example                     # Sanitized Environment Blueprint (COMMIT)
├── next.config.ts                   # Next.js Runtime Configuration
└── README.md                        # Primary Technical Documentation
```

---

## 🏷️ Structural Taxonomy (Naming Standards)

### File Nomenclature Constraints

| Stratum              | Explicit Convention        | Authorized Example          |
| :------------------- | :------------------------- | :-------------------------- |
| **React Components** | `PascalCase.tsx`           | `AuthenticationGate.tsx`    |
| **Next.js Routing**  | `page.tsx`, `layout.tsx`   | `app/dashboard/page.tsx`    |
| **Route Handlers**   | `route.ts`                 | `app/api/webhooks/route.ts` |
| **Pure Utilities**   | `camelCase.ts`             | `calculateLatency.ts`       |
| **React Hooks**      | `use*.ts`                  | `useSessionTelemetry.ts`    |
| **Domain Models**    | `*.types.ts`               | `transaction.types.ts`      |
| **Data Mappers**     | `*.dto.ts`                 | `user.dto.ts`               |
| **System Config**    | `*.config.ts`              | `tailwind.config.ts`        |
| **Test Suites**      | `*.test.ts` or `*.spec.ts` | `TransactionDAO.spec.ts`    |

### Syntax Abstraction Constraints

| Variable Type        | Convention                     | Example                                      |
| :------------------- | :----------------------------- | :------------------------------------------- |
| **Primitives**       | `camelCase`                    | `const maxConcurrency = 5;`                  |
| **Globals/Envs**     | `SCREAMING_SNAKE_CASE`         | `const MAX_RETRIES = 3;`                     |
| **Functions**        | `camelCase` (Imperative Verb)  | `async function establishConnection() {}`    |
| **Classes/Services** | `PascalCase`                   | `class PaymentGatewayService {}`             |
| **Interfaces/Types** | `PascalCase` (No `I` prefix)   | `interface PaymentIntent {}`                 |
| **Enums**            | `PascalCase`                   | `enum TransactionState { Pending, Settled }` |
| **Internal Scopes**  | `_prefix`                      | `const _inMemoryCache = new Map();`          |
| **Predicates**       | `is*`, `has*`, `can*`, `will*` | `const isFullyHydrated = true;`              |

---

## 🏛️ Inelastic Architectural Patterns

### 1. Hexagonal Infrastructure Isolation (Thread-Safe Singletons)

**Axiom**: External systems (Databases, Message Queues, Payment APIs) must be abstracted behind connection-pooled, thread-safe singletons to prevent memory leaks in serverless/edge environments.

```typescript
// ✅ MANDATORY: Caching the global connection instance in Serverless Runtimes
import { createClient, SupabaseClient } from "@supabase/supabase-js";
import type { Database } from "@/types/database.types";

const globalForSupabase = globalThis as unknown as {
  supabaseClient: SupabaseClient<Database> | undefined;
};

export function getSupabaseServerSingleton(): SupabaseClient<Database> {
  if (!globalForSupabase.supabaseClient) {
    const url = process.env.NEXT_PUBLIC_SUPABASE_URL!;
    const key = process.env.SUPABASE_SERVICE_ROLE_KEY!; // Server-side execution only
    globalForSupabase.supabaseClient = createClient<Database>(url, key);
  }
  return globalForSupabase.supabaseClient;
}
```

---

### 2. The Render Hierarchy (RSC Default)

**Axiom**: Next.js React Server Components (RSC) are the absolute default execution boundary. The boundary shifts to the client (`'use client'`) strictly and only when interactive lifecycle hooks or Web APIs are demanded.

**Client Boundary Triggers (`'use client'`)**:

- ✅ State orchestration (`useState`, `useReducer`, Context APIs).
- ✅ Lifecycle ingestion (`useEffect`, `useLayoutEffect`).
- ✅ User Event propagation (`onClick`, `onKeyDown`).
- ✅ Browser API coupling (`window.navigator`, `IntersectionObserver`).

**Server Boundary Triggers (Default)**:

- ✅ Secure Secret Access (Tokens, DB Passwords).
- ✅ Zero-latency database queries.
- ✅ Downward prop sterilization via Data Transfer Objects (DTOs).
- ✅ Edge-cached data resolution (ISR/SSG).

---

### 3. Asymmetric Separation of Concerns (UI vs Business Logic)

**Axiom**: The Presentation Layer (Components) remains strictly mathematically pure relative to its properties. Complex asynchronous mutations must route through specific orchestrators (Custom Hooks for Client, Server Actions for Server).

```tsx
// ✅ SERVER ACTION (Business Logic Layer)
// server/actions/publish-article.ts
"use server";
import { getSupabaseServerSingleton } from "@/lib/supabase/server";
import { ArticleDTO } from "@/server/dtos/article.dto";

export async function publishArticleAction(formData: FormData) {
  const supabase = getSupabaseServerSingleton();
  const payload = ArticleDTO.parse(formData); // Validate via Zod
  return await supabase.from("articles").insert(payload);
}

// ✅ PRESENTATION COMPONENT (Dumb Layer)
// components/features/articles/PublishButton.tsx
("use client");
import { useTransition } from "react";
import { publishArticleAction } from "@/server/actions/publish-article";

export function PublishButton({ formData }: { formData: FormData }) {
  const [isPending, startTransition] = useTransition();

  return (
    <button
      onClick={() => startTransition(() => publishArticleAction(formData))}
      disabled={isPending}
      className={isPending ? "opacity-50 cursor-not-allowed" : ""}
    >
      {isPending ? "Committing..." : "Publish to Edge"}
    </button>
  );
}
```

---

### 4. Edge vs Node Runtime Optimization

**Axiom**: Middleware and high-concurrency read operations must target the `edge` runtime. Heavy computing processes or non-standard Node.js native module usage must explicitly define the `nodejs` runtime.

```typescript
// ✅ EDGE ALLOCATION: Maximized global TTFB reduction
// app/api/fast-proxy/route.ts
export const runtime = "edge";
export const preferredRegion = "iad1"; // e.g. Washington D.C near the DB

export async function GET(req: Request) {
  // Edge-compatible fetch proxy
}
```

---

### 5. Inverted Component Composition

**Axiom**: Avoid monolithic "God components" by aggressively employing "slots" and `children` props. Prop drilling > 3 levels is a critical architectural odor indicating failed composition.

```tsx
// ✅ COMPOSITION (Inversion of Control)
// The parent injects the highly specific component into the generic layout.
export function DashboardShell({
  Sidebar,
  Content,
}: {
  Sidebar: ReactNode;
  Content: ReactNode;
}) {
  return (
    <div className="grid grid-cols-[250px_1fr]">
      <aside className="border-r">{Sidebar}</aside>
      <main>{Content}</main>
    </div>
  );
}

// Consumed at the page level
<DashboardShell
  Sidebar={<AdminNavigation userRole="admin" />}
  Content={<FinancialMetricsChart data={financialData} />}
/>;
```

---

## 🔐 Cryptographic State Boundaries

**Mandatory Environmental Topology**:

```bash
# .env.example (Safe to Commit - Acts as Architecture Map)
NEXT_PUBLIC_TELEMETRY_KEY=publishable_key_here
SUPABASE_SERVICE_ROLE_KEY=do_not_commit_secrets_here
API_RATE_LIMIT=100
```

**Access Axioms**:

- ✅ `NEXT_PUBLIC_*` prefixes are deliberately leaked to the client bundle. Only harmless tracking or public routing variables belong here.
- ✅ Unprefixed variables are strictly isolated to Server Components, API Routes, or Server Actions. Exposing them to client files will trigger build-time failures in Next.js.

---

## 📚 Core References

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md)
- [CODE_STANDARDS.md](./CODE_STANDARDS.md)
- [QUALITY_GATES.md](./QUALITY_GATES.md)
