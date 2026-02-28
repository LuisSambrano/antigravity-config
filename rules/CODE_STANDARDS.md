# 💻 Antigravity Code Standards

**Version**: 1.0.0
**Status**: MANDATORY
**Level**: 1 (Code - Transversal)

---

## 🎯 Purpose

This document dictates the **mandatory coding standards** required across all Antigravity properties. These rules traverse both frontend and backend environments and are aggressively audited by automated gates.

---

## 📘 TypeScript Standards

### Mandatory Configuration

**File**: `tsconfig.json`

```json
{
  "compilerOptions": {
    "strict": true, // ← MANDATORY
    "noUncheckedIndexedAccess": true, // ← MANDATORY
    "noImplicitReturns": true, // ← MANDATORY
    "noFallthroughCasesInSwitch": true, // ← MANDATORY
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

**Verification Protocol**:

```bash
# Pre-commit gate execution
tsc --noEmit
```

---

### Typing Directives

#### 1. Prohibition of `any`

```typescript
// ❌ INCORRECT
function processData(data: any) {
  return data.value;
}

// ✅ CORRECT: Explicit typing
interface DataStructure {
  value: string;
}

function processData(data: DataStructure) {
  return data.value;
}

// ✅ CORRECT: `unknown` with type guarding for dynamic payloads
function processUnknownData(data: unknown) {
  if (typeof data === "object" && data !== null && "value" in data) {
    return (data as DataStructure).value;
  }
  throw new Error("Invalid data structure");
}
```

---

#### 2. Interfaces vs. Types

**Directive**: Use `interface` for declaring public objects. Use `type` for defining unions or intersections.

```typescript
// ✅ CORRECT: Interface for standard object definitions
export interface User {
  id: string;
  name: string;
  email: string;
}

// ✅ CORRECT: Type for union definitions
export type Status = "draft" | "published" | "archived";

// ✅ CORRECT: Type for intersection configurations
export type AuthenticatedUser = User & {
  token: string;
  expiresAt: Date;
};

// ❌ INCORRECT: Mapping a basic object syntax to a Type
export type UserType = {
  id: string;
  name: string;
};
```

---

#### 3. Descriptive Generics

**Directive**: Abstract generic syntax must explicitly document intended behavior.

```typescript
// ❌ INCORRECT: Cryptic typing abstracts logic context
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

// ✅ CORRECT: Descriptive generics aligned with domain logic
function transformArticles<TArticle extends Article, TViewModel>(
  articles: TArticle[],
  toViewModel: (article: TArticle) => TViewModel,
): TViewModel[] {
  return articles.map(toViewModel);
}
```

---

#### 4. Null vs. Undefined Directives

**Directive**: Declare `null` for intentional value absences (e.g., cleared data). Resort to `undefined` for uninitialized memory paths.

```typescript
// ✅ CORRECT
interface User {
  id: string;
  name: string;
  avatar: string | null; // Null signifies intentional omission.
  bio?: string; // Undefined optional parameter.
}

// ❌ INCORRECT: Conflating null and undefined creates type ambiguity.
interface ConfusingUser {
  avatar: string | null | undefined;
}
```

---

## 💬 Comment Directives

### Trigger Scenarios

**Directive**: Comments document **WHY**, never **WHAT**.

```typescript
// ❌ INCORRECT: Comment describes exactly what the code does
// Increment the counter by 1
count++;

// ✅ CORRECT: Comment describes business context explaining the "WHY"
// Modifying counter directly to bypass React tree re-renders during high-frequency scroll events
count++;
```

---

### Comment Formatting

#### 1. Inline Annotations

```typescript
// ✅ CORRECT: Annotation placed strictly above target
// Establishing a 5-minute CDN cache horizon to throttle DB ingress.
const CACHE_DURATION = 5 * 60 * 1000;

// ❌ INCORRECT: Appended annotation disrupts tracking
const CACHE_DURATION = 5 * 60 * 1000; // Cache de 5 minutos
```

---

#### 2. JSDoc for Public Exports

````typescript
// ✅ MANDATORY: Generating documentation for external or consumed services.
/**
 * Resolves user dataset authenticated via Supabase.
 *
 * Implements a 5-minute memory cache to heavily restrict API egress latency.
 * Invalidated by Supabase realtime broadcast events.
 *
 * @param userId - Extracted UUID mapping.
 * @returns Serialized User object, or null.
 * @throws {Error} Fatal if Supabase engine initialization collapses.
 *
 * @example
 * ```typescript
 * const user = await fetchUser('UUID-1234');
 * ```
 */
export async function fetchUser(userId: string): Promise<User | null> {
  // Logic
}
````

---

## 📦 Import Formatting Directives

### Mandatory Sequencing

```typescript
// 1. React Runtime Packages
import React, { useState } from "react";
import type { ReactNode } from "react";

// 2. Third-Party Vendor Dependencies (Alphabetical Sort)
import { createClient } from "@supabase/supabase-js";
import { z } from "zod";

// 3. Internal Application Topology (Alphabetical Sort)
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils/cn";

// 4. Type Declarations
import type { User } from "@/types/user.types";

// 5. CSS Stylesheets (Mandatory Last Position)
import "./styles.css";
```

---

## 🔧 Function and Method Constraints

### Length Directives

**Directive**: Rigidly enforce a 50-line maximum depth per functional block. Delegate logic upon breach.

```typescript
// ❌ INCORRECT: Monolithic function orchestrating distinct behaviors
function processArticle(article: Article) {
  // ~100 heterogeneous lines of code
}

// ✅ CORRECT: Functional separation and orchestration
function processArticle(article: Article) {
  const validated = validateArticle(article);
  const enriched = enrichMetadata(validated);
  return publishToDatabase(enriched);
}
```

### Extensibility Pattern (Single Responsibility)

```typescript
// ❌ INCORRECT: Conglomerated actions within a single sequence
function saveUserAndEmail(user: User) {
  database.save(user);
  emailConfig.send(user.email, "Welcome");
}

// ✅ CORRECT: Atomic functional segregation orchestrated downstream
function saveUser(user: User) {
  return database.save(user);
}

function dispatchWelcome(user: User) {
  return emailConfig.send(user.email, "Welcome");
}

async function userRegistrationPipeline(user: User) {
  const account = await saveUser(user);
  await dispatchWelcome(account);
  return account;
}
```

---

## 🚨 Error Handling Paradigms

### Try-Catch Integrity

**Directive**: Every asynchronous promise or operation must route through a defensive try-catch boundary.

```typescript
// ❌ INCORRECT: Susceptible to unhandled promise rejections
async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// ✅ CORRECT: Validated boundary handling
async function fetchUser(id: string): Promise<User | null> {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Fetch rejection intercepted:", error);
    return null;
  }
}
```

---

### Graceful Return Fallbacks (No-Throw Design in Production)

```typescript
// ✅ CORRECT: Returning defined Result payloads instead of aggressively throwing
type Result<T> = { success: true; data: T } | { success: false; error: string };

async function fetchEntity(id: string): Promise<Result<User>> {
  try {
    const user = await database.users.findById(id);
    if (!user) return { success: false, error: "Missing Entity Record" };
    return { success: true, data: user };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : "Fatal Unknown Context",
    };
  }
}
```

---

## 🔒 Security Posture

### Hardcoding Violations

```typescript
// ❌ CRITICAL VIOLATION: Hardcoded authentication token
const API_KEY = "sk_live_123456789";

// ✅ CORRECT: Validated environment extraction
const API_KEY = process.env.STRIPE_SECRET_KEY;
if (!API_KEY) {
  throw new Error("Missing required STRIPE_SECRET_KEY environment variable");
}
```

### Input Schema Validation

```typescript
// ✅ CORRECT: Defense-in-depth via Zod schema parsers
import { z } from "zod";

const UserSchema = z.object({
  email: z.string().email(),
  age: z.number().min(18).max(120),
});

function insertUserRecord(input: unknown) {
  const payload = UserSchema.parse(input);
  return database.users.create(payload);
}
```

---

## 📚 Core References

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Level 0
- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Level 1
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Level 1
