---
name: database-design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

# Diseño de base de datos

> **Aprenda a PENSAR, no a copiar patrones SQL.**

## 🎯 Regla de lectura selectiva

**¡Lea SOLO archivos relevantes para la solicitud!** Consulte el mapa de contenido y encuentre lo que necesita.

| Archivo | Descripción | Cuándo leer |
|------|-------------|--------------|
| `selección-base-de-datos.md` | PostgreSQL vs Neón vs Turso vs SQLite | Elegir base de datos |
| `orm-selección.md` | Llovizna vs Prisma vs Kysely | Elegir ORM |
| `esquema-diseño.md` | Normalización, PK, relaciones | Diseño de esquema |
| `indexación.md` | Tipos de índices, índices compuestos | Ajuste de rendimiento |
| `optimización.md` | N+1, EXPLICAR ANALIZAR | Optimización de consultas |
| `migraciones.md` | Migraciones seguras, bases de datos sin servidor | Cambios de esquema |

## ⚠️ Principio básico

- PREGUNTE al usuario por las preferencias de la base de datos cuando no esté claro
- Elija la base de datos/ORM según el CONTEXTO
- No utilice PostgreSQL por defecto para todo

## Lista de verificación de decisiones

Antes de diseñar el esquema:

- [] ¿Preguntó al usuario sobre la preferencia de la base de datos?
- [ ] ¿Base de datos elegida para ESTE contexto?
- [] ¿Entorno de implementación considerado?
- [] ¿Estrategia de índice planificada?
- [ ] ¿Tipos de relación definidos?

## Antipatrones

❌ PostgreSQL predeterminado para aplicaciones simples (SQLite puede ser suficiente)
❌ Saltar indexación
❌ Utilice SELECT * en producción
❌ Almacene JSON cuando los datos estructurados sean mejores
❌ Ignorar consultas N+1