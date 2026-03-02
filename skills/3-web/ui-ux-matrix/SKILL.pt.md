---
name: ui-ux-matrix
description: "Diagnostic matrix for UI/UX compliance. Validates web/mobile structures against 50+ stylistic rules, color contrast thresholds, interaction feedback loops, and framework-specific patterns."
---

---

```bash
python3 --version || python --version
```

```bash
brew install python3
```

```bash
sudo apt update && sudo apt install python3
```

```powershell
winget install Python.Python.3.12
```

---

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

# UI/UX Pro Max - Inteligência de Design

Guia de design abrangente para aplicativos web e móveis. Contém mais de 50 estilos, 97 paletas de cores, 57 combinações de fontes, 99 diretrizes de UX e 25 tipos de gráficos em 9 pilhas de tecnologia. Banco de dados pesquisável com recomendações baseadas em prioridades.

## Quando aplicar

Consulte estas diretrizes quando:

- Projetar novos componentes ou páginas de UI
- Escolha de paletas de cores e tipografia
- Revisão de código para problemas de UX
- Criação de landing pages ou dashboards
- Implementação de requisitos de acessibilidade

## Categorias de regras por prioridade

| Prioridade | Categoria | Impacto | Domínio |
| -------- | ------------------- | -------- | --------------------- |
| 1 | Acessibilidade | CRÍTICO | `ux` |
| 2 | Toque e interação | CRÍTICO | `ux` |
| 3 | Desempenho | ALTO | `ux` |
| 4 | Layout e responsivo | ALTO | `ux` |
| 5 | Tipografia e Cor | MÉDIO | `tipografia`, `cor` |
| 6 | Animação | MÉDIO | `ux` |
| 7 | Seleção de estilo | MÉDIO | `estilo`, `produto` |
| 8 | Gráficos e dados | BAIXO | `gráfico` |

## Referência rápida

### 1. Acessibilidade (CRÍTICO)

- `color-contrast` - Proporção mínima de 4,5:1 para texto normal
- `focus-states` - Anéis de foco visíveis em elementos interativos
- `alt-text` - Texto alternativo descritivo para imagens significativas
- `aria-labels` - aria-label para botões somente de ícone
- `keyboard-nav` - A ordem das guias corresponde à ordem visual
- `form-labels` - Use o rótulo com o atributo for

### 2. Toque e interação (CRÍTICO)

- `touch-target-size` - Alvos de toque mínimos de 44x44px
- `hover-vs-tap` - Use clique/toque para interações primárias
- `loading-buttons` - Desativa o botão durante operações assíncronas
- `error-feedback` - Limpa mensagens de erro próximas ao problema
- `cursor-pointer` - Adicione o ponteiro do cursor aos elementos clicáveis

### 3. Desempenho (ALTO)

- `otimização de imagem` - Use WebP, srcset, carregamento lento
- `movimento reduzido` - Marque prefere movimento reduzido
- `content-jumping` - Reserve espaço para conteúdo assíncrono

### 4. Layout e responsivo (ALTO)

- `viewport-meta` - largura = largura do dispositivo escala inicial = 1
- `readable-font-size` - Corpo de texto mínimo de 16px no celular
- `horizontal-scroll` - Certifique-se de que o conteúdo se ajuste à largura da janela de visualização
- `z-index-management` - Definir escala do índice z (10, 20, 30, 50)

### 5. Tipografia e cores (MÉDIO)

- `line-height` - Use 1,5-1,75 para o corpo do texto
- `line-length` - Limite de 65 a 75 caracteres por linha
- `font-pairing` - Corresponde às personalidades da fonte do título/corpo

### 6. Animação (MÉDIO)

- `duration-timing` - Use 150-300ms para microinterações
- `transform-performance` - Use transformação/opacidade, não largura/altura
- `loading-states` - Telas esqueleto ou spinners

### 7. Seleção de estilo (MÉDIO)

- `style-match` - Combina o estilo com o tipo de produto
- `consistência` - Use o mesmo estilo em todas as páginas
- `no-emoji-icons` - Use ícones SVG, não emojis

### 8. Gráficos e dados (BAIXO)

- `chart-type` - Combina o tipo de gráfico com o tipo de dados
- `color-guidance` - Use paletas de cores acessíveis
- `data-table` - Fornece alternativa de tabela para acessibilidade

## Como usar

Pesquise domínios específicos usando a ferramenta CLI abaixo.

## Pré-requisitos

Verifique se o Python está instalado:

Se o Python não estiver instalado, instale-o com base no sistema operacional do usuário:

**macOS:**

**Ubuntu/Debian:**

**Janelas:**

## Como usar esta habilidade

Quando o usuário solicitar trabalho de UI/UX (projetar, construir, criar, implementar, revisar, corrigir, melhorar), siga este fluxo de trabalho:

### Etapa 1: analisar os requisitos do usuário

Extraia informações importantes da solicitação do usuário:

- **Tipo de produto**: SaaS, e-commerce, portfólio, dashboard, landing page, etc.
- **Palavras-chave de estilo**: mínimo, divertido, profissional, elegante, modo escuro, etc.
- **Indústria**: saúde, fintech, jogos, educação, etc.
- **Stack**: React, Vue, Next.js ou padrão para `html-tailwind`

### Etapa 2: Gerar Sistema de Design (OBRIGATÓRIO)

**Sempre comece com `--design-system`** para obter recomendações abrangentes com raciocínio:

Este comando:

1. Pesquisa 5 domínios em paralelo (produto, estilo, cor, destino, tipografia)
2. Aplica regras de raciocínio de `ui-reasoning.csv` para selecionar as melhores correspondências
3. Retorna sistema de design completo: padrão, estilo, cores, tipografia, efeitos
4. Inclui antipadrões para evitar

**Exemplo:**

### Etapa 3: Suplemento com pesquisas detalhadas (conforme necessário)

Depois de obter o sistema de design, use pesquisas de domínio para obter detalhes adicionais:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

---

---

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

```bash
# Get UX guidelines for animation and accessibility
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
```

---

```bash
# ASCII box (default) - best for terminal display
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

---

**Quando usar pesquisas detalhadas:**

| Necessidade | Domínio | Exemplo |
| --------------------- | ------------ | --------------------------------------- |
| Mais opções de estilo | `estilo` | `--estilo de domínio "glassmorphism dark"` |
| Recomendações gráficas | `gráfico` | `--gráfico de domínio "painel em tempo real"` |
| Melhores práticas de experiência do usuário | `ux` | `--domain ux "acessibilidade de animação"` |
| Fontes alternativas | `tipografia` | `--domain tipografia "luxo elegante"` |
| Estrutura de pouso | `pouso` | `--domain landing "hero social-proof"` |

### Etapa 4: Diretrizes de pilha (padrão: html-tailwind)

Obtenha práticas recomendadas específicas de implementação. Se o usuário não especificar uma pilha, **o padrão é `html-tailwind`**.

Pilhas disponíveis: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

## Referência de pesquisa

### Domínios Disponíveis

| Domínio | Usar para | Exemplos de palavras-chave |
| ------------ | ------------------------------------ | ----------------------------------------------------------------------- |
| `produto` | Recomendações de tipo de produto | SaaS, e-commerce, portfólio, saúde, beleza, serviços |
| `estilo` | Estilos, cores e efeitos da interface do usuário | morfismo de vidro, minimalismo, modo escuro, brutalismo |
| `tipografia` | Pareamentos de fontes, Google Fonts | elegante, lúdico, profissional, moderno |
| `cor` | Paletas de cores por tipo de produto | saas, comércio eletrônico, saúde, beleza, fintech, serviços |
| `pouso` | Estrutura da página, estratégias de CTA | herói, centrado no herói, depoimento, preços, prova social |
| `gráfico` | Tipos de gráficos, recomendações de biblioteca | tendência, comparação, linha do tempo, funil, torta |
| `ux` | Melhores práticas, antipadrões | animação, acessibilidade, índice z, carregamento |
| `reagir` | Desempenho do React/Next.js | cachoeira, pacote, suspense, memorando, renderização, cache |
| `web` | Diretrizes para interface web | ária, foco, teclado, semântica, virtualização |
| `aviso` | Solicitações de IA, palavras-chave CSS | (nome do estilo) |

### Pilhas disponíveis

| Pilha | Foco |
| --------------- | -------------------------------------------------------- |
| `html-tailwind` | Utilitários Tailwind, responsivos, a11y (PADRÃO) |
| `reagir` | Estado, ganchos, desempenho, padrões |
| `nextjs` | SSR, roteamento, imagens, rotas API |
| `vue` | API de composição, Pinia, roteador Vue |
| `esbelto` | Runas, lojas, SvelteKit |
| `Swiftui` | Visualizações, Estado, Navegação, Animação |
| `react-nativo` | Componentes, Navegação, Listas |
| `vibração` | Widgets, Estado, Layout, Temas |
| `shadcn` | componentes shadcn/ui, temas, formulários, padrões |

## Exemplo de fluxo de trabalho

**Solicitação do usuário:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

### Etapa 1: Analisar Requisitos

Tipo de produto: Serviço de beleza/spa
- Palavras-chave de estilo: elegante, profissional, suave
- Indústria: Beleza/Bem-Estar
- Pilha: html-tailwind (padrão)

### Etapa 2: Gerar Sistema de Design (OBRIGATÓRIO)

**Resultado:** Sistema de design completo com padrão, estilo, cores, tipografia, efeitos e antipadrões.

### Etapa 3: Suplemento com pesquisas detalhadas (conforme necessário)

# Obtenha opções alternativas de tipografia, se necessário
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "serif de luxo elegante" - tipografia de domínio
```

### Etapa 4: Diretrizes de pilha

**Então:** Sintetize o sistema de design + pesquisas detalhadas e implemente o design.

## Formatos de saída

O sinalizador `--design-system` suporta dois formatos de saída:

# Markdown – melhor para documentação
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "criptografia fintech" --design-system -f markdown
```

## Dicas para melhores resultados

---

---

1. **Seja específico com palavras-chave** - "painel SaaS de saúde" > "aplicativo"
2. **Pesquise várias vezes** – Palavras-chave diferentes revelam insights diferentes
3. **Combinar domínios** - Estilo + Tipografia + Cor = Sistema de design completo
4. **Sempre verifique a UX** - Pesquise "animação", "z-index", "acessibilidade" para problemas comuns
5. **Usar sinalizador de pilha** – Obtenha práticas recomendadas específicas de implementação
6. **Iterar** - Se a primeira pesquisa não corresponder, tente palavras-chave diferentes

## Regras comuns para UI profissional

Esses são problemas frequentemente esquecidos que fazem a IU parecer pouco profissional:

### Ícones e elementos visuais

| Regra | Faça | Não |
| -------------------------- | ---------------------------------------------------------- | -------------------------------------- |
| **Sem ícones de emoji** | Use ícones SVG (Heroicons, Lucide, Simple Icons) | Use emojis como 🎨 🚀 ⚙️ como ícones da interface do usuário |
| **Estados de foco estáveis** | Use transições de cor/opacidade ao passar o mouse | Use transformações de escala que mudam o layout |
| **Logotipos de marca corretos** | Pesquise SVG oficial da Simple Icons | Adivinhe ou use caminhos de logotipo incorretos |
| **Dimensionamento consistente de ícones** | Utilize viewBox fixa (24x24) com w-6 h-6 | Misture diferentes tamanhos de ícones aleatoriamente |

### Interação e Cursor

| Regra | Faça | Não |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------- |
| **Ponteiro do cursor** | Adicione `ponteiro de cursor` a todos os cartões clicáveis/flutuantes | Deixar o cursor padrão nos elementos interativos |
| **Comentários ao passar o mouse** | Fornece feedback visual (cor, sombra, borda) | Nenhum elemento de indicação é interativo |
| **Transições suaves** | Use `duração das cores de transição-200` | Mudanças instantâneas de estado ou muito lentas (>500ms) |

### Contraste do modo claro/escuro

| Regra | Faça | Não |
| ------------------------- | ----------------------------------- | --------------------------------------- |
| **Modo de luz do cartão de vidro** | Use `bg-white/80` ou opacidade superior | Use `bg-white/10` (muito transparente) |
| **Luz de contraste de texto** | Use `#0F172A` (slate-900) para texto | Use `#94A3B8` (slate-400) para o corpo do texto |
| **Luz de texto silenciada** | Use `#475569` (slate-600) no mínimo | Use cinza-400 ou mais claro |
| **Visibilidade da fronteira** | Use `border-gray-200` no modo claro | Use `border-white/10` (invisível) |

### Layout e espaçamento

| Regra | Faça | Não |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| **Barra de navegação flutuante** | Adicionar espaçamento `top-4 left-4 right-4` | Cole a barra de navegação em `top-0 left-0 right-0` |
| **Preenchimento de conteúdo** | Conta para altura fixa da barra de navegação | Deixe o conteúdo se esconder atrás de elementos fixos |
| **Largura máxima consistente** | Use o mesmo `max-w-6xl` ou `max-w-7xl` | Misture diferentes larguras de recipientes |

## Lista de verificação de pré-entrega

Antes de entregar o código da IU, verifique estes itens:

### Qualidade Visual

- [] Nenhum emojis usado como ícones (use SVG)
- [] Todos os ícones do conjunto de ícones consistente (Heroicons/Lucide)
- [] Os logotipos das marcas estão corretos (verificados em Simple Icons)
- [] Os estados de foco não causam mudança de layout
- [] Use as cores do tema diretamente (bg-primary) e não o wrapper var()

### Interação

- [] Todos os elementos clicáveis possuem `ponteiro de cursor`
- [] Os estados de foco fornecem feedback visual claro
- [] As transições são suaves (150-300ms)
- [] Estados de foco visíveis para navegação pelo teclado

### Modo claro/escuro

- [] O texto no modo claro tem contraste suficiente (mínimo de 4,5:1)
- [] Elementos de vidro/transparentes visíveis no modo claro
- [] Bordas visíveis em ambos os modos
- [] Teste ambos os modos antes da entrega

###Layout

- [] Os elementos flutuantes têm espaçamento adequado das bordas
- [] Nenhum conteúdo oculto atrás de barras de navegação fixas
- [] Responsivo em 375px, 768px, 1024px, 1440px
- [] Sem rolagem horizontal no celular

### Acessibilidade

- [] Todas as imagens possuem texto alternativo
- [] As entradas do formulário possuem rótulos
- [] A cor não é o único indicador
- [] `prefere movimento reduzido` respeitado