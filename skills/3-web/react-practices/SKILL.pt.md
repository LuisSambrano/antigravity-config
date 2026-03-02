---
name: react-practices
description: React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
---

# Práticas recomendadas do Vercel React

Guia abrangente de otimização de desempenho para aplicativos React e Next.js, mantido pela Vercel. Contém 45 regras em 8 categorias, priorizadas por impacto para orientar a refatoração automatizada e a geração de código.

## Quando aplicar

Consulte estas diretrizes quando:
- Escrever novos componentes React ou páginas Next.js
- Implementação de busca de dados (cliente ou servidor)
- Revisão de código para problemas de desempenho
- Refatoração do código React/Next.js existente
- Otimizando o tamanho do pacote ou tempos de carregamento

## Categorias de regras por prioridade

| Prioridade | Categoria | Impacto | Prefixo |
|----------|----------|--------|--------|
| 1 | Eliminando Cachoeiras | CRÍTICO | `assíncrono-` |
| 2 | Otimização do tamanho do pacote | CRÍTICO | `pacote-` |
| 3 | Desempenho do lado do servidor | ALTO | `servidor-` |
| 4 | Busca de dados do lado do cliente | MÉDIO-ALTO | `cliente-` |
| 5 | Otimização de nova renderização | MÉDIO | `renderizar-` |
| 6 | Desempenho de renderização | MÉDIO | `renderização-` |
| 7 | Desempenho de JavaScript | BAIXO-MÉDIO | `js-` |
| 8 | Padrões Avançados | BAIXO | `avançado-` |

## Referência rápida

### 1. Eliminando Cachoeiras (CRÍTICO)

- `async-defer-await` - Mova o await para as ramificações onde realmente é usado
- `async-parallel` - Use Promise.all() para operações independentes
- `async-dependencies` - Use melhor para dependências parciais
- `async-api-routes` - Comece promessas mais cedo, aguarde mais tarde nas rotas da API
- `async-suspense-boundaries` - Use Suspense para transmitir conteúdo

### 2. Otimização do tamanho do pacote (CRÍTICO)

- `bundle-barrel-imports` - Importe diretamente, evite arquivos barril
- `bundle-dynamic-imports` - Use next/dynamic para componentes pesados
- `bundle-defer-third-party` - Carregar análises/registro após hidratação
- `bundle-conditional` - Carrega módulos somente quando o recurso está ativado
- `bundle-preload` - Pré-carregamento ao passar o mouse/foco para velocidade percebida

### 3. Desempenho do lado do servidor (ALTO)

- `server-cache-react` - Use React.cache() para desduplicação por solicitação
- `server-cache-lru` - Use cache LRU para cache de solicitação cruzada
- `server-serialization` - Minimiza os dados passados para os componentes do cliente
- `server-parallel-fetching` - Reestrutura componentes para paralelizar buscas
- `server-after-nonblocking` - Use after() para operações sem bloqueio

### 4. Busca de dados do lado do cliente (MÉDIO-ALTO)

- `client-swr-dedup` - Use SWR para desduplicação automática de solicitações
- `client-event-listeners` - Desduplica ouvintes de eventos globais

### 5. Otimização de nova renderização (MÉDIO)

- `rerender-defer-reads` - Não assine o estado usado apenas em retornos de chamada
- `rerender-memo` - Extrai trabalhos caros em componentes memorizados
- `rerender-dependencies` - Use dependências primitivas em efeitos
- `rerender-derived-state` - Assine booleanos derivados, não valores brutos
- `rerender-funcional-setstate` - Use setState funcional para retornos de chamada estáveis
- `rerender-lazy-state-init` - Passa a função para useState para valores caros
- `rerender-transitions` - Use startTransition para atualizações não urgentes

### 6. Desempenho de renderização (MÉDIO)

- `rendering-animate-svg-wrapper` - Anima o wrapper div, não o elemento SVG
- `rendering-content-visibility` - Use content-visibility para listas longas
- `rendering-hoist-jsx` - Extrai componentes JSX estáticos externos
- `rendering-svg-precision` - Reduz a precisão das coordenadas SVG
- `rendering-hydration-no-flicker` - Use script embutido para dados somente do cliente
- `rendering-activity` - Use o componente Activity para mostrar/ocultar
- `rendering-conditional-render` - Use ternário, não && para condicionais

### 7. Desempenho de JavaScript (BAIXO-MÉDIO)

- `js-batch-dom-css` - Agrupe alterações de CSS via classes ou cssText
- `js-index-maps` - Construa mapa para pesquisas repetidas
- `js-cache-property-access` - Armazena propriedades do objeto em cache em loops
- `js-cache-function-results` - Resultados da função de cache no mapa em nível de módulo
- `js-cache-storage` - Leituras de cache localStorage/sessionStorage
- `js-combine-iterations` - Combine vários filtros/mapas em um loop
- `js-length-check-first` - Verifique o comprimento do array antes de uma comparação cara
- `js-early-exit` - Retorna antecipadamente das funções
- `js-hoist-regexp` - Criação de RegExp do Hoist fora dos loops
- `js-min-max-loop` - Use loop para min/max em vez de classificação
- `js-set-map-lookups` - Use Set/Map para pesquisas O(1)
- `js-tosorted-immutable` - Use toSorted() para imutabilidade

### 8. Padrões avançados (BAIXO)

- `advanced-event-handler-refs` - Armazena manipuladores de eventos em refs
- `advanced-use-latest` - useLatest para referências de retorno de chamada estáveis

## Como usar

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
rules/_sections.md
```

Leia arquivos de regras individuais para obter explicações detalhadas e exemplos de código:

Cada arquivo de regras contém:
- Breve explicação de por que isso é importante
- Exemplo de código incorreto com explicação
- Exemplo de código correto com explicação
- Contexto e referências adicionais

## Documento compilado completo

Para o guia completo com todas as regras expandidas: `AGENTS.md`