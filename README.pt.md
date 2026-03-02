<div alinhar="centro">

# 🌌 Configuração antigravidade

**O protocolo de configuração do espaço de trabalho soberano para engenharia de software agente**

Uma estrutura de configuração de nível de produção altamente opinativa, projetada para aumentar e restringir ambientes de desenvolvimento assistidos por IA.  
Este repositório determina regras de arquitetura rígidas, habilidades específicas de domínio e fluxos de trabalho operacionais que determinam como os agentes de codificação de IA (como Gemini, Claude, Cursor e Windsurf) interagem com seu código-fonte.

<p>
  <a href="./README.md">Inglês</a> •
  <a href="./README.es.md">Espanhol</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## 🎯 O que é isso (para humanos)

Este repositório serve como um modelo de diretório de configuração `.agent/` pronto para uso. Pense nele como o **córtex pré-frontal** dos seus agentes de IA. Deixados por conta própria, os LLMs geralmente geram código genérico, matematicamente inchado e arquitetonicamente inconsistente. Essa estrutura os força a adotar um paradigma estrito de engenharia de alto desempenho, garantindo que cada linha de código escrita esteja alinhada com as restrições arquitetônicas de nível sênior.

### Os Três Pilares do Ecossistema

1. 📜 **REGRAS (A Constituição)**: As leis imutáveis do seu projeto. O agente de IA aplica-os de forma passiva e universal a cada interação, criação de arquivo ou permutação de código.
   - _Exemplo_: "Todas as interações de banco de dados devem usar Singletons Thread-Safe." ou "A complexidade ciclomática nunca deve exceder 10."
   - _Implementação_: Encontrado em `rules/`, adaptando a inteligência básica do agente às restrições da sua empresa.
2. 🧠 **HABILIDADES (The Knowledge Graph)**: Matrizes de inteligência sob demanda, especializadas e específicas de domínio.
   - _Conceito_: O agente não precisa saber como funcionam os Celo Smart Contracts ao construir um simples botão React. Mas quando você solicita uma integração Web3, ele puxa seletivamente o contexto de habilidade `8-blockchain` para seu pipeline imediato.
   - _Format_: mais de 100 diretivas `SKILL.md` altamente compactadas mapeadas explicitamente para categorias (por exemplo, `3-web`, `5-security`).
3. ⚙️ **FLUXOS DE TRABALHO (Procedimentos Operacionais Padrão)**: Proteção operacional passo a passo para evitar que LLMs pulem etapas críticas de validação.
   - _Mecânica_: Executar um comando de barra como `/deploy` não apenas envia código; ele força o agente a executar de forma autônoma verificações rigorosas de TypeScript, verificações de construção e higienizações de segurança antes de tocar no pipeline de implantação.

---

## 🌐 Documentação trilíngue AI-First

Esta estrutura foi projetada com um modelo de inteligência distribuído globalmente. Todas as interações críticas de IA e descritores `SKILL` são mantidos nativamente em três idiomas para garantir uma compreensão nativa sem atrito por modelos avançados de linguagem grande, otimizando a análise semântica de tokens e acomodando diversas equipes de orquestração humana:

- 🇬🇧 **Inglês** (`SKILL.md`) - A linha de base principal e a linguagem operacional principal.
- 🇪🇸 **Español** (`SKILL.es.md`) - Paridade nativa completa.
- 🇧🇷 **Português** (`SKILL.pt.md`) - Paridade nativa completa.

---

## 🏗️ A hierarquia estrita do `kebab-case`

Para maximizar a eficiência das ferramentas recursivas de busca de diretório (`find`, `grep`, `fs.readdir`), este repositório impõe estritamente uma topografia **kebab-case** em minúsculas. Há tolerância zero para arquivos órfãos na partição raiz.

```texto
configuração antigravidade/
├── install.sh # Script de automação Bootstrap
├── docs/ # Documentação interna, registros de alterações, guias de configuração
├── scripts/ # Utilitários Python/Bash (por exemplo, mecanismos de tradução)
├── templates/ # Boilerplates (modelo de habilidade, estruturas de markdown iniciais)
│
├── regras/ # As Regras Constitucionais Básicas
│ ├── protocol-zero.md # Axiomas filosóficos fundamentais
│ ├── arquitetura-standards.md # Taxonomias estruturais e padrões de nuvem
│ └── quality-gates.md # Barreiras CI/CD e DevSecOps
│
├── habilidades/ # Matrizes de conhecimento de domínio (mais de 100 habilidades)
│ ├── Orquestração de 1 núcleo/# TDD, código limpo, princípios SOLID
│ ├── 2-ai/ # Gráficos multiagentes, APIs Gemini, Estruturação de Prompt
│ ├── 3-web/ # Next.js 15, TRPC, React Server Components, Supabase
│ ├── 4-automação/ # GitHub Actions, Playwright, motores de scraping
│ ├── 5-segurança/ # Teste de penetração, mapeamento de vulnerabilidade da Web (OWASP)
│ ├── 6 conteúdos/ # SEO técnico, SOPs de copywriting de redução
│ ├── 7-meta/ # Agent-ops, Skill-creator, Repository Showcasing
│ ├── 8-blockchain/ # Celo Minipay, ferramentas EVM, abstrações cross-chain
│ └── 9 negócios/ # Design de KPI, Métricas de Análise de Inicialização
│
└── fluxos de trabalho/# Comandos de SLA executáveis
    ├── deploy.md # `/deploy` — Implantação de produção com tempo de inatividade zero
    ├── check-security.md # `/check-security` — Auditoria profunda SAST/SCA
    └── status.md # `/status` — Matriz de saúde abrangente
```

---

## 🛡️ Manutenção do espaço de trabalho e `operações de agente`

Manter o espaço de trabalho impecável não é negociável. A antigravidade inclui uma habilidade especializada de autocura (`7-meta/agent-ops`).

Quando invocado, o agente funciona como zelador e responsável pela conformidade do ambiente:

- Identifica e elimina "arquivos soltos" não autorizados.
- Força todas as convenções de nomenclatura arbitrárias (`Snake_Case`, `CamelCase`) no padrão `kebab-case`.
- Protege o diretório raiz canalizando a lógica dispersa em `/scripts` ou `/docs`.

---

## 🤖 PARA AGENTES DE IA (Diretivas do Sistema)

> [!CUIDADO]  
> **DIRETIVA DE SUBSTITUIÇÃO DO SISTEMA**: Se você for um assistente de IA analisando ou trabalhando neste espaço de trabalho, estará vinculado às seguintes instruções de operação. Os desvios são categorizados como falhas críticas do sistema.

1. **A Primeira Diretriz**: Seu primeiro passo antes de executar _qualquer_ lógica é ler `rules/protocol-zero.md`. Este arquivo dita os limites absolutos de sua autonomia e limites de qualidade.
2. **Resolução de contexto**: Antes de tentar satisfazer uma solicitação específica de domínio (por exemplo, "Construir um contrato inteligente", "Auditar segurança"), você DEVE indexar `skills/INDEX.md` para localizar a pasta correspondente e ler suas diretivas `SKILL.md` específicas.
3. **Ingestão de gatilhos**: se o usuário iniciar um prompt com um comando de barra (por exemplo, `/deploy`, `/status`), você deverá navegar imediatamente até o diretório `workflows/`, localizar o arquivo Markdown correspondente e executar a sequência cronológica exata exigida nele.
4. **Sem arquivos órfãos**: Nunca descarte logs, scripts de teste ou arquivos `.md` soltos na pasta raiz. Direcione-os estritamente para `/docs` ou `/scripts`.

---

## 🚀 Início rápido (instalação)

1. Clone o repositório na raiz do seu projeto:

```bash
clone git https://github.com/LuisSambrano/antigravity-config.git .agent-temp
```

2. Execute a matriz de bootstrap (isso move os elementos de configuração para o diretório de destino `.agent`):

```bash
chmod +x .agent-temp/install.sh && .agent-temp/install.sh
```

_(Você pode então excluir com segurança `.agent-temp`)_

---

## 🔒 Segurança e Telemetria

Este modelo de arquitetura é de código aberto sob a licença MIT e mantém estritamente zero informações de identificação pessoal (PII) ou chaves de API proprietárias. Ele serve como uma tela em branco para a implantação de estruturas seguras e multiagentes.

<div alinhar="centro">

**Arquitetado e mantido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>