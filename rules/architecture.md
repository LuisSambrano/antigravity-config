# 🏗️ Architecture Rules

**Version**: 1.0.0
**Status**: ACTIVE
**Level**: 2 (Project Architecture)

---

## 📁 Project Structure

### Directory Organization

```text
src/
├── app/                    # Next.js App Router root
│   ├── (routes)/           # Route grouping bounds
│   ├── api/                # API endpoints
│   └── layout.tsx          # Root layout scaffolding
├── components/             # React component domains
│   ├── home/               # Landing/Index components
│   ├── news/               # Feed aggregation components
│   ├── layout/             # Structural layouts (Header, Footer)
│   └── ui/                 # Primitive UI layer (shadcn/ui)
├── lib/                    # Core utilities and configuration
│   ├── api/                # Remote API client gateways
│   ├── utils/              # Helper utilities
│   └── constants/          # Static variable configurations
└── types/                  # TypeScript interface declarations
```

### Component Architecture

#### Feature-Driven Structuring

- Organize components explicitly by domain feature.
- Isolate features within dedicated subdirectories.
- Extract generic, reusable UI primitives to `/components/ui`.

#### Component Boundaries

- Enforce strictly one component per file.
- Anchor filename to component declaration (PascalCase).
- Enforce named exports (Prohibit `default` exports for components).
- Co-locate `.types.ts` schemas alongside feature-specific components.

### Naming Conventions

#### File Topology

- **Components**: `PascalCase.tsx` (e.g., `NewsFeed.tsx`)
- **Utilities**: `kebab-case.ts` (e.g., `format-date.ts`)
- **Constants**: `SCREAMING_SNAKE_CASE.ts` (e.g., `API_ENDPOINTS.ts`)
- **Types**: `PascalCase.types.ts` (e.g., `Article.types.ts`)

#### Syntax Topology

- **Variables**: `camelCase`
- **Functions**: `camelCase`
- **Components**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Types/Interfaces**: `PascalCase`

---

## ⚛️ Component Standards

### Server vs. Client Components

#### Server Component Defaults

```typescript
// Server Component (Default isolation)
export async function ArticleList() {
  // Direct asynchronous data hydration permitted
  const articles = await fetchArticles();
  return <div>{/* Render logic */}</div>;
}
```

#### Explicit Client Components

```typescript
"use client"; // Explicit opt-in boundary

// Required for hook lifecycle, events, or DOM interfaces
export function InteractiveButton() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

**Client Component Triggers**:

- `useState`, `useEffect`, `useContext` implementations.
- Synthetic event dispatch (`onClick`, `onChange`).
- Browser API bindings (`window`, `document`, `localStorage`).
- Dependent external libraries demanding client runtime.

### TypeScript Integrity

#### Interface over Type (Props)

```typescript
// ✅ CORRECT: Standardize prop definitions using interfaces
interface ArticleCardProps {
  title: string;
  description: string;
  image?: string;
  onClick?: () => void;
}

// ❌ INCORRECT: Avoid mapping basic objects to types
type ArticleCardProps = {
  title: string;
};
```

#### Strict Typing Validation

```typescript
// ✅ CORRECT: Statically typed resolution
const articles: Article[] = await fetchArticles();

// ❌ INCORRECT: Arbitrary suppression
const articles: any = await fetchArticles();

// ✅ CORRECT: Dynamic payload validation
const data: unknown = JSON.parse(response);
if (isArticle(data)) {
  const article: Article = data;
}
```

---

## 🎨 Styling Architecture

### Tailwind CSS Operations

#### Utility Extensiblity

```tsx
// ✅ CORRECT: Inline utility mapping
<div className="flex items-center gap-4 p-6 rounded-lg bg-white dark:bg-zinc-900">

// ❌ INCORRECT: Hardcoded DOM styling
<div style={{ display: 'flex', padding: '24px' }}>
```

#### Semantic Token Integration

```tsx
// ✅ CORRECT: Contextual variable mapping
<div className="bg-primary text-primary-foreground">

// ❌ INCORRECT: Hardcoded absolute colors
<div className="bg-blue-500 text-white">
```

#### Viewport Responsiveness

```tsx
// ✅ CORRECT: Mobile-first breakpoint targeting
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
// Mandated validation breakpoints: 375px, 768px, 1024px, 1440px
```

### Dark Mode Adherence

```tsx
// ✅ CORRECT: Binary mode support
<div className="bg-white dark:bg-zinc-900 text-zinc-900 dark:text-white">
```

---

## 🌐 Data Hydration

### Server API Routing

```typescript
// src/app/api/articles/route.ts
export async function GET(request: Request) {
  try {
    const articles = await fetchFromSupabase();
    return Response.json(articles);
  } catch (error) {
    return Response.json(
      { error: "Failed to fetch resource" },
      { status: 500 },
    );
  }
}
```

### Client Fetching Patterns

```tsx
// Utilize SWR or React Query architectures for client ingress
import useSWR from "swr";

export function ArticleList() {
  const { data, error, isLoading } = useSWR("/api/articles", fetcher);

  if (isLoading) return <LoadingState />;
  if (error) return <ErrorState />;
  return <ArticleGrid articles={data} />;
}
```

---

## 🔍 SEO Benchmarks

### Next.js Metadata Generation

```typescript
// app/news/[slug]/page.tsx
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const article = await getArticle(params.slug);

  return {
    title: article.title,
    description: article.description,
    openGraph: {
      title: article.title,
      description: article.description,
      images: [article.image],
      type: "article",
      publishedTime: article.publishedAt,
      authors: [article.author],
    },
    twitter: {
      card: "summary_large_image",
      title: article.title,
      description: article.description,
      images: [article.image],
    },
  };
}
```

### Semantic HTML Scaffolding

```tsx
// ✅ CORRECT: Explicit semantic regions
<article>
  <header>
    <h1>{title}</h1>
    <time dateTime={publishedAt}>{formatDate(publishedAt)}</time>
  </header>
  <section>
    <p>{content}</p>
  </section>
</article>

// ❌ INCORRECT: Generic `div` nesting obliterating screen readers
<div>
  <div>{title}</div>
  <div>{content}</div>
</div>
```

---

## ⚡ Performance Matrix

### Asset Optimization (Images)

```tsx
// ✅ CORRECT: Enforced Next.js Image optimization pipeline
import Image from 'next/image';

<Image
  src={article.image}
  alt={article.title}
  width={1200}
  height={630}
  priority={isFeatured} // LCP optimization
  placeholder="blur"
  blurDataURL={article.blurDataURL}
/>

// ❌ CRITICAL: Unoptimized DOM injection
<img src={article.image} alt={article.title} />
```

### Splitting Architecture

```tsx
// ✅ CORRECT: Deferred loading for heavy dependencies
import dynamic from "next/dynamic";

const HeavyChart = dynamic(() => import("./HeavyChart"), {
  loading: () => <ChartSkeleton />,
  ssr: false,
});
```

---

## 🚨 Error Control

### Boundary Triaging

```typescript
// ✅ CORRECT: Wrapping egress in defensive Try/Catch structures
async function fetchArticles() {
  try {
    const response = await fetch("/api/articles");
    if (!response.ok) throw new Error("Ingress failure");
    return await response.json();
  } catch (error) {
    console.error("Transmission error logged:", error);
    throw error;
  }
}
```

### Interface Error Boundaries

```tsx
// app/error.tsx
"use client";

export default function ErrorBoundary({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="flex flex-col items-center">
      <h2>Critical Rendering Failure</h2>
      <button onClick={reset}>Attempt Soft Reset</button>
    </div>
  );
}
```

---

## 🔐 Security Baselines

### Environment Variable Sanitization

```typescript
// ✅ CORRECT: Variables orchestrated via .env definitions
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;

// ❌ CRITICAL: Exposed cleartext secrets
const supabaseUrl = "https://myproject.supabase.co";
```

### Payload Validation

```typescript
// ✅ CORRECT: Standardize rigorous input sanitization parameters
function sanitizeInput(input: string): string {
  return input.trim().replace(/<script>/gi, ""); // Or delegate to DOMPurify
}
```
