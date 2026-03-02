---
name: postgres-practices
description: Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.
license: MIT
metadata:
  author: supabase
  version: "1.0.0"
---

```
rules/query-missing-indexes.md
rules/schema-partial-indexes.md
rules/_sections.md
```

# Mejores prácticas de Supabase Postgres

Guía completa de optimización del rendimiento para Postgres, mantenida por Supabase. Contiene reglas en 8 categorías, priorizadas por impacto para guiar la optimización automatizada de consultas y el diseño de esquemas.

## Cuándo presentar la solicitud

Consulte estas pautas cuando:
- Escribir consultas SQL o diseñar esquemas.
- Implementación de índices u optimización de consultas.
- Revisión de problemas de rendimiento de la base de datos.
- Configuración de agrupación o escalado de conexiones
- Optimización para funciones específicas de Postgres
- Trabajar con seguridad a nivel de fila (RLS)

## Categorías de reglas por prioridad

| Prioridad | Categoría | Impacto | Prefijo |
|----------|----------|--------|--------|
| 1 | Rendimiento de consultas | CRÍTICO | `consulta-` |
| 2 | Gestión de conexiones | CRÍTICO | `conn-` |
| 3 | Seguridad y SPI | CRÍTICO | `seguridad-` |
| 4 | Diseño de esquemas | ALTA | `esquema-` |
| 5 | Simultaneidad y bloqueo | MEDIO-ALTO | `bloquear-` |
| 6 | Patrones de acceso a datos | MEDIANO | `datos-` |
| 7 | Monitoreo y Diagnóstico | BAJO-MEDIO | `monitor-` |
| 8 | Funciones avanzadas | BAJO | `avanzado-` |

## Cómo utilizar

Lea archivos de reglas individuales para obtener explicaciones detalladas y ejemplos de SQL:

Cada archivo de reglas contiene:
- Breve explicación de por qué es importante.
- Ejemplo de SQL incorrecto con explicación.
- Ejemplo de SQL correcto con explicación.
- Salida o métricas EXPLAIN opcionales
- Contexto y referencias adicionales.
- Notas específicas de Supabase (cuando corresponda)

## Documento compilado completo

Para obtener la guía completa con todas las reglas ampliadas: `AGENTS.md`