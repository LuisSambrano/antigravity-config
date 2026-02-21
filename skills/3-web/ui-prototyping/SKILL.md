---
name: ui-prototyping
description: UI/UX prototyping workflow using generate_image tool. Use when the user wants to design mockups, wireframes, or visual prototypes before coding.
---

# UI/UX Prototyping with generate_image

Create visual mockups and iterate on UI designs before writing code.

## When to Use

- User says "diseña una UI", "crea un mockup", "prototipa esto"
- Before building complex UI components
- When the user wants to visualize a layout before coding

## Workflow

### 1. Understand Requirements

- What is the purpose of the page/component?
- Who is the target audience?
- What is the design style? (glassmorphism, minimal, brutalist, etc.)
- Mobile-first or desktop-first?

### 2. Generate Initial Mockup

Use `generate_image` with a detailed prompt describing:

- Layout structure (header, sidebar, content area, footer)
- Color palette and style
- Key UI elements (buttons, cards, forms, tables)
- Typography preferences
- Dark/light mode

### 3. Iterate on Feedback

Refine the design based on user feedback using follow-up `generate_image` calls with adjustments.

### 4. Extract Design Tokens

From the approved mockup, define:

- Color variables (CSS custom properties)
- Spacing scale
- Typography scale
- Border radius, shadows
- Component patterns

### 5. Implement

Translate the approved mockup into code using the established design tokens.

## Prompt Tips

- Be specific about layout ("3-column grid with sidebar")
- Reference known design systems ("inspired by Linear/Notion/Vercel")
- Specify exact colors when possible ("use #0A0A0A background")
- Include content examples, not Lorem Ipsum
- Specify dark mode with glass effects if using glassmorphism

## Anti-Patterns

- ❌ Generating before understanding requirements
- ❌ Coding before getting mockup approval
- ❌ Using placeholder text in final mockups
- ❌ Ignoring mobile responsiveness in prototypes
