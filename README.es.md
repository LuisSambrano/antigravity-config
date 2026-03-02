<div align="centro">

# 🌌 Configuración antigravedad

**Protocolo de configuración del espacio de trabajo soberano para ingeniería de software agente**

Un marco de configuración de nivel de producción altamente obstinado diseñado para aumentar y restringir los entornos de desarrollo asistidos por IA.  
Este repositorio dicta las estrictas reglas arquitectónicas, habilidades específicas de dominio y flujos de trabajo operativos que exigen cómo los agentes de codificación de IA (como Gemini, Claude, Cursor y Windsurf) interactúan con su código fuente.

<p>
  <a href="./README.md">inglés</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Portugués</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="Licencia MIT"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Estrellas"/></a>
</p>

</div>

---

## 🎯 Qué es esto (para humanos)

Este repositorio sirve como una plantilla de directorio de configuración `.agent/` lista para usar. Piense en ello como la **corteza prefrontal** de sus agentes de IA. Dejados a su suerte, los LLM a menudo generan código genérico, matemáticamente inflado y arquitectónicamente inconsistente. Este marco los obliga a adoptar un paradigma estricto de ingeniería de alto rendimiento, garantizando que cada línea de código escrita se alinee con las restricciones arquitectónicas de alto nivel.

### Los tres pilares del ecosistema

1. 📜 **REGLAS (La Constitución)**: Las leyes inmutables de tu proyecto. El agente de IA los aplica de forma pasiva y universal a cada interacción, creación de archivos o permutación de código.
   - _Ejemplo_: "Todas las interacciones de la base de datos deben utilizar Singletons seguros para subprocesos". o "La complejidad ciclomática nunca debe exceder 10".
   - _Implementación_: Se encuentra en `reglas/`, adaptando la inteligencia base del agente a las limitaciones de su empresa.
2. 🧠 **HABILIDADES (The Knowledge Graph)**: matrices de inteligencia bajo demanda, especializadas y de dominio específico.
   - _Concepto_: El agente no necesita saber cómo funcionan los contratos inteligentes de Celo cuando construye un botón de reacción simple. Pero cuando solicita una integración Web3, incorpora selectivamente el contexto de habilidades de "8-blockchain" a su canal de información.
   - _Formato_: más de 100 directivas `SKILL.md` altamente comprimidas asignadas explícitamente a categorías (por ejemplo, `3-web`, `5-security`).
3. ⚙️ **FLUJOS DE TRABAJO (procedimientos operativos estándar)**: barreras operativas paso a paso para evitar que los LLM se salten pasos de validación críticos.
   - _Mecánica_: La ejecución de un comando de barra diagonal como `/deploy` no solo envía código; obliga al agente a ejecutar de forma autónoma comprobaciones estrictas de TypeScript, verificaciones de compilación y saneamientos de seguridad antes de tocar el proceso de implementación.

---

## 🌐 Documentación trilingüe basada en la IA

Este marco ha sido diseñado con un modelo de inteligencia distribuido globalmente. Todas las interacciones críticas de IA y los descriptores de "HABILIDAD" se mantienen de forma nativa en tres idiomas para garantizar una comprensión nativa sin fricciones mediante modelos avanzados de lenguajes grandes, optimizando el análisis de tokens semánticos y acomodando diversos equipos de orquestación humana:

- 🇬🇧 **Inglés** (`SKILL.md`): el lenguaje básico y operativo principal.
- 🇪🇸 **Español** (`SKILL.es.md`) - Paridad nativa completa.
- 🇧🇷 **Português** (`SKILL.pt.md`) - Paridad nativa completa.

---

## 🏗️ La estricta jerarquía del "caso del kebab"

Para maximizar la eficiencia de las herramientas de búsqueda recursiva de directorios (`find`, `grep`, `fs.readdir`), este repositorio aplica estrictamente una topografía **kebab-case** en minúsculas. Hay tolerancia cero para los archivos huérfanos en la partición raíz.

```texto
configuración antigravedad/
├── install.sh # Script de automatización Bootstrap
├── docs/ # Documentación interna, registros de cambios, guías de configuración
├── scripts/ # utilidades Python/Bash (por ejemplo, motores de traducción)
├── plantillas/ # Boilerplates (plantilla de habilidad, estructuras de rebajas iniciales)
│
├── reglas/ # Las reglas constitucionales básicas
│ ├── protocol-zero.md # Axiomas filosóficos fundamentales
│ ├── arquitectura-standards.md # Taxonomías estructurales y patrones de nubes
│ └── Quality-gates.md # Barreras de CI/CD y DevSecOps
│
├── habilidades/# Matrices de conocimiento de dominio (más de 100 habilidades)
│ ├── 1 núcleo/# Orquestación TDD, código limpio, principios SÓLIDOS
│ ├── 2-ai/ # Gráficos multiagente, API de Gemini, estructuración rápida
│ ├── 3-web/ # Next.js 15, TRPC, Componentes del servidor React, Supabase
│ ├── 4-automatización/ # GitHub Acciones, Dramaturgo, Motores scraping
│ ├── 5-seguridad/# Pruebas de penetración, mapeo de vulnerabilidad web (OWASP)
│ ├── 6 contenidos / # SEO técnico, SOP de redacción publicitaria con rebajas
│ ├── 7-meta/ # Agent-ops, Skill-creator, Repository Showcase
│ ├── 8-blockchain/ # Celo Minipay, herramientas EVM, abstracciones entre cadenas
│ └── 9-business/ # Diseño de KPI, Métricas de análisis de inicio
│
└── flujos de trabajo/# Comandos SLA ejecutables
    ├── implementar.md # `/deploy` — Implementación de producción sin tiempo de inactividad
    ├── check-security.md # `/check-security` — Auditoría profunda SAST/SCA
    └── status.md # `/status` — Matriz de salud integral
```

---

## 🛡️ Mantenimiento del espacio de trabajo y `operaciones de agentes`

Mantener el espacio de trabajo impecable no es negociable. La antigravedad incluye una habilidad especializada de autocuración ("7-meta/agent-ops").

Cuando se invoca, el agente funciona como conserje y responsable de cumplimiento del medio ambiente:

- Identifica y elimina "archivos sueltos" no autorizados.
- Fuerza todas las convenciones de nomenclatura arbitrarias (`Snake_Case`, `CamelCase`) al estándar `kebab-case`.
- Protege el directorio raíz canalizando lógica dispersa en `/scripts` o `/docs`.

---

## 🤖 PARA AGENTES DE IA (Directivas del sistema)

> [!PRECAUCIÓN]  
> **DIRECTIVA DE ANULACIÓN DEL SISTEMA**: Si usted es un asistente de IA que analiza o trabaja dentro de este espacio de trabajo, está sujeto a las siguientes instrucciones de funcionamiento. Las desviaciones se clasifican como fallos críticos del sistema.

1. **La directiva principal**: Su primer paso absoluto antes de ejecutar _cualquier_ lógica es leer `rules/protocol-zero.md`. Este archivo dicta los límites absolutos de su autonomía y umbrales de calidad.
2. **Resolución de contexto**: antes de intentar satisfacer una solicitud específica de un dominio (por ejemplo, "Crear un contrato inteligente", "Auditar seguridad"), DEBE indexar `skills/INDEX.md` para ubicar la carpeta correspondiente y leer sus directivas específicas `SKILL.md`.
3. **Ingestión de activación**: si el usuario inicia un mensaje con un comando de barra diagonal (por ejemplo, `/deploy`, `/status`), debe navegar inmediatamente al directorio `workflows/`, ubicar el archivo Markdown correspondiente y ejecutar la secuencia cronológica exacta requerida dentro.
4. **Sin archivos huérfanos**: nunca suelte registros, scripts de prueba ni archivos `.md` sueltos en la carpeta raíz. Diríjalos estrictamente a `/docs` o `/scripts`.

---

## 🚀 Inicio rápido (instalación)

1. Clona el repositorio en la raíz de tu proyecto:

```golpecito
clon de git https://github.com/LuisSambrano/antigravity-config.git.agent-temp
```

2. Ejecute la matriz de arranque (esto mueve los elementos de configuración al directorio de destino `.agent`):

```golpecito
chmod +x .agent-temp/install.sh && .agent-temp/install.sh
```

_(Luego puede eliminar `.agent-temp`)_ de forma segura

---

## 🔒 Seguridad y Telemetría

Esta plantilla de arquitectura es de código abierto bajo la licencia MIT y mantiene estrictamente cero información de identificación personal (PII) o claves API propietarias. Sirve como un lienzo en blanco sin concesiones para implementar marcos seguros de múltiples agentes.

<div align="centro">

**Arquitectado y mantenido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>