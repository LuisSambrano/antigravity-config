---
name: content-creator
description: Create SEO-optimized marketing content with consistent brand voice. Includes brand voice analyzer, SEO optimizer, content frameworks, and social media templates. Use when writing blog posts, creating social media content, analyzing brand voice, optimizing SEO, planning content calendars, or when user mentions content creation, brand voice, SEO optimization, social media marketing, or content strategy.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  domain: content-marketing
  updated: 2025-10-20
  python-tools: brand_voice_analyzer.py, seo_optimizer.py
  tech-stack: SEO, social-media-platforms
---

# Criador de conteúdo

Análise de voz de marca de nível profissional, otimização de SEO e estruturas de conteúdo específicas de plataforma.

## Palavras-chave
criação de conteúdo, postagens de blog, SEO, voz da marca, mídia social, calendário de conteúdo, conteúdo de marketing, estratégia de conteúdo, marketing de conteúdo, consistência de marca, otimização de conteúdo, marketing de mídia social, planejamento de conteúdo, redação de blog, estruturas de conteúdo, diretrizes de marca, estratégia de mídia social

## Início rápido

### Para desenvolvimento de voz de marca
1. Execute `scripts/brand_voice_analyzer.py` no conteúdo existente para estabelecer a linha de base
2. Revise `references/brand_guidelines.md` para selecionar atributos de voz
3. Aplique a voz escolhida de forma consistente em todo o conteúdo

### Para criação de conteúdo de blog
1. Escolha o modelo em `references/content_frameworks.md`
2. Pesquise palavras-chave para o tópico
3. Escreva o conteúdo seguindo a estrutura do modelo
4. Execute `scripts/seo_optimizer.py [arquivo] [palavra-chave primária]` para otimizar
5. Aplique recomendações antes de publicar

### Para conteúdo de mídia social
1. Revise as práticas recomendadas da plataforma em `references/social_media_optimization.md`
2. Use o modelo apropriado de `references/content_frameworks.md`
3. Otimize com base nas diretrizes específicas da plataforma
4. Agende usando `assets/content_calendar_template.md`

## Fluxos de trabalho principais

### Estabelecendo a voz da marca (configuração inicial)

Ao criar conteúdo para uma nova marca ou cliente:

1. **Analise o conteúdo existente** (se disponível)
   ```bash
   scripts python/brand_voice_analyzer.py existente_content.txt
   ```
   
2. **Definir atributos de voz**
   - Revise os arquétipos de personalidade da marca em `references/brand_guidelines.md`
   - Selecione arquétipos primários e secundários
   - Escolha 3-5 atributos de tom
   - Documento nas diretrizes da marca

3. **Criar amostra de voz**
   - Escreva 3 peças de amostra na voz escolhida
   - Teste a consistência usando o analisador
   - Refinar com base nos resultados

### Criação de postagens de blog otimizadas para SEO

1. **Pesquisa de palavras-chave**
   - Identifique a palavra-chave primária (volume de pesquisa 500-5000/mês)
   - Encontre de 3 a 5 palavras-chave secundárias
   - Liste de 10 a 15 palavras-chave LSI

2. **Estrutura de conteúdo**
   - Use o modelo de blog de `references/content_frameworks.md`
   - Incluir palavra-chave no título, primeiro parágrafo e 2-3 H2s
   - Procure usar de 1.500 a 2.500 palavras para uma cobertura abrangente

3. **Verificação de otimização**
   ```bash
   scripts python/seo_optimizer.py blog_post.md "palavra-chave primária" "secundária, palavras-chave, lista"
   ```

4. **Aplique recomendações de SEO**
   - Ajuste a densidade de palavras-chave para 1-3%
   - Garantir uma estrutura de cabeçalho adequada
   - Adicione links internos e externos
   - Otimize a meta descrição

### Criação de conteúdo de mídia social

1. **Seleção de plataforma**
   - Identifique plataformas primárias com base no público
   - Revise as diretrizes específicas da plataforma em `references/social_media_optimization.md`

2. **Adaptação de Conteúdo**
   - Comece com uma postagem no blog ou mensagem principal
   - Use a matriz de reaproveitamento de `references/content_frameworks.md`
   - Adapte-se para cada plataforma seguindo modelos

3. **Lista de verificação de otimização**
   - Comprimento adequado à plataforma
   - Tempo ideal de postagem
   - Dimensões corretas da imagem
   - Hashtags específicas da plataforma
   - Elementos de engajamento (enquetes, perguntas)

### Planejamento de calendário de conteúdo

1. **Planejamento Mensal**
   - Copie `assets/content_calendar_template.md`
   - Definir metas mensais e KPIs
   - Identificar as principais campanhas/temas

2. **Distribuição Semanal**
   - Siga a proporção do pilar de conteúdo 40/25/25/10
   - Equilibre plataformas ao longo da semana
   - Alinhe-se com os horários de postagem ideais

3. **Criação em lote**
   - Crie todo o conteúdo semanal em uma sessão
   - Mantenha uma voz consistente em todas as peças
   - Prepare todos os recursos visuais juntos

## Scripts-chave

### brand_voice_analyzer.py
Analisa o conteúdo do texto quanto a características de voz, legibilidade e consistência.

**Uso**: `scripts python/brand_voice_analyzer.py <arquivo> [json|texto]`

**Retornos**:
- Perfil de voz (formalidade, tom, perspectiva)
- Pontuação de legibilidade
- Análise da estrutura das frases
- Recomendações de melhoria

### seo_optimizer.py
Analisa conteúdo para otimização de SEO e fornece recomendações práticas.

**Uso**: `python scripts/seo_optimizer.py <arquivo> [palavra-chave_primária] [palavras-chave_secundárias]`

**Retornos**:
- Pontuação de SEO (0-100)
- Análise de densidade de palavras-chave
- Avaliação da estrutura
- Sugestões de meta tags
- Recomendações específicas de otimização

## Guias de referência

### Quando usar cada referência

```bash
# Analyze brand voice
python scripts/brand_voice_analyzer.py content.txt

**referências/brand_guidelines.md**
- Configurando a nova voz da marca
- Garantir consistência em todo o conteúdo
- Treinamento de novos membros da equipe
- Resolução de questões de voz/tom

**referências/content_frameworks.md**
- Iniciando qualquer novo conteúdo
- Estruturação de diferentes tipos de conteúdo
- Criação de modelos de conteúdo
- Planejamento de reaproveitamento de conteúdo

**referências/social_media_optimization.md**
- Otimização específica da plataforma
- Desenvolvimento de estratégia de hashtag
- Compreender os fatores do algoritmo
- Configurando o rastreamento analítico

## Melhores práticas

### Processo de criação de conteúdo
1. Sempre comece com a necessidade/ponto problemático do público
2. Pesquise antes de escrever
3. Crie um esboço usando modelos
4. Escreva o primeiro rascunho sem editar
5. Otimize para SEO
6. Edite a voz da marca
7. Revise e verifique os fatos
8. Otimize para plataforma
9. Agende estrategicamente

### Indicadores de Qualidade
- Pontuação de SEO acima de 75/100
- Legibilidade apropriada para o público
- Voz consistente da marca em todo o processo
- Proposta de valor clara
- Conclusões acionáveis
- Formatação visual adequada
- Otimizado para plataforma

### Armadilhas comuns a serem evitadas
- Escrever antes de pesquisar palavras-chave
- Ignorar requisitos específicos da plataforma
- Voz da marca inconsistente
- Otimização excessiva para SEO (recheio de palavras-chave)
- Faltam CTAs claros
- Publicação sem revisão
- Ignorando o feedback analítico

## Métricas de desempenho

Acompanhe estes KPIs para sucesso de conteúdo:

### Métricas de conteúdo
- Crescimento orgânico do tráfego
- Tempo médio na página
- Taxa de rejeição
- Compartilhamentos sociais
- Backlinks ganhos

### Métricas de engajamento
- Comentários e discussões
- Taxas de cliques de e-mail
- Taxa de engajamento nas redes sociais
- Downloads de conteúdo
- Envios de formulários

### Métricas de negócios
- Leads gerados
- Taxa de conversão
- Custo de aquisição de clientes
- Atribuição de receita
- ROI por conteúdo

## Pontos de Integração

Esta habilidade funciona melhor com:
- Plataformas analíticas (Google Analytics, insights de mídia social)
- Ferramentas de SEO (para pesquisa de palavras-chave)
- Ferramentas de design (para conteúdo visual)
- Plataformas de agendamento (para distribuição de conteúdo)
- Sistemas de email marketing (para conteúdo de newsletter)

## Comandos rápidos

# Otimize para SEO
scripts python/seo_optimizer.py artigo.md "palavra-chave principal"

# Verifique o conteúdo de acordo com as diretrizes da marca
grep -f referências/brand_guidelines.md content.txt

# Crie um calendário mensal
cp assets/content_calendar_template.md this_month_calendar.md
```