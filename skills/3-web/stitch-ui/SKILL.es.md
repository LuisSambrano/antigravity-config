---
name: stitch-ui
description: Expert guide for creating effective prompts for Google Stitch AI UI design tool. Use when user wants to design UI/UX in Stitch, create app interfaces, generate mobile/web designs, or needs help crafting Stitch prompts. Covers prompt structure, specificity techniques, iteration strategies, and design-to-code workflows for Stitch by Google.
risk: safe
source: "self"
---

```
[Screen/Component Type] for [User/Context]

# Solicitud de diseño de interfaz de usuario de Stitch

Orientación experta para crear indicaciones efectivas en Google Stitch, la herramienta de diseño de interfaz de usuario impulsada por IA de Google Labs. Esta habilidad ayuda a crear indicaciones precisas y procesables que generan diseños de interfaz de usuario de alta calidad para aplicaciones web y móviles.

## ¿Qué es Google Stitch?

Google Stitch es un generador de UI de IA experimental impulsado por Gemini 2.5 Flash que transforma indicaciones de texto y referencias visuales en diseños de UI funcionales. Soporta:

- Generación de texto a interfaz de usuario a partir de indicaciones en lenguaje natural
- Conversión de imagen a UI a partir de bocetos, esquemas o capturas de pantalla
- Flujos de aplicaciones multipantalla y diseños responsivos
- Exportar a HTML/CSS, Figma y código
- Refinamiento iterativo con variantes y anotaciones.

## Principios básicos de motivación

### 1. Sea específico y detallado

Las indicaciones genéricas producen resultados genéricos. Las indicaciones específicas con requisitos claros producen diseños profesionales y personalizados.

** Mensaje deficiente: **
```
Crear un panel
```

**Aviso efectivo:**
```
Panel de control para miembros con cuadrícula de módulos del curso, barra de seguimiento del progreso, 
y barra lateral de alimentación de la comunidad con un tema morado y un diseño basado en tarjetas
```

**Por qué funciona:** Especifica componentes (módulos, progreso, feed), estructura de diseño (cuadrícula, barra lateral), estilo visual (tema morado, tarjetas) y contexto (panel de control de miembros).

### 2. Definir estilo visual y tema

Incluya siempre combinaciones de colores, estética del diseño y dirección visual para evitar resultados genéricos de IA.

**Componentes a especificar:**
- Paleta de colores (colores primarios, colores de acento)
- Estilo de diseño (minimalista, moderno, divertido, profesional, glassmorphic)
- Preferencias de tipografía (si corresponde)
- Espaciamiento y densidad (compacto, espacioso, equilibrado)

**Ejemplo:**
```
Página de producto de comercio electrónico con galería de imágenes destacadas, CTA para agregar al carrito, 
sección de reseñas y carrusel de productos relacionados. Utilice un estilo limpio y minimalista. 
diseño con detalles en verde salvia y generosos espacios en blanco.
```

### 3. Estructurar claramente los flujos multipantalla

Para aplicaciones con varias pantallas, enumere cada pantalla como viñetas antes de la generación.

**Enfoque:**
```
Aplicación de seguimiento de actividad física con:
- Pantalla de incorporación con selección de objetivos.
- Panel de inicio con estadísticas diarias y anillos de actividad.
- Biblioteca de ejercicios con filtros de categorías.
- Pantalla de perfil con logros y configuraciones.
```

Stitch pedirá confirmación antes de generar múltiples pantallas, asegurando la alineación con su visión.

### 4. Especificar plataforma y comportamiento responsivo

Indique si el diseño es para dispositivos móviles, tabletas, computadoras de escritorio o web responsivo.

**Ejemplos:**
```
Pantalla de inicio de sesión de la aplicación móvil (estilo iOS) con campos de correo electrónico/contraseña y botones de autenticación social

Página de destino responsiva que se adapta desde dispositivos móviles (320 px) a computadoras de escritorio (1440 px) 
con navegación plegable
```

### 5. Incluir requisitos funcionales

Describir elementos interactivos, estados y flujos de usuarios para generar diseños más completos.

**Elementos a especificar:**
- Acciones de botones y CTA.
- Campos de formulario y validación.
- Patrones de navegación
- Estados de carga
- Estados vacíos
- Manejo de errores

**Ejemplo:**
```
Flujo de pago con:
- Resumen del carrito con ajustadores de cantidad.
- Formulario de dirección de envío con validación.
- Selección de método de pago (tarjetas, PayPal, Apple Pay)
- Confirmación de pedido con número de seguimiento.
```

## Plantilla de estructura de mensajes

Utilice esta plantilla para obtener indicaciones completas:

Características clave:
- [Característica 1 con detalles específicos]
- [Característica 2 con detalles específicos]
- [Característica 3 con detalles específicos]

Estilo visual:
- [Esquema de colores]
- [Diseño estético]
- [Enfoque de diseño]

Plataforma: [Móvil/Web/Responsivo]
```

**Ejemplo:**
```
Panel de control para la plataforma de análisis SaaS

Características clave:
- Tarjetas de métricas principales que muestran MRR, usuarios activos, tasa de abandono
- Gráfico de líneas para tendencias de ingresos (últimos 30 días)
- Feed de actividad reciente con acciones de usuario.
- Botones de acción rápida para informes y exportaciones.

Estilo visual:
- Modo oscuro con detalles en degradado azul/púrpura
- Modernas tarjetas glassmorphic con sombras sutiles.
- Visualización de datos limpia con colores accesibles.

Plataforma: web responsiva (primero el escritorio)
```

## Estrategias de iteración

### Refinar con anotaciones

Utilice la función "anotar para editar" de Stitch para realizar cambios específicos sin tener que reescribir todo el mensaje.

**Flujo de trabajo:**
1. Genere el diseño inicial desde el mensaje
2. Anotar elementos específicos que necesitan cambios.
3. Describir modificaciones en lenguaje natural.
4. Stitch actualiza solo las áreas anotadas

**Anotaciones de ejemplo:**
- "Agrande este botón y use el color primario"
- "Agrega más espacio entre estas tarjetas"
- "Cambiar esto a un diseño horizontal"

### Generar variantes

```
Generate 3 variants of this hero section:
1. Image-focused with minimal text
2. Text-heavy with supporting graphics
3. Video background with overlay content
```

```
SaaS landing page for [product name]

```
Food delivery app home screen

```
Admin dashboard for content management system

```
Multi-step signup form for B2B platform

---

---

Solicite múltiples variaciones para explorar diferentes direcciones de diseño:

### Refinamiento progresivo

Comience de manera amplia y luego agregue especificidad en las indicaciones de seguimiento:

**Inicial:**
```
Página de inicio de comercio electrónico
```

**Refinamiento 1:**
```
Agregue una sección de productos destacados con cuadrícula de 4 columnas y efectos de desplazamiento
```

**Refinamiento 2:**
```
Actualizar la combinación de colores a tonos tierra (terracota, salvia, crema) 
y agregue un banner promocional en la parte superior
```

## Casos de uso comunes

### Páginas de destino

Secciones:
- Héroe con título, subtítulo, CTA y captura de pantalla del producto.
- Prueba social con logotipos de clientes.
- Cuenta con cuadrícula (3 columnas) con iconos.
- Carrusel de testimonios
- Tabla de precios (3 niveles)
- Preguntas frecuentes sobre acordeón
- Pie de página con enlaces y suscripción al boletín

Estilo: moderno, profesional, generador de confianza.
Colores: azul marino primario, detalles en azul claro, fondo blanco.
```

### Aplicaciones móviles

Componentes:
- Barra de búsqueda con selector de ubicación.
- Chips de categoría (Pizza, Hamburguesas, Sushi, etc.)
- Tarjetas de restaurante con imagen, nombre, calificación, tiempo de entrega y rango de precios.
- Navegación inferior (Inicio, Búsqueda, Pedidos, Perfil)

Estilo: Vibrante, atractivo, fácil de escanear
Colores: Naranja primario, fondo blanco, fotografía de comida.
Plataforma: móvil iOS (375 px de ancho)
```

### Paneles de control

Diseño:
- Navegación en la barra lateral izquierda con menú plegable
- Barra superior con búsqueda, notificaciones y perfil de usuario.
- Área de contenido principal con:
  - Resumen de estadísticas (4 tarjetas de métricas)
  - Tabla de publicaciones recientes con acciones.
  - Cronograma de actividades
  - Panel de acciones rápidas

Estilo: limpio, centrado en datos, profesional
Colores: Grises neutros con detalles en azul.
Plataforma: Web de escritorio (1440px)
```

### Formularios y entradas

Pasos:
1. Detalles de la cuenta (nombre de la empresa, correo electrónico, contraseña)
2. Información de la empresa (industria, tamaño, función)
3. Configuración del equipo (invitar miembros)
4. Confirmación con mensaje de éxito.

Características:
- Indicador de progreso en la parte superior
- Validación de campo con errores en línea.
- Navegación atrás/siguiente
- Saltar opción para el paso 3

Estilo: Mínimo, enfocado, de baja fricción
Colores: fondo blanco, verde para estados de éxito.
```

## Flujo de trabajo de diseño a código

### Opciones de exportación

Stitch proporciona múltiples formatos de exportación:

1. **HTML/CSS**: marcado semántico y limpio para proyectos web
2. **Figma** - "Pegar en Figma" para la integración del sistema de diseño
3. **Fragmentos de código**: exportaciones a nivel de componentes para marcos

### Mejores prácticas para la exportación

**Antes de exportar:**
- Verificar puntos de interrupción receptivos
- Verifique el contraste de color para accesibilidad
- Garantizar que los estados interactivos estén definidos.
- Revisar el nombre y la estructura de los componentes.

**Después de la exportación:**
- Refactorizar código generado para estándares de producción.
- Agregar etiquetas HTML semánticas adecuadas
- Implementar atributos de accesibilidad (etiquetas ARIA, texto alternativo)
- Optimizar imágenes y activos.
- Añadir animaciones y microinteracciones.

## Antipatrones a evitar

### ❌ Indicaciones vagas
```
Haz un buen sitio web
```

### ✅ Indicaciones específicas
```
Sitio web de portafolio para fotógrafos con galería de imágenes en pantalla completa, 
estudios de casos de proyectos y formulario de contacto. Minimalista en blanco y negro 
estética con tipografía serif.
```

### ❌ Falta contexto
```
Crear una página de inicio de sesión
```

### ✅ Indicaciones ricas en contexto
```
Página de inicio de sesión para el portal de atención médica con campos de correo electrónico/contraseña, 
Casilla de verificación "Recordarme", enlace "Olvidé mi contraseña" y opciones de SSO 
(Google, Microsoft). Diseño profesional y confiable con 
tema médico azul.
```

### ❌ Sin dirección visual
```
Diseñar una aplicación para la gestión de tareas.
```

### ✅ Dirección visual clara
```
Aplicación de gestión de tareas con diseño de tablero kanban, tarjetas de arrastrar y soltar, 
etiquetas de prioridad e indicadores de fecha de vencimiento. Moderno, centrado en la productividad 
diseño con detalles degradados en violeta/verde azulado y soporte para modo oscuro.
```

## Consejos para obtener mejores resultados

1. **Haga referencia a diseños existentes**: cargue capturas de pantalla o bocetos como referencias visuales junto con indicaciones de texto.

2. **Utilice terminología de diseño** - Términos como "sección de héroe", "diseño de tarjeta", "glassmorphic", "rejilla bento" ayudan a Stitch a comprender su intención.

3. **Especificar interacciones**: describa los estados de desplazamiento, las acciones de clic y las transiciones para obtener diseños más completos.

4. **Piense en componentes**: divida pantallas complejas en componentes reutilizables (encabezado, tarjeta, formulario, etc.)

5. **Repita de forma incremental**: realice cambios pequeños y específicos en lugar de rediseños completos

6. **Pruebe la capacidad de respuesta**: verifique siempre los diseños en múltiples puntos de interrupción (móvil, tableta, computadora de escritorio)

7. **Considere la accesibilidad**: mencione el contraste de color, los tamaños de fuente y los tamaños de los objetivos táctiles en las indicaciones.

8. **Aprovechar variantes**: genere múltiples opciones para explorar diferentes direcciones de diseño rápidamente

## Integración con el flujo de trabajo de desarrollo

### Puntada → Figma → Código
1. Genere una interfaz de usuario en Stitch con indicaciones detalladas
2. Exportar a Figma para la integración del sistema de diseño.
3. Entregar a los desarrolladores las especificaciones de diseño.
4. Implementar con código listo para producción

### Puntada → HTML → Marco
1. Generar y perfeccionar la interfaz de usuario en Stitch
2. Exportar código HTML/CSS
3. Convertir a componentes React/Vue/Svelte
4. Integre en el código base de la aplicación

### Creación rápida de prototipos
1. Cree múltiples variaciones de pantalla rápidamente
2. Pruebe con usuarios o partes interesadas
3. Iterar en función de los comentarios
4. Finalizar el diseño para el desarrollo.

## Conclusión

Las indicaciones efectivas de Stitch son específicas, ricas en contexto y visualmente descriptivas. Si sigue estos principios y plantillas, podrá generar diseños de UI profesionales que sirvan como bases sólidas para aplicaciones de producción.

**Recuerda:** La puntada es un punto de partida, no un producto final. Úselo para acelerar el proceso de diseño, explorar ideas rápidamente y establecer una dirección visual; luego, refine con criterio humano y estándares de producción.