---
name: vercel-rn
description:
  React Native and Expo best practices for building performant mobile apps. Use
  when building React Native components, optimizing list performance,
  implementing animations, or working with native modules. Triggers on tasks
  involving React Native, Expo, mobile performance, or native platform APIs.
license: MIT
metadata:
  author: vercel
  version: '1.0.0'
---

```
rules/list-performance-virtualize.md
rules/animation-gpu-properties.md
```

# Reaccionar habilidades nativas

Mejores prácticas integrales para aplicaciones React Native y Expo. Contiene
reglas en múltiples categorías que cubren rendimiento, animaciones, patrones de interfaz de usuario,
y optimizaciones específicas de la plataforma.

## Cuándo presentar la solicitud

Consulte estas pautas cuando:

- Creación de aplicaciones React Native o Expo
- Optimización del rendimiento de lista y desplazamiento
- Implementación de animaciones con Reanimated
- Trabajar con imágenes y medios.
- Configuración de módulos o fuentes nativas.
- Estructuración de proyectos monorepo con dependencias nativas.

## Categorías de reglas por prioridad

| Prioridad | Categoría | Impacto | Prefijo |
| -------- | ---------------- | -------- | -------------------- |
| 1 | Rendimiento de la lista | CRÍTICO | `lista-rendimiento-` |
| 2 | Animación | ALTA | `animación-` |
| 3 | Navegación | ALTA | `navegación-` |
| 4 | Patrones de interfaz de usuario | ALTA | `ui-` |
| 5 | Gestión Estatal | MEDIANO | `reaccionar-estado-` |
| 6 | Representación | MEDIANO | `renderizado-` |
| 7 | Monorepo | MEDIANO | `monorepo-` |
| 8 | Configuración | BAJO | `fuentes-`, `importaciones-` |

## Referencia rápida

### 1. Rendimiento de la lista (CRÍTICO)

- `list-rendimiento-virtualizar` - Utilice FlashList para listas grandes
- `list-performance-item-memo` - Memorizar los componentes de los elementos de la lista
- `list-rendimiento-callbacks` - Estabilizar referencias de devolución de llamada
- `list-rendimiento-inline-objects` - Evitar objetos de estilo en línea
- `list-rendimiento-función-referencias` - Extraer funciones fuera del renderizado
- `list-rendimiento-images` - Optimizar imágenes en listas
- `list-rendimiento-elemento-costoso` - Mover el trabajo costoso fuera de los elementos
- `list-rendimiento-item-types` - Usar tipos de elementos para listas heterogéneas

### 2. Animación (ALTA)

- `animation-gpu-properties` - Animar solo transformación y opacidad
- `animation-derived-value` - Utilice useDerivedValue para animaciones calculadas
- `animation-gesture-detector-press` - Utilice Gesture.Tap en lugar de Pressable

### 3. Navegación (ALTA)

- `navigation-native-navigators` - Utilice pila nativa y pestañas nativas sobre navegadores JS

### 4. Patrones de interfaz de usuario (ALTO)

- `ui-expo-image` - Usa expo-image para todas las imágenes
- `ui-image-gallery` - Utilice Galeria para cajas de luz de imágenes
- `ui-pressable` - Utilice Pressable sobre TouchableOpacity
- `ui-safe-area-scroll` - Maneja áreas seguras en ScrollViews
- `ui-scrollview-content-inset` - Utilice contentInset para encabezados
- `ui-menus` - Usar menús contextuales nativos
- `ui-native-modals` - Utilice modales nativos cuando sea posible
- `ui-measure-views` - Utilice onLayout, no medida()
- `ui-styling` - Utilice StyleSheet.create o Nativewind

### 5. Gestión del Estado (MEDIO)

- `react-state-minimize` - Minimizar las suscripciones estatales
- `react-state-dispatcher` - Usa el patrón de despachador para devoluciones de llamadas
- `react-state-fallback`: muestra el respaldo en el primer renderizado
- `react-compiler-destructure-functions` - Deestructura para React Compiler
- `react-compiler-reanimated-shared-values` - Maneja valores compartidos con el compilador

### 6. Renderizado (MEDIO)

- `rendering-text-in-text-component` - Ajustar texto en componentes de texto
- `rendering-no-falsy-and` - Evita falsy && para renderizado condicional

### 7. Monorepo (MEDIO)

- `monorepo-native-deps-in-app` - Mantiene las dependencias nativas en el paquete de la aplicación
- `monorepo-single-dependency-versions`: utiliza versiones únicas en todos los paquetes

### 8. Configuración (BAJA)

- `fonts-config-plugin`: utiliza complementos de configuración para fuentes personalizadas
- `imports-design-system-folder` - Organizar las importaciones del sistema de diseño
- `js-hoist-intl` - Creación de objetos Hoist Intl

## Cómo utilizar

Lea archivos de reglas individuales para obtener explicaciones detalladas y ejemplos de código:

Cada archivo de reglas contiene:

- Breve explicación de por qué es importante.
- Ejemplo de código incorrecto con explicación.
- Ejemplo de código correcto con explicación.
- Contexto y referencias adicionales.

## Documento compilado completo

Para obtener la guía completa con todas las reglas ampliadas: `AGENTS.md`