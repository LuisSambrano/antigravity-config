#!/usr/bin/env python3
import os
import re

def process_skill_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple Frontmatter Parser (Regex-based)
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    
    frontmatter_content = ""
    body = content
    
    if fm_match:
        frontmatter_content = fm_match.group(1)
        body = content[fm_match.end():]
    
    # Extract existing fields
    fm_dict = {}
    for line in frontmatter_content.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm_dict[key.strip()] = val.strip().strip('"').strip("'")

    # Set default metadata if missing
    folder_name = os.path.basename(os.path.dirname(file_path))
    skill_name = fm_dict.get('name') or folder_name
    description = fm_dict.get('description') or f"Antigravity skill for {skill_name}"
    version = fm_dict.get('version') or "1.0"
    author = fm_dict.get('author') or "Antigravity"

    # Reconstruct Frontmatter
    new_fm = f"""---
name: {skill_name}
description: {description}
version: {version}
author: {author}
---"""

    # Reference block
    protocol_ref = """
> [!IMPORTANT]
> This skill MUST be executed strictly under the **Omni-Architect Agent Protocol v1.0**.
> All tool executions, code modifications, and communications MUST adhere to the 13 core protocols.
"""
    
    # Check if protocol ref already exists
    if "Omni-Architect Agent Protocol" not in body:
        # Inject after first heading or at the top
        heading_match = re.search(r'^# .*\n', body)
        if heading_match:
            insert_pos = heading_match.end()
            body = body[:insert_pos] + protocol_ref + body[insert_pos:]
        else:
            body = protocol_ref + body

    # Reconstruct file
    new_content = f"{new_fm}\n\n{body.strip()}\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    skills_dir = "skills"
    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file.lower() in ["skill.md", "skill.es.md", "skill.en.md", "readme.md"] and file.endswith(".md"):
                if "/." in root: continue
                # Do not process index.md or main meta files
                if file.lower() == "index.md": continue
                process_skill_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
