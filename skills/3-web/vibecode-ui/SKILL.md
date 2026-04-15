---
name: vibecode-ui
description: UI/UX implementation guidelines specializing in Glassmorphism and high-performance Web Interfaces. Enforces Next.js 14+ architectural standards and WCAG accessibility compliance.
version: 1.0
author: Antigravity
---

# Framework Vibecode UI/UX Pro Max

> [!IMPORTANT]
> This skill MUST be executed strictly under the **Omni-Architect Agent Protocol v1.0**.
> All tool executions, code modifications, and communications MUST adhere to the 13 core protocols.

Este skill fusiona la filosofía de diseño "Vibecode" con estándares de ingeniería de "Next Level Builder".

## � Biblioteca de Datos Extendida (Full Mode)

Este Skill tiene acceso a una base de datos de reglas detallada en `./data/`.
Antes de realizar tareas complejas, **consulta los archivos CSV relevantes** en `~/playground/.agent/skills/vibecode-ui/data/`:

- `ux-guidelines.csv`: Lista de verificación UX exhaustiva (100+ reglas).
- `styles.csv`: Definiciones detalladas de 67 estilos visuales.
- `stacks/`: Guías específicas para frameworks (Next.js, Vue, Flutter, etc.).
- `ui-reasoning.csv`: Lógica para decidir qué patrón usar según el tipo de producto.

**Instrucción de Activación**: Si el usuario pide un stack específico (ej: "Astro") o un estilo inusual (ej: "Neubrutalism"), LEE el archivo CSV correspondiente primero.

## �📋 Las 5 Dimensiones del Diseño (Estética)

Al generar CUALQUIER UI, debes cumplir estas 5 reglas visuales:

### 1. **PATRÓN Y DISEÑO**

- **SaaS**: Hero + Social Proof + CTA (Valor primero).
- **Luxury/E-commerce**: Hero Slider + Galería Inmersiva.
- **Dashboard**: Bento Grid + Data Density.

### 2. **ESTILO (Glassmorphism Luxury)**

- `backdrop-filter: blur(12px)`
- `bg-white/5` (Dark Mode) o `bg-black/5` (Light Mode).
- Bordes sutiles: `border-white/10`.
- **Sombra Interior**: `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.1)]`.

### 3. **COLOR & TEMA**

- **Palette**: Luxury Dark (`#0A0A0A`, `#1C1917`, Gold `#CA8A04`).
- **Gradient**: Aurora Beams (usar imágenes o CSS radial gradients).

### 4. **ANIMACIONES (El Alma)**

- **Entrada**: `initial={{ opacity: 0, y: 20 }}` -> `animate={{ opacity: 1, y: 0 }}`.
- **Scroll**: Stagger children con `framer-motion`.
- **Micro**: Escala `1.02` en hover.

---

## � Módulos Avanzados (Google Antigravity)

Integración de capacidades de alto nivel detectadas en su repositorio local:

### **Módulo 3D (Web Experience)**

- **Herramienta Preferida**: `Spline` para escenas rápidas ("Gorgeous" con bajo esfuerzo) o `React Three Fiber` para interactividad compleja.
- **Performance**: Modelos GLB comprimidos (Draco). NUNCA bloquear el thread principal.
- **Regla de Oro**: Si el 3D no aporta valor narrativo o estético, usa una imagen/video optimizado.

### **Módulo de Diseño Intencional (Frontend Design)**

- **Mandato Anti-Genérico**: Evita layouts predecibles de Tailwind. "Rompe la grilla" intencionalmente con asimetría y superposiciones.
- **Índice DFII**: Evalúa cada diseño: ¿Es memorable? ¿Tiene un ancla visual única?
- **Tipografía Estructural**: Usa fuentes display expresivas, no solo System Fonts.

---

## �🛠️ Estándares de Ingeniería (Next.js 15+ / React)

Reglas estrictas extraídas de `ui-ux-pro-max`:

### **Routing & Rendering**

1.  **Server Components por Defecto**: Mantén la lógica en el servidor. Solo usa `'use client'` en las hojas (botones, inputs).
2.  **App Router**: Estructura `app/(marketing)/page.tsx` para grupos de rutas.
3.  **Loading**: Usa `loading.tsx` y `<Suspense>` para streaming de UI.

### **Performance & Images**

1.  **Next/Image**: OBLIGATORIO. Nunca uses `<img>`.
2.  **Dimensiones**: Siempre define `width/height` o usa `fill` con un padre relativo.
3.  **Fuentes**: Usa `next/font` (Inter/JetBrains Mono) para evitar CLS (Cumulative Layout Shift).

### **Data Fetching**

1.  **Server Actions**: Usa Server Actions para mutaciones (formularios), no API Routes antiguas.
2.  **Direct Fetch**: Haz fetch de datos directamente en Server Components (`await fetch()`).

---

## 🛡️ Garantía de UX y Accesibilidad

Antes de entregar código, verifica:

### **Interacción**

- [ ] **Touch Targets**: Mínimo 44x44px en móviles.
- [ ] **Feedback**: Estados de carga (Spinners/Skeletons) para acciones > 300ms.
- [ ] **Errores**: Mensajes de error claros y cercanos al input fallido.

### **Accesibilidad**

- [ ] **Contraste**: Texto gris claro sobre fondo oscuro debe ser legible (`text-neutral-400` mínimo).
- [ ] **Focus**: Nunca quites `outline` sin poner un reemplazo (`ring-2 ring-accent`).
- [ ] **Etiquetas**: Todos los inputs deben tener `label` o `aria-label`.

---

## 🚫 Anti-Patrones (Prohibido)

- ❌ **Flash over Function**: Animaciones que duran > 500ms.
- ❌ **Layout Shift**: Imágenes sin dimensionar que empujan el contenido.
- ❌ **Prop Drilling**: Pasar props más de 3 niveles (usa Composition o Context).
- ❌ **Div Soup**: Divs anidados innecesariamente. Usa `Fragment` (`<>`) o Grid/Flex inteligentemente.

---

**Inyección de Prompt**:
"Genera un Dashboard de Ventas" ->

1.  **Estilo**: Bento Grid, Glassmorphism, Dark Mode.
2.  **Tecnología**: Next.js App Router, Server Components para data, Recharts para gráficos.
3.  **UX**: Skeletons al cargar, tooltips en gráficos.
