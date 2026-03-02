import os
from deep_translator import GoogleTranslator

base_dir = '/Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/skills'

es_translator = GoogleTranslator(source='en', target='es')
pt_translator = GoogleTranslator(source='en', target='pt')

def translate_markdown(content, translator):
    paragraphs = content.split('\n\n')
    translated_paragraphs = []
    current_chunk = ""
    for p in paragraphs:
        if p.startswith('```') or p.startswith('---'):
            translated_paragraphs.append(p)
            continue
        if len(current_chunk) + len(p) < 4500:
            current_chunk += p + '\n\n'
        else:
            try:
                translated = translator.translate(current_chunk)
                translated_paragraphs.append(translated)
            except:
                translated_paragraphs.append(current_chunk)
            current_chunk = p + '\n\n'
    if current_chunk:
        try:
            translated = translator.translate(current_chunk)
            translated_paragraphs.append(translated)
        except:
            translated_paragraphs.append(current_chunk)
    return '\n\n'.join(translated_paragraphs)

skill_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f == 'SKILL.md':
            skill_files.append(os.path.join(root, f))

print(f"Found {len(skill_files)} SKILL.md files to process.")

for path in skill_files:
    es_path = path.replace('SKILL.md', 'SKILL.es.md')
    pt_path = path.replace('SKILL.md', 'SKILL.pt.md')
    
    # Check if they already exist to skip
    if os.path.exists(es_path) and os.path.exists(pt_path):
        continue
        
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Translating {path} to ES...")
        with open(es_path, 'w', encoding='utf-8') as f:
            f.write(translate_markdown(content, es_translator))
            
        print(f"Translating {path} to PT...")
        with open(pt_path, 'w', encoding='utf-8') as f:
            f.write(translate_markdown(content, pt_translator))
    except Exception as e:
        print(f"Failed on {path}: {str(e)}")

print("Done translating all missing files.")
