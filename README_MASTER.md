# 🌌 Google Antigravity: Sistema Operativo de Inteligencia Colectiva

**Estado:** Activo | **Arquitectura:** Modular | **Idioma del Índice:** Español

Bienvenido al núcleo de Antigravity. Este repositorio es un monorepo que centraliza capacidades (Skills), herramientas de automatización y patrones de arquitectura de software.

Este documento sirve como Mapa de Navegación para visualizar la jerarquía funcional del sistema, abstraída de la estructura física de carpetas y traducida para facilitar la toma de decisiones.

---

## 🗺️ Mapa de Dominios

### 1. 🧠 Inteligencia Artificial y Agentes

Capacidades cognitivas, memoria y orquestación de LLMs.

- **Arquitectura:**
  - **Arquitecto de Agentes**: Diseño de sistemas multi-agente robustos.
  - **Gestor de Agentes**: Ciclo de vida y supervisión.
  - **Evaluación**: Métricas de calidad para respuestas de IA.
- **Memoria:**
  - **Gestión de Contexto**: Optimización de tokens.
  - **Memoria MCP**: Protocolo de memoria persistente.
- **Motores:**
  - **CrewAI**: Orquestación de equipos.
  - **NotebookLM**: RAG avanzado sobre documentos.

### 2. 💻 Desarrollo Web Moderno

Stack tecnológico, patrones de UI y frameworks.

- **Frontend & UX:**
  - **UI/UX Pro Max**: Sistema de diseño inteligente (Protocolo Zero).
  - **React Best Practices**: Patrones para Next.js 15+/React 19.
  - **Tailwind Patterns**: Arquitectura CSS escalable.
- **Backend & Infra:**
  - **Guías Backend**: Estándares para APIs y Microservicios.
  - **Postgres & SQL**: Optimización de bases de datos.
  - **Autenticación**: Flujos seguros con Supabase/Clerk.
- **Plataformas:**
  - **Shopify Dev**: E-commerce headless.
  - **Telegram Apps**: Mini apps y bots.

### 3. 🛡️ Seguridad Ofensiva y Defensiva

Ciberseguridad y pentesting ético.

- **Web & API:**
  - **Vulnerabilidades Web**: OWASP Top 10.
  - **Inyección SQL**: Detección y prevención.
- **Infraestructura:**
  - **AWS Security**: Auditoría de nubes.
  - **Privilege Escalation**: Técnicas Linux/Windows.

### 4. 🚀 Crecimiento y Producto

Estrategias de negocio.

- **Growth Hacking:**
  - **Fundamentos SEO**: Posicionamiento orgánico.
  - **ASO (App Store)**: Optimización móvil.
  - **CRO**: Optimización de conversiones.

### 5. 🤖 Automatización (Tools)

Scripts para eficiencia operativa.

- **Browser Automation**: Playwright/Puppeteer.
- **GitHub Workflows**: CI/CD.
- **N8N Automator**: Flujos low-code.

### 6. 🧬 Meta-Skills

Capacidades del propio sistema.

- **Modo Loki**: Operación autónoma avanzada.
- **Creador de Skills**: Fábrica de nuevas capacidades.

---

## 🏗️ Convenciones del Repositorio

Consulta [docs/architecture/REPOSITORY_GOVERNANCE.md](docs/architecture/REPOSITORY_GOVERNANCE.md) para entender las reglas de contribución.

### Estructura Física:

```text
google-antigravity/
├── assets/                 # Recursos estáticos globales
├── docs/                   # Documentación de arquitectura
├── rules/                  # Reglas de linter y cursor
├── skills/                 # CATÁLOGO DE FUNCIONALIDADES
└── tools/                  # Herramientas CLI (Python/Bash)
```

> [!NOTE]
> Este índice se genera automáticamente mediante `scripts/maintenance/generate_index.py`. No editar manualmente las secciones del mapa de dominios.
