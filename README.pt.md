<div align="center">

# Antigravity Config

Um framework de configuração para ambientes de desenvolvimento assistidos por IA.  
Regras, skills e workflows que padronizam como agentes de código IA operam nos seus projetos.

<p>
  <a href="./README.md">English</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/Licença-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## O que é isto

Este repositório fornece um diretório `.agent/` pronto para usar com assistentes de código IA (Gemini, Cursor, Windsurf, etc.). Ele age como o cérebro e a lei para o seu agente IA, dando-lhe limites claros e conhecimento especializado para usar em seus projetos.

### Os Três Pilares

- **Rules (A Constituição)** — As leis imutáveis do seu projeto. O agente IA aplica-as automaticamente a cada arquivo que cria ou edita (ex: "usar sempre TypeScript estrito", "seguir convenções específicas de nomenclatura"). Estas são modificadas em `GEMINI.md` ou na pasta `rules/` para adaptar o agente às preferências da sua equipe.
- **Skills (A Biblioteca)** — Conhecimento especializado sob demanda. O agente as lê passivamente ao trabalhar em tópicos específicos, ou você pode instruí-lo explicitamente "Leia a skill X antes de fazer Y" para dar um contexto profundo e de domínio (105+ skills em 10 categorias disponíveis).
- **Workflows (Os Procedimentos Operacionais Padrão / POPs)** — Guias passo a passo para executar tarefas complexas. Esta é a parte mais interativa: você os invoca explicitamente usando "Slash commands" (como `/deploy`, `/idea`, `/check-security`). O uso de um workflow garante que o agente IA nunca pule etapas críticas ao realizar operações em várias fases.

O objetivo é direto: clonar, instalar e ter um ambiente de desenvolvimento consistente e opinativo onde seu assistente IA segue padrões profissionais.

---

## 🤖 For AI Agents (How to Read This Repo)

**SYSTEM DIRECTIVE**: If you are an AI assistant analyzing or working within this workspace, follow these operating instructions:

1. **Start Here**: Your first step is ALWAYS to read `rules/PROTOCOL_ZERO.md` to understand the foundational philosophy.
2. **Skill Discovery**: Check `skills/INDEX.md` to find relevant knowledge before writing domain-specific code. If a skill matches the user's request, read its `SKILL.md` file unconditionally.
3. **Workflow Execution**: If you see the user typing a command like `/deploy` or `/idea`, immediately view the corresponding `.md` file in the `workflows/` directory and execute it step-by-step, exactly as written.

---

## Início Rápido

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config && chmod +x install.sh && ./install.sh
```

O instalador copia rules, skills e workflows para o diretório `.agent/` do seu workspace e configura `GEMINI.md` como arquivo de regras globais.

---

## Estrutura do Repositório

```
antigravity-config/
├── GEMINI.md                  # Template de regras globais (personalizável)
├── install.sh                 # Script de instalação
│
├── rules/                     # Padrões de código e arquitetura
│   ├── PROTOCOL_ZERO.md       # Filosofia base e princípios
│   ├── ARCHITECTURE_STANDARDS.md
│   ├── CODE_STANDARDS.md
│   ├── QUALITY_GATES.md
│   ├── frontend/              # Regras específicas de frontend
│   └── backend/               # Regras específicas de backend
│
├── skills/                    # Conhecimento de domínio (105+ skills)
│   ├── 1-core/                # Fundamentos de código
│   ├── 2-ai/                  # Agentes IA, RAG, prompting
│   ├── 3-web/                 # Desenvolvimento web (Next.js, React, Tailwind)
│   ├── 4-automation/          # Testing, CI/CD, scraping
│   ├── 5-security/            # Segurança API, pentesting
│   ├── 6-content/             # Escrita técnica, SEO
│   ├── 7-meta/                # Criação e gestão de skills
│   ├── 8-blockchain/
│   ├── 9-business/
│   └── 10-tools/              # Docs, presentações, browser testing, Chrome DevTools MCP
│
├── workflows/                 # Scripts de comandos do agente
│   ├── deploy.md              # /deploy — deployment para produção
│   ├── idea.md                # /idea — avaliar ideias de projeto
│   ├── status.md              # /status — health check do projeto
│   ├── create-component.md    # /create-component — scaffold de componentes
│   └── help.md                # /help — listar comandos disponíveis
│
├── templates/                 # Templates de projeto
├── research/                  # Log de decisões e descobertas
└── docs/                      # Documentação adicional
```

---

## Referência de Skills

Skills são arquivos markdown que dão ao agente IA conhecimento específico de domínio. Cada skill contém instruções, padrões e referências que o agente utiliza ao trabalhar nesse domínio.

### 1-core — Fundamentos (+6 skills)

Convenções de código, padrões de estrutura de projeto e padrões TypeScript aplicáveis a todos os projetos.

### 2-ai — IA e Agentes (21 skills)

Orquestração multi-agente (LangGraph, CrewAI), sistemas RAG, engenharia de prompts, desenvolvimento de Voice AI e frameworks de avaliação de agentes.

### 3-web — Desenvolvimento Web (17 skills)

Padrões de Next.js App Router, melhores práticas de React, arquitetura Tailwind CSS, integração com Supabase, deployment no Vercel e princípios de design UI/UX.

### 4-automation — Testing e DevOps (10 skills)

Testing com Playwright, workflows de GitHub Actions, procedimentos de deployment e web scraping com Firecrawl.

### 5-security — Segurança (5 skills)

Melhores práticas de segurança API e checklists de penetration testing.

### 6-content — Criação de Conteúdo

Guias de escrita técnica, copywriting SEO e padrões de documentação.

### 7-meta — Gestão de Skills (3 skills)

Ferramentas para criar novos skills, planejamento com arquivos e melhoria contínua (Kaizen).

### 8-blockchain — Celo e EVM (19 skills)

Stack completo de desenvolvimento Celo: integração com MiniPay, fee abstraction, endereços de stablecoins, scaffolding com Celo Composer, bibliotecas viem/wagmi, tooling Hardhat/Foundry, bridging cross-chain, integração com protocolos DeFi, protocolo de confiança ERC-8004 e protocolo de pagamentos HTTP x402.

> Ver [skills/INDEX.md](./skills/INDEX.md) para o detalhamento skill por skill.

---

## Resumo de Rules

As rules definem como o agente IA escreve e valida código. São carregadas no contexto do agente e aplicadas automaticamente.

| Rule                        | Propósito                                                               |
| --------------------------- | ----------------------------------------------------------------------- |
| `PROTOCOL_ZERO.md`          | Filosofia base: qualidade sobre velocidade, local como fonte de verdade |
| `ARCHITECTURE_STANDARDS.md` | Estrutura de projeto, organização de componentes, nomenclatura          |
| `CODE_STANDARDS.md`         | TypeScript strict mode, ordem de imports, error handling, JSDoc         |
| `QUALITY_GATES.md`          | Checks pre-commit, verificação de build, acessibilidade, performance    |

---

## Personalização

`GEMINI.md` é o arquivo de configuração principal. Agrega todas as rules em um único documento que o agente IA lê. Edite-o para:

- Adicionar ou remover rules
- Mudar convenções de nomenclatura
- Ajustar limites de qualidade
- Adicionar routing de workflows para seus próprios comandos

As seções marcadas com `<!-- CUSTOMIZE -->` são projetadas para modificação.

---

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes sobre adicionar skills, workflows ou rules.

```bash
git checkout -b feature/sua-feature
git commit -m 'feat(skills): add nome-do-skill'
git push origin feature/sua-feature
```

---

## Pesquisa e Log de Decisões

| Documento                                     | Propósito                                 |
| --------------------------------------------- | ----------------------------------------- |
| [KEY_FINDINGS.md](./research/KEY_FINDINGS.md) | Princípios base e descobertas de pesquisa |
| [prompts/](./research/prompts/)               | Prompts de definição de rules e iterações |
| [rules/](./rules/)                            | Os documentos de padrões resultantes      |

---

## Licença

MIT — ver [LICENSE](LICENSE) para detalhes.

---

<div align="center">

**Mantido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
