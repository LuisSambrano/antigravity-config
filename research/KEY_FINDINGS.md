# 🧠 KEY FINDINGS - Antigravity Config

> _Fundamentos, principios y estándares que gobiernan el ecosistema Antigravity._

Este documento consolida las decisiones arquitectónicas y filosóficas maestras que deben replicarse en todos los proyectos del usuario.

---

## Hallazgo #1: Protocolo Zero (La Constitución)

**Descubrimiento**: La velocidad sin control genera deuda técnica impagable. Necesidad de reglas inmutables.

**Decisión**: Establecer **PROTOCOL ZERO** como la ley suprema:

1. **Playground = Verdad**: GitHub es solo un espejo. Edición local obligatoria.
2. **Calidad > Velocidad**: Tests, Lint y Build deben pasar siempre.
3. **Docs as Code**: README Trilingüe Senior (EN/ES/PT) es obligatorio.
4. **Autonomía Transparente**: Agentes libres pero responsables de documentar.
5. **Kaizen**: Boy Scout Rule aplicada a cada commit.

📄 Fuente: [PROTOCOL_ZERO.md](../rules/PROTOCOL_ZERO.md)

---

## Hallazgo #2: Separación Lingüística Estricta

**Problema**: El "Spanglish" en código causa confusión y reduce la calidad profesional.

**Standard**:

- **CÓDIGO (Inglés)**: Variables, funciones, commits, PRs, términos técnicos.
- **COMUNICACIÓN (Español)**: Explicaciones, razonamientos, planes, research.
- **DOCS PÚBLICOS (Trilingüe)**: EN, ES, PT para alcance global.

**Beneficio**: Código estándar internacional + Comunicación fluida en idioma nativo.

📄 Fuente: [GEMINI.md](../GEMINI.md) (Regla Crítica)

---

## Hallazgo #3: Metodología Research-First

**Problema**: Proyectos sin documentación de decisiones se vuelven inmantibles.

**Solución**: Estandarizar la carpeta `research/` en todos los repos:

- `KEY_FINDINGS.md`: Destilado de decisiones (Contexto para IAs).
- `prompts/`: Módulos de investigación.
- `data/`: Evidencia cruda.
- `proposals/`: Exploración de opciones.

**Impacto**: Cualquier IA futura puede leer `KEY_FINDINGS.md` y entender el "alma" del proyecto instantáneamente.

📄 Fuente: [implementation_plan.md](../../brain/cce57f6c-25e8-461d-acfc-f9dc3bdee58a/implementation_plan.md)

---

## Hallazgo #4: Stack "One Man Army"

**Contexto**: Un solo desarrollador compitiendo con equipos grandes.

**Estrategia**: Apalancamiento máximo con IA y herramientas Best-in-Class.

- **Frontend**: Next.js 16 + Tailwind v4 + Shadcn/UI (Velocidad visual).
- **Backend**: Supabase (Postgres + Auth + Edge Functions).
- **IA**: Gemini 3 Pro (Thinking) + Claude Sonnet 4.5 (Coding).

📄 Fuente: [ARCHITECTURE_STANDARDS.md](../rules/ARCHITECTURE_STANDARDS.md)

---

## Hallazgo #5: Valores No Negociables

1. **Seguridad First**: RLS en base de datos es mandatorio.
2. **Accesibilidad**: WCAG 2.1 AA mínimo.
3. **Performance**: Core Web Vitals en verde. No shipping de código lento.

📄 Fuente: [PROTOCOL_ZERO.md](../rules/PROTOCOL_ZERO.md)

---

## 📚 Mapa de Reglas Maestras

| Archivo                                                         | Nivel | Propósito                         |
| --------------------------------------------------------------- | ----- | --------------------------------- |
| [PROTOCOL_ZERO.md](../rules/PROTOCOL_ZERO.md)                   | 0     | Principios inmutables y filosofía |
| [ARCHITECTURE_STANDARDS.md](../rules/ARCHITECTURE_STANDARDS.md) | 1     | Reglas de estructura y patrones   |
| [CODE_STANDARDS.md](../rules/CODE_STANDARDS.md)                 | 2     | Estilo de código, naming, TS      |
| [QUALITY_GATES.md](../rules/QUALITY_GATES.md)                   | 3     | Checks pre-commit y pre-delivery  |

---

_Última actualización: 2026-02-05_
_Generado por Antigravity Research-First Protocol_
