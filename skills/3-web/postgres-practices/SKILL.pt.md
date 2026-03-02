---
name: postgres-practices
description: Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.
license: MIT
metadata:
  author: supabase
  version: "1.0.0"
---

```
rules/query-missing-indexes.md
rules/schema-partial-indexes.md
rules/_sections.md
```

# Práticas recomendadas do Supabase Postgres

Guia abrangente de otimização de desempenho para Postgres, mantido pela Supabase. Contém regras em 8 categorias, priorizadas por impacto para orientar a otimização automatizada de consultas e o design de esquemas.

## Quando aplicar

Consulte estas diretrizes quando:
- Escrever consultas SQL ou projetar esquemas
- Implementação de índices ou otimização de consultas
- Revisão de problemas de desempenho do banco de dados
- Configurando pooling ou escalonamento de conexões
- Otimização para recursos específicos do Postgres
- Trabalhando com segurança em nível de linha (RLS)

## Categorias de regras por prioridade

| Prioridade | Categoria | Impacto | Prefixo |
|----------|----------|--------|--------|
| 1 | Desempenho de consulta | CRÍTICO | `consulta-` |
| 2 | Gerenciamento de conexão | CRÍTICO | `con-` |
| 3 | Segurança e RLS | CRÍTICO | `segurança-` |
| 4 | Projeto de esquema | ALTO | `esquema-` |
| 5 | Simultaneidade e bloqueio | MÉDIO-ALTO | `bloqueio-` |
| 6 | Padrões de acesso a dados | MÉDIO | `dados-` |
| 7 | Monitoramento e Diagnóstico | BAIXO-MÉDIO | `monitorar-` |
| 8 | Recursos Avançados | BAIXO | `avançado-` |

## Como usar

Leia arquivos de regras individuais para obter explicações detalhadas e exemplos de SQL:

Cada arquivo de regras contém:
- Breve explicação de por que isso é importante
- Exemplo SQL incorreto com explicação
- Exemplo SQL correto com explicação
- Saída ou métricas EXPLAIN opcionais
- Contexto e referências adicionais
- Notas específicas da Supabase (quando aplicável)

## Documento compilado completo

Para o guia completo com todas as regras expandidas: `AGENTS.md`