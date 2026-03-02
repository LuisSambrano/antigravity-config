---
name: vercel-rn
description:
  React Native and Expo best practices for building performant mobile apps. Use
  when building React Native components, optimizing list performance,
  implementing animations, or working with native modules. Triggers on tasks
  involving React Native, Expo, mobile performance, or native platform APIs.
license: MIT
metadata:
  author: vercel
  version: '1.0.0'
---

```
rules/list-performance-virtualize.md
rules/animation-gpu-properties.md
```

# Reagir habilidades nativas

Práticas recomendadas abrangentes para aplicativos React Native e Expo. Contém
regras em várias categorias, abrangendo desempenho, animações, padrões de UI,
e otimizações específicas da plataforma.

## Quando aplicar

Consulte estas diretrizes quando:

- Criação de aplicativos React Native ou Expo
- Otimizando lista e desempenho de rolagem
- Implementação de animações com Reanimated
- Trabalhar com imagens e mídias
- Configurando módulos ou fontes nativas
- Estruturação de projetos monorepo com dependências nativas

## Categorias de regras por prioridade

| Prioridade | Categoria | Impacto | Prefixo |
| -------- | ---------------- | -------- | -------------------- |
| 1 | Desempenho da lista | CRÍTICO | `lista-desempenho-` |
| 2 | Animação | ALTO | `animação-` |
| 3 | Navegação | ALTO | `navegação-` |
| 4 | Padrões de IU | ALTO | `ui-` |
| 5 | Gestão Estadual | MÉDIO | `reagir-estado-` |
| 6 | Renderização | MÉDIO | `renderização-` |
| 7 | Monorepo | MÉDIO | `monorepo-` |
| 8 | Configuração | BAIXO | `fontes-`, `importações-` |

## Referência rápida

### 1. Desempenho da lista (CRÍTICO)

- `list-performance-virtualize` - Use FlashList para listas grandes
- `list-performance-item-memo` - Memoriza os componentes do item da lista
- `list-performance-callbacks` - Estabiliza referências de retorno de chamada
- `list-performance-inline-objects` - Evite objetos de estilo inline
- `list-performance-function-references` - Extrai funções fora da renderização
- `list-performance-images` - Otimize imagens em listas
- `list-performance-item-expensive` - Mover trabalhos caros para fora dos itens
- `list-performance-item-types` - Use tipos de itens para listas heterogêneas

### 2. Animação (ALTA)

- `animation-gpu-properties` - Anima apenas transformação e opacidade
- `animation-derived-value` - Use useDerivedValue para animações computadas
- `animation-gesture-detector-press` - Use Gesture.Tap em vez de Pressable

### 3. Navegação (ALTA)

- `navigation-native-navigators` - Use pilha nativa e guias nativas em navegadores JS

### 4. Padrões de UI (ALTO)

- `ui-expo-image` - Use expo-image para todas as imagens
- `ui-image-gallery` - Use a Galeria para lightboxes de imagens
- `ui-pressable` - Use Pressable sobre TouchableOpacity
- `ui-safe-area-scroll` - Manipula áreas seguras em ScrollViews
- `ui-scrollview-content-inset` - Use contentInset para cabeçalhos
- `ui-menus` - Use menus de contexto nativos
- `ui-native-modals` - Use modais nativos quando possível
- `ui-measure-views` - Use onLayout, não Measure()
- `ui-styling` - Use StyleSheet.create ou Nativewind

### 5. Gestão de Estado (MÉDIO)

- `react-state-minimize` - Minimiza assinaturas de estado
- `react-state-dispatcher` - Use o padrão do despachante para retornos de chamada
- `react-state-fallback` - Mostra substituto na primeira renderização
- `react-compiler-destructure-functions` - Deestrutura para React Compiler
- `react-compiler-reanimated-shared-values` - Manipula valores compartilhados com o compilador

### 6. Renderização (MÉDIO)

- `rendering-text-in-text-component` - Quebrar texto em componentes de texto
- `rendering-no-falsy-and` - Evite falsy && para renderização condicional

### 7. Monorepo (MÉDIO)

- `monorepo-native-deps-in-app` - Mantenha as dependências nativas no pacote do aplicativo
- `monorepo-single-dependency-versions` - Use versões únicas entre pacotes

### 8. Configuração (BAIXA)

- `fonts-config-plugin` - Use plugins de configuração para fontes personalizadas
- `imports-design-system-folder` - Organizar importações do sistema de design
- `js-hoist-intl` - Criação de objeto Hoist Intl

## Como usar

Leia arquivos de regras individuais para obter explicações detalhadas e exemplos de código:

Cada arquivo de regras contém:

- Breve explicação de por que isso é importante
- Exemplo de código incorreto com explicação
- Exemplo de código correto com explicação
- Contexto e referências adicionais

## Documento compilado completo

Para o guia completo com todas as regras expandidas: `AGENTS.md`