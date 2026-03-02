---
name: i18n-localization
description: Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support.
allowed-tools: Read, Glob, Grep
---

---

---

---

```tsx
import { useTranslation } from 'react-i18next';

```tsx
import { useTranslations } from 'next-intl';

```python
from gettext import gettext as _

---

```
locales/
├── en/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
├── tr/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
└── ar/          # RTL
    └── ...
```

---

---

---

```css
/* CSS Logical Properties */
.container {
  margin-inline-start: 1rem;  /* Not margin-left */
  padding-inline-end: 1rem;   /* Not padding-right */
}

---

---

# i18n e localização

> Melhores práticas de Internacionalização (i18n) e Localização (L10n).

## 1. Conceitos Básicos

| Prazo | Significado |
|------|---------|
| **i18n** | Internacionalização - tornando o aplicativo traduzível |
| **L10n** | Localização - traduções reais |
| **Localidade** | Idioma + Região (en-US, tr-TR) |
| **RTL** | Idiomas da direita para a esquerda (árabe, hebraico) |

## 2. Quando usar i18n

| Tipo de projeto | i18n Necessário? |
|--------------|--------------|
| Aplicativo web público | ✅ Sim |
| Produto SaaS | ✅ Sim |
| Ferramenta interna | ⚠️Talvez |
| Aplicativo de região única | ⚠️Considere o futuro |
| Projeto pessoal | ❌ Opcional |

## 3. Padrões de implementação

### Reagir (react-i18next)

função Bem-vindo() {
  const { t } = useTranslation();
  retornar <h1>{t('welcome.title')}</h1>;
}
```

### Next.js (next-intl)

função padrão de exportação Page() {
  const t = useTranslations('Home');
  retornar <h1>{t('título')}</h1>;
}
```

### Python (gettexto)

print(_("Bem vindo ao nosso aplicativo"))
```

## 4. Estrutura do arquivo

## 5. Melhores práticas

### FAÇA ✅

- Use chaves de tradução, não texto bruto
- Traduções de namespace por recurso
- Apoiar a pluralização
- Lidar com formatos de data/número por localidade
- Planeje o RTL desde o início
- Use o formato de mensagem ICU para strings complexas

### NÃO ❌

- Strings codificadas em componentes
- Concatenar strings traduzidas
- Assuma o comprimento do texto (o alemão é 30% maior)
- Esqueça o layout RTL
- Misture idiomas no mesmo arquivo

## 6. Problemas comuns

| Edição | Solução |
|-------|----------|
| ausente tradução | Retorno ao idioma padrão |
| Strings codificadas | Use script linter/verificador |
| Formato de data | Usar Intl.DateTimeFormat |
| Formato numérico | Usar Intl.NumberFormat |
| Pluralização | Use formato de mensagem ICU |

## 7. Suporte RTL

[dir="rtl"] .icon {
  transformar: escalaX(-1);
}
```

## 8. Lista de verificação

Antes do envio:

- [] Todas as strings voltadas para o usuário usam chaves de tradução
- [] Existem arquivos de localidade para todos os idiomas suportados
- [] A formatação de data/número usa API internacional
- [] Layout RTL testado (se aplicável)
- [] Idioma substituto configurado
- [] Nenhuma string codificada nos componentes

## Roteiro

| Roteiro | Finalidade | Comando |
|--------|---------|---------|
| `scripts/i18n_checker.py` | Detectar strings codificadas e traduções ausentes | `python scripts/i18n_checker.py <project_path>` |