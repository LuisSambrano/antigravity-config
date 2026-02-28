# 📝 Content Standards

**Version**: 1.0.0
**Status**: ACTIVE
**Level**: 2 (Content & SEO)

---

## 📰 Article Configuration

### Word Count Matrices

- **Standard News**: 800 - 1500 words
- **Analysis/In-Depth**: 1200 - 2000 words
- **Breaking Alert**: 400 - 600 words (Explicitly flagged exception)
- **Opinion/Editorial**: 1000 - 1800 words

### Structural Architecture

#### General Assembly

1. **Headline** (Target: 60-70 characters)
   - Must be engaging, clear, and explicitly SEO-optimized.
   - Must embed primary focus keyword.
2. **Lead Paragraph** (Target: 100-150 words)
   - Mandatory resolution of the "5 W's + How".
   - Primary focus keyword embedded fluidly.
3. **Core Body** (Target: 600-1200 words)
   - Separated into 3-5 distinct sub-sections using `H2` headers.
   - Section density: 200-300 words.
   - Requires verified statistics, source citations, and direct quotes.
   - Mandatory internal routing to adjacent content payloads.
4. **Conclusion** (Target: 100-150 words)
   - Aggregate summation of critical insights.
   - Explicit Call-to-Action (CTA) if contextually appropriate.

---

## 🔍 SEO Parameters

### Metadata Specifications

- **Meta Title**: 50-60 characters (Must contain focus keyword).
- **Meta Description**: 150-160 characters (Must contain focus keyword and prompt engagement).
- **Keyword Distribution**: Headline, H1, Lead Paragraph, and 2-3 organic placements within the Core Body.
- **Density Index**: 1% to 2% max threshold (Avoid keyword stuffing metrics).

### Link Architecture

- **Internal Ingress**: 2-3 explicit bounds to related platform content.
- **External Egress**: 1-2 outbound references to high-authority/verified sources.
- **Anchor Semantics**: Links must utilize descriptive, contextual text (Prohibit arbitrary "click here" syntax).

### Media Specifications

- **OpenGraph Hero**: 1200x630px absolute minimum bounds.
- **Inline Density**: 2-3 auxiliary images supporting the Core Body.
- **Alt Processing**: Meaningful contextual string; inject focus keyword natively only if relevant to the graphic.
- **File Nomenclature**: Kebab-case formatting, highly descriptive (e.g., `venezuela-economy-report-2026.jpg`).

---

## 🧩 JSON-LD Structured Data

**MANDATORY**: All article renders must aggressively inject `NewsArticle` schema formatting.

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Article Title (Max 110 characters strict limit)",
  "description": "Article summary data (150-160 characters bounds)",
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/asset-url.jpg",
    "width": 1200,
    "height": 630
  },
  "datePublished": "2026-02-02T10:00:00-04:00",
  "dateModified": "2026-02-02T15:30:00-04:00",
  "author": {
    "@type": "Person",
    "name": "Author Full Name",
    "url": "https://example.com/author/author-name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Legal Entity",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo-asset.png",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/canonical-article-slug"
  }
}
```

---

## ✅ Content Quality Gate

**Pre-Flight Verification Protocol**:

- [ ] Volume density achieves minimum bounds (800+ standard).
- [ ] Heading hierarchy parses linearly (`H1` → `H2` → `H3`). No skipped depths.
- [ ] Lead density fulfills 5W+H requirements.
- [ ] Minimum 3 `H2` segmented divisions present.
- [ ] Meta Title within 50-60 character bounds.
- [ ] Meta Description within 150-160 character bounds.
- [ ] Focus keyword mapped sequentially (Title, Lead, x2 Body).
- [ ] Hero graphic uploaded and satisfies 1200x630px requirements.
- [ ] Alt tags mapped to 100% of injected graphical assets.
- [ ] Link topology validated (2 internal, 1 external minimum).
- [ ] `NewsArticle` JSON-LD payload injected and syntax verified.
- [ ] Grammar/Linter pass cleared.

---

## 🏛️ Google News Aggregation Parameters

### Enforcement Requirements

- **Origin Attribution**: Explicit author identity and biographic payload.
- **Temporal Stamping**: ISO 8601 formatting explicitly rendered.
- **Originality Matrix**: Deeply verified unique perspective; zero plagiarism tolerance.
- **Factual Integrity**: Stringent source verification algorithms applied.
- **Entity Transparency**: Corrections flagged; Publisher contact details structurally accessible.

### Absolute Prohibitions

- ❌ Manipulation/Clickbait meta-text schemas.
- ❌ Synthetically generated rumors or spoofed datasets.
- ❌ Code or content mirroring without canonical attribution/tagging.
- ❌ Interstitial or layout-shifting advertising elements.
- ❌ Autoplay audio configurations.
