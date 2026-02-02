# Gobernanza del Repositorio: Google Antigravity

Este documento define las reglas de organización y contribución para el ecosistema de Antigravity.

## 🏛️ Filosofía de Organización basado en Dominios

A diferencia de los repositorios tradicionales que se agrupan por tipo de archivo, Antigravity utiliza una estructura **orientada a dominios funcionales**.

### Reglas de Oro:

1.  **Prioridad del Dominio**: Una funcionalidad debe vivir en su carpeta de dominio (ej. `skills/security/`) sin importar si contiene Python, Bash o Markdown.
2.  **No Movilidad de Legado**: Para preservar la estabilidad de los agentes y sus rutas de ejecución (prompts), no se deben renombrar ni mover carpetas existentes sin una auditoría de impacto masiva.
3.  **Indización Requerida**: Toda nueva capacidad añadida a `skills/` debe ser catalogada en el `README_MASTER.md`.

## 📂 Estructura de Carpetas

| Carpeta   | Propósito                                        | Responsable            |
| :-------- | :----------------------------------------------- | :--------------------- |
| `assets/` | Recursos estáticos (imágenes, logos, diagramas)  | UI/UX Pro Max          |
| `docs/`   | Documentación estratégica y técnica (en Español) | Tech Lead              |
| `rules/`  | Directivas de comportamiento para Agentes        | Arquitecto             |
| `skills/` | Capacidades modulares (Skills)                   | Agente / Desarrollador |
| `tools/`  | Herramientas de soporte y CLI                    | Automatizador          |

## 🛠️ Procedimiento de Actualización

1.  Añadir la nueva funcionalidad en la subcarpeta de dominio correspondiente.
2.  Ejecutar el script de mantenimiento `python3 scripts/maintenance/generate_index.py` para actualizar el mapa visual.
3.  Documentar cualquier cambio arquitectónico en `docs/architecture/`.

## 🌐 Idiomas

- **Documentos de Gestión (Master Index, Gobernanza)**: Español (para la toma de decisiones del Tech Lead).
- **Código y Lógica Interna**: Inglés (estándar de la industria).
- **Instrucciones Expertas (SKILL.md)**: Inglés (optimizado para el razonamiento de los LLMs).
