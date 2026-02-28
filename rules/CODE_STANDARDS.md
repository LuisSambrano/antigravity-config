# 💻 Enterprise Code Standards

**Version**: 2.0.0
**Status**: MANDATORY
**Level**: 1 (Transversal Engineering Protocols)

---

## 🎯 Purpose

This document operationalizes the execution of Antigravity codebases. It enforces strict mathematical determinism, cognitive simplicity, and defensive error orchestration. Adherence is aggressively monitored via unyielding CI/CD validation gates.

---

## 📘 Strict Type Theory (TypeScript)

### The Configuration Absolute

**File**: `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "strict": true, // ← The bedrock. Must remain true.
    "noUncheckedIndexedAccess": true, // ← Forces undefined checks on array index Lookups
    "noImplicitReturns": true, // ← Blocks silent function escape routes
    "noFallthroughCasesInSwitch": true,
    "verbatimModuleSyntax": true, // ← Mandates `import type` enforcement at build
    "exactOptionalPropertyTypes": true // ← Prevents writing `undefined` to explicit optionals
  }
}
```

### Type Invariants

#### 1. Complete Annihilation of `any`

Using `any` explicitly abandons the compiler and introduces runtime chaos.

```typescript
// ❌ FATAL VIOLATION: Bypasses static analysis
function parsePayload(payload: any) {
  return payload.secureHash;
}

// ✅ MANDATORY: Type narrowing via 'unknown' and guards
import { z } from "zod";

const PayloadSchema = z.object({ secureHash: z.string() });

function parsePayload(payload: unknown): string {
  const result = PayloadSchema.safeParse(payload);
  if (!result.success) throw new Error("Payload structural violation");
  return result.data.secureHash;
}
```

#### 2. Delineation of Domains: `interface` vs `type`

- **Interfaces**: Utilized exclusively for OOP contracts and public class/object outlines. Preferred for their declaration merging optimizations.
- **Types**: Utilized exclusively for defining Unions, Intersections, Mapped types, and discrete primitives.

```typescript
// ✅ INTERFACE: Public structural blueprint
export interface TransactionRecord {
  id: string;
  amount: number;
}

// ✅ TYPE: Intersections and unions
export type FinancialClassification = "credit" | "debit" | "hold";
export type SettledTransaction = TransactionRecord & { status: "settled" };
```

---

## 🧠 Cognitive and Cyclomatic Bounds

### Complexity Limits

**Constraint**: Code must be read infinitely more than it is written.

- ✅ **Function Length**: Hard limit of **50 lines**. Any function breaching this limit must be mathematically factored into smaller pure functions.
- ✅ **Cyclomatic Complexity**: Functions must not exceed a complexity score of **10** (measured by identical nested IF/ELSE loops or SWITCH bounds).
- ✅ **Cognitive Bounds**: Deeply nested ternaries (`condition ? a : b ? c : d`) are strictly forbidden. Use early returns (Guard Clauses).

```typescript
// ❌ VIOLATION: Pyramid of Doom (Excessive Cognitive Load)
async function processOrder(order: Order) {
  if (order.isValid) {
    if (order.paymentMethod === "card") {
      if (order.amount > 100) {
        // ... logic
      }
    }
  }
}

// ✅ MANDATORY: Flat Hierarchy via Guard Clauses
async function processOrder(order: Order) {
  if (!order.isValid) return fail("Invalid Schema");
  if (order.paymentMethod !== "card") return fail("Unsupported Gateway");
  if (order.amount <= 100) return fail("Below Minimum Transfer");

  // Clean execution path
  return await executeExecution(order);
}
```

---

## 🚨 Error Orchestration and Telemetry

### Predictable Failure Propagation

**Constraint**: Throwing raw errors dynamically crashes threads and pollutes stacks. Use structured Result Wrappers for business logic, and reserve `throw` exclusively for fatal application collapse.

```typescript
// ✅ MANDATORY: The Result Pattern for predictable flow control
export type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export async function fetchUserBalance(userId: string): Promise<Result<number>> {
  try {
    const data = await db.query(...);
    if (!data) return { ok: false, error: new Error("Balance isolated") };
    return { ok: true, value: data.amount };
  } catch (err) {
    // Inject telemetry tags here for Sentry/Datadog tracking
    logger.error({ event: "db_fetch_fail", userId, details: err });
    return { ok: false, error: err as Error };
  }
}

// Utilization Context
const balanceResult = await fetchUserBalance("UUID-1234");
if (!balanceResult.ok) {
  return renderFallbackUI(balanceResult.error);
}
// V8 engine infers balanceResult.value is a safe number here.
```

---

## ⚡ State Immutability and Functional Purity

**Constraint**: Data structures are immutable by default. Mutating parameters passed into functions causes side-effects that are impossible to trace in highly parallel applications.

```typescript
// ❌ FATAL VIOLATION: Mutating an argument object
function applyDiscount(cart: Cart) {
  cart.total = cart.total * 0.9;
  return cart;
}

// ✅ MANDATORY: Pure function utilizing spread operations or structural cloning
function applyDiscount(cart: Readonly<Cart>): Cart {
  return {
    ...cart,
    total: cart.total * 0.9,
    discountApplied: true,
  };
}
```

---

## 💬 Teleological Commenting Algorithms

**Constraint**: Comments must explain the business imperative ("Why") algorithms were chosen. They must never translate syntax to English.

```typescript
// ❌ NOISE: Translating syntax
// Filters out disabled users from the array
const activeUsers = users.filter((u) => u.status === "active");

// ✅ CONTEXTUAL: Explaining the business parameters
// Overruling the global index cache here specifically because
// billing synchronization requires microsecond accuracy on 'active' state.
const activeUsers = users.filter((u) => u.status === "active");
```

---

## 📦 Dependency and Import Topologies

**Constraint**: Imports must be aggressively clustered to minimize tracking fatigue.

```typescript
// 1. External ecosystem runtimes
import React, { useMemo } from "react";

// 2. High-Order Third Party libraries (Alphabetized)
import { createBrowserClient } from "@supabase/ssr";
import { clsx, type ClassValue } from "clsx";
import { z } from "zod";

// 3. Absolute Internal Paths (Domain Driven)
import { UserDTO } from "@/server/dtos/user.dto";
import { telemetryLogger } from "@/lib/utils/telemetry";

// 4. Relative paths (Component specific scopes)
import { SubNavigation } from "./SubNavigation";
import styles from "./Dashboard.module.css";
```

---

## 📚 Core References

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md)
- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md)
- [QUALITY_GATES.md](./QUALITY_GATES.md)
