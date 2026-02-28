# Architecture Rules - Venezuela News App

## Project Structure

### Directory Organization

```
src/
├── app/                    # Next.js App Router pages
│   ├── (routes)/          # Route groups
│   ├── api/               # API routes
│   └── layout.tsx         # Root layout
├── components/            # React components
│   ├── home/             # Landing page components
│   ├── news/             # News feed components
│   ├── layout/           # Layout components (Header, Footer)
│   └── ui/               # shadcn/ui components
├── lib/                  # Utilities and configurations
│   ├── api/             # API client functions
│   ├── utils/           # Helper functions
│   └── constants/       # Constants and config
└── types/               # TypeScript type definitions
```

### Component Organization

#### Feature-Based Structure

- Group related components by feature
- Each feature has its own directory
- Shared components go in `/components/ui`

#### Component Rules

- One component per file
- File name matches component name (PascalCase)
- Export as named export (not default)
- Co-locate types with components when feature-specific

### Naming Conventions

#### Files

- **Components**: `PascalCase.tsx` (e.g., `NewsFeed.tsx`)
- **Utilities**: `kebab-case.ts` (e.g., `format-date.ts`)
- **Constants**: `SCREAMING_SNAKE_CASE.ts` (e.g., `API_ENDPOINTS.ts`)
- **Types**: `PascalCase.types.ts` (e.g., `Article.types.ts`)

#### Code

- **Variables**: `camelCase`
- **Functions**: `camelCase`
- **Components**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Types/Interfaces**: `PascalCase`

---

## Component Standards

### Server vs Client Components

#### Default to Server Components

```typescript
// Server Component (default)
export function ArticleList() {
  // Can fetch data directly
  const articles = await fetchArticles();
  return <div>{/* ... */}</div>;
}
```

#### Use Client Components Only When Needed

```typescript
"use client"; // Only when using hooks, event handlers, browser APIs

export function InteractiveButton() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

**Use "use client" for**:

- `useState`, `useEffect`, `useContext`
- Event handlers (`onClick`, `onChange`, etc.)
- Browser APIs (`window`, `document`, `localStorage`)
- Third-party libraries that use hooks

### TypeScript Standards

#### Props Interface

```typescript
// ✅ CORRECT: Use interface for props
interface ArticleCardProps {
  title: string;
  description: string;
  image?: string; // Optional with ?
  onClick?: () => void;
}

// ❌ WRONG: Don't use type for props
type ArticleCardProps = {
  title: string;
};
```

#### Type Safety

```typescript
// ✅ CORRECT: Proper typing
const articles: Article[] = await fetchArticles();

// ❌ WRONG: Using any
const articles: any = await fetchArticles();

// ✅ CORRECT: Use unknown if truly unknown
const data: unknown = JSON.parse(response);
if (isArticle(data)) {
  // Type guard
  const article: Article = data;
}
```

---

## Styling Standards

### Tailwind CSS

#### Use Utility Classes

```typescript
// ✅ CORRECT: Tailwind utilities
<div className="flex items-center gap-4 p-6 rounded-lg bg-white dark:bg-zinc-900">

// ❌ WRONG: Inline styles
<div style={{ display: 'flex', padding: '24px' }}>
```

#### Semantic Color Tokens

```typescript
// ✅ CORRECT: Use semantic tokens
<div className="bg-primary text-primary-foreground">

// ❌ WRONG: Hardcoded colors
<div className="bg-blue-500 text-white">
```

#### Responsive Design

```typescript
// ✅ CORRECT: Mobile-first responsive
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">

// Test breakpoints: 375px, 768px, 1024px, 1440px
```

### Dark Mode

```typescript
// ✅ CORRECT: Dark mode support
<div className="bg-white dark:bg-zinc-900 text-zinc-900 dark:text-white">

// Always test both light and dark modes
```

---

## Data Fetching

### API Routes

```typescript
// src/app/api/articles/route.ts
export async function GET(request: Request) {
  try {
    const articles = await fetchFromSupabase();
    return Response.json(articles);
  } catch (error) {
    return Response.json({ error: "Failed to fetch" }, { status: 500 });
  }
}
```

### Client-Side Fetching

```typescript
// Use SWR or React Query for client-side fetching
import useSWR from 'swr';

export function ArticleList() {
  const { data, error, isLoading } = useSWR('/api/articles', fetcher);

  if (isLoading) return <LoadingState />;
  if (error) return <ErrorState />;
  return <ArticleGrid articles={data} />;
}
```

---

## SEO Standards

### Metadata

```typescript
// app/noticias/[slug]/page.tsx
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

### Semantic HTML

```typescript
// ✅ CORRECT: Semantic elements
<article>
  <header>
    <h1>{title}</h1>
    <time dateTime={publishedAt}>{formatDate(publishedAt)}</time>
  </header>
  <section>
    <p>{content}</p>
  </section>
</article>

// ❌ WRONG: Generic divs
<div>
  <div>{title}</div>
  <div>{content}</div>
</div>
```

---

## Performance Standards

### Image Optimization

```typescript
// ✅ CORRECT: Next.js Image component
import Image from 'next/image';

<Image
  src={article.image}
  alt={article.title}
  width={1200}
  height={630}
  priority={isFeatured}
  placeholder="blur"
  blurDataURL={article.blurDataURL}
/>

// ❌ WRONG: Regular img tag
<img src={article.image} alt={article.title} />
```

### Code Splitting

```typescript
// ✅ CORRECT: Dynamic imports for heavy components
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <ChartSkeleton />,
  ssr: false, // If component uses browser APIs
});
```

---

## Error Handling

### Try-Catch Blocks

```typescript
// ✅ CORRECT: Proper error handling
async function fetchArticles() {
  try {
    const response = await fetch("/api/articles");
    if (!response.ok) throw new Error("Failed to fetch");
    return await response.json();
  } catch (error) {
    console.error("Error fetching articles:", error);
    throw error; // Re-throw for caller to handle
  }
}
```

### Error Boundaries

```typescript
// app/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

---

## Security Standards

### Environment Variables

```typescript
// ✅ CORRECT: Use env variables
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;

// ❌ WRONG: Hardcoded credentials
const supabaseUrl = "https://myproject.supabase.co";
```

### Input Validation

```typescript
// ✅ CORRECT: Validate user input
function sanitizeInput(input: string): string {
  return input.trim().replace(/<script>/gi, "");
}
```

---

**End of Architecture Rules**
