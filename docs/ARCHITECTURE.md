# Antigravity System Architecture

## 1. Introduction

The Antigravity ecosystem serves as the central orchestration layer for all AI-assisted engineering tasks within the workspace. By enforcing strict topographical boundaries and operational blueprints, it ensures consistent code quality and seamless context handoffs across multiple projects.

## 2. Topographical Divisions

The workspace is strictly bifurcated into two environments:

### `github/` (Public / Remote Sync)

Contains all canonical application code and system configuration intended for version control. These repositories are prefixed numerically (`01-antigravity`, `02-profile`, etc.) for deterministic sorting and explicit architectural intent.

### `local/` (Private / Untracked)

Contains sensitive, experimental, or client-specific data. This includes `n8n` instances, `Flowise` workflows, and legacy archives. It is shielded by a global `.gitignore` to prevent secret leakage.

## 3. Protocol Zero

All AI and human agents must adhere to the immutable principles of `Protocol Zero`, instantiated centrally in `.agent/rules/PROTOCOL_ZERO.md`.

- **Safety First:** Read operations take precedence over destructives. Secrets must never be stored in plaintext.
- **Verification:** Unit and end-to-end tests act as the final gate before pushing to remote origins.
- **Local-First Consistency:** The developer machine determines the source of truth; GitHub acts solely as the synchronization layer.

## 4. Workflows and Workspaces

- **Workspaces:** Individual directories in `github/` function as isolated context bubbles (`04-puente`, `08-libertad`). They may extend global rules using local `.gemini` configurations.
- **Workflows:** Complex operational scenarios (e.g., executing audits or deploying to Verel) are governed by markdown definitions within `.agent/workflows/`.
