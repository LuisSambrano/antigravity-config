import os
import glob
from deep_translator import GoogleTranslator

base_dir = '/Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/skills'
readme_files = glob.glob(f'{base_dir}/**/README.md', recursive=True)

es_translator = GoogleTranslator(source='en', target='es')
pt_translator = GoogleTranslator(source='en', target='pt')

def translate_markdown(content, translator):
    paragraphs = content.split('\n\n')
    translated_paragraphs = []
    current_chunk = ""
    for p in paragraphs:
        if p.startswith('```'):
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

for path in readme_files:
    if 'README.es.md' in path or 'README.pt.md' in path: 
        continue
    
    es_path = path.replace('README.md', 'README.es.md')
    pt_path = path.replace('README.md', 'README.pt.md')
    
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
