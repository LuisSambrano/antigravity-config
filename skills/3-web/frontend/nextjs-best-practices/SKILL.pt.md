---
name: nextjs-best-practices
description: Next.js App Router principles. Server Components, data fetching, routing patterns.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

```
Does it need...?
│
├── useState, useEffect, event handlers
│   └── Client Component ('use client')
│
├── Direct data fetching, no interactivity
│   └── Server Component (default)
│
└── Both? 
    └── Split: Server parent + Client child
```

---

---

---

---

---

---

---

---

---

```
app/
├── (marketing)/     # Route group
│   └── page.tsx
├── (dashboard)/
│   ├── layout.tsx   # Dashboard layout
│   └── page.tsx
├── api/
│   └── [resource]/
│       └── route.ts
└── components/
    └── ui/
```

---

# Práticas recomendadas Next.js

> Princípios para desenvolvimento do Next.js App Router.

## 1. Componentes Servidor vs Cliente

### Árvore de decisão

### Por padrão

| Tipo | Usar |
|------|-----|
| **Servidor** | Busca de dados, layout, conteúdo estático |
| **Cliente** | Formulários, botões, UI interativa |

## 2. Padrões de busca de dados

### Estratégia de busca

| Padrão | Usar |
|--------|-----|
| **Padrão** | Estático (armazenado em cache na construção) |
| **Revalidar** | ISR (atualização baseada no tempo) |
| **Sem loja** | Dinâmico (cada solicitação) |

### Fluxo de dados

| Fonte | Padrão |
|--------|---------|
| Banco de dados | Busca de componentes do servidor |
| API | buscar com cache |
| Entrada do usuário | Estado do cliente + ação do servidor |

## 3. Princípios de roteamento

### Convenções de arquivo

| Arquivo | Finalidade |
|------|---------|
| `página.tsx` | UI de rota |
| `layout.tsx` | Layout compartilhado |
| `carregando.tsx` | Estado de carregamento |
| `erro.tsx` | Limite de erro |
| `não-encontrado.tsx` | página 404 |

### Organização da rota

| Padrão | Usar |
|--------|-----|
| Grupos de rotas `(nome)` | Organizar sem URL |
| Rotas paralelas `@slot` | Várias páginas do mesmo nível |
| Interceptando `(.)` | Sobreposições modais |

## 4. Rotas de API

### Manipuladores de rota

| Método | Usar |
|--------|-----|
| OBTER | Ler dados |
| POSTAR | Criar dados |
| COLOCAR/PATCH | Atualizar dados |
| EXCLUIR | Remover dados |

### Melhores Práticas

- Validar entrada com Zod
- Retornar códigos de status adequados
- Lidar com erros normalmente
- Use o tempo de execução do Edge quando possível

## 5. Princípios de Desempenho

### Otimização de imagem

- Use o componente próximo/imagem
- Definir prioridade para a dobra acima
- Fornece espaço reservado para desfoque
- Use tamanhos responsivos

### Otimização de pacote

- Importações dinâmicas de componentes pesados
- Divisão de código baseada em rota (automática)
- Analisar com analisador de pacote

## 6. Metadados

### Estático vs Dinâmico

| Tipo | Usar |
|------|-----|
| Exportação estática | Metadados fixos |
| gerarMetadados | Dinâmico por rota |

### Tags essenciais

- título (50-60 caracteres)
- descrição (150-160 caracteres)
- Imagens abertas do gráfico
- URL canônico

## 7. Estratégia de cache

### Camadas de cache

| Camada | Controle |
|-------|---------|
| Solicitação | buscar opções |
| Dados | revalidar/etiquetas |
| Percurso completo | configuração de rota |

### Revalidação

| Método | Usar |
|--------|-----|
| Baseado no tempo | `revalidar: 60` |
| Sob demanda | `revalidarCaminho/Tag` |
| Sem cache | `sem loja` |

## 8. Ações do servidor

### Casos de uso

- Envios de formulários
- Mutações de dados
- Gatilhos de revalidação

### Melhores Práticas

- Marque com 'usar servidor'
- Validar todas as entradas
- Retornar respostas digitadas
- Lidar com erros

## 9. Antipadrões

| ❌Não | ✅ Faça |
|----------|-------|
| 'usar cliente' em qualquer lugar | Servidor por padrão |
| Buscar componentes do cliente | Buscar no servidor |
| Ignorar estados de carregamento | Usar carregamento.tsx |
| Ignorar limites de erro | Usar erro.tsx |
| Grandes pacotes de clientes | Importações dinâmicas |

## 10. Estrutura do Projeto

> **Lembre-se:** Os componentes do servidor são o padrão por um motivo. Comece por aí, adicione cliente somente quando necessário.