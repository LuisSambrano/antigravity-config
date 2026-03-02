---
name: vibecode-ui
description: "UI/UX implementation guidelines specializing in Glassmorphism and high-performance Web Interfaces. Enforces Next.js 14+ architectural standards and WCAG accessibility compliance."
---

---

---

---

---

---

# Marco Vibecode UI/UX Pro Max

Esta habilidad fusiona la filosofía de diseño "Vibecode" con los estándares de ingeniería de "Next Level Builder".

## � Biblioteca de Datos Extendida (Modo Completo)

Este Skill tiene acceso a una base de datos de reglas detalladas en `./data/`.
Antes de realizar tareas complejas, **consulta los archivos CSV relevantes** en `~/playground/.agent/skills/vibecode-ui/data/`:

- `ux-guidelines.csv`: Lista de verificación UX exhaustiva (100+ reglas).
- `styles.csv`: Definiciones detalladas de 67 estilos visuales.
- `stacks/`: Guías específicas para frameworks (Next.js, Vue, Flutter, etc.).
- `ui-reasoning.csv`: Lógica para decidir qué patrón usar según el tipo de producto.

**Instrucción de Activación**: Si el usuario pide un stack específico (ej: "Astro") o un estilo inusual (ej: "Neubrutalism"), LEE el archivo CSV correspondiente primero.

## �📋 Las 5 Dimensiones del Diseño (Estética)

Al generar CUALQUIER UI, debes cumplir estas 5 reglas visuales:

### 1. **PATRÓN Y DISEÑO**

- **SaaS**: Héroe + Prueba social + CTA (Valor primero).
- **Lujo/E-commerce**: Hero Slider + Galería Inmersiva.
- **Panel**: Bento Grid + Densidad de datos.

### 2. **ESTILO (Glasmorfismo de lujo)**

- `filtro de fondo: desenfoque (12px)`
- `bg-white/5` (Modo Oscuro) o `bg-black/5` (Modo Claro).
- Bordes sutiles: `borde-blanco/10`.
- **Sombra Interior**: `sombra-[inset_0_1px_0_0_rgba(255,255,255,0.1)]`.

### 3. **COLOR Y TEMA**

- **Paleta**: Lujo Oscuro (`#0A0A0A`, `#1C1917`, Dorado `#CA8A04`).
- **Gradient**: Aurora Beams (usar imágenes o gradientes radiales CSS).

### 4. **ANIMACIONES (El Alma)**

- **Entrada**: `inicial={{ opacidad: 0, y: 20 }}` -> `animate={{ opacidad: 1, y: 0 }}`.
- **Scroll**: Escalonar a los niños con `framer-motion`.
- **Micro**: Escala `1.02` al pasar el mouse.

## � Módulos Avanzados (Google Antigravity)

Integración de capacidades de alto nivel detectadas en su repositorio local:

### **Módulo 3D (Experiencia Web)**

- **Herramienta Preferida**: `Spline` para escenas rápidas ("Gorgeous" con bajo esfuerzo) o `React Three Fiber` para interactividad compleja.
- **Rendimiento**: Modelos GLB comprimidos (Draco). NUNCA bloquea el hilo principal.
- **Regla de Oro**: Si el 3D no aporta valor narrativo o estético, utiliza una imagen/video optimizado.

### **Módulo de Diseño Intencional (Diseño Frontend)**

- **Mandato Anti-Genérico**: Evita diseños predecibles de Tailwind. "Rompe la grilla" intencionalmente con asimetría y superposiciones.
- **Índice DFII**: Evalúa cada diseño: ¿Es memorable? ¿Tiene una ancla visual única?
- **Tipografía Estructural**: Usa fuentes que muestran expresivas, no solo System Fonts.

## �🛠️ Estándares de Ingeniería (Next.js 15+ / React)

Reglas estrictas extraídas de `ui-ux-pro-max`:

### **Enrutamiento y renderizado**

1. **Componentes del servidor por defecto**: Mantén la lógica en el servidor. Solo usa `'use client'` en las hojas (botones, insumos).
2. **App Router**: Estructura `app/(marketing)/page.tsx` para grupos de rutas.
3. **Loading**: Usa `loading.tsx` y `<Suspense>` para streaming de UI.

### **Rendimiento e imágenes**

1. **Siguiente/Imagen**: OBLIGATORIO. Nunca usa `<img>`.
2. **Dimensiones**: Siempre define `width/height` o usa `fill` con un padre relativo.
3. **Fuentes**: Usa `next/font` (Inter/JetBrains Mono) para evitar CLS (Cumulative Layout Shift).

### **Obtención de datos**

1. **Acciones del servidor**: Usa Server Actions para mutaciones (formularios), no API Routes antiguas.
2. **Obtención directa**: Busque datos directamente en los componentes del servidor (`await fetch()`).

## 🛡️ Garantía de UX y Accesibilidad

Antes de entregar el código, verifique:

### **Interacción**

- [ ] **Objetivos táctiles**: Mínimo 44x44px en móviles.
- [ ] **Comentarios**: Estados de carga (Spinners/Skeletons) para acciones > 300ms.
- [ ] **Errores**: Mensajes de error claros y cercanos al input fallido.

### **Accesibilidad**

- [ ] **Contraste**: Texto gris claro sobre fondo oscuro debe ser legible (`text-neutral-400` mínimo).
- [ ] **Focus**: Nunca quites `outline` sin poner un reemplazo (`ring-2 ring-accent`).
- [ ] **Etiquetas**: Todos los inputs deben tener `label` o `aria-label`.

## 🚫 Anti-Patrones (Prohibido)

- ❌ **Función Flash over**: Animaciones que duran > 500ms.
- ❌ **Layout Shift**: Imágenes sin dimensión que empujan el contenido.
- ❌ **Prop Drilling**: Pasar props más de 3 niveles (usa Composition o Context).
- ❌ **Div Soup**: Divs anidados innecesariamente. Usa `Fragment` (`<>`) o Grid/Flex inteligentemente.

**Inyección de Aviso**:
"Genera un Panel de Ventas" ->

1. **Estilo**: Bento Grid, Glassmorfismo, Modo oscuro.
2. **Tecnología**: Next.js App Router, Server Components para datos, Recharts para gráficos.
3. **UX**: Esqueletos al cargar, información sobre herramientas y gráficos.