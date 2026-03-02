---
name: ui-ux-matrix
description: "Diagnostic matrix for UI/UX compliance. Validates web/mobile structures against 50+ stylistic rules, color contrast thresholds, interaction feedback loops, and framework-specific patterns."
---

---

```bash
python3 --version || python --version
```

```bash
brew install python3
```

```bash
sudo apt update && sudo apt install python3
```

```powershell
winget install Python.Python.3.12
```

---

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

# UI/UX Pro Max - Inteligencia de diseño

Guía de diseño integral para aplicaciones web y móviles. Contiene más de 50 estilos, 97 paletas de colores, 57 combinaciones de fuentes, 99 pautas de UX y 25 tipos de gráficos en 9 pilas de tecnología. Base de datos con capacidad de búsqueda con recomendaciones basadas en prioridades.

## Cuándo presentar la solicitud

Consulte estas pautas cuando:

- Diseño de nuevos componentes o páginas de UI.
- Elección de paletas de colores y tipografía.
- Revisión de código para problemas de UX.
- Creación de páginas de destino o paneles de control.
- Implementación de requisitos de accesibilidad.

## Categorías de reglas por prioridad

| Prioridad | Categoría | Impacto | Dominio |
| -------- | ------------------- | -------- | --------------------- |
| 1 | Accesibilidad | CRÍTICO | `ux` |
| 2 | Toque e interacción | CRÍTICO | `ux` |
| 3 | Rendimiento | ALTA | `ux` |
| 4 | Diseño y Responsivo | ALTA | `ux` |
| 5 | Tipografía y color | MEDIANO | `tipografía`, `color` |
| 6 | Animación | MEDIANO | `ux` |
| 7 | Selección de estilo | MEDIANO | `estilo`, `producto` |
| 8 | Gráficos y datos | BAJO | `gráfico` |

## Referencia rápida

### 1. Accesibilidad (CRÍTICO)

- `color-contraste` - Relación mínima de 4,5:1 para texto normal
- `focus-states` - Anillos de enfoque visibles en elementos interactivos
- `alt-text`: texto alternativo descriptivo para imágenes significativas
- `aria-labels` - aria-label para botones de solo íconos
- `keyboard-nav` - El orden de las tabulaciones coincide con el orden visual
- `form-labels` - Usar etiqueta con atributo for

### 2. Toque e interacción (CRÍTICO)

- `touch-target-size` - Objetivos táctiles mínimos de 44x44px
- `hover-vs-tap`: use hacer clic/tocar para interacciones principales
- `botones de carga` - Deshabilitar el botón durante operaciones asíncronas
- `error-feedback` - Borrar mensajes de error cerca del problema
- `cursor-pointer` - Agrega puntero de cursor a elementos en los que se puede hacer clic

### 3. Rendimiento (ALTO)

- `optimización de imagen` - Utilice WebP, srcset, carga diferida
- `movimiento-reducido` - Marque prefiere-movimiento-reducido
- `content-jumping` - Reserva espacio para contenido asíncrono

### 4. Diseño y capacidad de respuesta (ALTO)

- `viewport-meta` - ancho=ancho-dispositivo-escala-inicial=1
- `readable-font-size` - Texto del cuerpo mínimo de 16 píxeles en dispositivos móviles
- `horizontal-scroll`: garantiza que el contenido se ajuste al ancho de la ventana gráfica
- `z-index-management` - Definir la escala del índice z (10, 20, 30, 50)

### 5. Tipografía y color (MEDIO)

- `line-height` - Utilice 1,5-1,75 para el cuerpo del texto
- `line-length` - Límite de 65 a 75 caracteres por línea
- `emparejamiento de fuentes` - Coincidencia de personalidades de fuente de encabezado/cuerpo

### 6. Animación (MEDIO)

- `duración-tiempo` - Utilice 150-300 ms para microinteracciones
- `transform-rendimiento` - Utilice transformación/opacidad, no ancho/alto
- `estados de carga` - Pantallas de esqueleto o hilanderos

### 7. Selección de estilo (MEDIO)

- `style-match` - Combina el estilo con el tipo de producto
- `consistencia`: use el mismo estilo en todas las páginas
- `no-emoji-icons` - Utilice iconos SVG, no emojis

### 8. Gráficos y datos (BAJO)

- `chart-type` - Relaciona el tipo de gráfico con el tipo de datos
- `color-guidance` - Utilice paletas de colores accesibles
- `data-table`: proporciona una tabla alternativa para accesibilidad

## Cómo utilizar

Busque dominios específicos utilizando la herramienta CLI a continuación.

## Requisitos previos

Compruebe si Python está instalado:

Si Python no está instalado, instálelo según el sistema operativo del usuario:

**macOS:**

**Ubuntu/Debian:**

**Windows:**

## Cómo utilizar esta habilidad

Cuando el usuario solicite trabajo de UI/UX (diseño, construcción, creación, implementación, revisión, corrección, mejora), siga este flujo de trabajo:

### Paso 1: Analizar los requisitos del usuario

Extraiga información clave de la solicitud del usuario:

- **Tipo de producto**: SaaS, comercio electrónico, portafolio, panel de control, página de destino, etc.
- **Palabras clave de estilo**: minimalista, divertido, profesional, elegante, modo oscuro, etc.
- **Industria**: salud, tecnología financiera, juegos, educación, etc.
- **Pila**: React, Vue, Next.js o por defecto `html-tailwind`

### Paso 2: Generar sistema de diseño (REQUERIDO)

**Comience siempre con `--design-system`** para obtener recomendaciones completas y razonadas:

Este comando:

1. Busca 5 dominios en paralelo (producto, estilo, color, landing, tipografía)
2. Aplica reglas de razonamiento de `ui-reasoning.csv` para seleccionar las mejores coincidencias
3. Devuelve el sistema de diseño completo: patrón, estilo, colores, tipografía, efectos.
4. Incluye antipatrones a evitar

**Ejemplo:**

### Paso 3: Complementar con búsquedas detalladas (según sea necesario)

Después de obtener el sistema de diseño, utilice búsquedas de dominio para obtener detalles adicionales:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

---

---

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

```bash
# Get UX guidelines for animation and accessibility
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
```

---

```bash
# ASCII box (default) - best for terminal display
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

---

**Cuándo utilizar búsquedas detalladas:**

| Necesidad | Dominio | Ejemplo |
| --------------------- | ------------ | --------------------------------------- |
| Más opciones de estilo | `estilo` | `--estilo de dominio "glassmorfismo oscuro"` |
| Recomendaciones de gráficos | `gráfico` | `--gráfico de dominio "panel de control en tiempo real"` |
| Mejores prácticas de experiencia de usuario | `ux` | `--domain ux "accesibilidad de animación"` |
| Fuentes alternativas | `tipografía` | `--tipografía de dominio "lujo elegante"` |
| Estructura de aterrizaje | `aterrizaje` | `--dominio de aterrizaje "hero social-proof"` |

### Paso 4: Pautas de pila (predeterminado: html-tailwind)

Obtenga prácticas recomendadas específicas para la implementación. Si el usuario no especifica una pila, **el valor predeterminado es `html-tailwind`**.

Pilas disponibles: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

## Buscar referencia

### Dominios disponibles

| Dominio | Usar para | Palabras clave de ejemplo |
| ------------ | ------------------------------------ | -------------------------------------------------------- |
| `producto` | Recomendaciones de tipo de producto | SaaS, comercio electrónico, cartera, salud, belleza, servicio |
| `estilo` | Estilos, colores y efectos de la interfaz de usuario | glassmorfismo, minimalismo, modo oscuro, brutalismo |
| `tipografía` | Emparejamientos de fuentes, Google Fonts | elegante, lúdico, profesional, moderno |
| `color` | Paletas de colores por tipo de producto | saas, comercio electrónico, salud, belleza, fintech, servicio |
| `aterrizaje` | Estructura de página, estrategias de CTA | héroe, centrado en héroes, testimonial, precios, prueba social |
| `gráfico` | Tipos de gráficos, recomendaciones de bibliotecas | tendencia, comparación, línea de tiempo, embudo, pastel |
| `ux` | Mejores prácticas, antipatrones | animación, accesibilidad, índice z, carga |
| `reaccionar` | Rendimiento de React/Next.js | cascada, paquete, suspenso, memorándum, renderizado, caché |
| `web` | Directrices de la interfaz web | aria, foco, teclado, semántica, virtualizar |
| `rápido` | Avisos de IA, palabras clave CSS | (nombre de estilo) |

### Pilas disponibles

| Pila | Enfoque |
| --------------- | ---------------------------------------------- |
| `html-viento de cola` | Utilidades Tailwind, responsivas, todos los años (POR PREDETERMINADO) |
| `reaccionar` | Estado, ganchos, rendimiento, patrones |
| `siguientejs` | SSR, enrutamiento, imágenes, rutas API |
| `vista` | API de composición, Pinia, Vue Router |
| `esbelto` | Runas, tiendas, SvelteKit |
| `rápido` | Vistas, Estado, Navegación, Animación |
| `reaccionar-nativo` | Componentes, Navegación, Listas |
| `aleteo` | Widgets, estado, diseño, tematización |
| `shadcn` | componentes shadcn/ui, temas, formularios, patrones |

## Ejemplo de flujo de trabajo

**Solicitud de usuario:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

### Paso 1: Analizar los requisitos

- Tipo de producto: Servicio de Belleza/Spa
- Palabras clave de estilo: elegante, profesional, suave.
- Industria: Belleza/Bienestar
- Pila: html-tailwind (predeterminado)

### Paso 2: Generar sistema de diseño (REQUERIDO)

**Salida:** Sistema de diseño completo con patrones, estilos, colores, tipografía, efectos y anti-patrones.

### Paso 3: Complementar con búsquedas detalladas (según sea necesario)

# Obtenga opciones de tipografía alternativas si es necesario
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegante serifa de lujo" --tipografía de dominio
```

### Paso 4: Directrices de pila

**Entonces:** Sintetizar el sistema de diseño + búsquedas detalladas e implementar el diseño.

## Formatos de salida

El indicador `--design-system` admite dos formatos de salida:

# Markdown: lo mejor para la documentación
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "criptofintech" --design-system -f markdown
```

## Consejos para obtener mejores resultados

---

---

1. **Sea específico con las palabras clave** - "panel de control SaaS de atención médica" > "aplicación"
2. **Busca varias veces**: diferentes palabras clave revelan distintos conocimientos
3. **Combinar dominios** - Estilo + Tipografía + Color = Sistema de diseño completo
4. **Verifique siempre la UX**: busque "animación", "índice z", "accesibilidad" para problemas comunes
5. **Utilice el indicador de pila**: obtenga prácticas recomendadas específicas de la implementación
6. **Repetir**: si la primera búsqueda no coincide, pruebe con otras palabras clave

## Reglas comunes para la interfaz de usuario profesional

Estos son problemas que con frecuencia se pasan por alto y que hacen que la interfaz de usuario parezca poco profesional:

### Iconos y elementos visuales

| Regla | Hacer | No |
| -------------------------- | ----------------------------------------- | -------------------------------------- |
| **Sin íconos emoji** | Utilice iconos SVG (Heroicons, Lucide, Iconos simples) | Utilice emojis como 🎨 🚀 ⚙️ como íconos de la interfaz de usuario |
| **Estados de desplazamiento estable** | Utilice transiciones de color/opacidad al pasar el mouse | Utilice transformaciones de escala que cambien el diseño |
| **Logotipos de marca correctos** | SVG oficial de investigación de Simple Icons | Adivina o utiliza rutas de logotipo incorrectas |
| **Tamaño de ícono consistente** | Utilice viewBox fijo (24x24) con w-6 h-6 | Mezcle diferentes tamaños de íconos al azar |

### Interacción y cursor

| Regla | Hacer | No |
| ---------------------- | ----------------------------------------------- | -------------------------------------------- |
| **Puntero del cursor** | Agregue `puntero de cursor` a todas las tarjetas en las que se puede hacer clic/desplazarse | Dejar cursor predeterminado en elementos interactivos |
| **Retroalimentación al pasar el mouse** | Proporcionar información visual (color, sombra, borde) | Ningún elemento de indicación es interactivo |
| **Transiciones suaves** | Utilice `duración de colores de transición-200` | Cambios de estado instantáneos o demasiado lentos (>500ms) |

### Contraste del modo claro/oscuro

| Regla | Hacer | No |
| ------------------------- | ----------------------------------- | --------------------------------------- |
| **Modo de luz de tarjeta de cristal** | Utilice `bg-white/80` o una opacidad superior | Utilice `bg-white/10` (demasiado transparente) |
| **Luz de contraste de texto** | Utilice `#0F172A` (slate-900) para texto | Utilice `#94A3B8` (slate-400) para el cuerpo del texto |
| **Luz de texto apagada** | Utilice `#475569` (slate-600) mínimo | Utilice gris-400 o más claro |
| **Visibilidad de la frontera** | Utilice `border-gray-200` en modo claro | Utilice `borde-blanco/10` (invisible) |

### Diseño y espaciado

| Regla | Hacer | No |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| **Barra de navegación flotante** | Agregue espaciado `top-4 izquierda-4 derecha-4` | Pegue la barra de navegación a `top-0 izquierda-0 derecha-0` |
| **Relleno de contenido** | Cuenta para la altura fija de la barra de navegación | Deje que el contenido se esconda detrás de elementos fijos |
| **Ancho máximo consistente** | Utilice el mismo `max-w-6xl` o `max-w-7xl` | Mezclar diferentes anchos de contenedores |

## Lista de verificación previa a la entrega

Antes de entregar el código de UI, verifique estos elementos:

### Calidad visual

- [] No se utilizan emojis como íconos (use SVG en su lugar)
- [] Todos los íconos del conjunto de íconos consistente (Heroicons/Lucide)
- [] Los logotipos de la marca son correctos (verificados a partir de Simple Icons)
- [] Los estados de desplazamiento no provocan cambios en el diseño
- [] Utilice los colores del tema directamente (bg-primary), no el contenedor var()

### Interacción

- [] Todos los elementos en los que se puede hacer clic tienen "puntero de cursor"
- [] Los estados de desplazamiento proporcionan información visual clara
- [] Las transiciones son suaves (150-300 ms)
- [] Estados de enfoque visibles para la navegación con el teclado

### Modo claro/oscuro

- [] El texto del modo de luz tiene suficiente contraste (mínimo 4,5:1)
- [ ] Elementos de vidrio/transparentes visibles en modo claro
- [] Bordes visibles en ambos modos
- [] Pruebe ambos modos antes de la entrega

### Diseño

- [] Los elementos flotantes tienen una separación adecuada desde los bordes
- [] No hay contenido oculto detrás de barras de navegación fijas
- [] Responsivo a 375px, 768px, 1024px, 1440px
- [] Sin desplazamiento horizontal en el móvil

### Accesibilidad

- [] Todas las imágenes tienen texto alternativo.
- [] Las entradas del formulario tienen etiquetas
- [] El color no es el único indicador
- [ ] `prefiere-movimiento-reducido` respetado