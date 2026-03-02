---
name: nextjs-best-practices
description: Next.js App Router principles. Server Components, data fetching, routing patterns.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

```
Does it need...?
│
├── useState, useEffect, event handlers
│   └── Client Component ('use client')
│
├── Direct data fetching, no interactivity
│   └── Server Component (default)
│
└── Both? 
    └── Split: Server parent + Client child
```

---

---

---

---

---

---

---

---

---

```
app/
├── (marketing)/     # Route group
│   └── page.tsx
├── (dashboard)/
│   ├── layout.tsx   # Dashboard layout
│   └── page.tsx
├── api/
│   └── [resource]/
│       └── route.ts
└── components/
    └── ui/
```

---

# Mejores prácticas de Next.js

> Principios para el desarrollo de Next.js App Router.

## 1. Componentes del servidor frente al cliente

### Árbol de decisión

### Por defecto

| Tipo | Uso |
|------|-----|
| **Servidor** | Obtención de datos, diseño, contenido estático |
| **Cliente** | Formularios, botones, UI interactiva |

## 2. Patrones de obtención de datos

### Estrategia de recuperación

| Patrón | Uso |
|---------|-----|
| **Predeterminado** | Estático (almacenado en caché durante la compilación) |
| **Revalidar** | ISR (actualización basada en tiempo) |
| **Sin tienda** | Dinámico (cada solicitud) |

### Flujo de datos

| Fuente | Patrón |
|--------|---------|
| Base de datos | Recuperación de componentes del servidor |
| API | buscar con almacenamiento en caché |
| Entrada de usuario | Estado del cliente + acción del servidor |

## 3. Principios de enrutamiento

### Convenciones de archivos

| Archivo | Propósito |
|------|---------|
| `página.tsx` | Interfaz de usuario de ruta |
| `diseño.tsx` | Diseño compartido |
| `cargando.tsx` | Estado de carga |
| `error.tsx` | Límite de error |
| `no-encontrado.tsx` | 404 página |

### Organización de ruta

| Patrón | Uso |
|---------|-----|
| Grupos de rutas `(nombre)` | Organizar sin URL |
| Rutas paralelas `@slot` | Varias páginas del mismo nivel |
| Interceptando `(.)` | Superposiciones modales |

## 4. Rutas API

### Controladores de ruta

| Método | Uso |
|--------|-----|
| OBTENER | Leer datos |
| PUBLICAR | Crear datos |
| PONER/PARCHE | Actualizar datos |
| BORRAR | Eliminar datos |

### Mejores prácticas

- Validar entrada con Zod
- Devolver códigos de estado adecuados
- Manejar los errores con gracia
- Utilice el tiempo de ejecución de Edge cuando sea posible

## 5. Principios de desempeño

### Optimización de imagen

- Usar el componente siguiente/imagen
- Establecer prioridad para el pliegue superior
- Proporcionar marcador de posición borroso
- Utilice tamaños receptivos

### Optimización de paquetes

- Importaciones dinámicas para componentes pesados.
- División de código basada en ruta (automática)
- Analizar con analizador de paquetes.

## 6. Metadatos

### Estático vs Dinámico

| Tipo | Uso |
|------|-----|
| Exportación estática | Metadatos fijos |
| generarMetadatos | Dinámico por ruta |

### Etiquetas esenciales

- título (50-60 caracteres)
- descripción (150-160 caracteres)
- Abrir imágenes de gráficos
- URL canónica

## 7. Estrategia de almacenamiento en caché

### Capas de caché

| Capa | Controlar |
|-------|---------|
| Solicitar | opciones de búsqueda |
| Datos | revalidar/etiquetas |
| Ruta completa | configuración de ruta |

### Revalidación

| Método | Uso |
|--------|-----|
| Basado en el tiempo | `revalidar: 60` |
| Bajo demanda | `revalidarRuta/Etiqueta` |
| Sin caché | `sin tienda` |

## 8. Acciones del servidor

### Casos de uso

- Envíos de formularios
- Mutaciones de datos
- Desencadenantes de revalidación

### Mejores prácticas

- Marcar con 'usar servidor'
- Validar todas las entradas
- Devolver respuestas escritas
- Manejar errores

## 9. Antipatrones

| ❌ No | ✅ Hacer |
|----------|-------|
| 'usar cliente' en todas partes | Servidor por defecto |
| Obtener componentes del cliente | Buscar en el servidor |
| Saltar estados de carga | Utilice cargando.tsx |
| Ignorar los límites de error | Utilice error.tsx |
| Grandes paquetes de clientes | Importaciones dinámicas |

## 10. Estructura del proyecto

> **Recuerde:** Los componentes del servidor son los predeterminados por una razón. Comience allí, agregue cliente solo cuando sea necesario.