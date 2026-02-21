---
name: comic-generator
description: Generate complete AI comics from a simple idea using NotebookLM. Use when the user wants to create comics, graphic stories, or illustrated narratives.
---

# Comic Generator with AI

Automated comic creation workflow using NotebookLM.

## When to Use

- User says "genera un cómic", "crea una historia ilustrada", "haz un comic"
- User wants to create graphic narratives with AI

## Prerequisites

- NotebookLM MCP configured (`nlm` CLI available)
- `PATH` includes `/Users/luissambrano/.local/bin`

## Variables

| Variable          | Description       | Example                   |
| ----------------- | ----------------- | ------------------------- |
| `NOMBRE_HISTORIA` | Comic name        | "Tortuga vs Liebre"       |
| `IDEA_USUARIO`    | Basic idea        | "A dev who codes reality" |
| `PUBLICO`         | Audience          | niños, jóvenes, adultos   |
| `PAGINAS`         | Page count (5-20) | 12                        |
| `ESTILO`          | Visual style      | manga, cyberpunk, noir    |
| `TONO`            | Tone              | motivador, humorístico    |

## Available Styles

`manga` · `americano_90s` · `looney_tunes` · `cyberpunk` · `superhéroes` · `pixel_art` · `acuarela` · `noir`

## Steps

### 1. Create Notebook

```bash
nlm notebook create "Cómic: ${NOMBRE_HISTORIA}"
```

### 2. Upload Scriptwriter Prompt

Create and upload the master scriptwriter prompt that defines output format (cover, pages, panels, dialogue, composition).

### 3. Generate Script

Query the notebook with the user's idea, audience, pages, style, and character details. The AI generates a full technical comic script.

### 4. Save Script as Source

Add the generated script back to the notebook as a new source.

### 5. Generate Visuals

In NotebookLM browser:

1. Deselect "Scriptwriter" source, keep only the script source
2. Click Presentations → "Detailed presentation"
3. Add style instructions and generate

### 6. Download & Verify

Download as PDF/PPTX. Check: character consistency, illustration quality, narrative coherence, correct dialogue.

## Tips

- Be very specific with character visual traits
- Use known style references (Marvel, Pixar, etc.)
- Include clothing, accessories, and expression details
- Max 20 pages recommended
