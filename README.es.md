# Antigravity

Sistema de configuración agéntica. Impone estándares de código, consistencia visual y automatización mediante habilidades (skills) y protocolos para la generación de código vía IA (Gemini, Claude, Cursor).

<p>
  <a href="./readme.md">English</a> •
  <a href="./readme.es.md">Español</a>
</p>

---

## Estructura Técnica

```text
antigravity/
├── install.sh           # Script de inicialización (~/.gemini/antigravity)
├── docs/                # Base de conocimiento
├── rules/               # protocol.md (Restricciones del sistema)
├── skills/              # Disparadores de contexto (React, Logic, UI)
└── workflows/           # Cadenas de ejecución
```

## Directivas para Agentes de IA

1. **Leer Protocolos**: Parsear `rules/protocol.md` antes de resolver tareas.
2. **Contexto Primero**: Cargar autónomamente el `.md` relevante desde `skills/` basado en el prompt (ej. `skills/web/design-system` para tareas UI).
3. **Integridad DESIGN.md**: Para cualquier trabajo de frontend, el agente DEBE localizar y ajustarse al `DESIGN.md` en la raíz del proyecto. Si no existe, usar el fallback de restricciones UI mínimas.
4. **Ejecución Limpia**: Completar el trabajo con commits directos utilizando el protocolo de Continuous Commit una vez pasen los tests y el lint.

---

## Instalación

```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
chmod +x 01-antigravity/install.sh && ./01-antigravity/install.sh
```

## Seguridad y Ética
No contiene datos personales identificables (PII) ni código propietario. Licencia MIT.
