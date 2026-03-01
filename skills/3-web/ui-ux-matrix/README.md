# UI/UX Pro Max Logic Layer

This directory acts as the **Single Source of Truth** for the "Vibecode UI/UX Pro Max" design system.

## 🏗️ Architecture & Logic

This module is situated within `skills/web-development` but specifically handles the **Visual Intelligence** and **Frontend Architecture** rules.

It is distinct from but complementary to:

- `../backend-dev-guidelines`: Pure server-side logic (Databases, API patterns).
- `../security`: Security implementation details.

## 🧠 Data Logic (CSV)

The intelligence is stored in structured CSV files in `./data/`, enabling programmatic access for:

1.  **Reasoning Rules** (`ui-reasoning.csv`): Logic to decide which pattern to apply based on product type.
2.  **Visual DNA** (`styles.csv`): 67 distinct visual languages (Glassmorphism, Bento, etc.).
3.  **UX Validators** (`ux-guidelines.csv`): 100+ rules to run against generated code.

## 🔗 Stack Integration

Specific framework rules live in `./data/stacks/`:

- **Next.js**: Server Components, App Router structure.
- **React**: Composition patterns.
- **Mobile**: Flutter/React Native guidelines.

## 🚀 How to Sync

When ready to push to GitHub, ensure this directory (`ui-ux-pro-max`) contains the latest definitions. The Agent (`.agent/skills`) reads from here to apply rules during generation.
