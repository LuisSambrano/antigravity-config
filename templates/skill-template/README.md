# How to Use This Template

## Quick Start

1. Copy this entire folder to `skills/<category>/your-skill-name/`
2. Edit `SKILL.md` with your skill content
3. Update the YAML frontmatter
4. Add to `skills/INDEX.md`
5. Submit a PR

## Folder Structure

```
your-skill-name/
├── SKILL.md          # Required: Main skill file
├── README.md         # Optional: This file (can delete)
├── examples/         # Optional: Example files
└── scripts/          # Optional: Helper scripts
```

## YAML Frontmatter

Required fields:

- `name`: Skill identifier (kebab-case)
- `version`: Semantic version
- `description`: One-line summary
- `category`: Where this skill lives
- `author`: Your GitHub username

Optional fields:

- `tags`: Search keywords
- `license`: Default MIT
- `requires`: Dependent skills

## Tips

- Keep SKILL.md focused and actionable
- Include real code examples
- Link to external documentation
- Test your skill locally before submitting
