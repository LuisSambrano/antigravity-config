---
name: api-patterns
description: API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

---

---

# Padrões de API

> Princípios de design de API e tomada de decisões para 2025.
> **Aprenda a PENSAR, não copie padrões fixos.**

## 🎯 Regra de leitura seletiva

**Leia SOMENTE os arquivos relevantes para a solicitação!** Verifique o mapa de conteúdo e encontre o que você precisa.

## 📑 Mapa de Conteúdo

| Arquivo | Descrição | Quando ler |
|------|-------------|-------------|
| `api-style.md` | Árvore de decisão REST vs GraphQL vs tRPC | Escolhendo o tipo de API |
| `rest.md` | Nomenclatura de recursos, métodos HTTP, códigos de status | Projetando API REST |
| `resposta.md` | Padrão de envelope, formato de erro, paginação | Estrutura de resposta |
| `graphql.md` | Design de esquema, quando usar, segurança | Considerando GraphQL |
| `trpc.md` | Monorepo TypeScript, segurança de tipo | Projetos fullstack de TS |
| `versionamento.md` | Controle de versão de URI/cabeçalho/consulta | Planejamento de evolução de API |
| `auth.md` | JWT, OAuth, chave de acesso, chaves de API | Seleção de padrão de autenticação |
| `limitação de taxa.md` | Balde de fichas, janela deslizante | Proteção API |
| `documentação.md` | Práticas recomendadas de OpenAPI/Swagger | Documentação |
| `testes de segurança.md` | Top 10 da API OWASP, testes de autenticação/authz | Auditorias de segurança |

## 🔗 Habilidades relacionadas

| Necessidade | Habilidade |
|------|-------|
| Implementação de API | `@[habilidades/desenvolvimento de back-end]` |
| Estrutura de dados | `@[habilidades/design de banco de dados]` |
| Detalhes de segurança | `@[habilidades/fortalecimento da segurança]` |

## ✅ Lista de verificação de decisão

Antes de projetar uma API:

- [ ] **Perguntou ao usuário sobre os consumidores da API?**
- [ ] **Estilo de API escolhido para ESTE contexto?** (REST/GraphQL/tRPC)
- [ ] **Formato de resposta consistente definido?**
- [ ] **Estratégia de versionamento planejada?**
- [ ] **Necessidades de autenticação consideradas?**
- [ ] **Limitação de taxa planejada?**
- [ ] **Abordagem de documentação definida?**

## ❌ Antipadrões

**NÃO:**
- Padrão REST para tudo
- Use verbos em endpoints REST (/getUsers)
- Retornar formatos de resposta inconsistentes
- Expor erros internos aos clientes
- Limitação de taxa de salto

**FAZER:**
- Escolha o estilo da API com base no contexto
- Pergunte sobre os requisitos do cliente
- Documente minuciosamente
- Use códigos de status apropriados

## Roteiro

| Roteiro | Finalidade | Comando |
|--------|---------|---------|
| `scripts/api_validator.py` | Validação de endpoint de API | `scripts python/api_validator.py <caminho_do_projeto>` |