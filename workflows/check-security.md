---
description: Auditoría profunda de seguridad, vulnerabilidades y fugas de datos en proyectos web
---

# /check-security - Auditoría Exhaustiva de Seguridad

Usa este workflow regularmente para evaluar y blindar la postura de seguridad de un proyecto web, aplicación o infraestructura, identificando posibles brechas y fugas de datos antes de llegar a producción.

## Lo que YO hago automáticamente

1. **Escaneo de Entorno y Secretos**
   - Verifico si hay archivos `.env` expuestos o en staging de Git.
   - Busco credenciales, tokens, y claves API hardcodeadas en el código fuente (especialmente en el cliente).
   - Valido la convención correcta de variables de entorno (ej. `NEXT_PUBLIC_` solo cuando es estrictamente público).

2. **Auditoría de Base de Datos y Backend (Ej. Supabase/Postgres)**
   - Corro el Asesor de Seguridad (MCP Linter) para detectar vulnerabilidades en la BBDD.
   - Valido que **todas** las tablas sensibles tengan _Row Level Security_ (RLS) activo y con políticas explícitas bien definidas.
   - Reviso que funciones almacenadas y "Security Definers" posean un `search_path` blindado para evitar inyecciones de esquema.
   - Compruebo privilegios excesivos en vistas y tablas hacia roles públicos (`anon`).

3. **Autenticación, Sesiones y Middleware**
   - Reviso la ejecución de middlewares (estilo Zero-Trust) para asegurar que las rutas privadas estén blindadas.
   - Verifico el correcto saneamiento y destrucción de cookies/sesiones (incluyendo mitigación de "sesiones zombies").
   - Evalúo flujos OAuth y redirecciones contra vulnerabilidades y secuestros de sesión.

4. **Configuraciones HTTP y Red del Framework**
   - Examino cabeceras críticas (security headers) en tu configuración de framework (ej. `next.config.ts` o `next.config.js`): `Content-Security-Policy (CSP)`, `Strict-Transport-Security (HSTS)`, `X-Frame-Options`, `X-Content-Type-Options`.
   - Audito la configuración y origen CORS para prevenir consumo de API desde dominios riesgosos o no autorizados.

5. **Sanitización y Mitigación Avanzada (Checklist Exhaustivo)**
   - Examino el código contra las siguientes vulnerabilidades estructuradas:
     - **Inyecciones**: SQL Injection (SQLi), NoSQL Injection, OS Command Injection, LDAP Injection, XML External Entity (XXE) Injection, Server-Side Template Injection (SSTI).
     - **Vulnerabilidades de Cliente y Peticiones**: Cross-Site Scripting (XSS) (Reflected, Stored, DOM-based), Server-Side Request Forgery (SSRF), Cross-Site Request Forgery (CSRF), Unvalidated Redirects and Forwards, Clickjacking (UI Redressing).
     - **Control de Acceso y Autorización**: Insecure Direct Object Reference (IDOR) / Broken Access Control, Missing Function-Level Access Control, Directory Traversal / Path Traversal, Local File Inclusion (LFI), Remote File Inclusion (RFI), Parameter Tampering / Mass Assignment.
     - **Autenticación y Sesiones**: Default Passwords / Weak Passwords, Credential Stuffing / Brute Force, Session Fixation, Session Hijacking, Insufficient Session Expiration, JSON Web Token (JWT) Vulnerabilities (None Algorithm, Signature bypass).
     - **Datos, Lógica e Integridad**: Sensitive Data Exposure, Insecure Deserialization, Business Logic Flaws, Race Conditions (Time-of-check to time-of-use - TOCTOU), Denial of Service (DoS) / Buffer Overflows.
     - **Configuración y Operaciones**: Security Misconfiguration, Missing or Weak HTTP Security Headers (CORS, CSP, HSTS), Insecure Cryptographic Storage / Weak Ciphers, Using Components with Known Vulnerabilities, Open Cloud Storage Buckets (S3, GCP), Insufficient Logging & Monitoring.
     - **Ejecución de Código**: Remote Code Execution (RCE).
   - Identifico dependencias y paquetes de terceros obsoletos ejecutando auditorías de ecosistema (como `npm audit`).

## Generación del Reporte (Veredicto)

Al terminar el escaneo profundo, presentaré los resultados estilo Semáforo con _Action Items_:

- ❌ **CRÍTICO**: Bloqueantes urgentes de despliegue (ej. contraseñas quemadas en código libre, RLS apagado en datos personales). Requiero aplicar parches o purgas de inmediato.
- ⚠️ **ADVERTENCIA**: Riesgos moderados (ej. falta estandarizar CSP, dependencias secundarias obsoletas).
- 📝 **MEJORA**: Oportunidades leves y optimizaciones recomendadas para arquitectura de redes.
- ✅ **SEGURO**: Un balance de lo que la aplicación ya está protegiendo satisfactoriamente.

## Cuándo usarlo

- Pre-lanzamiento hacia producción formal (antes de comprar un dominio definitivo).
- Tras añadir nuevas arquitecturas o sistemas al stack principal (ej. incorporar pasarelas de pago o Storage de archivos).
- Trimestralmente como un testeo de fortaleza (_Penta/Health-Check_).

## Ejemplo de Uso

Tú: `/check-security`
(Opcional enfoque específico) Tú: `/check-security enfócate en el RLS de la base de datos Supabase`
(Opcional enfoque local) Tú: `/check-security revisa si hay variables .env hardcodeadas en Componentes UI`

Yo: _(Asumiré mi rol de experto, correré bash commands, grep, invocaré MCP si aplica y redactaré tu informe ejecutivo de fallos y parches)_.

## TÚ NO necesitas

- ❌ Interpretar las complejas políticas tipo Content-Security-Policy o Row Level Security en SQL.
- ❌ Brindarme los secretos de tus contraseñas base.
- ❌ Decirme exactamente cómo buscar fallos, comandos del linter, etc.
- ❌ Conocer al detalle el OWASP Top 10.

Solo solicita el workflow; yo actuaré como tu Arquitecto de Seguridad y documentaré o resolveré tu plataforma.
