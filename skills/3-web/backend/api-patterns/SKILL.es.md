---
name: api-patterns
description: API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

---

---

# Patrones API

> Principios de diseño de API y toma de decisiones para 2025.
> **Aprenda a PENSAR, no a copiar patrones fijos.**

## 🎯 Regla de lectura selectiva

**¡Lea SOLO archivos relevantes para la solicitud!** Consulte el mapa de contenido y encuentre lo que necesita.

## 📑 Mapa de contenido

| Archivo | Descripción | Cuándo leer |
|------|-------------|--------------|
| `estilo-api.md` | Árbol de decisión REST vs GraphQL vs tRPC | Elegir el tipo de API |
| `rest.md` | Denominación de recursos, métodos HTTP, códigos de estado | Diseño de API REST |
| `respuesta.md` | Patrón de sobre, formato de error, paginación | Estructura de respuesta |
| `graphql.md` | Diseño de esquemas, cuándo usarlo, seguridad | Considerando GraphQL |
| `trpc.md` | TypeScript monorepo, seguridad de tipos | Proyectos TS fullstack |
| `versionado.md` | Versiones de URI/encabezado/consulta | Planificación de la evolución de API |
| `auth.md` | JWT, OAuth, clave de acceso, claves API | Selección de patrón de autenticación |
| `limitación de velocidad.md` | Cubo para fichas, ventana corredera | Protección API |
| `documentación.md` | Mejores prácticas de OpenAPI/Swagger | Documentación |
| `pruebas-de-seguridad.md` | OWASP API Top 10, pruebas de autenticación/authz | Auditorías de seguridad |

## 🔗 Habilidades relacionadas

| Necesidad | Habilidad |
|------|-------|
| Implementación de API | `@[habilidades/desarrollo-backend]` |
| Estructura de datos | `@[habilidades/diseño-de-base de datos]` |
| Detalles de seguridad | `@[habilidades/refuerzo de seguridad]` |

## ✅ Lista de verificación de decisiones

Antes de diseñar una API:

- [] **¿Preguntó al usuario sobre los consumidores de API?**
- [] **¿Estilo de API elegido para ESTE contexto?** (REST/GraphQL/tRPC)
- [] **¿Formato de respuesta consistente definido?**
- [] **¿Estrategia de versiones planificada?**
- [] **¿Necesidades de autenticación consideradas?**
- [] **¿Límite de tasa planificada?**
- [ ] **¿Enfoque de documentación definido?**

## ❌ Anti-Patrones

**NO HACER:**
- Por defecto REST para todo
- Usar verbos en puntos finales REST (/getUsers)
- Devolver formatos de respuesta inconsistentes
- Exponer errores internos a los clientes.
- Limitación de velocidad de salto

**HACER:**
- Elija el estilo de API según el contexto
- Preguntar por los requisitos del cliente.
- Documentar a fondo
- Utilice códigos de estado apropiados

## guión

| Guión | Propósito | Comando |
|--------|---------|---------|
| `scripts/api_validator.py` | Validación de puntos finales API | `python scripts/api_validator.py <ruta_proyecto>` |