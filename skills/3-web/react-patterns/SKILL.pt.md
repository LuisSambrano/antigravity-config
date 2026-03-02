---
name: react-patterns
description: Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

---

---

---

---

---

---

---

---

---

# Padrões de reação

> Princípios para construir aplicativos React prontos para produção.

## 1. Princípios de design de componentes

### Tipos de componentes

| Tipo | Usar | Estado |
|------|-----|-------|
| **Servidor** | Busca de dados, estática | Nenhum |
| **Cliente** | Interatividade | useState, efeitos |
| **Apresentação** | Exibição da interface do usuário | Apenas adereços |
| **Contêiner** | Lógica/estado | Estado pesado |

### Regras de projeto

- Uma responsabilidade por componente
- Adereços para baixo, eventos para cima
- Composição sobre herança
- Prefira componentes pequenos e focados

## 2. Padrões de gancho

### Quando extrair ganchos

| Padrão | Extrair quando |
|--------|-------------|
| **usarLocalStorage** | É necessária a mesma lógica de armazenamento |
| **useDebounce** | Vários valores debounced |
| **useFetch** | Padrões de busca repetidos |
| **usarFormulário** | Estado de formulário complexo |

### Regras do Gancho

- Ganchos apenas no nível superior
- Mesma ordem em cada renderização
- Ganchos personalizados começam com "use"
- Limpar efeitos ao desmontar

## 3. Seleção de gestão estadual

| Complexidade | Solução |
|------------|----------|
| Simples | useState, useReducer |
| Local compartilhado | Contexto |
| Estado do servidor | Consulta de reação, SWR |
| Global complexo | Zustand, kit de ferramentas Redux |

### Colocação estadual

| Escopo | Onde |
|-------|-------|
| Componente único | usarEstado |
| Pai-filho | Levante o estado |
| Subárvore | Contexto |
| Em todo o aplicativo | Loja global |

## 4. Reagir 19 padrões

### Novos Ganchos

| Gancho | Finalidade |
|------|---------|
| **useActionState** | Estado de envio do formulário |
| **useOtimista** | Atualizações otimistas da interface do usuário |
| **usar** | Leia recursos em renderização |

### Benefícios do compilador

- Memoização automática
- Menos uso manualMemo/useCallback
- Foco em componentes puros

## 5. Padrões de composição

### Componentes compostos

- Pai fornece contexto
- As crianças consomem contexto
- Composição flexível baseada em slots
- Exemplo: guias, acordeão, menu suspenso

### Renderizar adereços versus ganchos

| Caso de uso | Prefiro |
|----------|--------|
| Lógica reutilizável | Gancho personalizado |
| Flexibilidade de renderização | Renderizar adereços |
| Corte transversal | Componente de ordem superior |

## 6. Princípios de Desempenho

### Quando otimizar

| Sinal | Ação |
|--------|--------|
| Renderizações lentas | Perfil primeiro |
| Listas grandes | Virtualizar |
| Cálculo caro | usarMemorando |
| Retornos de chamada estáveis ​​| usarCallback |

### Ordem de otimização

1. Verifique se realmente está lento
2. Perfil com DevTools
3. Identifique o gargalo
4. Aplique correção direcionada

## 7. Tratamento de erros

### Uso do limite de erro

| Escopo | Colocação |
|-------|-----------|
| Em todo o aplicativo | Nível raiz |
| Recurso | Nível de rota/recurso |
| Componente | Em torno do componente de risco |

### Recuperação de erros

- Mostrar interface de usuário substituta
- Erro de registro
- Oferecer opção de nova tentativa
- Preservar dados do usuário

## 8. Padrões TypeScript

### Digitação de acessórios

| Padrão | Usar |
|--------|-----|
| Interface | Adereços de componentes |
| Tipo | Sindicatos complexos |
| Genérico | Componentes reutilizáveis ​​|

### Tipos Comuns

| Necessidade | Tipo |
|------|------|
| Crianças | ReactNode |
| Manipulador de eventos | MouseEventHandler |
| Referência | RefObject<Elemento> |

## 9. Princípios de teste

| Nível | Foco |
|-------|-------|
| Unidade | Funções puras, ganchos |
| Integração | Comportamento dos componentes |
| E2E | Fluxos de usuários |

### Prioridades de teste

- Comportamento visível ao usuário
- Casos extremos
- Estados de erro
- Acessibilidade

## 10. Antipadrões

| ❌Não | ✅ Faça |
|----------|-------|
| Perfuração profunda | Usar contexto |
| Componentes gigantes | Dividir menor |
| useEffect para tudo | Componentes do servidor |
| Otimização prematura | Perfil primeiro |
| Índice como chave | ID exclusivo estável |

> **Lembre-se:** React é uma questão de composição. Construa pequeno e combine cuidadosamente.