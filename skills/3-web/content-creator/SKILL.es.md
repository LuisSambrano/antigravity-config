---
name: content-creator
description: Create SEO-optimized marketing content with consistent brand voice. Includes brand voice analyzer, SEO optimizer, content frameworks, and social media templates. Use when writing blog posts, creating social media content, analyzing brand voice, optimizing SEO, planning content calendars, or when user mentions content creation, brand voice, SEO optimization, social media marketing, or content strategy.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  domain: content-marketing
  updated: 2025-10-20
  python-tools: brand_voice_analyzer.py, seo_optimizer.py
  tech-stack: SEO, social-media-platforms
---

# Creador de contenido

Análisis de voz de marca de nivel profesional, optimización SEO y marcos de contenido específicos de la plataforma.

## Palabras clave
creación de contenido, publicaciones de blog, SEO, voz de marca, redes sociales, calendario de contenido, contenido de marketing, estrategia de contenido, marketing de contenido, consistencia de marca, optimización de contenido, marketing de redes sociales, planificación de contenido, redacción de blogs, marcos de contenido, pautas de marca, estrategia de redes sociales

## Inicio rápido

### Para el desarrollo de la voz de la marca
1. Ejecute `scripts/brand_voice_analyzer.py` en el contenido existente para establecer una línea de base.
2. Revise `references/brand_guidelines.md` para seleccionar atributos de voz
3. Aplique la voz elegida de manera consistente en todo el contenido.

### Para la creación de contenido de blog
1. Elija la plantilla de `references/content_frameworks.md`
2. Investiga palabras clave para el tema.
3. Escriba contenido siguiendo la estructura de la plantilla.
4. Ejecute `scripts/seo_optimizer.py [archivo] [palabra clave principal]` para optimizar
5. Aplicar recomendaciones antes de publicar.

### Para contenido de redes sociales
1. Revise las mejores prácticas de la plataforma en `references/social_media_optimization.md`
2. Utilice la plantilla adecuada de `references/content_frameworks.md`
3. Optimice según pautas específicas de la plataforma
4. Programe usando `assets/content_calendar_template.md`

## Flujos de trabajo principales

### Establecimiento de la voz de la marca (configuración por primera vez)

Al crear contenido para una nueva marca o cliente:

1. **Analizar contenido existente** (si está disponible)
   ```golpecito
   scripts de Python/brand_voice_analyzer.py contenido_existente.txt
   ```
   
2. **Definir atributos de voz**
   - Revisar los arquetipos de personalidad de marca en `references/brand_guidelines.md`
   - Seleccionar arquetipos primarios y secundarios.
   - Elija entre 3 y 5 atributos de tono
   - Documento en lineamientos de marca.

3. **Crear muestra de voz**
   - Escribe 3 piezas de muestra con la voz elegida.
   - Probar la consistencia usando el analizador.
   - Refinar en función de los resultados.

### Creación de publicaciones de blog optimizadas para SEO

1. **Investigación de palabras clave**
   - Identificar la palabra clave principal (volumen de búsqueda 500-5000/mes)
   - Encuentre de 3 a 5 palabras clave secundarias
   - Enumere entre 10 y 15 palabras clave LSI

2. **Estructura de contenido**
   - Utilice la plantilla de blog de `references/content_frameworks.md`
   - Incluir palabra clave en el título, primer párrafo y 2-3 H2
   - Intente utilizar entre 1500 y 2500 palabras para una cobertura completa

3. **Verificación de optimización**
   ```golpecito
   python scripts/seo_optimizer.py blog_post.md "palabra clave principal" "secundaria, palabras clave, lista"
   ```

4. **Aplica recomendaciones de SEO**
   - Ajustar la densidad de palabras clave al 1-3%
   - Garantizar una estructura de encabezado adecuada.
   - Agregar enlaces internos y externos
   - Optimizar la meta descripción

### Creación de contenido para redes sociales

1. **Selección de plataforma**
   - Identificar plataformas principales según la audiencia.
   - Revise las pautas específicas de la plataforma en `references/social_media_optimization.md`

2. **Adaptación de contenido**
   - Comience con una publicación de blog o un mensaje principal.
   - Utilice la matriz de reutilización de `references/content_frameworks.md`
   - Adaptarse para cada plataforma siguiendo plantillas.

3. **Lista de verificación de optimización**
   - Longitud adecuada a la plataforma
   - Tiempo de publicación óptimo
   - Dimensiones correctas de la imagen.
   - Hashtags específicos de la plataforma
   - Elementos de participación (encuestas, preguntas)

### Planificación del calendario de contenidos

1. **Planificación mensual**
   - Copiar `assets/content_calendar_template.md`
   - Establecer objetivos mensuales y KPI.
   - Identificar campañas/temas clave

2. **Distribución semanal**
   - Siga la proporción de pilares de contenido 40/25/25/10
   - Equilibrio de plataformas durante toda la semana.
   - Alinearse con tiempos de publicación óptimos

3. **Creación por lotes**
   - Crea todo el contenido semanal en una sola sesión.
   - Mantener una voz consistente en todas las piezas.
   - Preparar todos los recursos visuales juntos.

## Guiones clave

### marca_voice_analyzer.py
Analiza el contenido del texto en busca de características de voz, legibilidad y coherencia.

**Uso**: `python scripts/brand_voice_analyzer.py <archivo> [json|texto]`

**Devoluciones**:
- Perfil de voz (formalidad, tono, perspectiva)
- Puntuación de legibilidad
- Análisis de la estructura de la oración.
- Recomendaciones de mejora

### seo_optimizador.py
Analiza el contenido para la optimización SEO y proporciona recomendaciones prácticas.

**Uso**: `python scripts/seo_optimizer.py <archivo> [palabra clave_primaria] [palabras clave_secundarias]`

**Devoluciones**:
- Puntuación SEO (0-100)
- Análisis de densidad de palabras clave.
- Evaluación de estructuras
- Sugerencias de metaetiquetas
- Recomendaciones de optimización específicas.

## Guías de referencia

### Cuándo utilizar cada referencia

```bash
# Analyze brand voice
python scripts/brand_voice_analyzer.py content.txt

**referencias/brand_guidelines.md**
- Configuración de una nueva voz de marca.
- Garantizar la coherencia en todo el contenido.
- Formación de nuevos miembros del equipo.
- Resolver preguntas de voz/tono.

**referencias/content_frameworks.md**
- Iniciar cualquier contenido nuevo.
- Estructuración de diferentes tipos de contenidos.
- Creación de plantillas de contenido.
- Planificación de la reutilización de contenidos.

**referencias/social_media_optimization.md**
- Optimización específica de la plataforma
- Desarrollo de estrategia de hashtags.
- Comprender los factores del algoritmo.
- Configuración del seguimiento analítico

## Mejores prácticas

### Proceso de creación de contenido
1. Comience siempre con la necesidad o el punto débil de la audiencia
2. Investiga antes de escribir
3. Crea un esquema usando plantillas.
4. Escribe el primer borrador sin editar.
5. Optimizar para SEO
6. Edite para darle voz a la marca
7. Revisar y verificar hechos
8. Optimizar para la plataforma
9. Programe estratégicamente

### Indicadores de calidad
- Puntuación SEO superior a 75/100
- Legibilidad apropiada para la audiencia
- Voz de marca consistente en todo
- Propuesta de valor clara
- Conclusiones procesables
- Formato visual adecuado
- Plataforma optimizada

### Errores comunes que se deben evitar
- Escribir antes de investigar palabras clave.
- Ignorar los requisitos específicos de la plataforma.
- Voz de marca inconsistente
- Optimización excesiva para SEO (relleno de palabras clave)
- Faltan CTA claras
- Publicar sin revisión
- Ignorar los comentarios analíticos

## Métricas de rendimiento

Realice un seguimiento de estos KPI para lograr el éxito del contenido:

### Métricas de contenido
- Crecimiento orgánico del tráfico
- Tiempo promedio en la página
- Tasa de rebote
- acciones sociales
- Vínculos de retroceso obtenidos

### Métricas de participación
- Comentarios y discusiones.
- Tasas de clics de correo electrónico
- Tasa de participación en las redes sociales
- Descargas de contenido
- Envíos de formularios

### Métricas comerciales
- Clientes potenciales generados
- Tasa de conversión
- Costo de adquisición de clientes
- Atribución de ingresos
- ROI por pieza de contenido

## Puntos de integración

Esta habilidad funciona mejor con:
- Plataformas de análisis (Google Analytics, insights de redes sociales)
- Herramientas SEO (para investigación de palabras clave)
- Herramientas de diseño (para contenido visual)
- Plataformas de programación (para distribución de contenidos)
- Sistemas de marketing por correo electrónico (para contenido de newsletters)

## Comandos rápidos

# Optimizar para SEO
python scripts/seo_optimizer.py artículo.md "palabra clave principal"

# Verifique el contenido con las pautas de la marca
grep -f referencias/brand_guidelines.md contenido.txt

# Crear calendario mensual
cp activos/content_calendar_template.md this_month_calendar.md
```