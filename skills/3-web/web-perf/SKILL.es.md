---
name: web-perf
description: "Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance"
---

```markdown
## Performance Audit Results

# Optimización del rendimiento web

## Descripción general

Ayude a los desarrolladores a optimizar el rendimiento de los sitios web y las aplicaciones web para mejorar la experiencia del usuario, las clasificaciones SEO y las tasas de conversión. Esta habilidad proporciona enfoques sistemáticos para medir, analizar y mejorar la velocidad de carga, el rendimiento del tiempo de ejecución y las métricas de Core Web Vitals.

## Cuándo utilizar esta habilidad

- Úselo cuando el sitio web o la aplicación se carga lentamente
- Úselo al optimizar para Core Web Vitals (LCP, FID, CLS)
- Úselo al reducir el tamaño del paquete de JavaScript
- Úselo al mejorar el tiempo de interacción (TTI)
- Úselo al optimizar imágenes y recursos.
- Úselo al implementar estrategias de almacenamiento en caché
- Úselo al depurar cuellos de botella en el rendimiento.
- Úselo al prepararse para auditorías de desempeño.

## Cómo funciona

### Paso 1: Medir el rendimiento actual

Te ayudaré a establecer métricas de referencia:
- Ejecutar auditorías de Lighthouse
- Medir los elementos básicos de la web (LCP, FID, CLS)
- Verifique los tamaños de los paquetes
- Analizar la cascada de la red.
- Identificar cuellos de botella en el rendimiento.

### Paso 2: Identificar los problemas

Analizar problemas de rendimiento:
- Grandes paquetes de JavaScript
- Imágenes no optimizadas
- Recursos de bloqueo de renderizado
- Tiempos de respuesta lentos del servidor
- Faltan encabezados de almacenamiento en caché
- Cambios de diseño
- Tareas largas que bloquean el hilo principal.

### Paso 3: Priorizar las optimizaciones

Centrarse en mejoras de alto impacto:
- Optimización de la ruta de renderizado crítico
- División de código y carga diferida
- Optimización de imagen
- Estrategias de almacenamiento en caché
- Optimización de secuencias de comandos de terceros

### Paso 4: implementar optimizaciones

Aplicar mejoras de rendimiento:
- Optimizar activos (imágenes, fuentes, CSS, JS)
- Implementar división de código.
- Agregar encabezados de almacenamiento en caché
- Carga diferida de recursos no críticos
- Optimizar la ruta de renderizado crítica

### Paso 5: Verificar las mejoras

Medir el impacto de los cambios:
- Volver a ejecutar las auditorías de Lighthouse
- Comparar métricas antes/después
- Monitorear métricas reales de usuarios (RUM)
- Prueba en diferentes dispositivos y redes.

## Ejemplos

### Ejemplo 1: Optimización de Core Web Vitals

### Métricas actuales (antes de la optimización)
- **LCP (pintura con mayor contenido):** 4,2 s ❌ (debe ser < 2,5 s)
- **FID (Retraso de la primera entrada):** 180 ms ❌ (debe ser < 100 ms)
- **CLS (cambio de diseño acumulativo):** 0,25 ❌ (debe ser < 0,1)
- **Puntuación del faro:** 62/100

### Problemas identificados

1. **Problema de LCP:** La imagen principal (2,5 MB) se carga lentamente
2. **Problema de FID:** Un paquete grande de JavaScript (850 KB) bloquea el hilo principal
3. **Problema de CLS:** Las imágenes sin dimensiones provocan cambios en el diseño

### Plan de optimización

#### Arreglar LCP (pintura con contenido más grande)

**Problema:** La imagen principal pesa 2,5 MB y se carga lentamente.

**Soluciones:**
\`\`\`html
<!-- Antes: Imagen no optimizada -->
<img src="/hero.jpg" alt="Héroe">

<!-- Después: Optimizado con formatos modernos -->
<imagen>
  <fuente srcset="/hero.avif" tipo="imagen/avif">
  <fuente srcset="/hero.webp" tipo="imagen/webp">
  <img 
    src="/héroe.jpg" 
    alt="Héroe"
    ancho="1200" 
    altura="600"
    cargando="ansioso"
    fetchpriority="alto"
  >
</imagen>
\`\`\`

**Optimizaciones adicionales:**
- Comprimir imagen a <200 KB
- Utilice CDN para una entrega más rápida
- Precargar imagen principal: `<link rel="preload" as="image" href="/hero.avif">`

#### Reparar FID (retraso de la primera entrada)

**Problema:** El paquete JavaScript de 850 KB bloquea el hilo principal

**Soluciones:**

1. **División de código:**
\`\`\`javascript
// Antes: Todo en un solo paquete
importar { HeavyComponent } desde './HeavyComponent';
importar { Analytics } desde './analytics';
importar { ChatWidget } desde './chat';

// Después: carga diferida de código no crítico
const HeavyComponent = lazy(() => import('./HeavyComponent'));
const ChatWidget = lazy(() => import('./chat'));

// Cargar análisis después de la página interactiva
if (tipo de ventana! == 'indefinido') {
  ventana.addEventListener('cargar', () => {
    importar('./analytics').luego(({ Analytics }) => {
      Analytics.init();
    });
  });
}
\`\`\`

2. **Eliminar dependencias no utilizadas:**
\`\`\`golpe
# Analizar paquete
analizador-de-paquetes-webpack-npx

# Eliminar paquetes no utilizados
Momento de desinstalación de npm # Use date-fns en su lugar (más pequeño)
npm instala fecha-fns
\`\`\`

3. **Aplazar secuencias de comandos no críticas:**
\`\`\`html
<!-- Antes: Representación de bloques -->
<script src="/analytics.js"></script>

<!-- Después: Diferido -->
<script src="/analytics.js" aplazar></script>
\`\`\`

#### Arreglar CLS (cambio de diseño acumulativo)

**Problema:** Las imágenes sin dimensiones provocan cambios en el diseño.

**Soluciones:**
\`\`\`html
<!-- Antes: Sin dimensiones -->
<img src="/producto.jpg" alt="Producto">

<!-- Después: Con dimensiones -->
<img 
  src="/producto.jpg" 
  alt="Producto"
  ancho="400" 
  altura="300"
  estilo="relación de aspecto: 4/3;"
>
\`\`\`

```markdown
## Bundle Size Optimization

```markdown
## Image Optimization

**Para contenido dinámico:**
\`\`\`css
/* Reservar espacio para contenido que se carga más tarde */
.esqueleto-cargador {
  altura mínima: 200 px;
  fondo: gradiente lineal (90 grados, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  tamaño de fondo: 200% 100%;
  animación: cargando 1,5 s infinito;
}

@keyframes cargando {
  0% { posición-fondo: 200% 0; }
  100% { posición-fondo: -200% 0; }
}
\`\`\`

### Resultados después de la optimización

- **LCP:** 1,8s ✅ (mejorado en un 57%)
- **FID:** 45 ms ✅ (mejorado en un 75%)
- **CLS:** 0,05 ✅ (mejorado en un 80%)
- **Puntuación del faro:** 94/100 ✅
```

### Ejemplo 2: Reducir el tamaño del paquete de JavaScript

### Estado actual
- **Paquete total:** 850 KB (comprimido con g: 280 KB)
- **Paquete principal:** 650 KB
- **Paquete de proveedor:** 200 KB
- **Tiempo de carga (3G):** 8,2 s

### Análisis

\`\`\`golpe
# Analizar la composición del paquete
npx webpack-bundle-analyzer dist/stats.json
\`\`\`

**Hallazgos:**
1. Moment.js: 67 KB (se puede reemplazar con date-fns: 12 KB)
2. Lodash: 72 KB (usando la biblioteca completa, solo necesita 5 funciones)
3. Código no utilizado: ~150 KB de código inactivo
4. Sin división de códigos: todo en un solo paquete

### Pasos de optimización

#### 1. Reemplazar dependencias pesadas

\`\`\`golpe
# Eliminar moment.js (67KB) → Usar date-fns (12KB)
momento de desinstalación de npm
npm instala fecha-fns

# Antes
importar momento desde 'momento';
const formateado = momento(fecha).format('AAAA-MM-DD');

# Después
importar {formato} desde 'fecha-fns';
const formateado = formato (fecha, 'aaaa-MM-dd');
\`\`\`

**Ahorro:** 55 KB

#### 2. Utilice Lodash de forma selectiva

\`\`\`javascript
// Antes: importar la biblioteca completa (72 KB)
importar _ desde 'lodash';
const único = _.uniq(matriz);

// Después: Importa sólo lo que necesitas (5KB)
importar uniq desde 'lodash/uniq';
const único = uniq(matriz);

// O usar métodos nativos
const único = [...nuevo conjunto (matriz)];
\`\`\`

**Ahorro:** 67 KB

#### 3. Implementar la división del código

\`\`\`javascript
// ejemplo de Next.js
importar dinámica desde 'siguiente/dinámica';

// Carga diferida de componentes pesados
const Gráfico = dinámico(() => importar('./Gráfico'), {
  cargando: () => <div>Cargando gráfico...</div>,
  ssr: falso
});

const AdminPanel = dinámico(() => importar('./AdminPanel'), {
  cargando: () => <div>Cargando...</div>
});

// División de código basada en rutas (automática en Next.js)
// páginas/admin.js: solo se carga al visitar /admin
// páginas/dashboard.js: solo se carga al visitar /dashboard
\`\`\`

#### 4. Eliminar código inactivo

\`\`\`javascript
// Habilitar la vibración del árbol en webpack.config.js
módulo.exportaciones = {
  modo: 'producción',
  optimización: {
    Exportaciones usadas: verdadero,
    efectos secundarios: falso
  }
};

// En paquete.json
{
  "efectos secundarios": falso
}
\`\`\`

#### 5. Optimice los scripts de terceros

\`\`\`html
<!-- Antes: Carga inmediatamente -->
<script src="https://analytics.com/script.js"></script>

<!-- Después: Cargar después de la página interactiva -->
<guión>
  ventana.addEventListener('cargar', () => {
    script constante = document.createElement('script');
    script.src = 'https://analytics.com/script.js';
    script.async = verdadero;
    documento.body.appendChild(guión);
  });
</script>
\`\`\`

### Resultados

- **Paquete total:** 380 KB ✅ (reducido en 55 %)
- **Paquete principal:** 180KB ✅
- **Paquete de proveedores:** 80 KB ✅
- **Tiempo de carga (3G):** 3,1 s ✅ (mejorado en un 62 %)
```

### Ejemplo 3: estrategia de optimización de imágenes

### Problemas actuales
- 15 imágenes con un total de 12 MB
- Sin formatos modernos (WebP, AVIF)
- No hay imágenes responsivas
- Sin carga diferida

### Estrategia de optimización

#### 1. Convertir a formatos modernos

\`\`\`golpe
# Instalar herramientas de optimización de imágenes
npm instala Sharp

# Script de conversión (optimize-images.js)
const agudo = requerir('sostenido');
const fs = requerir('fs');
ruta constante = requerir('ruta');

función asíncrona optimizarImagen(inputPath, outputDir) {
  const nombre de archivo = ruta.nombrebase(inputPath, ruta.extname(inputPath));
  
  // Generar WebP
  aguardar fuerte (inputPath)
    .webp({ calidad: 80 })
    .toFile(path.join(outputDir, \`\${nombre de archivo}.webp\`));
  
  // Generar AVIF (mejor compresión)
  aguardar fuerte (inputPath)
    .avif({ calidad: 70 })
    .toFile(path.join(outputDir, \`\${nombre de archivo}.avif\`));
  
  // Generar respaldo JPEG optimizado
  aguardar fuerte (inputPath)
    .jpeg({ calidad: 80, progresivo: verdadero })
    .toFile(path.join(outputDir, \`\${filename}.jpg\`));
}

// Procesar todas las imágenes
imágenes constantes = fs.readdirSync('./images');
imágenes.forEach(img => {
  optimizarImagen(\`./images/\${img}\`, './images/optimizado');
});
\`\`\`

#### 2. Implementar imágenes responsivas

\`\`\`html
<!-- Imágenes responsivas con formatos modernos -->
<imagen>
  <!-- AVIF para navegadores que lo soporten (mejor compresión) -->
  <fuente 
    srcset="
      /images/hero-400.avif 400w,
      /images/hero-800.avif 800w,
      /images/hero-1200.avif 1200w
    "
    tipo="imagen/avif"
    tamaños="(ancho máximo: 768px) 100vw, 50vw"
  >
  
  <!-- WebP para navegadores que lo soporten -->
  <fuente 
    srcset="
      /images/hero-400.webp 400w,
      /images/hero-800.webp 800w,
      /images/hero-1200.webp 1200w
    "
    tipo="imagen/webp"
    tamaños="(ancho máximo: 768px) 100vw, 50vw"
  >
  
  <!-- Reserva JPEG -->
  <img 
    src="/images/hero-800.jpg"
    srcset="
      /images/hero-400.jpg 400w,
      /images/hero-800.jpg 800w,
      /images/hero-1200.jpg 1200w
    "
    tamaños="(ancho máximo: 768px) 100vw, 50vw"
    alt="Imagen principal"
    ancho="1200"
    altura="600"
    cargando="perezoso"
  >
</imagen>
\`\`\`

#### 3. Carga diferida

\`\`\`html
<!-- Carga diferida nativa -->
<img 
  src="/imagen.jpg" 
  alt="Descripción"
  cargando="perezoso"
  ancho="800"
  altura="600"
>

<!-- Carga ansiosa por imágenes en la mitad superior de la página -->
<img 
  src="/héroe.jpg" 
  alt="Héroe"
  cargando="ansioso"
  fetchpriority="alto"
>
\`\`\`

#### 4. Componente de imagen Next.js

\`\`\`javascript
importar imagen desde 'siguiente/imagen';

// Optimización automática
<Imagen
  src="/héroe.jpg"
  alt="Héroe"
  ancho={1200}
  altura={600}
  prioridad // Para imágenes en la mitad superior de la página
  calidad={80}
/>

// Carga diferida
<Imagen
  src="/producto.jpg"
  alt="Producto"
  ancho={400}
  altura={300}
  cargando="perezoso"
/>
\`\`\`

### Resultados

| Métrica | Antes | Después | Mejora |
|--------|--------|-------|-------------|
| Tamaño total de la imagen | 12 MB | 1,8 MB | Reducción del 85% |
| LCP | 4,5s | 1,6s | 64% más rápido |
| Carga de página (3G) | 18 años | 4,2s | 77% más rápido |
```

## Mejores prácticas

### ✅ Haz esto

- **Medir primero**: establezca siempre métricas de referencia antes de optimizar
- **Utilice Lighthouse**: ejecute auditorías periódicamente para realizar un seguimiento del progreso
- **Optimizar imágenes** - Utilice formatos modernos (WebP, AVIF) e imágenes responsivas
- **División de código**: divide paquetes grandes en trozos más pequeños
- **Carga diferida** - Aplazar recursos no críticos
- **Caché agresivo** - Establezca encabezados de caché adecuados para activos estáticos
- **Minimizar el trabajo del hilo principal** - Mantener la ejecución de JavaScript por debajo de 50 ms
- **Precargar recursos críticos** - Utilice `<link rel="preload">` para activos críticos
- **Utilice CDN**: proporcione activos estáticos desde CDN para una entrega más rápida
- **Monitorear usuarios reales** - Seguimiento de Core Web Vitals de usuarios reales

### ❌ No hagas esto

- **No optimice a ciegas**: primero mida y luego optimice
- **No ignorar dispositivos móviles** - Pruebe en dispositivos móviles reales y redes lentas
- **No bloquear el renderizado** - Evite CSS y JavaScript que bloqueen el renderizado
- **No cargar todo por adelantado** - Carga diferida de recursos no críticos
- **No olvides las dimensiones** - Siempre especifica el ancho/alto de la imagen
- **No utilice secuencias de comandos sincrónicas** - Utilice atributos asíncronos o diferidos
- **No ignore los scripts de terceros**: a menudo causan problemas de rendimiento
- **No omita la compresión**: siempre comprima y minimice los recursos

## Errores comunes

### Problema: optimizado para escritorio pero lento en dispositivos móviles
**Síntomas:** Buena puntuación de Lighthouse en computadoras de escritorio, pobre en dispositivos móviles
**Solución:**
- Prueba en dispositivos móviles reales
- Utilice la limitación móvil de Chrome DevTools
- Optimizar para redes 3G/4G
- Reducir el tiempo de ejecución de JavaScript
```golpecito
# Prueba con aceleración
faro https://yoursite.com --throttling.cpuSlowdownMultiplier=4
```

### Problema: paquete de JavaScript grande
**Síntomas:** Largo tiempo de interacción (TTI), FID alto
**Solución:**
- Analizar paquete con webpack-bundle-analyzer
- Eliminar dependencias no utilizadas
- Implementar división de código.
- Carga diferida de código no crítico
```golpecito
# Analizar paquete
npx webpack-bundle-analyzer dist/stats.json
```

### Problema: Imágenes que provocan cambios en el diseño
**Síntomas:** Puntuación CLS alta, salto de contenido
**Solución:**
- Especifique siempre ancho y alto
- Usar propiedad CSS de relación de aspecto
- Reserva de espacio con cargadores esqueleto.
```css
imagen {
  relación de aspecto: 16/9;
  ancho: 100%;
  altura: automático;
}
```

---

### Problema: tiempo de respuesta lento del servidor
**Síntomas:** TTFB alto (tiempo hasta el primer byte)
**Solución:**
- Implementar el almacenamiento en caché del lado del servidor.
- Utilice CDN para activos estáticos
- Optimizar consultas de bases de datos.
- Considere la generación de sitios estáticos (SSG)
```javascript
// Next.js: generación estática
exportar función asíncrona getStaticProps() {
  datos constantes = esperar fetchData();
  devolver {
    accesorios: {datos},
    revalidar: 60 // Regenerar cada 60 segundos
  };
}
```

## Lista de verificación de desempeño

### Imágenes
- [] Convertir a formatos modernos (WebP, AVIF)
- [] Implementar imágenes responsivas
- [] Agregar carga diferida
- [ ] Especificar dimensiones (ancho/alto)
- [] Comprimir imágenes (< 200 KB cada una)
- [] Utilice CDN para la entrega

### JavaScript
- [] Tamaño del paquete <200 KB (comprimido con g)
- [] Implementar división de código
- [] Carga diferida de código no crítico
- [] Eliminar dependencias no utilizadas
- [] Minimizar y comprimir
- [] Utilice async/difer para scripts

### CSS
- [] CSS crítico en línea
- [] Aplazar CSS no crítico
- [] Eliminar CSS no utilizado
- [] Minimizar archivos CSS
- [] Usar contención CSS

### Almacenamiento en caché
- [] Establecer encabezados de caché para activos estáticos
- [] Implementar trabajador de servicio
- [] Usar almacenamiento en caché CDN
- [] Respuestas de API de caché
- [] Versión de activos estáticos

### Elementos vitales web básicos
- [ ] LCP < 2,5 s
- [ ] FID < 100ms
- [ ] CLS < 0,1
- [ ] TTFB<600ms
- [ ] TTI < 3,8s

## Herramientas de rendimiento

### Herramientas de medición
- **Lighthouse** - Auditoría integral de desempeño
- **WebPageTest** - Análisis detallado de la cascada
- **Chrome DevTools** - Perfiles de rendimiento
- **PageSpeed Insights** - Métricas de usuario reales
- **Extensión Web Vitals** - Supervisar Core Web Vitals

### Herramientas de análisis
- **webpack-bundle-analyzer** - Visualiza la composición del paquete
- **source-map-explorer** - Analizar el tamaño del paquete
- **Bundlephobia** - Verifique el tamaño de los paquetes antes de instalar
- **ImageOptim** - Herramienta de compresión de imágenes

### Herramientas de monitoreo
- **Google Analytics** - Seguimiento de los elementos básicos de la web
- **Sentry** - Supervisión del rendimiento
- **New Relic** - Monitoreo del rendimiento de la aplicación
- **Datadog** - Monitoreo de usuarios reales

## Habilidades relacionadas

- `@react-best-practices` - Patrones de rendimiento de React
- `@frontend-dev-guidelines` - Estándares de desarrollo frontend
- `@systematic-debugging` - Problemas de rendimiento de depuración
- `@senior-architect` - Arquitectura para el rendimiento

## Recursos adicionales

- [Rendimiento de Web.dev](https://web.dev/rendimiento/)
- [Vitales web principales](https://web.dev/vitals/)
- [Documentación del faro] (https://developers.google.com/web/tools/lighthouse)
- [Guía de rendimiento de MDN](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Rendimiento de Next.js](https://nextjs.org/docs/advanced-features/measuring-performance)
- [Guía de optimización de imágenes](https://web.dev/fast/#optimize-your-images)

**Consejo profesional:** Concéntrese primero en Core Web Vitals (LCP, FID, CLS): ¡tienen el mayor impacto en la experiencia del usuario y en las clasificaciones SEO!