import os
import re
def parse_skill_md(file_path):
    """Parses a SKILL.md file to extract name and description."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to parse YAML frontmatter with regex
        yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            name_match = re.search(r'^name:\s*(.+)$', yaml_content, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', yaml_content, re.MULTILINE)
            
            name = name_match.group(1).strip() if name_match else None
            description = desc_match.group(1).strip() if desc_match else None
            
            if name and description:
                # Remove quotes if present
                name = name.strip('"').strip("'")
                description = description.strip('"').strip("'")
                return name, description

        # Fallback: Parse Markdown headers/text
        name = os.path.basename(os.path.dirname(file_path)).replace("-", " ").title()
        
        # Look for the first H1 or first few lines for description
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            name = h1_match.group(1)
            
        # Look for a paragraph after the header or frontmatter
        body = content
        if yaml_match:
            body = content[yaml_match.end():]
        
        # Simple extraction of the first sentence-like thing if description is missing
        desc_match = re.search(r'^(?!#)(.+)$', body, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else "Sin descripción disponible."
        
        return name, description
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None, None

def get_domain_category(path):
    """Heuristic to categorize skill based on path."""
    path_lower = path.lower()
    if any(k in path_lower for k in ["ai", "agent", "intelligence", "crew", "llm", "memory", "context"]):
        return "🧠 Inteligencia Artificial y Agentes"
    elif any(k in path_lower for k in ["web", "react", "nextjs", "ui", "ux", "frontend", "backend", "tailwind", "auth", "shopify", "telegram"]):
        return "💻 Desarrollo Web Moderno"
    elif any(k in path_lower for k in ["security", "vulnerability", "pen-test", "aws-security", "escalation", "injection"]):
        return "🛡️ Seguridad Ofensiva y Defensiva"
    elif any(k in path_lower for k in ["growth", "seo", "aso", "cro", "product", "marketing"]):
        return "🚀 Crecimiento y Producto"
    elif any(k in path_lower for k in ["automation", "n8n", "workflow", "maintenance", "browser", "playwright"]):
        return "🤖 Automatización (Tools)"
    elif any(k in path_lower for k in ["meta", "skill-creator", "loki", "framework"]):
        return "🧬 Meta-Skills"
    else:
        return "📦 Otros Dominios"

def generate_readme_master():
    base_path = "."
    skills_dir = os.path.join(base_path, "skills")
    
    if not os.path.exists(skills_dir):
        print(f"Error: {skills_dir} no encontrado.")
        return

    domain_mapping = {
        "🧠 Inteligencia Artificial y Agentes": [],
        "💻 Desarrollo Web Moderno": [],
        "🛡️ Seguridad Ofensiva y Defensiva": [],
        "🚀 Crecimiento y Producto": [],
        "🤖 Automatización (Tools)": [],
        "🧬 Meta-Skills": [],
        "📦 Otros Dominios": []
    }

    # Iterate skills
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            file_path = os.path.join(root, "SKILL.md")
            name, description = parse_skill_md(file_path)
            
            if name:
                rel_path = os.path.relpath(file_path, base_path)
                category = get_domain_category(rel_path)
                
                # Sanitize description (keep it to 1 line)
                if description:
                    description = description.split('\n')[0].strip()
                    if len(description) > 120:
                        description = description[:117] + "..."
                
                domain_mapping[category].append({
                    "name": name,
                    "path": rel_path,
                    "desc": description
                })

    # Build Content
    header = """# 🌌 Google Antigravity: Sistema Operativo de Inteligencia Colectiva

**Estado:** Activo | **Arquitectura:** Modular | **Idioma del Índice:** Español

Este documento es el **Mapa de Navegación Maestro**. Organiza las capacidades del sistema en dominios lógicos para facilitar la auditoría y la toma de decisiones estrátegicas.

---

## 🗺️ Mapa de Dominios
"""

    body = ""
    for domain, items in domain_mapping.items():
        if not items:
            continue
            
        body += f"\n### {domain}\n"
        for item in sorted(items, key=lambda x: x["name"]):
            body += f"*   [{item['name']}]({item['path']}): {item['desc']}\n"

    footer = """
---

## 🏗️ Convenciones del Repositorio

Consulta [docs/architecture/REPOSITORY_GOVERNANCE.md](docs/architecture/REPOSITORY_GOVERNANCE.md) para entender las reglas de contribución.

### Estructura Física:
```text
google-antigravity/
├── assets/                 # Recursos estáticos globales
├── docs/                   # Documentación de arquitectura
├── rules/                  # Reglas de linter y cursor
├── skills/                 # CATÁLOGO DE FUNCIONALIDADES
└── tools/                  # Herramientas CLI (Python/Bash)
```

> [!NOTE]
> Este índice se genera automáticamente mediante `scripts/maintenance/generate_index.py`. No editar manualmente las secciones del mapa de dominios.
"""

    with open("README_MASTER.md", "w", encoding="utf-8") as f:
        f.write(header + body + footer)

    print("README_MASTER.md actualizado correctamente.")

if __name__ == "__main__":
    generate_readme_master()
