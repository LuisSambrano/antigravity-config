import os
import re

def generate_index():
    base_path = "."
    skills_path = os.path.join(base_path, "skills")
    readme_path = os.path.join(base_path, "README_MASTER.md")
    
    if not os.path.exists(skills_path):
        print(f"Error: {skills_path} not found.")
        return

    # Logic to map folders to domains (simplified for now)
    # in a real scenario, this would read SKILL.md metadata
    domains = {
        "🧠 Inteligencia Artificial y Agentes": [],
        "💻 Desarrollo Web Moderno": [],
        "🛡️ Seguridad Ofensiva y Defensiva": [],
        "🚀 Crecimiento y Producto": [],
        "🤖 Automatización (Tools)": [],
        "🧬 Meta-Skills": []
    }

    # Crawl skills/ directory
    for root, dirs, files in os.walk(skills_path):
        if "SKILL.md" in files:
            skill_name = os.path.basename(root).replace("-", " ").title()
            relative_path = os.path.relpath(root, base_path)
            
            # Simple heuristic mapping based on path
            if "security" in relative_path or "vulnerability" in relative_path:
                domains["🛡️ Seguridad Ofensiva y Defensiva"].append((skill_name, relative_path))
            elif "web" in relative_path or "ui" in relative_path or "react" in relative_path:
                domains["💻 Desarrollo Web Moderno"].append((skill_name, relative_path))
            elif "ai" in relative_path or "agent" in relative_path or "crew" in relative_path:
                domains["🧠 Inteligencia Artificial y Agentes"].append((skill_name, relative_path))
            elif "growth" in relative_path or "seo" in relative_path:
                domains["🚀 Crecimiento y Producto"].append((skill_name, relative_path))
            elif "automation" in relative_path or "n8n" in relative_path:
                domains["🤖 Automatización (Tools)"].append((skill_name, relative_path))
            elif "meta" in relative_path or "creator" in relative_path:
                domains["🧬 Meta-Skills"].append((skill_name, relative_path))
            else:
                # Default to AI for now if unclassified
                domains["🧠 Inteligencia Artificial y Agentes"].append((skill_name, relative_path))

    print("Index mapping complete. (This script is a placeholder for actual regeneration logic)")
    print("In a complete version, it would rewrite README_MASTER.md sections between markers.")

if __name__ == "__main__":
    generate_index()
