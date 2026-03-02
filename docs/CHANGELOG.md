# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.2.0] - 2026-02-26

### Added

- New skill: `chrome-devtools-mcp` — Ultra-fast UI testing with Chrome DevTools Protocol
  - Direct CDP integration replaces slow visual emulation (browser_subagent)
  - 34 tools: input automation, navigation, emulation, performance, network, debugging
  - Decision tree for when to use CDP vs browser_subagent
  - 4 operational protocols (UI testing, debugging, performance, responsive)
  - Installation guide with 3 configuration options

### Changed

- Updated skill count: 100 → 101 (10-tools category: 4 → 5)
- Updated trilingual READMEs (EN, ES, PT) with new skill reference

## [3.1.0] - 2026-02-03

### Added

- Professional repository reorganization
- Trilingual README (English, Spanish, Portuguese)
- One-click installation script (`install.sh`)
- CONTRIBUTING.md guidelines
- CODE_OF_CONDUCT.md (Contributor Covenant)
- SECURITY.md policy
- Skills INDEX.md catalog
- New category structure (1-core through 7-meta)
- SKILL_TEMPLATE for creating new skills

### Changed

- Reorganized skills into numbered categories
- Removed `cc-skill-` prefix from coding-standards
- Simplified workflows to 3 core commands

### Removed

- Empty `archive/` folder
- Empty `lab/` folder
- `nextlevelbuilder/` (moved to separate repo)
- Obsolete workflows

## [3.0.0] - 2026-02-01

### Added

- 100+ AI skills across 12 categories
- Master rules (Protocol Zero, Architecture, Code, Quality)
- GitHub issue templates
- GitHub Actions workflow

### Changed

- Renamed from google-antigravity to antigravity-config
- Restructured for plug-and-play installation

## [2.0.0] - 2026-01-15

### Added

- Initial skill library
- Basic installation script
- README documentation

---

[3.2.0]: https://github.com/LuisSambrano/antigravity-config/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/LuisSambrano/antigravity-config/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/LuisSambrano/antigravity-config/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.com/LuisSambrano/antigravity-config/releases/tag/v2.0.0
