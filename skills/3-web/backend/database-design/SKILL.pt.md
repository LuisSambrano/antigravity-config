---
name: database-design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

# Projeto de banco de dados

> **Aprenda a PENSAR, não a copiar padrões SQL.**

## 🎯 Regra de leitura seletiva

**Leia SOMENTE os arquivos relevantes para a solicitação!** Verifique o mapa de conteúdo e encontre o que você precisa.

| Arquivo | Descrição | Quando ler |
|------|-------------|-------------|
| `seleção de banco de dados.md` | PostgreSQL vs Neon vs Turso vs SQLite | Escolhendo banco de dados |
| `orm-selection.md` | Chuvisco vs Prisma vs Kysely | Escolhendo ORM |
| `schema-design.md` | Normalização, PKs, relacionamentos | Projetando esquema |
| `indexação.md` | Tipos de índices, índices compostos | Ajuste de desempenho |
| `otimização.md` | N+1, EXPLICAR ANALISAR | Otimização de consulta |
| `migrações.md` | Migrações seguras, bancos de dados sem servidor | Mudanças de esquema |

## ⚠️ Princípio Fundamental

- PERGUNTE ao usuário as preferências do banco de dados quando não estiver claro
- Escolha banco de dados/ORM com base no CONTEXTO
- Não use o PostgreSQL como padrão para tudo

## Lista de verificação de decisão

Antes de projetar o esquema:

- [] Perguntou ao usuário sobre a preferência do banco de dados?
- [ ] Base de dados escolhida para ESTE contexto?
- [ ] Ambiente de implantação considerado?
- [] Estratégia de índice planejada?
- [] Tipos de relacionamento definidos?

## Antipadrões

❌ PostgreSQL padrão para aplicativos simples (SQLite pode ser suficiente)
❌ Pular indexação
❌ Use SELECT * na produção
❌ Armazene JSON quando os dados estruturados forem melhores
❌ Ignorar consultas N+1