# 🌌 Configuración Antigravity

**Marco de configuración de espacios de trabajo para ingeniería de software agéntica**

Un marco de configuración estandarizado para definir restricciones arquitectónicas, habilidades especializadas y flujos de trabajo operativos para agentes de IA (Gemini, Claude, Cursor, Windsurf).

<p>
  <a href="./readme.md">English</a> •
  <a href="./readme.es.md">Español</a> •
  <a href="./readme.pt.md">Português</a>
</p>

---

## 🎯 Descripción General

Este repositorio proporciona una estructura de configuración estandarizada para entornos de desarrollo con IA. Garantiza la consistencia del código y el cumplimiento de estándares arquitectónicos a través de tres componentes principales:

### Componentes Principales

1. **Reglas (Rules)**: Restricciones arquitectónicas globales aplicadas a todas las interacciones del agente.
   - *Ejemplo*: Aplicación de patrones thread-safe o límites de complejidad.
   - *Ubicación*: `rules/`
2. **Habilidades (Skills)**: Módulos de conocimiento especializado para dominios específicos.
   - *Concepto*: Información contextual (ej. `8-blockchain`) cargada solo cuando es relevante para la tarea.
   - *Formato*: Archivos `SKILL.md` estandarizados y organizados por categoría.
3. **Flujos de Trabajo (Workflows)**: Procedimientos automatizados para tareas multi-paso.
   - *Mecánica*: Secuencias predefinidas para operaciones como `/deploy` o auditorías de seguridad.

---

## 🌐 Soporte Trilingüe

La documentación principal está disponible en inglés, español y portugués. Las instrucciones técnicas de las habilidades (`skill.md`) se mantienen en inglés para optimizar el uso de tokens y garantizar la precisión técnica entre diferentes modelos de lenguaje.

---

## 🏗️ Estándares de Directorio

Este repositorio impone el uso de **lowercase kebab-case** para todos los nombres de archivos y directorios para asegurar la compatibilidad con herramientas de línea de comandos.

```text
antigravity-config/
├── install.sh           # Script de instalación
├── docs/                # Documentación del proyecto
├── scripts/             # Utilidades y scripts internos
├── template/            # Plantillas para nuevos componentes
├── rules/               # Reglas arquitectónicas globales
├── skills/              # Conocimiento por dominio (100+ Skills)
└── workflows/           # Secuencias operativas automatizadas
```

---

## 🛡️ Mantenimiento del Espacio de Trabajo

La habilidad `7-meta/agent-ops` automatiza la organización del espacio de trabajo:
- Impone convenciones de nomenclatura.
- Elimina archivos no autorizados o temporales.
- Organiza archivos dispersos en `/scripts` o `/docs`.

---

## 🤖 Guía para Agentes de IA

> [!IMPORTANT]
> Instrucciones de soporte para agentes de IA que operan en este espacio de trabajo:

1. **Inicialización**: Leer `rules/protocol-zero.md` antes de ejecutar cualquier tarea para entender las restricciones locales.
2. **Selección de Contexto**: Referenciar `skills/index.md` para identificar y cargar las habilidades de dominio relevantes.
3. **Ejecución de Flujos**: Para comandos (ej. `/deploy`), seguir la secuencia exacta definida en el archivo correspondiente en `workflows/`.
4. **Organización**: Almacenar logs y scripts temporales en `/docs` o `/scripts`. No añadir archivos huérfanos al directorio raíz.

---

## 🚀 Inicio Rápido (Instalación)

1. Clona este repositorio en cualquier lugar:
```bash
git clone https://github.com/LuisSambrano/01-antigravity.git
```

2. Ejecute el instalador de arranque (esto configura todo en `~/.gemini/antigravity`):
```bash
chmod +x 01-antigravity/install.sh && ./01-antigravity/install.sh --minimal
```

*Opcionalmente use `--full` para vincular las más de 100 habilidades.*

---

## 🔒 Seguridad

Esta plantilla es de código abierto bajo la licencia MIT y no contiene información de identificación personal (PII) ni claves de API.

<div align="center">

**Arquitectado y mantenido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
