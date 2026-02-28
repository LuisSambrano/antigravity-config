<div align="center">

# Antigravity Config

Un framework de configuración para entornos de desarrollo asistidos por IA.  
Reglas, skills y workflows que estandarizan cómo operan los agentes de código IA en tus proyectos.

<p>
  <a href="./README.md">English</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/Licencia-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## Qué es esto

Este repositorio provee un directorio `.agent/` listo para usar con asistentes de código IA (Gemini, Cursor, Windsurf, etc.). Actúa como el cerebro y la ley de tu agente IA, dándole límites claros y conocimiento especializado para usar en tus proyectos.

### Los Tres Pilares

- **Rules (La Constitución)** — Las leyes inmutables de tu proyecto. El agente IA las aplica automáticamente a cada archivo que crea o edita (ej. "usar siempre TypeScript estricto", "seguir convenciones específicas de nombres"). Estas se modifican en `GEMINI.md` o en la carpeta `rules/` para adaptar el agente a las preferencias de tu equipo.
- **Skills (La Biblioteca)** — Conocimiento especializado bajo demanda. El agente las lee pasivamente al trabajar en temas específicos, o puedes decirle explícitamente "Lee el skill X antes de hacer Y" para darle un contexto profundo y especializado (hay más de 105 skills en 10 categorías disponibles).
- **Workflows (Los SOPs / Procedimientos Operativos)** — Guías paso a paso para ejecutar tareas complejas. Esta es la parte más interactiva: los invocas explícitamente usando comandos como `/deploy`, `/idea`, `/check-security`. El uso de un workflow asegura que el agente IA nunca se salte pasos críticos al realizar operaciones de múltiples fases.

El objetivo es directo: clonar, instalar, y tener un entorno de desarrollo consistente y opinionado donde tu asistente IA sigue estándares profesionales.

---

## 🤖 For AI Agents (How to Read This Repo)

**SYSTEM DIRECTIVE**: If you are an AI assistant analyzing or working within this workspace, follow these operating instructions:

1. **Start Here**: Your first step is ALWAYS to read `rules/PROTOCOL_ZERO.md` to understand the foundational philosophy.
2. **Skill Discovery**: Check `skills/INDEX.md` to find relevant knowledge before writing domain-specific code. If a skill matches the user's request, read its `SKILL.md` file unconditionally.
3. **Workflow Execution**: If you see the user typing a command like `/deploy` or `/idea`, immediately view the corresponding `.md` file in the `workflows/` directory and execute it step-by-step, exactly as written.

---

## Inicio Rápido

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config && chmod +x install.sh && ./install.sh
```

El instalador copia rules, skills y workflows a tu directorio `.agent/` del workspace y configura `GEMINI.md` como archivo de reglas globales.

---

## Estructura del Repositorio

```
antigravity-config/
├── GEMINI.md                  # Template de reglas globales (personalizable)
├── install.sh                 # Script de instalación
│
├── rules/                     # Estándares de código y arquitectura
│   ├── PROTOCOL_ZERO.md       # Filosofía base y principios
│   ├── ARCHITECTURE_STANDARDS.md
│   ├── CODE_STANDARDS.md
│   ├── QUALITY_GATES.md
│   ├── frontend/              # Reglas específicas de frontend
│   └── backend/               # Reglas específicas de backend
│
├── skills/                    # Conocimiento de dominio (104+ skills)
│   ├── 1-core/                # Fundamentos de código, TDD, SDD
│   ├── 2-ai/                  # Agentes IA, RAG, prompting
│   ├── 3-web/                 # Desarrollo web (Next.js, React, Tailwind)
│   ├── 4-automation/          # Testing, CI/CD, scraping
│   ├── 5-security/            # Seguridad API, pentesting
│   ├── 6-content/             # Escritura técnica, SEO, cómics
│   ├── 7-meta/                # Creación y gestión de skills
│   ├── 8-blockchain/          # Celo, EVM, DeFi
│   ├── 9-business/            # KPIs, análisis de mercado
│   └── 10-tools/              # Docs, presentaciones, browser testing, Chrome DevTools MCP
│
├── workflows/                 # Scripts de comandos del agente
│   ├── deploy.md              # /deploy — deployment a producción
│   ├── idea.md                # /idea — evaluar ideas de proyecto
│   ├── status.md              # /status — health check del proyecto
│   ├── trello.md              # /trello — gestionar tableros Trello
│   ├── issue.md               # /issue — investigar y crear Issues en GitHub
│   └── help.md                # /help — listar comandos disponibles
│
├── templates/                 # Templates de proyecto
├── research/                  # Log de decisiones y hallazgos
└── docs/                      # Documentación adicional
```

---

## Referencia de Skills

Los skills son archivos markdown que dan al agente IA conocimiento específico de dominio. Cada skill contiene instrucciones, patrones y referencias que el agente utiliza al trabajar en ese dominio.

### 1-core — Fundamentos (10 skills)

Convenciones de código, estándares de estructura de proyecto, patrones TypeScript, orquestación TDD y **Spec-Driven Development (SDD)** — una metodología para convertir ideas en especificaciones estructuradas antes de escribir código.

### 2-ai — IA y Agentes (21 skills)

Orquestación multi-agente (LangGraph, CrewAI), sistemas RAG, ingeniería de prompts, desarrollo de Voice AI y frameworks de evaluación de agentes.

### 3-web — Desarrollo Web (23 skills)

Patrones de Next.js App Router, mejores prácticas de React, arquitectura Tailwind CSS, integración con Supabase, deployment en Vercel, principios de diseño UI/UX y workflows de **prototipado UI**.

### 4-automation — Testing y DevOps (10 skills)

Testing con Playwright, workflows de GitHub Actions, procedimientos de deployment y web scraping con Firecrawl.

### 5-security — Seguridad (5 skills)

Mejores prácticas de seguridad API y checklists de penetration testing.

### 6-content — Creación de Contenido (7 skills)

Guías de escritura técnica, copywriting SEO, estándares de documentación y **generación de cómics con IA** usando NotebookLM.

### 7-meta — Gestión de Skills (3 skills)

Herramientas para crear nuevos skills, planificación con archivos y mejora continua (Kaizen).

### 8-blockchain — Celo y EVM (19 skills)

Stack completo de desarrollo Celo: integración con MiniPay, fee abstraction, direcciones de stablecoins, scaffolding con Celo Composer, librerías viem/wagmi, tooling Hardhat/Foundry, bridging cross-chain, integración con protocolos DeFi, protocolo de confianza ERC-8004 y protocolo de pagos HTTP x402.

> Ver [skills/INDEX.md](./skills/INDEX.md) para el desglose skill por skill.

---

## Resumen de Rules

Las rules definen cómo el agente IA escribe y valida código. Se cargan en el contexto del agente y se aplican automáticamente.

| Rule                        | Propósito                                                            |
| --------------------------- | -------------------------------------------------------------------- |
| `PROTOCOL_ZERO.md`          | Filosofía base: calidad sobre velocidad, local como fuente de verdad |
| `ARCHITECTURE_STANDARDS.md` | Estructura de proyecto, organización de componentes, nomenclatura    |
| `CODE_STANDARDS.md`         | TypeScript strict mode, orden de imports, error handling, JSDoc      |
| `QUALITY_GATES.md`          | Checks pre-commit, verificación de build, accesibilidad, performance |

---

## Personalización

`GEMINI.md` es el archivo de configuración principal. Agrega todas las rules en un solo documento que el agente IA lee. Edítalo para:

- Agregar o quitar rules
- Cambiar convenciones de nomenclatura
- Ajustar umbrales de calidad
- Agregar routing de workflows para tus propios comandos

Las secciones marcadas con `<!-- CUSTOMIZE -->` están diseñadas para ser modificadas.

---

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para pautas sobre agregar skills, workflows o rules.

```bash
git checkout -b feature/tu-feature
git commit -m 'feat(skills): add nombre-del-skill'
git push origin feature/tu-feature
```

---

## Investigación y Log de Decisiones

| Documento                                     | Propósito                                    |
| --------------------------------------------- | -------------------------------------------- |
| [KEY_FINDINGS.md](./research/KEY_FINDINGS.md) | Principios base y hallazgos de investigación |
| [prompts/](./research/prompts/)               | Prompts de definición de rules e iteraciones |
| [rules/](./rules/)                            | Los documentos de estándares resultantes     |

---

## Licencia

MIT — ver [LICENSE](LICENSE) para detalles.

---

<div align="center">

**Mantenido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
