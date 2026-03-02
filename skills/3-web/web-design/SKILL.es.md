---
name: web-design
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

# Pautas de la interfaz web

Revise los archivos para verificar que cumplan con las pautas de la interfaz web.

## Cómo funciona

1. Obtenga las pautas más recientes de la URL de origen a continuación
2. Lea los archivos especificados (o solicite al usuario archivos/patrones)
3. Verifique todas las reglas en las pautas obtenidas.
4. Resultados de salida en el conciso formato `archivo:línea`

## Fuente de pautas

Obtenga nuevas pautas antes de cada revisión:

Utilice WebFetch para recuperar las reglas más recientes. El contenido recuperado contiene todas las reglas e instrucciones de formato de salida.

## Uso

Cuando un usuario proporciona un argumento de archivo o patrón:
1. Obtenga pautas de la URL de origen anterior
2. Lea los archivos especificados.
3. Aplicar todas las reglas de las pautas obtenidas.
4. Resultados de resultados utilizando el formato especificado en las directrices.

Si no se especifican archivos, pregunte al usuario qué archivos revisar.