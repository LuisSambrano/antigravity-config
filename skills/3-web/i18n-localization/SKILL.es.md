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

# i18n y localización

> Mejores prácticas de Internacionalización (i18n) y Localización (L10n).

## 1. Conceptos básicos

| Término | Significado |
|------|---------|
| **i18n** | Internacionalización: hacer que la aplicación sea traducible |
| **L10n** | Localización - traducciones actuales |
| **Configuración regional** | Idioma + Región (en-US, tr-TR) |
| **RTL** | Idiomas de derecha a izquierda (árabe, hebreo) |

## 2. Cuándo utilizar i18n

| Tipo de proyecto | ¿Se necesita i18n? |
|--------------|--------------|
| Aplicación web pública | ✅ Sí |
| Producto SaaS | ✅ Sí |
| Herramienta interna | ⚠️ Quizás |
| Aplicación de región única | ⚠️ Considere el futuro |
| Proyecto personal | ❌ Opcional |

## 3. Patrones de implementación

### Reaccionar (reaccionar-i18siguiente)

función Bienvenido() {
  const { t } = usarTraducción();
  return <h1>{t('bienvenido.título')}</h1>;
}
```

### Next.js (siguiente-intl)

exportar función predeterminada Página() {
  const t = useTranslations('Inicio');
  devolver <h1>{t('título')}</h1>;
}
```

### Python (obtener texto)

print(_("Bienvenido a nuestra aplicación"))
```

## 4. Estructura de archivos

## 5. Mejores prácticas

### HACER ✅

- Utilice claves de traducción, no texto sin formato.
- Traducciones de espacios de nombres por característica
- Apoyar la pluralización
- Manejar formatos de fecha/número por localidad
- Planifique RTL desde el principio
- Utilice el formato de mensaje ICU para cadenas complejas

### NO LO HAGAS ❌

- Codificar cadenas en componentes.
- Concatenar cadenas traducidas
- Asuma la longitud del texto (el alemán es un 30% más largo)
- Olvídate del diseño RTL
- Mezclar idiomas en el mismo archivo

## 6. Problemas comunes

| Problema | Solución |
|-------|----------|
| desaparecido traducción | Volver al idioma predeterminado |
| Cadenas codificadas | Utilice el script linter/checker |
| Formato de fecha | Utilice formato internacional de fecha y hora |
| Formato de número | Utilice formato de número internacional |
| Pluralización | Utilice el formato de mensaje de la UCI |

## 7. Soporte RTL

[dir="rtl"] .icono {
  transformar: escalaX(-1);
}
```

## 8. Lista de verificación

Antes del envío:

- [] Todas las cadenas de cara al usuario utilizan claves de traducción
- [] Existen archivos locales para todos los idiomas admitidos
- [] El formato de fecha/número utiliza API internacional
- [] Diseño RTL probado (si corresponde)
- [] Idioma alternativo configurado
- [] No hay cadenas codificadas en los componentes

## guión

| Guión | Propósito | Comando |
|--------|---------|---------|
| `scripts/i18n_checker.py` | Detectar cadenas codificadas y traducciones faltantes | `python scripts/i18n_checker.py <ruta_proyecto>` |