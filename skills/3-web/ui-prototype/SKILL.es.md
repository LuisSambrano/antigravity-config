---
name: ui-prototype
description: UI/UX prototyping workflow using generate_image tool. Use when the user wants to design mockups, wireframes, or visual prototypes before coding.
---

# Creación de prototipos UI/UX con generate_image

Cree maquetas visuales e itere diseños de interfaz de usuario antes de escribir código.

## Cuándo utilizar

- El usuario dice "diseña una UI", "crea un mockup", "prototipa esto"
- Antes de construir componentes complejos de UI
- Cuando el usuario quiere visualizar un diseño antes de codificar.

## Flujo de trabajo

### 1. Comprender los requisitos

- ¿Cuál es el propósito de la página/componente?
- ¿Quién es el público objetivo?
- ¿Cuál es el estilo de diseño? (morfismo de vidrio, minimalista, brutalista, etc.)
- ¿Primero el móvil o el escritorio?

### 2. Generar maqueta inicial

Utilice `generate_image` con un mensaje detallado que describa:

- Estructura de diseño (encabezado, barra lateral, área de contenido, pie de página)
- Paleta de colores y estilo.
- Elementos clave de la interfaz de usuario (botones, tarjetas, formularios, tablas)
- Preferencias de tipografía
- Modo oscuro/claro

### 3. Repetir los comentarios

Refine el diseño basándose en los comentarios de los usuarios mediante llamadas de seguimiento "generate_image" con ajustes.

### 4. Extraer tokens de diseño

A partir de la maqueta aprobada, defina:

- Variables de color (propiedades personalizadas de CSS)
- Escala de espaciado
- Escala de tipografía
- Radio del borde, sombras.
- Patrones de componentes

### 5. Implementar

Traduzca la maqueta aprobada a código utilizando los tokens de diseño establecidos.

## Consejos rápidos

- Sea específico sobre el diseño ("cuadrícula de 3 columnas con barra lateral")
- Hacer referencia a sistemas de diseño conocidos ("inspirados en Linear/Notion/Vercel")
- Especifique los colores exactos cuando sea posible ("use el fondo #0A0A0A")
- Incluir ejemplos de contenido, no Lorem Ipsum.
- Especifique el modo oscuro con efectos de vidrio si usa morfismo de vidrio

## Antipatrones

- ❌ Generar antes de entender requisitos
- ❌ Codificación antes de obtener la aprobación de la maqueta
- ❌ Uso de texto de marcador de posición en maquetas finales
- ❌ Ignorar la capacidad de respuesta móvil en los prototipos