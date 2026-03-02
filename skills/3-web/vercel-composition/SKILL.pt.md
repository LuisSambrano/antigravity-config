---
name: vercel-composition
description:
  React composition patterns that scale. Use when refactoring components with
  boolean prop proliferation, building flexible component libraries, or
  designing reusable APIs. Triggers on tasks involving compound components,
  render props, context providers, or component architecture. Includes React 19
  API changes.
license: MIT
metadata:
  author: vercel
  version: '1.0.0'
---

```
rules/architecture-avoid-boolean-props.md
rules/state-context-interface.md
```

# Padrões de composição de reação

Padrões de composição para construir componentes React flexíveis e de fácil manutenção. Evite
proliferação de prop booleano usando componentes compostos, estado de elevação e
compondo internos. Esses padrões tornam as bases de código mais fáceis para humanos e IA
agentes com os quais trabalhar à medida que crescem.

## Quando aplicar

Consulte estas diretrizes quando:

- Refatoração de componentes com muitos adereços booleanos
- Construindo bibliotecas de componentes reutilizáveis
- Projetando APIs de componentes flexíveis
- Revisão da arquitetura de componentes
- Trabalhar com componentes compostos ou provedores de contexto

## Categorias de regras por prioridade

| Prioridade | Categoria | Impacto | Prefixo |
| -------- | ----------------------- | ------ | --------------- |
| 1 | Arquitetura de Componentes | ALTO | `arquitetura-` |
| 2 | Gestão Estadual | MÉDIO | `estado-` |
| 3 | Padrões de implementação | MÉDIO | `padrões-` |
| 4 | Reagir 19 APIs | MÉDIO | `react19-` |

## Referência rápida

### 1. Arquitetura de componentes (ALTA)

- `architecture-avoid-boolean-props` - Não adicione adereços booleanos para personalizar
  comportamento; usar composição
- `architecture-compound-components` - Estruture componentes complexos com compartilhamento
  contexto

### 2. Gestão de Estado (MÉDIO)

- `state-decouple-implementation` - O provedor é o único lugar que sabe como
  estado é gerenciado
- `state-context-interface` - Definir interface genérica com estado, ações, meta
  para injeção de dependência
- `state-lift-state` - Move o estado para os componentes do provedor para acesso irmão

### 3. Padrões de implementação (MÉDIO)

- `patterns-explicit-variants` - Crie componentes variantes explícitos em vez de
  modos booleanos
- `patterns-children-over-render-props` - Use filhos para composição
  de adereços renderX

### 4. APIs React 19 (MÉDIO)

> **⚠️ Apenas React 19+.** Pule esta seção se estiver usando React 18 ou anterior.

- `react19-no-forwardref` - Não use `forwardRef`; use `use()` em vez de `useContext()`

## Como usar

Leia arquivos de regras individuais para obter explicações detalhadas e exemplos de código:

Cada arquivo de regras contém:

- Breve explicação de por que isso é importante
- Exemplo de código incorreto com explicação
- Exemplo de código correto com explicação
- Contexto e referências adicionais

## Documento compilado completo

Para o guia completo com todas as regras expandidas: `AGENTS.md`