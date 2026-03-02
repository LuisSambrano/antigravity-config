---
name: tailwind-patterns
description: Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

```
@theme {
  /* Colors - use semantic names */
  --color-primary: oklch(0.7 0.15 250);
  --color-surface: oklch(0.98 0 0);
  --color-surface-dark: oklch(0.15 0 0);
  
  /* Spacing scale */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

---

---

---

---

---

---

# Patrones CSS de viento de cola (v4 - 2025)

> CSS moderno que prioriza las utilidades con configuración nativa de CSS.

## 1. Arquitectura Tailwind v4

### Qué cambió desde la versión 3

| v3 (heredado) | v4 (actual) |
|-------------|--------------|
| `tailwind.config.js` | Directiva `@theme` basada en CSS |
| Complemento PostCSS | Motor de óxido (10 veces más rápido) |
| Modo JIT | Nativo, siempre activo |
| Sistema de complementos | Funciones nativas de CSS |
| directiva `@apply` | Todavía funciona, desanimado |

### Conceptos básicos v4

| Concepto | Descripción |
|---------|-------------|
| **CSS primero** | Configuración en CSS, no JavaScript |
| **Motor de óxido** | Compilador basado en Rust, mucho más rápido |
| **Anidación nativa** | Anidamiento CSS sin PostCSS |
| **Variables CSS** | Todos los tokens expuestos como `--*` vars |

## 2. Configuración basada en CSS

### Definición del tema

### Cuándo extender o anular

| Acción | Usar cuando |
|--------|----------|
| **Extender** | Agregar nuevos valores junto con los valores predeterminados |
| **Anular** | Reemplazo completo de la escala predeterminada |
| **Fichas semánticas** | Denominación específica del proyecto (primario, superficie) |

## 3. Consultas de contenedor (v4 nativo)

### Punto de interrupción frente a contenedor

| Tipo | Responde a |
|------|-------------|
| **Punto de interrupción** (`md:`) | Ancho de la ventana gráfica |
| **Contenedor** ($@contenedor`) | Ancho del elemento principal |

### Uso de consultas de contenedor

| Patrón | Clases |
|---------|---------|
| Definir contenedor | `@container` en el padre |
| Punto de interrupción del contenedor | `@sm:`, `@md:`, `@lg:` en niños |
| Contenedores con nombre | `@container/card` para especificidad |

### Cuándo utilizar

| Escenario | Uso |
|----------|-----|
| Diseños a nivel de página | Puntos de interrupción de la ventana gráfica |
| Responsivo a nivel de componente | Consultas sobre contenedores |
| Componentes reutilizables | Consultas de contenedor (independientes del contexto) |

## 4. Diseño responsivo

### Sistema de punto de interrupción

| Prefijo | Ancho mínimo | Objetivo |
|--------|-----------|--------|
| (ninguno) | 0px | Base móvil primero |
| `sm:` | 640px | Teléfono grande/tableta pequeña |
| `md:` | 768 píxeles | Tableta |
| `lg:` | 1024px | Computadora portátil |
| `xl:` | 1280px | Escritorio |
| `2xl:` | 1536px | Escritorio grande |

### Principio de dispositivos móviles primero

1. Escriba primero los estilos móviles (sin prefijo)
2. Agregue anulaciones de pantalla más grandes con prefijos
3. Ejemplo: `w-full md:w-1/2 lg:w-1/3`

## 5. Modo oscuro

### Estrategias de configuración

| Método | Comportamiento | Usar cuando |
|--------|----------|----------|
| `clase` | Alternancia de clase `.dark` | Cambiador de temas manual |
| `medios` | Sigue la preferencia del sistema | Sin control de usuario |
| `selector` | Selector personalizado (v4) | Tematización compleja |

### Patrón de modo oscuro

| Elemento | Luz | Oscuro |
|---------|-------|------|
| Antecedentes | `bg-blanco` | `oscuro:bg-zinc-900` |
| Texto | `texto-zinc-900` | `oscuro: texto-zinc-100` |
| Fronteras | `frontera-zinc-200` | `oscuro: borde-zinc-700` |

## 6. Patrones de diseño modernos

### Patrones de caja flexible

| Patrón | Clases |
|---------|---------|
| Centro (ambos ejes) | `centro-de-elementos flexibles-centro-de-justificación` |
| Pila vertical | `flex flex-col brecha-4` |
| Fila horizontal | `flex gap-4` |
| Espacio entre | `flexionar justificación-entre elementos-centro` |
| Rejilla envolvente | `flex flex-wrap gap-4` |

### Patrones de cuadrícula

| Patrón | Clases |
|---------|---------|
| Ajuste automático responsivo | `grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))]` |
| Asimétrico (Bento) | `grid grid-cols-3 grid-rows-2` con tramos |
| Diseño de la barra lateral | `grid grid-cols-[auto_1fr]` |

> **Nota:** Prefiera diseños asimétricos/Bento a cuadrículas simétricas de 3 columnas.

## 7. Sistema de color moderno

### OKLCH frente a RGB/HSL

| Formato | Ventaja |
|--------|-----------|
| **OKLCH** | Perceptualmente uniforme, mejor para el diseño |
| **HSL** | Tono/saturación intuitivos |
| **RGB** | Compatibilidad heredada |

### Arquitectura de fichas de color

| Capa | Ejemplo | Propósito |
|-------|---------|---------|
| **Primitivo** | `--azul-500` | Valores de color crudo |
| **Semántico** | `--color-primario` | Denominación basada en propósitos |
| **Componente** | `--botón-bg` | Específico de componente |

## 8. Sistema de tipografía

### Patrón de pila de fuentes

| Tipo | Recomendado |
|------|-------------|
| Sin | `'Inter', 'SF Pro', sistema-ui, sans-serif` |
| Mono | `'JetBrains Mono', 'Código Fira', monoespacio` |
| Mostrar | `'Traje', 'Poppins', sans-serif` |

### Tipo Escala

| Clase | Tamaño | Uso |
|-------|------|-----|
| `texto-xs` | 0,75rem | Etiquetas, subtítulos |
| `texto-sm` | 0,875rem | Texto secundario |
| `base de texto` | 1rem | Texto del cuerpo |
| `texto-lg` | 1.125 rem | Texto principal |
| `texto-xl`+ | 1,25 rem+ | Encabezados |

## 9. Animación y transiciones

### Animaciones integradas

---

---

---

---

| Clase | Efecto |
|-------|--------|
| `animar-giro` | Rotación continua |
| `animar-ping` | Pulso de atención |
| `pulso-animado` | Pulso de opacidad sutil |
| `animar-rebote` | Efecto rebote |

### Patrones de transición

| Patrón | Clases |
|---------|---------|
| Todas las propiedades | `transición-toda la duración-200` |
| Específico | `duración-colores-de-transición-150` |
| Con flexibilización | `facilidad de salida` o `facilidad de entrada y salida` |
| Efecto de desplazamiento | `hover: escala-105 transición-transformación` |

## 10. Extracción de componentes

### Cuándo extraer

| Señal | Acción |
|--------|--------|
| Combo de la misma clase más de 3 veces | Extraer componente |
| Variantes de estado complejas | Extraer componente |
| Elemento del sistema de diseño | Extracto + documento |

### Métodos de extracción

| Método | Usar cuando |
|--------|----------|
| **Componente React/Vue** | Dinámico, se necesita JS |
| **@aplicar en CSS** | Estático, no se necesita JS |
| **Fichas de diseño** | Valores reutilizables |

## 11. Antipatrones

| No | Hacer |
|-------|-----|
| Valores arbitrarios en todas partes | Utilice la escala del sistema de diseño |
| `!importante` | Corregir la especificidad adecuadamente |
| En línea `estilo =` | Usar utilidades |
| Listas de clases largas duplicadas | Extraer componente |
| Mezcle la configuración v3 con v4 | Migrar completamente a CSS-first |
| Utilice `@apply` intensamente | Prefiere componentes |

## 12. Principios de desempeño

| Principio | Implementación |
|-----------|----------------|
| **Purgar no utilizado** | Automático en v4 |
| **Evitar el dinamismo** | Sin clases de cadena de plantilla |
| **Usar óxido** | Predeterminado en v4, 10 veces más rápido |
| **Compilaciones de caché** | Almacenamiento en caché de CI/CD |

> **Recuerde:** Tailwind v4 es CSS primero. Adopte variables CSS, consultas de contenedores y funciones nativas. El archivo de configuración ahora es opcional.