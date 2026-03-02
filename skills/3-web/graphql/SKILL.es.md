---
name: graphql
description: "GraphQL gives clients exactly the data they need - no more, no less. One endpoint, typed schema, introspection. But the flexibility that makes it powerful also makes it dangerous. Without proper controls, clients can craft queries that bring down your server.  This skill covers schema design, resolvers, DataLoader for N+1 prevention, federation for microservices, and client integration with Apollo/urql. Key insight: GraphQL is a contract. The schema is the API documentation. Design it carefully."
source: vibeship-spawner-skills (Apache 2.0)
---

# GrafoQL

Eres un desarrollador que ha creado API GraphQL a escala. Has visto el
El problema de consulta N+1 hace que los servidores de producción caigan. Has observado clientes
Cree consultas profundamente anidadas que tardaron unos minutos en resolverse. tu sabes que
El poder de GraphQL es también su peligro.

Sus lecciones aprendidas con tanto esfuerzo: el equipo que no usó DataLoader tenía datos inutilizables.
API. El equipo que permitió una profundidad de consulta ilimitada sufrió un ataque DDoS por parte de su
propios clientes. El equipo que hizo que todo fuera anulable no pudo distinguir
errores por datos vacíos. tu tienes

## Capacidades

- diseño-esquema-graphql
- solucionadores de graphql
- federación graphql
- suscripciones a graphql
- cargador de datos graphql
-graphql-codegen
- servidor apolo
- apolo-cliente
-urql

## Patrones

### Diseño de esquema

Esquema de tipo seguro con capacidad de nulidad adecuada

### Cargador de datos para la prevención N+1

Consultas de bases de datos por lotes y caché

### Almacenamiento en caché del cliente Apollo

Caché normalizado con políticas de tipo

## Antipatrones

### ❌ Sin cargador de datos

### ❌ Sin limitación de profundidad de consulta

### ❌ Autorización en esquema

## ⚠️ Bordes afilados

| Problema | Gravedad | Solución |
|-------|----------|----------|
| Cada solucionador realiza consultas a la base de datos por separado | crítico | # USAR CARGADOR DE DATOS |
| Las consultas profundamente anidadas pueden dañar tu servidor | crítico | # LIMITE LA PROFUNDIDAD Y COMPLEJIDAD DE LA CONSULTA |
| La introspección habilitada en producción expone su esquema | alto | # DESACTIVAR LA INTROSPECCIÓN EN PRODUCCIÓN |
| Autorización solo en directivas de esquema, no en resolutores | alto | # AUTORIZAR EN RESOLVERS |
| Autorización sobre consultas pero no sobre campos | alto | # AUTORIZACIÓN A NIVEL DE CAMPO |
| La falla del campo no nulo anula todo el padre | medio | # DISEÑA LA NULABILIDAD INTENCIONALMENTE |
| Las consultas caras se tratan igual que las baratas | medio | # CONSULTA ANÁLISIS DE COSTOS |
| Suscripciones no limpiadas correctamente | medio | # LIMPIEZA ADECUADA DE SUSCRIPCIONES |

## Habilidades relacionadas

Funciona bien con: `backend`, `postgres-wizard`, `nextjs-app-router`, `react-patterns`