---
description: Comprehensive security audit, vulnerabilities and data leaks prevention
---

# /check-security - Comprehensive Security Audit

Use this workflow to evaluate the security posture of a web project, application, or infrastructure, identifying potential breaches and data leaks before reaching production.

## Automated Execution Steps

1. **Environment & Secrets Scanning**
   - Check for exposed `.env` files or files in Git staging.
   - Scan for hardcoded credentials, tokens, and API keys in the source code (especially on the client).
   - Validate correct environment variable conventions (e.g., `NEXT_PUBLIC_` only when strictly public).

2. **Database and Backend Auditing (e.g., Supabase/Postgres)**
   - Run the Security Advisor (MCP Linter) to detect DB vulnerabilities.
   - Validate that **all** sensitive tables have `Row Level Security (RLS)` active with explicitly defined policies.
   - Check that stored procedures and "Security Definers" possess a secured `search_path` to prevent schema injections.
   - Verify excessive privileges in views and tables towards public roles (`anon`).

3. **Authentication, Sessions & Middleware**
   - Review middleware execution (Zero-Trust style) to ensure private routes are protected.
   - Verify correct sanitation and destruction of cookies/sessions (including "zombie sessions" mitigation).
   - Evaluate OAuth flows and redirects against vulnerabilities and session hijacking.

4. **Framework HTTP & Network Configurations**
   - Examine critical security headers in the framework configuration (e.g., `next.config.ts` or `next.config.js`): `Content-Security-Policy (CSP)`, `Strict-Transport-Security (HSTS)`, `X-Frame-Options`, `X-Content-Type-Options`.
   - Audit CORS configuration and origin to prevent API consumption from risky or unauthorized domains.

5. **Advanced Sanitization and Mitigation (Exhaustive Checklist)**
   - Examine the code against the following structured vulnerabilities:
     - **Injections**: SQL Injection (SQLi), NoSQL Injection, OS Command Injection, LDAP Injection, XML External Entity (XXE) Injection, Server-Side Template Injection (SSTI).
     - **Client & Request Vulnerabilities**: Cross-Site Scripting (XSS) (Reflected, Stored, DOM-based), Server-Side Request Forgery (SSRF), Cross-Site Request Forgery (CSRF), Unvalidated Redirects and Forwards, Clickjacking (UI Redressing).
     - **Access Control & Authorization**: Insecure Direct Object Reference (IDOR) / Broken Access Control, Missing Function-Level Access Control, Directory Traversal / Path Traversal, Local File Inclusion (LFI), Remote File Inclusion (RFI), Parameter Tampering / Mass Assignment.
     - **Authentication & Sessions**: Default Passwords / Weak Passwords, Credential Stuffing / Brute Force, Session Fixation, Session Hijacking, Insufficient Session Expiration, JSON Web Token (JWT) Vulnerabilities (None Algorithm, Signature bypass).
     - **Data, Logic & Integrity**: Sensitive Data Exposure, Insecure Deserialization, Business Logic Flaws, Race Conditions (Time-of-check to time-of-use - TOCTOU), Denial of Service (DoS) / Buffer Overflows.
     - **Configuration & Operations**: Security Misconfiguration, Missing or Weak HTTP Security Headers (CORS, CSP, HSTS), Insecure Cryptographic Storage / Weak Ciphers, Using Components with Known Vulnerabilities, Open Cloud Storage Buckets (S3, GCP), Insufficient Logging & Monitoring.
     - **Code Execution**: Remote Code Execution (RCE).
   - Identify obsolete third-party dependencies and packages by running ecosystem audits (like `npm audit`).

## Report Generation (Verdict)

Upon completing the deep scan, the results will be presented in a Traffic Light style with Action Items:

- ❌ **CRITICAL**: Urgent deployment blockers (e.g., hardcoded passwords, RLS disabled on personal data). Requires immediate patches or purges.
- ⚠️ **WARNING**: Moderate risks (e.g., non-standard CSP, obsolete secondary dependencies).
- 📝 **IMPROVEMENT**: Minor opportunities and recommended optimizations for network architecture.
- ✅ **SECURE**: A balance of what the application is already protecting satisfactorily.

## Usage Context

- Pre-launch to formal production (before buying a definitive domain).
- After adding new architectures or systems to the main stack (e.g., incorporating payment gateways or file Storage).
- Quarterly as a strength test (Penta/Health-Check).

## Usage Example

USER: `/check-security`
(Optional specific focus) USER: `/check-security focus on Supabase database RLS`
(Optional local focus) USER: `/check-security check for hardcoded .env variables in UI Components`

AGENT: _(Assumes the role of an expert, runs bash commands, grep, invokes MCP if applicable, and drafts an executive report of flaws and patches)_.

## Prerequisites

- ❌ Do not interpret complex policies like Content-Security-Policy or Row Level Security in SQL.
- ❌ Do not provide base password secrets.
- ❌ Do not specify exactly how to search for flaws, linter commands, etc.
- ❌ Do not need to know the OWASP Top 10 in detail.

Just request the workflow; the agent will act as your Security Architect and document or resolve the platform.
