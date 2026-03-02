---
name: vercel-react
description: React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
license: MIT
metadata:
  author: vercel
  version: "1.0.0"
---

# Mejores prácticas de Vercel React

Guía completa de optimización del rendimiento para aplicaciones React y Next.js, mantenida por Vercel. Contiene 57 reglas en 8 categorías, priorizadas por impacto para guiar la refactorización automatizada y la generación de código.

## Cuándo presentar la solicitud

Consulte estas pautas cuando:
- Escribir nuevos componentes de React o páginas Next.js
- Implementación de la recuperación de datos (del lado del cliente o del servidor)
- Revisión de código para problemas de rendimiento.
- Refactorización del código React/Next.js existente
- Optimización del tamaño del paquete o tiempos de carga.

## Categorías de reglas por prioridad

| Prioridad | Categoría | Impacto | Prefijo |
|----------|----------|--------|--------|
| 1 | Eliminando Cascadas | CRÍTICO | `asíncrono-` |
| 2 | Optimización del tamaño del paquete | CRÍTICO | `paquete-` |
| 3 | Rendimiento del lado del servidor | ALTA | `servidor-` |
| 4 | Obtención de datos del lado del cliente | MEDIO-ALTO | `cliente-` |
| 5 | Optimización de renderizado | MEDIANO | `renderizar-` |
| 6 | Rendimiento de renderizado | MEDIANO | `renderizado-` |
| 7 | Rendimiento de JavaScript | BAJO-MEDIO | `js-` |
| 8 | Patrones avanzados | BAJO | `avanzado-` |

## Referencia rápida

### 1. Eliminación de Cascadas (CRÍTICO)

- `async-defer-await` - Mover await a las ramas donde realmente se usa
- `async-parallel` - Utilice Promise.all() para operaciones independientes
- `async-dependencies` - Utilice mejor todo para dependencias parciales
- `async-api-routes`: inicia las promesas temprano, espera tarde en las rutas API
- `async-suspense-boundaries` - Usa Suspense para transmitir contenido

### 2. Optimización del tamaño del paquete (CRÍTICO)

- `bundle-barrel-imports` - Importar directamente, evitar archivos barril
- `bundle-dynamic-imports` - Utilice next/dynamic para componentes pesados
- `bundle-defer-third-party` - Análisis de carga/registro después de la hidratación
- `bundle-condicional`: carga módulos solo cuando la función está activada
- `bundle-preload` - Precarga al pasar el mouse/enfoque para la velocidad percibida

### 3. Rendimiento del lado del servidor (ALTO)

- `server-auth-actions`: autentica acciones del servidor como rutas API
- `server-cache-react` - Utilice React.cache() para la deduplicación por solicitud
- `server-cache-lru` - Utiliza el caché LRU para el almacenamiento en caché de solicitudes cruzadas
- `server-dedup-props`: evita la serialización duplicada en los accesorios RSC
- `server-serialization` - Minimiza los datos pasados a los componentes del cliente
- `server-parallel-fetching` - Reestructurar componentes para paralelizar las recuperaciones
- `server-after-nonblocking` - Utilice after() para operaciones sin bloqueo

### 4. Obtención de datos del lado del cliente (MEDIO-ALTO)

- `client-swr-dedup` - Utilice SWR para la deduplicación automática de solicitudes
- `client-event-listeners` - Deduplicar oyentes de eventos globales
- `client-passive-event-listeners` - Utilice oyentes pasivos para el desplazamiento
- `client-localstorage-schema` - Versionar y minimizar los datos de almacenamiento local

### 5. Optimización de renderizado (MEDIO)

- `rerender-defer-reads`: no suscribirse al estado que solo se usa en devoluciones de llamada
- `rerender-memo`: extrae trabajos costosos en componentes memorizados
- `rerender-memo-with-default-value` - Izar accesorios no primitivos predeterminados
- `rerender-dependencies` - Usa dependencias primitivas en efectos
- `rerender-derived-state`: suscríbete a valores booleanos derivados, no a valores sin procesar
- `rerender-derived-state-no-effect` - Deriva el estado durante el renderizado, no los efectos
- `rerender-function-setstate` - Utilice setState funcional para devoluciones de llamada estables
- `rerender-lazy-state-init` - Pasa la función a useState para valores caros
- `rerender-simple-expression-in-memo` - Evitar memo para primitivas simples
- `rerender-move-effect-to-event` - Poner lógica de interacción en controladores de eventos
- `rerender-transitions` - Utilice startTransition para actualizaciones no urgentes
- `rerender-use-ref-transient-values` - Utilice referencias para valores transitorios frecuentes

### 6. Rendimiento de renderizado (MEDIO)

- `rendering-animate-svg-wrapper` - Animar contenedor div, no elemento SVG
- `rendering-content-visibility` - Utilice content-visibility para listas largas
- `rendering-hoist-jsx` - Extrae componentes externos JSX estáticos
- `rendering-svg-precision` - Reducir la precisión de las coordenadas SVG
- `rendering-hidratación-no-flicker` - Utiliza script en línea para datos solo del cliente
- `rendering-hidratación-supresión-advertencia` - Suprime los desajustes esperados
- `rendering-activity` - Usar el componente Actividad para mostrar/ocultar
- `rendering-conditional-render` - Utilice ternario, no && para condicionales
- `rendering-usetransition-loading` - Prefiero useTransition para el estado de carga

### 7. Rendimiento de JavaScript (BAJO-MEDIO)

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
```

- `js-batch-dom-css` - Agrupa cambios de CSS mediante clases o cssText
- `js-index-maps` - Crear mapa para búsquedas repetidas
- `js-cache-property-access` - Propiedades del objeto en caché en bucles
- `js-cache-function-results` - La función de caché da como resultado el mapa a nivel de módulo
- `js-cache-storage` - Caché de lecturas de almacenamiento local/almacenamiento de sesión
- `js-combine-iterations` - Combina múltiples filtros/mapas en un bucle
- `js-length-check-first` - Verifique la longitud de la matriz antes de una comparación costosa
- `js-early-exit` - Regreso temprano de funciones
- `js-hoist-regexp` - Creación de Hoist RegExp fuera de bucles
- `js-min-max-loop` - Usa bucle para min/max en lugar de ordenar
- `js-set-map-lookups` - Utilice Set/Map para búsquedas O(1)
- `js-tosorted-immutable` - Utilice toSorted() para inmutabilidad

### 8. Patrones avanzados (BAJO)

- `advanced-event-handler-refs` - Almacena controladores de eventos en referencias
- `advanced-init-once`: inicializa la aplicación una vez por carga de la aplicación
- `advanced-use-latest` - useLatest para referencias de devolución de llamada estables

## Cómo utilizar

Lea archivos de reglas individuales para obtener explicaciones detalladas y ejemplos de código:

Cada archivo de reglas contiene:
- Breve explicación de por qué es importante.
- Ejemplo de código incorrecto con explicación.
- Ejemplo de código correcto con explicación.
- Contexto y referencias adicionales.

## Documento compilado completo

Para obtener la guía completa con todas las reglas ampliadas: `AGENTS.md`