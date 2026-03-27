---
description: Create, update, sync, and audit NotebookLM project notebooks. Serves as the Universal Command for initiating ideas, running deep research, and managing living product architecture memory.
---

# /notebook — Universal Product Memory Workflow

Flujo de trabajo oficial para administrar los portafolios y proyectos mediante NotebookLM. Convierte ideas crudas en estructuras profesionales de Product Architecture. Trabaja de manera conjunta con la skill `notebooklm` (lee el SKILL.md para ver plantillas, convenciones de nombres y reglas de tono estricto).

## Prerequisites
- CLI de `nlm` instalada y autenticada (`nlm auth status`). Si la sesión expira o es la primera vez, usa `nlm login`.

---

## Comandos del Workflow

### 1. `/notebook init [Nombre o Concepto]`

**Uso**: Generar inmediatamente un "cerebro de proyecto" cuando el usuario presenta una idea base o solicita un nuevo proyecto. Esto hace el trabajo inicial de todo un equipo de desarrollo / arquitectura.

**Pasos de Ejecución Automática por Antigravity:**

1. **Crear Notebook**:
   ```bash
   nlm notebook create "[Nombre del Proyecto]"
   ```
2. **Generar Archivos Iniciales**: 
   Crea localmente en `/tmp/nlm_[proyecto]/` los documentos base definidos en la skill (01-Brief, 02-UX, 03-Arquitectura, 04-Features, 05-Infraestructura). Con el poco contexto de la idea, elabora hipótesis iniciales (fase conceptual 💭).
3. **Subir Fuentes al Notebook**:
   ```bash
   nlm source add <notebook-id> --file /tmp/nlm_[proyecto]/NN-file.md --title "NN — Título" --wait
   ```
4. **Disparar Deep Research Obligatorio**: 
   Basado en el brief inicial, lanza de forma autónoma una investigación para completar "lo que falta" (benchmarks, viabilidad técnica de la idea, stack recomendado).
   ```bash
   nlm research start <notebook-id> "Investiga a profundidad el mercado, los stacks técnicos recomendados y ejemplos similares para construir el proyecto descrito en el Source 01."
   ```
5. **Reportar**: Entrega al usuario el ID del notebook y notifica que el Deep Research está corriendo. Sugiere usar `nlm research import` cuando termine.

---

### 2. `/notebook sync [Nombre del Proyecto]`

**Uso**: Mantener el libro de NotebookLM sincronizado con el código base actual, deploy o decisiones de diseño que existan en el ecosistema real. Evita que la memoria se oxide.

**Pasos:**
1. **Identificar**:
   ```bash
   nlm notebook list
   ```
2. **Descargar Estado Actual**:
   ```bash
   nlm source content <source-id> -o /tmp/nlm_sync/NN-current.md
   ```
3. **Contrastar Localmente**:
   Verifica el código real del proyecto (`package.json`, esquemas de base de datos, URLs de despliegue, Vercel) y compara con lo descargado.
4. **Reescribir Stale Sources**: Modifica el markdown localmente donde haya discrepancia (ej. Features que pasaron de ⚠ a ✔ porque ya fueron codeadas; stack actualizado). **Aplicando el tono estricto**.
5. **Reemplazo Atómico**:
   ```bash
   nlm source delete <old-source-id> -y
   nlm source add <notebook-id> --file /tmp/nlm_sync/NN-updated.md --title "NN — Título" --wait
   ```
6. **Reportar**: Informa qué fuentes fueron actualizadas y por qué.

---

### 3. `/notebook log [Nombre del Proyecto]`

**Uso**: Añadir un registro tras una sesión de lluvia de ideas, depuración (debugging), o decisión de producto crítico (como elegir un servicio BaaS o cambiar una regla UX). Equivale a un ADR (Architecture Decision Record).

**Pasos:**
1. **Determinar la Secuencialidad**:
   Busca las fuentes existentes (`nlm source list`) y determina el número `NN` más alto para seguir la secuencia (ej. si hay 06, el siguiente es el 07).
2. **Crear el Archivo de Bitácora**:
   Plantilla base:
   ```markdown
   # NN — Bitácora: YYYY-MM-DD [Tema/Decisión]

   **Última Actualización**: YYYY-MM-DD
   
   ## Contexto de la Sesión
   [Describir de qué se hablaba o el bug a resolver]

   ## Decisiones Arquitectónicas (ADRs)
   | Decisión | Razón / Ventaja | Consecuencia a largo plazo |
   |----------|-----------------|----------------------------|
   | [X]      | [Por qué]       | [Afecta BD y Auth]         |

   ## Próximos pasos de Ejecución
   - Tareas derivadas.
   ```
3. **Subir Fuente**:
   ```bash
   nlm source add <notebook-id> --file /tmp/nlm_log/NN-bitacora.md --title "NN — Bitácora: YYYY-MM-DD [Tema]" --wait
   ```
4. **Trigger**: Si la decisión descrita en la bitácora invalida una arquitectura pasada (03) o cambia una funcionalidad (04), el agente debe proseguir invocando un **Sync inverso** para actualizar dichas capas fundamentales.

---

### 4. `/notebook audit [Nombre del Proyecto]`

**Uso**: Pasar un "Linter Humano" a la documentación para asegurar que la calidad de la información del proyecto sea premium, ejecutiva y libre de sesgos de ventas o estados mentirosos. 

**Pasos:**
1. Descarga del notebook entero a `/tmp/`. 
2. **Tone Check**: Buscar por superlativos ("ultra", "increíble", "el mejor"), promesas absolutas ("imposible de") y adjetivos marketing.
3. **State Check**: Revisa todas las flags de feature `✔ Operativo`. ¿El agente puede encontrar el commit / URL que lo verifica? Si no, se degrada a `⚠ En pruebas`.
4. **Reporte**: Genera archivo o comentario de GitHub indicando violaciones. Reescribe y resube si se autoriza automático.

## Filosofía Operativa (Zero Friction Context)

Cuando Antigravity, Gemini, o Stitch entren en contexto sin memoria asíncrona, basta con enviarles la orden: 
*"Lee el notebook [ID] y basate estricamente en él para seguir mi requerimiento"*. 

Con esto, el framework Open Source asegura de que ningún desarrollador, UI Architect o Project Manager deba escribir especificaciones manuales de nuevo para un Agente IA. Todo nace, vive y se audita en el libro.
