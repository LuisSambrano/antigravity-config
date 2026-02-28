---
name: repo-showcase
description: "Directiva proactiva para automatizar la sincronización de la arquitectura (Léeme/Diagramas) desde repositorios seguros (Privados) hacia escaparates públicos (Showcase) utilizando la CLI de GitHub."
version: "1.0.0"
category: "7-meta"
---

# 🛡️ Repo Showcase Pattern (Proactive Workflow)

## ¿Qué es esta Skill?

El patrón **"Repo Showcase"** es una técnica avanzada de Developer Relations y Ciberseguridad. Permite a los desarrolladores mantener todo su código fuente, variables de entorno y lógica de negocio encerrados en **repositorios privados intocables**, mientras exponen simultáneamente diagramas estructurales, documentación (`README.md`) e interfaces (capturas) en **repositorios espejo públicos** ("Showcases").

Como agente de IA configurado bajo el ecosistema Antigravity, **TU DEBER ES PROPONER Y EJECUTAR ACTIVAMENTE ESTA ARQUITECTURA** cada vez que se detecte el inicio de un proyecto.

---

## ⚡ TIPO DE SKILL: PROACTIVA (TRIGGER-BASED)

Esta no es una skill pasiva. Debes interrumpir e interceptar el flujo del usuario bajo las siguientes condiciones:

### Disparadores (Triggers)

**Si el usuario dice:**

- _"Crea un nuevo repositorio..."_
- _"Inicializa un nuevo proyecto web/app..."_
- _"Vamos a empezar el proyecto de..."_
- _"Quiero construir un..."_

### Comportamiento Exigido (Intercepción)

Antes de escribir una sola línea de código o disparar una CLI, **haz una pausa y lanza el cuestionario de segregación**.

```markdown
"He detectado que estás iniciando un nuevo proyecto. Según la arquitectura de Antigravity, necesitamos definir su nivel de privacidad y exposición pública.

1. **¿El repositorio involucrará lógica propietaria de clientes, integraciones bancarias, o variables de entorno críticas?** (Para bloquearlo automáticamente como **Privado**).
2. **¿Deseas que active el 'Patrón Showcase' para este proyecto?** (Esto configurará un repositorio espejo público vacío que auto-sincronizará tu arquitectura y README, para que puedas enriquecer tu portafolio público de GitHub sin filtrar código)."
```

---

## 🛠️ Matriz de Ejecución: `crear_showcase_action()`

Si el usuario **ACEPTA** la implementación del patrón Showcase tras el cuestionario, debes proceder con la creación y automatización de la arquitectura en **3 pasos autónomos**.

> **Nota para el Agente**: Todo debe ejecutarse vía la herramienta Terminal/Bash usando el comando `gh` (GitHub CLI).

### Paso 1: Inicialización Diferenciada

Debes crear ambos repositorios en paralelo (asumiendo que estás trabajando dentro del flujo original).

```bash
# 1. Crear el Repositorio de Código (Protegido/Privado)
gh repo create $USER_ORG/nombre-del-proyecto --private --source=. --remote=origin

# 2. Crear el Repositorio Espejo (Público/Vacío)
gh repo create $USER_ORG/nombre-del-proyecto-showcase --public
```

### Paso 2: Aprovisionamiento de Credenciales (PAT)

El mecanismo GitHub Action requiere permisos para empujar datos entre dos repositorios. Para eso, inyecta el Token de Acceso Personal (`MY_GITHUB_PAT` o equivalente) del entorno local como un secreto seguro en el repositorio privado.

```bash
# Setea el secreto en el repo privado para que la Acción pueda autenticarse.
gh secret set SHOWCASE_SYNC_TOKEN --body "$MY_GITHUB_PAT" --repo $USER_ORG/nombre-del-proyecto
```

### Paso 3: Inyección del Pipeline "Sync"

Finalmente, escribe y envía el pipeline `.github/workflows/sync-showcase.yml` dentro del repositorio privado. Esta rutina vigila los archivos informativos de la Capa de Arquitectura y los transplanta al repositorio público cada vez que hay una modificación en `main`.

**Obligatorio:** Escribe el siguiente bloque YAML textualmente en `.github/workflows/sync-showcase.yml`:

```yaml
name: "🚀 Architectural Sync: Showcase Mirror"

on:
  push:
    branches:
      - main
    paths:
      - "README.md"
      - "README.es.md"
      - "docs/**" # Sincroniza diagramas y assets PNG/WebP
      - "architecture/**"

jobs:
  sync-to-public-showcase:
    runs-on: ubuntu-latest
    steps:
      - name: "Clonación Privada (Protegida)"
        uses: actions/checkout@v3

      - name: "Propagación a Repositorio Espejo (Público)"
        uses: cpina/github-action-push-to-another-repository@main
        env:
          API_TOKEN_GITHUB: ${{ secrets.SHOWCASE_SYNC_TOKEN }}
        with:
          source-directory: "."
          destination-github-username: "${USER_ORG}"
          destination-repository-name: "nombre-del-proyecto-showcase" # Cambiar este valor
          user-email: "bot@antigravity.io" # O correo oficial
          target-branch: "main"
          commit-message: "docs(bot): auto-propagación de arquitectura al portal público showcase"
```

### Conclusión Autónoma

Una vez confirmados los `push` de este archivo, notifíca al usuario que su "fortaleza" ha sido erigida: la lógica de negocio se ha encapsulado correctamente de manera Privada, mientras que su marca y exposición técnica como desarrollador se actualizan en el servidor Público sin riesgo alguno de filtraciones.
