# Gobernanza del Repositorio: Google Antigravity

**Versión:** 1.0.0
**Propietario:** Tech Lead / Arquitecto de Soluciones

Este documento establece las normativas obligatorias para la convivencia técnica y organizativa dentro del ecosistema Antigravity.

---

## 🏛️ 1. Filosofía de Abstracción por Dominios

El repositorio utiliza una **Capa de Abstracción Lógica**. No agrupamos por lenguaje de programación ni por tipo de archivo, sino por **Dominio de Conocimiento**.

- **Sin Movimientos Físicos**: Para proteger las rutas locales y dependencias de otros agentes, está prohibido mover carpetas existentes sin un proceso de auditoría y deprecación formal.
- **Agrupación Semántica**: Las nuevas capacidades deben ser situadas en el "Dominio" que mejor represente su función de cara al negocio (ej: `skills/security/` para auditorías).

## 🌍 2. Capa de Idiomas y Comunicación

Para garantizar tanto el entendimiento humano como el rendimiento de la IA, se establece:

- **Nivel Estratégico (Humano)**: Toda la documentación de gobernanza, arquitectura y el índice maestro (`README_MASTER.md`, `REPOSITORY_GOVERNANCE.md`) debe estar en **ESPAÑOL**.
- **Nivel Técnico (IA)**: El código fuente, los nombres de archivos técnicos, los comentarios de código y, crucialmente, las instrucciones de las skills (`SKILL.md`), deben mantenerse en **INGLÉS**. Esto optimiza el razonamiento semántico de los modelos de lenguaje.

## 🛡️ 3. Reglas de Contribución y Deprecación

- **No-Destrucción**: Ninguna carpeta puede ser eliminada sin un ticket de deprecación que demuestre que no hay agentes externos ni flujos de trabajo apuntando a esa ruta.
- **Indización Obligatoria**: Cualquier cambio en el catálogo de habilidades debe ser seguido por la ejecución del script de mantenimiento para asegurar que el Product Owner siempre vea el estado real del sistema.
- **Atomicidad**: Los commits deben ser atómicos y seguir el estándar de Conventional Commits (ej: `feat:`, `fix:`, `docs:`).

## 🛠️ 4. Automatización de Mantenimiento

El archivo `README_MASTER.md` es un documento vivo. Su sección de "Mapa de Dominios" se regenera automáticamente mediante:

```bash
python3 scripts/maintenance/generate_index.py
```

Cualquier edición manual en las secciones generadas será sobrescrita en la siguiente ejecución.
