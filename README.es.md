# Antigravity

Sistema de configuración para agentes de IA. Instala skills, workflows y reglas en cualquier agente que lea archivos markdown desde un directorio de contexto.

Compatible con: Google Gemini CLI, Claude Code, Cursor.

[English](./readme.md) · [Español](./readme.es.md)

---

## Qué hace

El instalador detecta el agente activo según el flag `--target` y copia los archivos de configuración en el directorio correspondiente. A partir de ahí, el agente lee esos archivos al inicio de cada sesión o bajo demanda.

## Instalación

```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
cd 01-antigravity
chmod +x install.sh

# Gemini CLI  →  ~/.gemini/
./install.sh --target gemini

# Claude Code  →  CLAUDE.md + .claude/ en la raíz del proyecto
./install.sh --target claude

# Cursor  →  .cursor/rules/
./install.sh --target cursor
```

## Estructura

```
antigravity/
├── install.sh           # Instalador
├── AGENT.md             # Reglas globales del agente
├── rules/               # Protocolo base
├── skills/              # Módulos de dominio
└── workflows/           # Comandos slash
```

## Licencia

MIT. No contiene datos personales ni código propietario.
