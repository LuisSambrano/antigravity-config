---
name: Chrome DevTools MCP — Testing & Debugging Ultrarrápido
description: |
  Skill que prioriza automáticamente el servidor MCP chrome-devtools-mcp sobre la emulación visual (browser_subagent) para testing de UI, debugging de red/consola, y auditorías de rendimiento. Usa Chrome DevTools Protocol (CDP) directamente, eliminando la fricción de capturas de pantalla y clics emulados.
---

# Chrome DevTools MCP — Testing & Debugging Ultrarrápido

## 📌 Cuándo se Activa (Trigger Automático)

Esta skill se activa automáticamente cuando el agente necesita:

1. **Testear una interfaz web** (verificar que elementos existen, formularios funcionan, flujos de usuario son correctos)
2. **Debuggear errores** (consola del navegador, network requests, CORS, errores JS)
3. **Auditar rendimiento** (LCP, CLS, TBT, Lighthouse)
4. **Validar accesibilidad** (DOM inspection, ARIA attributes)
5. **Llenar y enviar formularios** programáticamente
6. **Ejecutar JavaScript** en el contexto de la página

## 🔴 REGLA CRÍTICA: CDP-First, Visual-Second

```
¿Necesito interactuar con un navegador?
│
├─ ¿Es para LEER datos (DOM, Network, Console, accesibilidad)?
│   └─ ✅ USAR chrome-devtools MCP (evaluate_script, list_network_requests, list_console_messages)
│
├─ ¿Es para AUTOMATIZAR acciones (clicks, formularios, navegación)?
│   └─ ✅ USAR chrome-devtools MCP (click, fill, fill_form, navigate_page, press_key)
│
├─ ¿Es para AUDITAR rendimiento?
│   └─ ✅ USAR chrome-devtools MCP (performance_start_trace, lighthouse_audit)
│
├─ ¿Es para VERIFICAR que algo SE VE bien (diseño, colores, layout)?
│   ├─ ¿Puedo verificar vía DOM/CSS?
│   │   └─ ✅ USAR chrome-devtools MCP (evaluate_script para leer computed styles)
│   └─ ¿Realmente necesito una captura visual para el usuario?
│       └─ ⚠️ USAR chrome-devtools MCP → take_screenshot (1 sola, no subagent)
│
└─ ¿Es una demostración visual para el usuario o un recording?
    └─ 🔄 USAR browser_subagent (ÚNICO caso válido — ver Skill "handling-browser-5mb-limit")
```

**NUNCA** uses `browser_subagent` para:

- Leer contenido de una página (usa `evaluate_script` o `take_snapshot`)
- Verificar si un elemento existe (usa `wait_for` o `evaluate_script`)
- Rellenar formularios (usa `fill` o `fill_form`)
- Navegar entre páginas (usa `navigate_page`)
- Inspeccionar network/consola (usa `list_network_requests`, `list_console_messages`)

## 🛠️ Herramientas Disponibles (34 tools)

### Input Automation

| Tool            | Descripción                              |
| --------------- | ---------------------------------------- |
| `click`         | Click en un elemento del DOM             |
| `drag`          | Arrastrar un elemento                    |
| `fill`          | Llenar un input específico               |
| `fill_form`     | Llenar múltiples campos de un formulario |
| `handle_dialog` | Manejar alerts/confirms/prompts          |
| `hover`         | Hover sobre un elemento                  |
| `press_key`     | Presionar una tecla (Enter, Tab, etc.)   |
| `type_text`     | Escribir texto caracter por caracter     |
| `upload_file`   | Subir un archivo a un input file         |

### Navigation

| Tool            | Descripción                                   |
| --------------- | --------------------------------------------- |
| `navigate_page` | Navegar a una URL                             |
| `new_page`      | Abrir nueva pestaña                           |
| `close_page`    | Cerrar pestaña                                |
| `list_pages`    | Listar todas las pestañas abiertas            |
| `select_page`   | Cambiar a otra pestaña                        |
| `wait_for`      | Esperar a que un selector/condición se cumpla |

### Emulation

| Tool          | Descripción                            |
| ------------- | -------------------------------------- |
| `emulate`     | Emular un dispositivo (mobile, tablet) |
| `resize_page` | Cambiar viewport size                  |

### Performance

| Tool                          | Descripción                   |
| ----------------------------- | ----------------------------- |
| `performance_start_trace`     | Iniciar trace de rendimiento  |
| `performance_stop_trace`      | Detener trace y obtener datos |
| `performance_analyze_insight` | Analizar insights del trace   |
| `take_memory_snapshot`        | Snapshot de memoria heap      |

### Network

| Tool                    | Descripción                        |
| ----------------------- | ---------------------------------- |
| `list_network_requests` | Listar todas las requests          |
| `get_network_request`   | Detalles de una request específica |

### Debugging

| Tool                    | Descripción                        |
| ----------------------- | ---------------------------------- |
| `evaluate_script`       | Ejecutar JS en la página           |
| `list_console_messages` | Listar mensajes de consola         |
| `get_console_message`   | Detalle de un mensaje específico   |
| `take_screenshot`       | Capturar screenshot (sin subagent) |
| `take_snapshot`         | Snapshot del DOM completo          |
| `lighthouse_audit`      | Auditoría Lighthouse completa      |

## 📋 Protocolos de Operación

### Protocolo 1: Testing de UI

```
1. navigate_page → URL del dev server
2. wait_for → selector del elemento clave
3. evaluate_script → verificar contenido/estado
4. fill_form → llenar formularios si aplica
5. click → interactuar con botones/links
6. list_console_messages → verificar 0 errores
7. list_network_requests → verificar responses OK
```

### Protocolo 2: Debugging

```
1. navigate_page → URL problemática
2. list_console_messages → buscar errores/warnings
3. list_network_requests → buscar requests fallidas
4. get_network_request → inspeccionar request específica
5. evaluate_script → inspeccionar estado de la app
```

### Protocolo 3: Performance Audit

```
1. navigate_page → URL a auditar
2. lighthouse_audit → auditoría completa
3. performance_start_trace → trace detallado
4. [interacciones del usuario simuladas]
5. performance_stop_trace → datos del trace
6. performance_analyze_insight → análisis de bottlenecks
```

### Protocolo 4: Responsive Testing

```
1. navigate_page → URL a testear
2. resize_page → 375x667 (mobile)
3. take_screenshot o evaluate_script → verificar layout
4. resize_page → 768x1024 (tablet)
5. resize_page → 1440x900 (desktop)
```

## ⚙️ Configuración

El servidor MCP ya está configurado en `~/.gemini/antigravity/mcp_config.json`:

```json
"chrome-devtools": {
  "command": "npx",
  "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"],
  "env": { "CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS": "true" },
  "disabled": false
}
```

### Flags Disponibles

| Flag                    | Default  | Descripción                                            |
| ----------------------- | -------- | ------------------------------------------------------ |
| `--autoConnect`         | `false`  | Conecta automáticamente a Chrome en ejecución          |
| `--headless`            | `false`  | Ejecutar sin ventana visible                           |
| `--slim`                | `false`  | Solo 3 herramientas (navegación, JS, screenshots)      |
| `--isolated`            | `false`  | Usa user-data-dir temporal                             |
| `--viewport`            | auto     | Tamaño inicial (ej. `1280x720`)                        |
| `--browserUrl`          | -        | URL de Chrome debuggable (ej. `http://127.0.0.1:9222`) |
| `--channel`             | `stable` | Canal de Chrome (`stable`, `canary`, `beta`, `dev`)    |
| `--no-performance-crux` | -        | Desactiva envío de URLs a Google CrUX API              |
| `--no-usage-statistics` | -        | Desactiva estadísticas de uso                          |

## 🔗 Integración con Otras Skills

- **`handling-browser-5mb-limit`**: Si necesitas una captura visual, usa `take_screenshot` de este MCP en lugar del `browser_subagent`, eliminando el riesgo de superar el límite de 5MB.
- **Pre-Delivery Gate**: Usa `lighthouse_audit` para verificar Performance ≥ 90 y Accessibility ≥ 95 antes de entregar.

## ⚠️ Limitaciones Conocidas

1. **No genera recordings/videos**: Para demos grabadas en video, usar `browser_subagent`
2. **No emula interacción humana visual**: Si el usuario quiere VER cómo luce el flujo paso a paso como un humano, usar `browser_subagent`
3. **Requiere Chrome abierto**: Si Chrome no está corriendo, algunas herramientas pueden fallar

---

**Recuerda**: Este MCP es tu herramienta primaria. El `browser_subagent` es tu fallback para evidencia visual. Velocidad > Capturas.
