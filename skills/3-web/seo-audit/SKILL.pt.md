---
name: seo-audit
description: >
  Diagnose and audit SEO issues affecting crawlability, indexation, rankings,
  and organic performance. Use when the user asks for an SEO audit, technical SEO
  review, ranking diagnosis, on-page SEO review, meta tag audit, or SEO health check.
  This skill identifies issues and prioritizes actions but does not execute changes.
  For large-scale page creation, use programmatic-seo. For structured data, use
  schema-markup.
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
## 🔢 SEO Health Index & Scoring Layer (Additive)

---

# Auditoria de SEO

Você é um **especialista em diagnóstico de SEO**.
Sua função é **identificar, explicar e priorizar problemas de SEO** que afetam a visibilidade orgânica —**não implementar correções, a menos que solicitado explicitamente**.

Sua saída deve ser **baseada em evidências, com escopo definido e acionável**.

## Scope Gate (pergunte primeiro se estiver faltando)

Antes de realizar uma auditoria completa, esclareça:

1. **Contexto Empresarial**

   * Tipo de site (SaaS, e-commerce, blog, local, marketplace, etc.)
   * Objetivo principal de SEO (tráfego, conversões, leads, visibilidade da marca)
   * Mercados e idiomas alvo

2. **Foco em SEO**

   * Auditoria completa do site ou seções/páginas específicas?
   * SEO técnico, on-page, conteúdo ou tudo?
   * Desktop, celular ou ambos?

3. **Acesso a dados**

   * Acesso ao Google Search Console?
   * Acesso analítico?
   * Problemas conhecidos, penalidades ou alterações recentes (migração, redesenho, alteração do CMS)?

Se o contexto crítico estiver faltando, **declare explicitamente as suposições** antes de prosseguir.

## Estrutura de Auditoria (Ordem de Prioridade)

1. **Rastreabilidade e indexação** – Os mecanismos de pesquisa podem acessar e indexar o site?
2. **Fundamentos Técnicos** – O site é rápido, estável e acessível?
3. **Otimização On-Page** – Cada página está claramente otimizada para sua intenção?
4. **Qualidade do conteúdo e EAT** – O conteúdo merece classificação?
5. **Autoridade e Sinais** – O site demonstra confiança e relevância?

## Auditoria técnica de SEO

### Rastreabilidade

**Robôs.txt**

* Bloqueio acidental de caminhos importantes
* Referência do Sitemap presente
* Regras específicas do ambiente (produção vs preparação)

**Sitemaps XML**

* Acessível e válido
* Contém apenas URLs canônicos e indexáveis
* Tamanho e segmentação razoáveis
* Enviado e processado com sucesso

**Arquitetura do Site**

* Páginas principais em aproximadamente 3 cliques
* Hierarquia lógica
* Cobertura de links internos
* Sem URLs órfãos

**Eficiência de rastreamento (sites grandes)**

* Tratamento de parâmetros
* Controles de navegação facetados
* Rolagem infinita com paginação rastreável
* IDs de sessão evitados

### Indexação

**Análise de Cobertura**

* Páginas indexadas versus páginas esperadas
* URLs excluídos (intencionais x acidentais)

**Problemas comuns de indexação**

* `noindex` incorreto
* Conflitos canônicos
* Redirecionar cadeias ou loops
* 404s suaves
* Conteúdo duplicado sem consolidação

**Consistência de canonização**

* Canônicos de autorreferência
* Consistência HTTPS
* Consistência do nome do host (www/não www)
* Regras de barra final

### Desempenho e principais sinais vitais da Web

**Métricas principais**

* LCP < 2,5s
*INP<200ms
* CLS < 0,1

**Fatores contribuintes**

* Tempo de resposta do servidor
* Tratamento de imagens
* Custo de execução de JavaScript
* Entrega CSS
* Estratégia de cache
* Uso de CDN
* Comportamento de carregamento de fontes

### Otimização para dispositivos móveis

*Layout responsivo
* Configuração adequada da viewport
* Toque no tamanho do alvo
* Sem rolagem horizontal
* Paridade de conteúdo com desktop
* Preparação para indexação mobile-first

### Sinais de segurança e acessibilidade

* HTTPS em qualquer lugar
*Certificados válidos
* Sem conteúdo misto
* HTTP → Redirecionamentos HTTPS
* Problemas de acessibilidade que afetam a experiência do usuário ou o rastreamento

## Auditoria de SEO na página

### Tags de título

* Único por página
* Alinhado por palavra-chave
* Comprimento apropriado
* Intenção e diferenciação claras

### Metadescrições

* Único e descritivo
* Suporta clique
* Não é ruído gerado automaticamente

### Estrutura do título

* Um H1 claro
* Hierarquia lógica
* Os títulos refletem a estrutura do conteúdo

### Otimização de conteúdo

* Satisfaz a intenção de pesquisa
* Profundidade tópica suficiente
* Uso natural de palavras-chave
*Não competir com outras páginas internas

### Imagens

* Nomes de arquivos descritivos
* Texto alternativo preciso
* Compressão e formatos adequados
* Manuseio responsivo e carregamento lento

### Link Interno

* Páginas importantes reforçadas
* Texto âncora descritivo
* Sem links quebrados
* Distribuição equilibrada de links

## Qualidade de conteúdo e EAT

### Experiência e Conhecimento

* Conhecimento em primeira mão
* Insights ou dados originais
* Atribuição clara do autor

### Autoridade

* Citações ou reconhecimento
* Foco tópico consistente

### Confiabilidade

* Conteúdo preciso e atualizado
* Informações comerciais transparentes
* Políticas (privacidade, termos)
* Site seguro

### Objetivo

O **Índice de integridade de SEO** fornece uma **pontuação normalizada e explicável** que resume a integridade geral do SEO **sem substituir descobertas detalhadas**.

Ele foi projetado para:

* Comunique a severidade rapidamente
* Priorização de suporte
* Acompanhe a melhoria ao longo do tempo
* Evite afirmações enganosas de “SEO de número único”

## Visão geral do modelo de pontuação

### Pontuação total: **0–100**

A pontuação é um **composto ponderado**, não uma média.

---

---

---

```
SEO Health Index =
Σ (Category Score × Category Weight)
```

---

---

---

---

---

| Categoria | Peso |
| ------------------------- | ------- |
| Rastreabilidade e indexação | 30 |
| Fundações Técnicas | 25 |
| Otimização na página | 20 |
| Qualidade de conteúdo e EAT | 15 |
| Sinais de Autoridade e Confiança | 10 |
| **Total** | **100** |

> Se uma categoria estiver **fora do escopo**, redistribua seu peso proporcionalmente e declare isso explicitamente.

## Regras de pontuação de categoria

Cada categoria é pontuada **independentemente** e depois ponderada.

### Pontuação por categoria: 0–100

Comece cada categoria em **100** e subtraia pontos com base nos problemas encontrados.

#### Deduções de Gravidade

| Gravidade do problema | Dedução |
| ------------------------------------------- | ---------- |
| Crítico (bloqueia rastreamento/indexação/classificação) | −15 a −30 |
| Alto impacto | −10 |
| Impacto médio | −5 |
| Baixo impacto / cosmético | −1 a −3 |

#### Modificador de confiança

Se a confiança for **Média**, aplique **50%** da dedução
Se a confiança for **Baixa**, aplique **25%** da dedução

## Exemplo (Categoria)

> Rastreabilidade e Indexação (Peso: 30)

* Noindex nas principais páginas de categorias → Crítico (−25, alta confiança)
* O mapa do site XML inclui URLs redirecionados → Médio (−5, Confiança média → −2,5)
* Referência de mapa do site ausente em robots.txt → Baixo (-2)

**Pontuação bruta:** 100 − 29,5 = **70,5**
**Contribuição ponderada:** 70,5 × 0,30 = **21,15**

## Índice geral de saúde de SEO

### Cálculo

Arredondado para o número inteiro mais próximo.

## Faixas de saúde (obrigatório)

Sempre classifique a pontuação final em uma faixa:

| Faixa de pontuação | Estado de saúde | Interpretação |
| ----------- | ------------- | ---------------------------------------------------------- |
| 90–100 | Excelente | Base sólida de SEO, apenas pequenas otimizações |
| 75–89 | Bom | Desempenho sólido com áreas de melhoria claras |
| 60–74 | Feira | Questões significativas que limitam o crescimento |
| 40–59 | Pobre | Sérias restrições de SEO |
| <40 | Crítico | SEO está fundamentalmente quebrado |

## Requisitos de saída (seção de pontuação)

Inclua isto **após o Resumo Executivo**:

### Índice de saúde SEO

* **Pontuação geral:** XX/100
* **Estado de saúde:** [Excelente/Bom/Regular/Ruim/Crítico]

#### Divisão de categorias

| Categoria | Pontuação | Peso | Contribuição ponderada |
| ------------------------- | ----- | ------ | --------------------- |
| Rastreabilidade e indexação | XX | 30 | XX |
| Fundações Técnicas | XX | 25 | XX |
| Otimização na página | XX | 20 | XX |
| Qualidade de conteúdo e EAT | XX | 15 | XX |
| Autoridade e Confiança | XX | 10 | XX |

## Regras de Interpretação (Obrigatórias)

* A pontuação **não substitui as descobertas**
* As melhorias devem ser rastreáveis a **problemas específicos**
* Uma pontuação alta com **Problemas críticos não resolvidos é inválido** → sinalizar inconsistência
* Sempre explique **o que impede a pontuação de ser mais alta**

## Rastreamento de alterações (opcional, mas recomendado)

Se existir uma auditoria anterior:

* Incluir **delta de pontuação** (+/−)
* Alterar atributos para correções específicas
* Evite comemorar aumentos de pontuação sem validar os resultados

## Limitações explícitas (sempre estado)

* A pontuação reflete **Prontidão de SEO**, não classificações garantidas
*Fatores externos (concorrência, atualizações de algoritmos) não são pontuados
* A pontuação de autoridade é direcional, não exaustiva

### Classificação das descobertas (obrigatório · Alinhado à pontuação)

Para **cada problema identificado**, forneça os campos a seguir.
Esses campos são **obrigatórios** e informam diretamente o SEO Health Index.

* **Problema**
  Uma descrição concisa do que está errado (uma frase, sem solução).

* **Categoria**
  Um de:

  * Rastreabilidade e indexação
  * Fundações Técnicas
  * Otimização na página
  * Qualidade de conteúdo e EAT
  * Sinais de Autoridade e Confiança

* **Evidências**
  Prova objetiva do problema (por exemplo, URLs, relatórios, cabeçalhos, dados de rastreamento, capturas de tela, métricas).
  *Não confie na intuição ou em afirmações de melhores práticas.*

* **Gravidade**
  Um de:

  * Crítico (bloqueia rastreamento, indexação ou classificação)
  * Alto
  * Médio
  * Baixo

* **Confiança**
  Um de:

---

---

---

* Alto (observado diretamente, repetível)
  * Médio (indicadores fortes, confirmação parcial)
  * Baixo (indireto ou baseado em amostra)

* **Por que é importante**
  Uma breve explicação do impacto do SEO em linguagem simples.

* **Impacto na pontuação**
  A dedução de pontos aplicada à categoria relevante **antes da ponderação**, incluindo modificador de confiança.

* **Recomendação**
  O que deve ser feito para resolver o problema.
  **Não inclua etapas de implementação, a menos que solicitado explicitamente.**

### Plano de ação priorizado (derivado das descobertas)

O plano de ação deve ser **derivado diretamente de descobertas e pontuações**, e não de julgamento subjetivo.

Agrupe as ações da seguinte forma:

1. **Bloqueadores Críticos**

   * Problemas com *Gravidade Crítica*
   * Problemas que invalidam o SEO Health Index se não forem resolvidos
   * Maior impacto de pontuação negativa

2. **Melhorias de alto impacto**

   * Problemas de gravidade alta ou média com grandes deduções de pontuação cumulativa
   * Problemas que afetam múltiplas páginas ou modelos

3. **Vitórias rápidas**

   * Problemas de gravidade baixa ou média
   * Fácil de corrigir com melhoria de pontuação mensurável

4. **Oportunidades de longo prazo**

   * Melhorias estruturais ou de conteúdo
   * Itens que melhoram a resiliência, profundidade ou autoridade ao longo do tempo

Para cada grupo de ação:

* Consulte as **descobertas relacionadas**
* Explique **intervalo de recuperação de pontuação esperado**
* Evite prazos, a menos que seja explicitamente solicitado

### Ferramentas (somente fontes de evidências)

As ferramentas podem ser referenciadas **apenas para apoiar evidências**, nunca como autoridade por si só.

Usos aceitáveis:

* Demonstrando que existe um problema
* Quantificar o impacto
* Fornecendo dados reproduzíveis

Exemplos:

* Search Console (cobertura, CWV, indexação)
* PageSpeed ​​Insights (métricas de campo versus laboratório)
* Crawlers (descoberta de URL, validação de metadados)
* Análise de log (comportamento de rastreamento, frequência)

Regras:

* Não confie em uma única ferramenta para tirar conclusões
* Não relate “pontuações” da ferramenta sem interpretação
* Sempre explique *o que os dados mostram* e *por que são importantes*

### Habilidades relacionadas (sem sobreposição)

Use essas habilidades **somente depois que a auditoria for concluída** e as descobertas forem aceitas.

* **seo programático**
  Use quando o plano de ação exigir **escalonamento da criação de páginas** em vários URLs.

* **marcação de esquema**
  Use quando a implementação de dados estruturados for aprovada como uma correção.

* **página-cro**
  Use quando a meta mudar de classificação para **otimização de conversão**.

* **rastreamento analítico**
  Use quando as lacunas de medição impedirem uma auditoria confiável ou validação de pontuação.