---
name: stitch-ui
description: Expert guide for creating effective prompts for Google Stitch AI UI design tool. Use when user wants to design UI/UX in Stitch, create app interfaces, generate mobile/web designs, or needs help crafting Stitch prompts. Covers prompt structure, specificity techniques, iteration strategies, and design-to-code workflows for Stitch by Google.
risk: safe
source: "self"
---

```
[Screen/Component Type] for [User/Context]

# Solicitação de design de UI do Stitch

Orientação especializada para criar prompts eficazes no Google Stitch, a ferramenta de design de IU com tecnologia de IA do Google Labs. Essa habilidade ajuda a criar prompts precisos e acionáveis ​​que geram designs de UI de alta qualidade para aplicativos da Web e móveis.

## O que é o Google Stitch?

Google Stitch é um gerador experimental de UI de IA desenvolvido com Gemini 2.5 Flash que transforma prompts de texto e referências visuais em designs de UI funcionais. Suporta:

- Geração de texto para UI a partir de prompts em linguagem natural
- Conversão de imagem para UI a partir de esboços, wireframes ou capturas de tela
- Fluxos de aplicativos multitelas e layouts responsivos
- Exportar para HTML/CSS, Figma e código
- Refinamento iterativo com variantes e anotações

## Princípios Básicos de Solicitação

### 1. Seja específico e detalhado

Prompts genéricos produzem resultados genéricos. Prompts específicos com requisitos claros produzem designs profissionais e personalizados.

**Indicação ruim:**
```
Crie um painel
```

**Prompt eficaz:**
```
Painel de controle do membro com grade de módulos do curso, barra de acompanhamento de progresso, 
e barra lateral do feed da comunidade usando tema roxo e layout baseado em cartão
```

**Por que funciona:** Especifica componentes (módulos, progresso, feed), estrutura de layout (grade, barra lateral), estilo visual (tema roxo, cartões) e contexto (painel de membros).

### 2. Defina estilo visual e tema

Sempre inclua esquemas de cores, estética de design e direção visual para evitar resultados genéricos de IA.

**Componentes a serem especificados:**
- Paleta de cores (cores primárias, cores de destaque)
- Estilo de design (minimalista, moderno, lúdico, profissional, glassmorphic)
- Preferências de tipografia (se houver)
- Espaçamento e densidade (compacto, espaçoso, equilibrado)

**Exemplo:**
```
Página de produto de comércio eletrônico com galeria de imagens principais, CTA adicionar ao carrinho, 
seção de comentários e carrossel de produtos relacionados. Use minimalista limpo 
design com detalhes em verde sábio e espaço em branco generoso.
```

### 3. Estruture claramente os fluxos de várias telas

Para aplicativos com várias telas, liste cada tela como marcadores antes da geração.

**Abordagem:**
```
Aplicativo de monitoramento de condicionamento físico com:
- Tela de integração com seleção de metas
- Painel inicial com estatísticas diárias e anéis de atividades
- Biblioteca de exercícios com filtros de categoria
- Tela de perfil com conquistas e configurações
```

Stitch pedirá confirmação antes de gerar várias telas, garantindo o alinhamento com sua visão.

### 4. Especifique a plataforma e o comportamento responsivo

Indique se o design é para celular, tablet, desktop ou web responsivo.

**Exemplos:**
```
Tela de login do aplicativo móvel (estilo iOS) com campos de e-mail/senha e botões de autenticação social

Página de destino responsiva que se adapta do celular (320px) ao desktop (1440px) 
com navegação dobrável
```

### 5. Incluir requisitos funcionais

Descreva elementos interativos, estados e fluxos de usuários para gerar designs mais completos.

**Elementos a serem especificados:**
- Ações de botão e CTAs
- Campos de formulário e validação
- Padrões de navegação
- Carregando estados
- Estados vazios
- Tratamento de erros

**Exemplo:**
```
Fluxo de checkout com:
- Resumo do carrinho com ajustadores de quantidade
- Formulário de endereço de entrega com validação
- Seleção da forma de pagamento (cartões, PayPal, Apple Pay)
- Confirmação do pedido com número de rastreamento
```

## Modelo de estrutura de prompt

Use este modelo para solicitações abrangentes:

Principais recursos:
- [Recurso 1 com detalhes específicos]
- [Recurso 2 com detalhes específicos]
- [Recurso 3 com detalhes específicos]

Estilo visual:
- [Esquema de cores]
- [Estética de design]
- [Abordagem de layout]

Plataforma: [Móvel/Web/Responsiva]
```

**Exemplo:**
```
Painel para plataforma de análise SaaS

Principais recursos:
- Principais cartões de métricas mostrando MRR, usuários ativos e taxa de rotatividade
- Gráfico de linhas para tendências de receita (últimos 30 dias)
- Feed de atividades recentes com ações do usuário
- Botões de ação rápida para relatórios e exportações

Estilo visual:
- Modo escuro com detalhes em gradiente azul/roxo
- Cartões glassmorphic modernos com sombras sutis
- Visualização de dados limpa com cores acessíveis

Plataforma: Web responsiva (primeiro desktop)
```

## Estratégias de iteração

### Refinar com anotações

Use o recurso "anotar para editar" do Stitch para fazer alterações direcionadas sem reescrever todo o prompt.

**Fluxo de trabalho:**
1. Gere o design inicial a partir do prompt
2. Anote elementos específicos que precisam de alterações
3. Descreva modificações em linguagem natural
4. Stitch atualiza apenas as áreas anotadas

**Exemplos de anotações:**
- "Aumente este botão e use a cor primária"
- "Adicione mais espaçamento entre esses cartões"
- "Altere para um layout horizontal"

### Gerar variantes

```
Generate 3 variants of this hero section:
1. Image-focused with minimal text
2. Text-heavy with supporting graphics
3. Video background with overlay content
```

```
SaaS landing page for [product name]

```
Food delivery app home screen

```
Admin dashboard for content management system

```
Multi-step signup form for B2B platform

---

---

Solicite diversas variações para explorar diferentes direções de design:

### Refinamento Progressivo

Comece de forma ampla e, em seguida, adicione especificidade nas instruções de acompanhamento:

**Inicial:**
```
Página inicial de comércio eletrônico
```

**Refinamento 1:**
```
Adicione seção de produtos em destaque com grade de 4 colunas e efeitos de foco
```

**Refinamento 2:**
```
Atualize o esquema de cores para tons terrosos (terracota, sálvia, creme) 
e adicione banner promocional na parte superior
```

## Casos de uso comuns

### Páginas de destino

Seções:
- Herói com título, subtítulo, CTA e captura de tela do produto
- Prova social com logotipos de clientes
- Grade de recursos (3 colunas) com ícones
- Carrossel de depoimentos
- Tabela de preços (3 níveis)
- FAQ acordeão
- Rodapé com links e inscrição na newsletter

Estilo: Moderno, profissional e de construção de confiança
Cores: Azul marinho primário, detalhes em azul claro, fundo branco
```

### Aplicativos móveis

Componentes:
- Barra de pesquisa com seletor de localização
- Categoria de chips (Pizza, Hambúrgueres, Sushi, etc.)
- Cartões de restaurante com imagem, nome, classificação, prazo de entrega e faixa de preço
- Navegação inferior (Início, Pesquisa, Pedidos, Perfil)

Estilo: Vibrante, atraente, fácil de digitalizar
Cores: primário laranja, fundo branco, fotografia de alimentos
Plataforma: iOS móvel (largura de 375px)
```

### Painéis

Disposição:
- Navegação na barra lateral esquerda com menu recolhível
- Barra superior com pesquisa, notificações e perfil do usuário
- Área de conteúdo principal com:
  - Visão geral das estatísticas (4 cartões métricos)
  - Tabela de postagens recentes com ações
  - Cronograma de atividades
  - Painel de ações rápidas

Estilo: Limpo, focado em dados, profissional
Cores: Cinzas neutros com detalhes em azul
Plataforma: Web para desktop (1440px)
```

### Formulários e entradas

Etapas:
1. Dados da conta (nome da empresa, email, senha)
2. Informações da empresa (setor, tamanho, função)
3. Configuração da equipe (convidar membros)
4. Confirmação com mensagem de sucesso

Recursos:
- Indicador de progresso no topo
- Validação de campo com erros inline
- Navegação Voltar/Próxima
- Opção de pular para a etapa 3

Estilo: Mínimo, focado, baixo atrito
Cores: fundo branco, verde para estados de sucesso
```

## Fluxo de trabalho do design ao código

### Opções de exportação

Stitch oferece vários formatos de exportação:

1. **HTML/CSS** – Marcação limpa e semântica para projetos web
2. **Figma** - "Colar no Figma" para integração do sistema de design
3. **Snippets de código** – Exportações em nível de componente para estruturas

### Melhores Práticas para Exportação

**Antes de exportar:**
- Verifique pontos de interrupção responsivos
- Verifique o contraste das cores para acessibilidade
- Garantir que os estados interativos sejam definidos
- Revise a nomenclatura e estrutura dos componentes

**Após exportação:**
- Refatorar código gerado para padrões de produção
- Adicione tags HTML semânticas adequadas
- Implementar atributos de acessibilidade (rótulos ARIA, texto alternativo)
- Otimize imagens e ativos
- Adicione animações e microinterações

## Antipadrões a serem evitados

### ❌ Prompts Vagos
```
Faça um site legal
```

### ✅ Solicitações específicas
```
Site de portfólio para fotógrafo com galeria de imagens em tela cheia, 
estudos de caso do projeto e formulário de contato. Preto e branco minimalista 
estética com tipografia serifada.
```

### ❌ Contexto ausente
```
Crie uma página de login
```

### ✅ Prompts ricos em contexto
```
Página de login do portal de saúde com campos de e-mail/senha, 
Caixa de seleção "Lembrar-me", link "Esqueci a senha" e opções de SSO 
(Google,Microsoft). Design profissional e confiável com 
tema médico azul.
```

### ❌ Sem direção visual
```
Projete um aplicativo para gerenciamento de tarefas
```

### ✅ Direção visual clara
```
Aplicativo de gerenciamento de tarefas com layout de quadro kanban, cartões de arrastar e soltar, 
rótulos de prioridade e indicadores de data de vencimento. Moderno e focado na produtividade 
design com detalhes em gradiente roxo/verde-azulado e suporte ao modo escuro.
```

## Dicas para melhores resultados

1. **Referência a designs existentes** - Faça upload de capturas de tela ou esboços como referências visuais junto com instruções de texto

2. **Use a terminologia de design** - Termos como "seção herói", "layout de cartão", "mórfico de vidro", "grade bento" ajudam Stitch a entender sua intenção

3. **Especifique interações** – Descreva estados de foco, ações de clique e transições para designs mais completos

4. **Pense em componentes** - Divida telas complexas em componentes reutilizáveis (cabeçalho, cartão, formulário, etc.)

5. **Iterar de forma incremental** – Faça alterações pequenas e focadas em vez de reformulações completas

6. **Teste a capacidade de resposta** - Sempre verifique os designs em vários pontos de interrupção (celular, tablet, desktop)

7. **Considere a acessibilidade** - Mencione contraste de cores, tamanhos de fonte e tamanhos de alvo de toque nos prompts

8. **Aproveitar variantes** - Gere diversas opções para explorar diferentes direções de design rapidamente

## Integração com fluxo de trabalho de desenvolvimento

### Ponto → Figma → Código
1. Gere UI no Stitch com prompts detalhados
2. Exporte para Figma para integração do sistema de design
3. Entregue aos desenvolvedores as especificações de design
4. Implemente com código pronto para produção

### Costura → HTML → Estrutura
1. Gere e refine a UI no Stitch
2. Exporte código HTML/CSS
3. Converter para componentes React/Vue/Svelte
4. Integre-se à base de código do aplicativo

### Prototipagem Rápida
1. Crie múltiplas variações de tela rapidamente
2. Teste com usuários ou partes interessadas
3. Iterar com base no feedback
4. Finalize o design para desenvolvimento

## Conclusão

Os prompts eficazes do Stitch são específicos, ricos em contexto e visualmente descritivos. Seguindo esses princípios e modelos, você pode gerar designs de UI profissionais que servem como bases sólidas para aplicativos de produção.

**Lembre-se:** O ponto é um ponto de partida, não um produto final. Use-o para acelerar o processo de design, explorar ideias rapidamente e estabelecer uma direção visual e, em seguida, refinar com julgamento humano e padrões de produção.