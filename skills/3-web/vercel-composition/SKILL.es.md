---
name: vercel-composition
description:
  React composition patterns that scale. Use when refactoring components with
  boolean prop proliferation, building flexible component libraries, or
  designing reusable APIs. Triggers on tasks involving compound components,
  render props, context providers, or component architecture. Includes React 19
  API changes.
license: MIT
metadata:
  author: vercel
  version: '1.0.0'
---

```
rules/architecture-avoid-boolean-props.md
rules/state-context-interface.md
```

# Reaccionar patrones de composición

Patrones de composición para construir componentes React flexibles y mantenibles. evitar
proliferación de accesorios booleanos mediante el uso de componentes compuestos, estado de elevación y
componer partes internas. Estos patrones facilitan las bases de código tanto para los humanos como para la IA
agentes con los que trabajar a medida que escalan.

## Cuándo presentar la solicitud

Consulte estas pautas cuando:

- Refactorización de componentes con muchos accesorios booleanos.
- Creación de bibliotecas de componentes reutilizables.
- Diseño de API de componentes flexibles
- Revisión de la arquitectura de los componentes.
- Trabajar con componentes compuestos o proveedores de contexto.

## Categorías de reglas por prioridad

| Prioridad | Categoría | Impacto | Prefijo |
| -------- | ----------------------- | ------ | --------------- |
| 1 | Arquitectura de componentes | ALTA | `arquitectura-` |
| 2 | Gestión Estatal | MEDIANO | `estado-` |
| 3 | Patrones de implementación | MEDIANO | `patrones-` |
| 4 | Reaccionar 19 API | MEDIANO | `reaccionar19-` |

## Referencia rápida

### 1. Arquitectura de componentes (ALTA)

- `architecture-avoid-boolean-props` - No agregue accesorios booleanos para personalizar
  comportamiento; usar composición
- `componentes-compuestos-de-arquitectura` - Estructurar componentes complejos con elementos compartidos.
  contexto

### 2. Gestión del Estado (MEDIO)

- `estado-desacoplamiento-implementación` - El proveedor es el único lugar que sabe cómo
  el estado es administrado
- `state-context-interface` - Definir interfaz genérica con estado, acciones, meta
  para inyección de dependencia
- `state-lift-state`: mueve el estado a los componentes del proveedor para acceso entre hermanos

### 3. Patrones de implementación (MEDIO)

- `patterns-explicit-variants` - Crea componentes variantes explícitos en lugar de
  modos booleanos
- `patrones-niños-sobre-render-props` - Utilice niños para la composición en su lugar
  de accesorios renderX

### 4. Reaccionar 19 API (MEDIO)

> **⚠️ Solo React 19+.** Omita esta sección si usa React 18 o una versión anterior.

- `react19-no-forwardref` - No utilice `forwardRef`; use `use()` en lugar de `useContext()`

## Cómo utilizar

Lea archivos de reglas individuales para obtener explicaciones detalladas y ejemplos de código:

Cada archivo de reglas contiene:

- Breve explicación de por qué es importante.
- Ejemplo de código incorrecto con explicación.
- Ejemplo de código correcto con explicación.
- Contexto y referencias adicionales.

## Documento compilado completo

Para obtener la guía completa con todas las reglas ampliadas: `AGENTS.md`