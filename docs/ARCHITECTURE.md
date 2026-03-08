# Antigravity System Architecture

## 1. Introduction

The Antigravity ecosystem serves as the central orchestration layer for all AI-assisted engineering tasks within the workspace. By enforcing strict topographical boundaries and operational blueprints, it ensures consistent code quality and seamless context handoffs across multiple projects.

## 2. Topographical Divisions

The workspace is strictly bifurcated into two environments:

### `github/` (Public / Remote Sync)

Contains all canonical application code and system configuration intended for version control. These repositories are prefixed numerically (`01-antigravity`, `02-profile`, etc.) for deterministic sorting and explicit architectural intent.

### `local/` (Private / Untracked)

Contains sensitive, experimental, or client-specific data. This includes `n8n` instances, `Flowise` workflows, and legacy archives. It is shielded by a global `.gitignore` to prevent secret leakage.
