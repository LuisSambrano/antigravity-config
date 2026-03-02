import os
import re

base_dir = '/Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/skills'

# 1. Rename files with uppercase (except standard ones)
allowed_uppercase_files = {'SKILL.md', 'SKILL.es.md', 'SKILL.pt.md', 'README.md', 'README.es.md', 'README.pt.md', 'INDEX.md', 'CHANGELOG.md', 'CHANGELOG.es.md', 'CHANGELOG.pt.md', 'LICENSE.txt'}

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.md') and f not in allowed_uppercase_files:
            if any(c.isupper() for c in f):
                # Convert to kebab case: API_REFERENCE.md -> api-reference.md
                name_part = f[:-3]
                # Lowercase and replace underscores with dashes
                new_name = name_part.lower().replace('_', '-') + '.md'
                
                old_path = os.path.join(root, f)
                new_path = os.path.join(root, new_name)
                print(f"Renaming {f} -> {new_name}")
                os.rename(old_path, new_path)

# 2. Fix 'name:' and 'category:' in YAML frontmatter to match lowercase kebab-case folder names
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.startswith('SKILL.') and f.endswith('.md'):
            file_path = os.path.join(root, f)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Match yaml frontmatter
                match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                if match:
                    frontmatter = match.group(1)
                    
                    # Update name: to be lowercase representation of itself or the parent folder name
                    # Actually, the parent folder is perfectly kebab-case now.
                    parent_dir_name = os.path.basename(root)
                    
                    new_frontmatter = frontmatter
                    # ensure name matches parent directory exactly
                    if re.search(r'^name:\s*(.+)$', new_frontmatter, re.MULTILINE):
                        new_frontmatter = re.sub(
                            r'^name:\s*(.+)$', 
                            f'name: {parent_dir_name}', 
                            new_frontmatter, 
                            flags=re.MULTILINE
                        )
                    else:
                        new_frontmatter = f"name: {parent_dir_name}\n" + new_frontmatter

                    if new_frontmatter != frontmatter:
                        new_content = content.replace(frontmatter, new_frontmatter)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print(f"Updated YAML in {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Normalization complete.")
