# Content Standards - Venezuela News App

## Article Requirements

### Word Count

- **News Articles**: 800-1500 words
- **Analysis Pieces**: 1200-2000 words
- **Breaking News**: 400-600 words (exception)
- **Opinion/Editorial**: 1000-1800 words

### Structure

#### Standard Article

1. **Headline** (60-70 characters)
   - Clear, compelling, SEO-optimized
   - Include focus keyword
2. **Lead Paragraph** (100-150 words)
   - Answer: Who, What, When, Where, Why, How
   - Hook the reader immediately
   - Include focus keyword naturally
3. **Body** (600-1200 words)
   - 3-5 sections with H2 headers
   - Each section 200-300 words
   - Supporting details and context
   - Quotes from sources (if applicable)
   - Data/statistics with sources
   - Internal links to related articles
4. **Conclusion** (100-150 words)
   - Summary of key points
   - Future implications
   - Call to action (if applicable)

### SEO Requirements

#### Metadata

- **Meta Title**: 50-60 characters (include focus keyword)
- **Meta Description**: 150-160 characters (compelling, includes keyword)
- **Focus Keyword**: In title, first paragraph, and 2-3 times in body
- **Keyword Density**: 1-2% (natural, not forced)

#### Links

- **Internal Links**: 2-3 to related articles
- **External Links**: 1-2 to authoritative sources
- **Anchor Text**: Descriptive, not "click here"

#### Images

- **Featured Image**: 1200x630px minimum (Open Graph)
- **In-Body Images**: 2-3 relevant images
- **Alt Text**: Descriptive, includes keyword when relevant
- **File Names**: Descriptive, kebab-case (e.g., `venezuela-economy-2026.jpg`)

### JSON-LD Structured Data

**All articles MUST include NewsArticle schema**:

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Article Title (max 110 characters)",
  "description": "Article description (150-160 characters)",
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/image.jpg",
    "width": 1200,
    "height": 630
  },
  "datePublished": "2026-02-02T10:00:00-04:00",
  "dateModified": "2026-02-02T15:30:00-04:00",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author/author-name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "M&T Venezuela",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-slug"
  }
}
```

### Quality Checklist

**Before publishing, verify**:

- [ ] Word count meets minimum (800+ for standard articles)
- [ ] Proper heading hierarchy (H1 → H2 → H3, no skipping)
- [ ] Lead paragraph answers 5 W's + How
- [ ] At least 3 body sections with H2 headers
- [ ] Conclusion summarizes key points
- [ ] Meta title written (50-60 chars)
- [ ] Meta description written (150-160 chars)
- [ ] Focus keyword optimized (title, first para, 2-3x in body)
- [ ] Featured image added (1200x630px min)
- [ ] All images have descriptive alt text
- [ ] 2-3 internal links to related articles
- [ ] 1-2 external links to authoritative sources
- [ ] JSON-LD NewsArticle schema included
- [ ] No spelling or grammar errors
- [ ] Facts verified and sources cited
- [ ] Dates and numbers double-checked

### Google News Compliance

#### Requirements

- **Author Attribution**: Clear author name and bio
- **Publication Date**: Visible and in ISO 8601 format
- **Original Content**: No plagiarism, unique perspective
- **Factual Accuracy**: All claims verified
- **Transparency**: Sources cited, corrections noted
- **Contact Information**: Author/editorial contact available

#### Prohibited

- ❌ Clickbait headlines
- ❌ Misleading information
- ❌ Unverified rumors
- ❌ Plagiarized content
- ❌ Excessive ads interrupting content
- ❌ Auto-playing videos with sound

---

## Documentation Standards

### README Files

- **English**: `README.md` (primary)
- **Spanish**: `README.es.md` (translation)
- Both files must be kept in sync
- Language switcher at top of both files

### Code Comments

- Explain **WHY**, not just WHAT
- Document complex logic
- Note performance considerations
- Reference issues/PRs when applicable

---

## Component Standards

### File Naming

- Use PascalCase for components: `NewsFeed.tsx`, `ArticleCard.tsx`
- Use kebab-case for utilities: `format-date.ts`, `fetch-news.ts`
- Use SCREAMING_SNAKE_CASE for constants: `API_ENDPOINTS.ts`

### Component Structure

```typescript
// 1. Imports (grouped: React, Next.js, third-party, local)
import { useState } from "react";
import Image from "next/image";
import { motion } from "framer-motion";
import { formatDate } from "@/lib/utils";

// 2. Types/Interfaces
interface ArticleCardProps {
  title: string;
  description: string;
  image: string;
  date: string;
}

// 3. Component
export function ArticleCard({ title, description, image, date }: ArticleCardProps) {
  // 4. Hooks
  const [isHovered, setIsHovered] = useState(false);

  // 5. Handlers
  const handleClick = () => {
    // ...
  };

  // 6. Render
  return (
    // ...
  );
}
```

### TypeScript Standards

- Always use `interface` for props (not `type`)
- Use `type` for unions, intersections, utilities
- Never use `any` (use `unknown` if truly unknown)
- Enable strict mode in tsconfig.json

---

**End of Content Standards**
