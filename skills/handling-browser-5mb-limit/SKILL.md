---
name: Handling Browser 5MB Limit Error
description: |
  Cómo prevenir y recuperarse de errores HTTP 400 y 401 causados por el límite de 5 Megabytes de Vertex AI al procesar capturas de pantalla de la herramienta browser_subagent.
---

# Handling Browser 5MB Limit Error (image exceeds 5 MB maximum)

## 📌 Contexto del Problema

El motor de inteligencia artificial subyacente (Vertex AI) tiene un **límite inamovible de 5 Megabytes por payload de imagen**.

Cosas que detonan este crash inmediatamente:

1. Ordenar al `browser_subagent` hacer un scroll largo tomando capturas de pantalla de toda la página ("Take a full page screenshot by scrolling down").
2. Solicitar al sub-agente capturar componentes web con muchísima carga de alta definición, gradientes, y overlays simultáneos.
3. Acumular más de 2 capturas de pantalla de un monitor moderno en una sola interacción (Response).

El error reportado luce exactamente así:
`messages.62.content.1.tool_result.content.1.image.source.base64: image exceeds 5 MB maximum: 6255808 bytes > 5242880 bytes` y suele devolver un HTTP 400 Bad Request o HTTP 401 Unauthorized.

## 🛑 Acciones Preventivas (ANTES de usar el Browser Subagent)

Cuando decidas auditar visualmente una aplicación usando el navegador temporal, **SIEMPRE agrega estas limitantes de forma EXPLÍCITA en tu TaskPrompt**:

1. **PROHIBIDO EL SCROLL INFINITO (Full-Page Screenshot)**: Nunca le pidas revisar la estructura haciendo screenshot de cada pedazo.
2. **PRIORIZA EL DOM**: Para auditorías de texto y clases HTML, instruye al sub-agente específicamente usar `browser_get_dom`.
3. **MÁXIMO 1 o 2 SCREENSHOTS**: Añade como directriz estricta dentro del prompt enviado a tu sub-hermano: _"CRITICAL: Do NOT return more than 1 or 2 screenshots total to avoid crashing the AI engine. Use DOM reading for the rest of your context."_
4. **VERSIONES MÓVIL/DESKTOP SEPARADAS**: Nunca le ordenes hacer Resize -> Screenshot -> Resize -> Screenshot repetitivamente. Pídelo en iteraciones distintas o tareas en paralelo mitigado.

## 🛠️ Acciones Reactivas (QUÉ HACER SI YA SUCEDIÓ)

Si durante tu planificación un usuario te envía un error 400/401 con este footprint (TraceID), significa que tú mismo has roto la memoria con tus request visuales:

1. **Reconoce Inmediatamente la Causa**: No mientas al usuario, explícale que las imágenes devueltas pesaban más de 5MB.
2. **Usa Otras Herramientas**: Detén momentáneamente la "auditoría visual completa". Descansa el contexto.
3. **Re-Audita Exclusivamente Analítica (DOM)**: Lanza de nuevo al `browser_subagent` pero con la orden severa: `"DO NOT take any screenshots at all. Try to describe what you see exclusively by reading the DOM (classes, ids, texts)."`.
4. **Confía en el Feedback del Usuario**: Si el sub-agente falló por memoria visual, pregúntale al usuario lo que vio él en su pantalla para parchear con código (`view_file`, `multi_replace`).

---

**Recuerda**: Somos eficientes escribiendo código, no consumiendo la memoria de Google intentando ver páginas web de 10000 píxeles de alto en una sola vista.
