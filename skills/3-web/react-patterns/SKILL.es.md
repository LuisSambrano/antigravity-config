---
name: react-patterns
description: Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

---

---

---

---

---

---

---

---

# Patrones de reacción

> Principios para crear aplicaciones React listas para producción.

## 1. Principios de diseño de componentes

### Tipos de componentes

| Tipo | Uso | Estado |
|------|-----|-------|
| **Servidor** | Obtención de datos, estática | Ninguno |
| **Cliente** | Interactividad | usoEstado, efectos |
| **Presentación** | Visualización de la interfaz de usuario | Sólo accesorios |
| **Contenedor** | Lógica/estado | Estado pesado |

### Reglas de diseño

- Una responsabilidad por componente
- Props abajo, eventos arriba
- Composición sobre herencia
- Prefiere componentes pequeños y enfocados

## 2. Patrones de gancho

### Cuándo extraer los ganchos

| Patrón | Extraer cuando |
|---------|-------------|
| **usarAlmacenamiento Local** | Se necesita la misma lógica de almacenamiento |
| **usarDebounce** | Múltiples valores rebotados |
| **usarFetch** | Patrones de búsqueda repetidos |
| **usarformulario** | Estado de forma compleja |

### Reglas de gancho

- Ganchos sólo en el nivel superior
- Mismo orden en cada render.
- Los ganchos personalizados comienzan con "usar"
- Limpiar efectos al desmontar

## 3. Selección de gestión estatal

| Complejidad | Solución |
|------------|----------|
| Sencillo | useState, useReducer |
| Local compartido | Contexto |
| Estado del servidor | Consulta de reacción, SWR |
| Global complejo | Zustand, kit de herramientas de Redux |

### Colocación estatal

| Alcance | Dónde |
|-------|-------|
| Un solo componente | utilizarEstado |
| Padre-hijo | Levante el estado |
| Subárbol | Contexto |
| En toda la aplicación | Tienda mundial |

## 4. Reaccionar 19 patrones

### Nuevos ganchos

| Gancho | Propósito |
|------|---------|
| **useActionState** | Estado de envío del formulario |
| **usoOptimista** | Actualizaciones optimistas de la interfaz de usuario |
| **uso** | Leer recursos en render |

### Beneficios del compilador

- Memorización automática
- Menos uso manualMemo/useCallback
- Centrarse en componentes puros

## 5. Patrones de composición

### Componentes compuestos

- El padre proporciona contexto
- Los niños consumen contexto.
- Composición flexible basada en tragamonedas
- Ejemplo: Tablaturas, Acordeón, Menú desplegable

### Representar accesorios frente a ganchos

| Caso de uso | Prefiero |
|----------|--------|
| Lógica reutilizable | Gancho personalizado |
| Flexibilidad de renderizado | Accesorios de renderizado |
| Transversales | Componente de orden superior |

## 6. Principios de desempeño

### Cuándo optimizar

| Señal | Acción |
|--------|--------|
| Renderizados lentos | Perfil primero |
| Listas grandes | Virtualizar |
| Cálculo caro | utilizarNota |
| Devoluciones de llamada estables | utilizarDevolución de llamada |

### Orden de optimización

1. Comprueba si realmente es lento
2. Perfil con DevTools
3. Identificar el cuello de botella
4. Aplique una solución específica

## 7. Manejo de errores

### Error en el uso de límites

| Alcance | Colocación |
|-------|-----------|
| En toda la aplicación | Nivel raíz |
| Característica | Nivel de ruta/función |
| Componente | En torno al componente riesgoso |

### Recuperación de errores

- Mostrar interfaz de usuario alternativa
- Error de registro
- Ofrecer opción de reintento
- Preservar los datos del usuario

## 8. Patrones de mecanografiado

### Escritura de accesorios

| Patrón | Uso |
|---------|-----|
| Interfaz | Accesorios de componentes |
| Tipo | Sindicatos complejos |
| Genérico | Componentes reutilizables |

### Tipos comunes

| Necesidad | Tipo |
|------|------|
| Niños | ReaccionarNodo |
| Controlador de eventos | Controlador de eventos del ratón |
| Árbitro | ObjetoRef<Elemento> |

## 9. Principios de prueba

| Nivel | Enfoque |
|-------|-------|
| Unidad | Funciones puras, ganchos |
| Integración | Comportamiento de los componentes |
| E2E | Flujos de usuarios |

### Prioridades de prueba

- Comportamiento visible para el usuario
- Casos extremos
- Estados de error
- Accesibilidad

## 10. Antipatrones

| ❌ No | ✅ Hacer |
|----------|-------|
| Perforación profunda de puntal | Usar contexto |
| Componentes gigantes | Dividir más pequeño |
| useEfecto para todo | Componentes del servidor |
| Optimización prematura | Perfil primero |
| Índice como clave | ID única estable |

> **Recuerda:** React se trata de composición. Construya en pequeño, combine cuidadosamente.