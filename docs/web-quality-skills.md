# 🌐 Web Quality Skills (Addy Osmani)

A collection of Agent Skills for optimizing web projects based on **Google Lighthouse** guidelines and **Core Web Vitals** best practices.

## Overview

These skills encode the collective wisdom of hundreds of Lighthouse audits and real-world performance engineering. They are framework-agnostic and designed to help you build performant, accessible, and SEO-optimized web applications.

## Available Skills

| Skill                   | Trigger Phrases                                 | Key Focus                                            |
| ----------------------- | ----------------------------------------------- | ---------------------------------------------------- |
| **`wq-audit`**          | "audit my site", "quality review", "lighthouse" | Complete orchestrator for all web quality aspects.   |
| **`wq-performance`**    | "speed up", "optimize performance", "load time" | Loading speed, JS bundling, image/font optimization. |
| **`wq-cwv`**            | "Core Web Vitals", "LCP", "INP", "CLS"          | Specific Google Search ranking metrics.              |
| **`wq-accessibility`**  | "accessibility", "a11y", "WCAG"                 | WCAG 2.1 compliance and assistive technologies.      |
| **`wq-seo`**            | "SEO", "search optimization", "meta tags"       | Technical/On-page SEO and structured data.           |
| **`wq-best-practices`** | "best practices", "security audit", "modern"    | Security headers, modern APIs, and code health.      |

## Usage Examples

### 1. Full Audit

> "Perform a full `wq-audit` of this codebase and prioritize the critical issues."

### 2. Performance Deep Dive

> "My LCP is high. Use `wq-cwv` to identify the cause and suggest fixes."

### 3. Accessibility Review

> "Run an `wq-accessibility` check on this component and ensure WCAG compliance."

### 4. SEO & Structured Data

> "Help me implement JSON-LD for this product page using `wq-seo`."

---

## Technical Thresholds (Targets)

- **Performance Score**: ≥ 90
- **Accessibility Score**: 100
- **SEO Score**: ≥ 95
- **LCP**: ≤ 2.5s
- **INP**: ≤ 200ms
- **CLS**: ≤ 0.1

---

## Attribution

Original skills by [Addy Osmani](https://github.com/addyosmani/web-quality-skills).
Integrated into Antigravity for automated web quality engineering.
