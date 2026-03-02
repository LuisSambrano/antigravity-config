---
name: web-perf
description: "Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance"
---

```markdown
## Performance Audit Results

# Otimização de desempenho da Web

## Visão geral

Ajude os desenvolvedores a otimizar o desempenho de sites e aplicativos da web para melhorar a experiência do usuário, classificações de SEO e taxas de conversão. Esta habilidade fornece abordagens sistemáticas para medir, analisar e melhorar a velocidade de carregamento, o desempenho do tempo de execução e as métricas Core Web Vitals.

## Quando usar esta habilidade

- Use quando o site ou aplicativo estiver carregando lentamente
- Use ao otimizar para Core Web Vitals (LCP, FID, CLS)
- Use ao reduzir o tamanho do pacote JavaScript
- Use ao melhorar o Time to Interactive (TTI)
- Use ao otimizar imagens e ativos
- Use ao implementar estratégias de cache
- Use ao depurar gargalos de desempenho
- Use ao se preparar para auditorias operacionais

## Como funciona

### Etapa 1: Medir o desempenho atual

Vou ajudá-lo a estabelecer métricas básicas:
- Executar auditorias Lighthouse
- Medir os principais sinais vitais da Web (LCP, FID, CLS)
- Verifique os tamanhos dos pacotes
- Analisar cascata de rede
- Identificar gargalos de desempenho

### Etapa 2: identificar problemas

Analise problemas de desempenho:
- Grandes pacotes de JavaScript
- Imagens não otimizadas
- Recursos de bloqueio de renderização
- Tempos de resposta lentos do servidor
- Cabeçalhos de cache ausentes
- Mudanças de layout
- Tarefas longas bloqueando o thread principal

### Etapa 3: Priorizar otimizações

Concentre-se em melhorias de alto impacto:
- Otimização crítica do caminho de renderização
- Divisão de código e carregamento lento
- Otimização de imagem
- Estratégias de cache
- Otimização de scripts de terceiros

### Etapa 4: implementar otimizações

Aplique melhorias de desempenho:
- Otimize ativos (imagens, fontes, CSS, JS)
- Implementar divisão de código
- Adicionar cabeçalhos de cache
- Carregamento lento de recursos não críticos
- Otimize o caminho crítico de renderização

### Etapa 5: Verifique as melhorias

Meça o impacto das mudanças:
- Executar novamente auditorias do Lighthouse
- Compare métricas antes/depois
- Monitore métricas reais do usuário (RUM)
- Teste em diferentes dispositivos e redes

## Exemplos

### Exemplo 1: Otimizando os principais sinais vitais da Web

### Métricas atuais (antes da otimização)
- **LCP (maior pintura com conteúdo):** 4,2s ❌ (deve ser <2,5s)
- **FID (atraso na primeira entrada):** 180ms ❌ (deve ser <100ms)
- **CLS (mudança cumulativa de layout):** 0,25 ❌ (deve ser <0,1)
- **Pontuação do Farol:** 62/100

### Problemas identificados

1. **Problema LCP:** A imagem principal (2,5 MB) carrega lentamente
2. **Problema de FID:** Grande pacote de JavaScript (850 KB) bloqueia o thread principal
3. **Problema CLS:** Imagens sem dimensões causam mudanças de layout

### Plano de otimização

#### Corrigir LCP (pintura com maior conteúdo)

**Problema:** A imagem principal tem 2,5 MB e carrega lentamente

**Soluções:**
\`\`\`html
<!-- Antes: imagem não otimizada -->
<img src="/hero.jpg" alt="Herói">

<!-- Depois: Otimizado com formatos modernos -->
<imagem>
  <fonte srcset="/hero.avif" type="image/avif">
  <source srcset="/hero.webp" type="image/webp">
  <img 
    src="/hero.jpg" 
    alt="Herói"
    largura = "1200" 
    altura = "600"
    carregando = "ansioso"
    buscarprioridade = "alta"
  >
</imagem>
\`\`\`

**Otimizações adicionais:**
- Compactar imagem para <200 KB
- Use CDN para entrega mais rápida
- Pré-carregar imagem principal: `<link rel="preload" as="image" href="/hero.avif">`

#### Corrigir FID (atraso na primeira entrada)

**Problema:** pacote JavaScript de 850 KB bloqueia o thread principal

**Soluções:**

1. **Divisão de código:**
\`\`\`javascript
// Antes: tudo em um pacote
importar {HeavyComponent} de './HeavyComponent';
importar {Analytics} de './analytics';
importar {ChatWidget} de './chat';

// Depois: carregamento lento de código não crítico
const HeavyComponent = preguiçoso(() => import('./HeavyComponent'));
const ChatWidget = preguiçoso(() => importar('./chat'));

// Carrega a análise após a página interativa
if (typeof window! == 'indefinido') {
  window.addEventListener('carregar', () => {
    import('./analytics').then(({ Analytics }) => {
      Analytics.init();
    });
  });
}
\`\`\`

2. **Remover dependências não utilizadas:**
\`\`\`bash
# Analisar pacote
npx webpack-bundle-analisador

#Remove pacotes não utilizados
momento de desinstalação do npm # Use date-fns (menor)
data de instalação npm-fns
\`\`\`

3. **Adiar scripts não críticos:**
\`\`\`html
<!-- Antes: Renderização de blocos -->
<script src="/analytics.js"></script>

<!-- Depois: Adiado -->
<script src="/analytics.js" defer></script>
\`\`\`

#### Corrigir CLS (mudança cumulativa de layout)

**Problema:** imagens sem dimensões causam alterações de layout

**Soluções:**
\`\`\`html
<!-- Antes: Sem dimensões -->
<img src="/produto.jpg" alt="Produto">

<!-- Depois: Com dimensões -->
<img 
  src="/produto.jpg" 
  alt="Produto"
  largura = "400" 
  altura = "300"
  estilo = "proporção: 4/3;"
>
\`\`\`

```markdown
## Bundle Size Optimization

```markdown
## Image Optimization

**Para conteúdo dinâmico:**
\`\`\`css
/* Reserve espaço para conteúdo que será carregado posteriormente */
.esqueleto-carregador {
  altura mínima: 200px;
  plano de fundo: gradiente linear (90 graus, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  tamanho de fundo: 200% 100%;
  animação: carregando 1,5s infinito;
}

@keyframes carregando {
  0% {posição de fundo: 200% 0; }
  100% {posição de fundo: -200% 0; }
}
\`\`\`

### Resultados após otimização

- **LCP:** 1,8s ✅ (melhorado em 57%)
- **FID:** 45ms ✅ (melhorado em 75%)
- **CLS:** 0,05 ✅ (melhorado em 80%)
- **Pontuação do Farol:** 94/100 ✅
```

### Exemplo 2: Reduzindo o tamanho do pacote JavaScript

### Estado Atual
- **Pacote total:** 850 KB (compactado: 280 KB)
- **Pacote principal:** 650 KB
- **Pacote do fornecedor:** 200 KB
**Tempo de carregamento (3G):** 8,2s

### Análise

\`\`\`bash
# Analise a composição do pacote
npx webpack-bundle-analyzer dist/stats.json
\`\`\`

**Constatações:**
1. Moment.js: 67 KB (pode substituir por date-fns: 12 KB)
2. Lodash: 72 KB (usando biblioteca inteira, só precisa de 5 funções)
3. Código não utilizado: ~150 KB de código morto
4. Sem divisão de código: tudo em um pacote

### Etapas de otimização

#### 1. Substitua dependências pesadas

\`\`\`bash
# Remova moment.js (67 KB) → Use date-fns (12 KB)
momento de desinstalação do npm
data de instalação npm-fns

# Antes
importar momento de 'momento';
const formatado = momento(data).format('AAAA-MM-DD');

# Depois
importar {formato} de 'data-fns';
const formatado = formato(data, 'aaaa-MM-dd');
\`\`\`

**Economia:** 55 KB

#### 2. Use Lodash seletivamente

\`\`\`javascript
// Antes: Importar biblioteca inteira (72KB)
importar _ de 'lodash';
const único = _.uniq(matriz);

// Depois: importe apenas o que você precisa (5KB)
importar uniq de 'lodash/uniq';
const único = uniq(matriz);

// Ou use métodos nativos
const único = [...novo conjunto(matriz)];
\`\`\`

**Economia:** 67 KB

#### 3. Implementar divisão de código

\`\`\`javascript
// Exemplo Next.js
importar dinâmico de 'próximo/dinâmico';

// Carregamento lento de componentes pesados
const Gráfico = dinâmico(() => importar('./Gráfico'), {
  carregando: () => <div>Carregando gráfico...</div>,
  ssr: falso
});

const AdminPanel = dinâmico(() => importação('./AdminPanel'), {
  carregando: () => <div>Carregando...</div>
});

// Divisão de código baseada em rota (automática em Next.js)
//pages/admin.js - Carregado apenas ao visitar /admin
//pages/dashboard.js - Carregado apenas ao visitar /dashboard
\`\`\`

#### 4. Remover código morto

\`\`\`javascript
// Habilita a agitação da árvore em webpack.config.js
módulo.exportações = {
  modo: 'produção',
  otimização: {
    usedExports: verdadeiro,
    efeitos colaterais: falso
  }
};

// Em pacote.json
{
  "Efeitos colaterais": falso
}
\`\`\`

#### 5. Otimize scripts de terceiros

\`\`\`html
<!-- Antes: Carrega imediatamente -->
<script src="https://analytics.com/script.js"></script>

<!-- Depois: Carregar depois da página interativa -->
<roteiro>
  window.addEventListener('carregar', () => {
    script const = document.createElement('script');
    script.src = 'https://analytics.com/script.js';
    script.async = verdadeiro;
    document.body.appendChild(script);
  });
</script>
\`\`\`

### Resultados

- **Pacote total:** 380 KB ✅ (reduzido em 55%)
- **Pacote principal:** 180 KB ✅
- **Pacote do fornecedor:** 80 KB ✅
- **Tempo de carregamento (3G):** 3,1s ✅ (melhorado em 62%)
```

### Exemplo 3: Estratégia de otimização de imagem

### Problemas atuais
- 15 imagens totalizando 12MB
- Sem formatos modernos (WebP, AVIF)
- Sem imagens responsivas
- Sem carregamento lento

### Estratégia de otimização

#### 1. Converter para formatos modernos

\`\`\`bash
# Instale ferramentas de otimização de imagem
npm instalar afiado

# Script de conversão (optimize-images.js)
const sustenido = require('sharp');
const fs = requer('fs');
const caminho = require('caminho');

função assíncrona optimizeImage(inputPath, outputDir) {
  const nome do arquivo = caminho.basename(inputPath, path.extname(inputPath));
  
  //Gera WebP
  aguarde afiado(inputPath)
    .webp({ qualidade: 80 })
    .toFile(path.join(outputDir, \`\${nome do arquivo}.webp\`));
  
  //Gera AVIF (melhor compactação)
  aguarde afiado(inputPath)
    .avif({ qualidade: 70 })
    .toFile(path.join(outputDir, \`\${nome do arquivo}.avif\`));
  
  // Gera substituto JPEG otimizado
  aguarde afiado(inputPath)
    .jpeg({ qualidade: 80, progressivo: verdadeiro })
    .toFile(path.join(outputDir, \`\${nome do arquivo}.jpg\`));
}

// Processa todas as imagens
imagens const = fs.readdirSync('./images');
imagens.forEach(img => {
  optimizeImage(\`./images/\${img}\`, './images/optimizado');
});
\`\`\`

#### 2. Implementar imagens responsivas

\`\`\`html
<!-- Imagens responsivas com formatos modernos -->
<imagem>
  <!-- AVIF para navegadores que o suportam (melhor compactação) -->
  <fonte 
    conjunto de dados = "
      /images/hero-400.avif 400w,
      /images/hero-800.avif 800w,
      /images/hero-1200.avif 1200w
    "
    type="imagem/avif"
    tamanhos = "(largura máxima: 768px) 100vw, 50vw"
  >
  
  <!-- WebP para navegadores que o suportam -->
  <fonte 
    conjunto de dados = "
      /images/hero-400.webp 400w,
      /images/hero-800.webp 800w,
      /images/hero-1200.webp 1200w
    "
    type="imagem/webp"
    tamanhos = "(largura máxima: 768px) 100vw, 50vw"
  >
  
  <!-- substituto JPEG -->
  <img 
    src="/images/hero-800.jpg"
    conjunto de dados = "
      /images/hero-400.jpg 400w,
      /images/hero-800.jpg 800w,
      /images/hero-1200.jpg 1200w
    "
    tamanhos = "(largura máxima: 768px) 100vw, 50vw"
    alt="Imagem do herói"
    largura = "1200"
    altura = "600"
    carregando = "preguiçoso"
  >
</imagem>
\`\`\`

#### 3. Carregamento lento

\`\`\`html
<!-- Carregamento lento nativo -->
<img 
  src="/imagem.jpg" 
  alt="Descrição"
  carregando = "preguiçoso"
  largura = "800"
  altura = "600"
>

<!-- Carregamento rápido para imagens acima da dobra -->
<img 
  src="/hero.jpg" 
  alt="Herói"
  carregando = "ansioso"
  buscarprioridade = "alta"
>
\`\`\`

#### 4. Componente de imagem Next.js

\`\`\`javascript
importar imagem de 'next/image';

// Otimização automática
<Imagem
  src="/hero.jpg"
  alt="Herói"
  largura={1200}
  altura={600}
  prioridade // Para imagens acima da dobra
  qualidade={80}
/>

// Carregamento lento
<Imagem
  src="/produto.jpg"
  alt="Produto"
  largura={400}
  altura={300}
  carregando = "preguiçoso"
/>
\`\`\`

### Resultados

| Métrica | Antes | Depois | Melhoria |
|--------|--------|-------|------------|
| Tamanho total da imagem | 12 MB | 1,8 MB | Redução de 85% |
| PCL | 4,5s | 1,6s | 64% mais rápido |
| Carregamento de página (3G) | 18 anos | 4,2s | 77% mais rápido |
```

## Melhores práticas

### ✅ Faça isso

- **Medir primeiro** - Sempre estabeleça métricas de linha de base antes de otimizar
- **Use o Lighthouse** - Execute auditorias regularmente para acompanhar o progresso
- **Otimizar imagens** - Use formatos modernos (WebP, AVIF) e imagens responsivas
- **Divisão de código** - Divida pacotes grandes em pedaços menores
- **Carga lenta** - Adiar recursos não críticos
- **Cache Agressivamente** - Defina cabeçalhos de cache adequados para ativos estáticos
- **Minimize o trabalho do thread principal** - Mantenha a execução do JavaScript em blocos de 50 ms
- **Pré-carregar recursos críticos** - Use `<link rel="preload">` para ativos críticos
- **Usar CDN** - Servir ativos estáticos da CDN para entrega mais rápida
- **Monitore usuários reais** - Acompanhe os principais sinais vitais da Web de usuários reais

### ❌ Não faça isso

- **Não otimize cegamente** - Meça primeiro e depois otimize
- **Não ignore dispositivos móveis** - Teste em dispositivos móveis reais e redes lentas
- **Não bloquear renderização** - Evite CSS e JavaScript que bloqueiam a renderização
- **Não carregue tudo antecipadamente** - Carregamento lento de recursos não críticos
- **Não se esqueça das dimensões** - Sempre especifique a largura/altura da imagem
- **Não use scripts síncronos** - Use atributos async ou defer
- **Não ignore scripts de terceiros** - Eles geralmente causam problemas de desempenho
- **Não ignore a compactação** - Sempre compacte e reduza os ativos

## Armadilhas Comuns

### Problema: otimizado para desktop, mas lento em dispositivos móveis
**Sintomas:** boa pontuação do Lighthouse em computadores, baixa em dispositivos móveis
**Solução:**
- Teste em dispositivos móveis reais
- Use a otimização móvel do Chrome DevTools
- Otimize para redes 3G/4G
- Reduza o tempo de execução do JavaScript
```bash
# Teste com limitação
farol https://yoursite.com --throttling.cpuSlowdownMultiplier=4
```

### Problema: grande pacote de JavaScript
**Sintomas:** Longo tempo para interação (TTI), alto FID
**Solução:**
- Analisar pacote com webpack-bundle-analyzer
- Remova dependências não utilizadas
- Implementar divisão de código
- Carregamento lento de código não crítico
```bash
# Analisar pacote
npx webpack-bundle-analyzer dist/stats.json
```

### Problema: imagens causando mudanças de layout
**Sintomas:** Pontuação CLS alta, salto de conteúdo
**Solução:**
- Sempre especifique largura e altura
- Use propriedade CSS de proporção de aspecto
- Reserve espaço com carregadores de esqueleto
```css
imagem {
  proporção: 16/9;
  largura: 100%;
  altura: automático;
}
```

---

### Problema: Tempo de resposta lento do servidor
**Sintomas:** TTFB alto (tempo até o primeiro byte)
**Solução:**
- Implementar cache do lado do servidor
- Use CDN para ativos estáticos
- Otimizar consultas de banco de dados
- Considere a geração de sites estáticos (SSG)
```javascript
// Next.js: geração estática
exportar função assíncrona getStaticProps() {
  const dados = aguarda fetchData();
  retornar {
    adereços: {dados},
    revalidate: 60 // Regenera a cada 60 segundos
  };
}
```

## Lista de verificação de desempenho

### Imagens
- [] Converter para formatos modernos (WebP, AVIF)
- [] Implementar imagens responsivas
- [] Adicionar carregamento lento
- [ ] Especifique as dimensões (largura/altura)
- [] Compactar imagens (<200 KB cada)
- [] Use CDN para entrega

### JavaScript
- [] Tamanho do pacote <200 KB (compactado)
- [] Implementar divisão de código
- [] Carregamento lento de código não crítico
- [] Remover dependências não utilizadas
- [] Minificar e compactar
- [] Use async/defer para scripts

### CSS
- [] CSS crítico embutido
- [] Adiar CSS não crítico
- [] Remover CSS não utilizado
- [] Minificar arquivos CSS
- [] Usar contenção CSS

### Cache
- [] Definir cabeçalhos de cache para ativos estáticos
- [] Implementar trabalhador de serviço
- [] Usar cache CDN
- [] Cache de respostas da API
- [] Versão de ativos estáticos

### Principais sinais vitais da Web
- [ ] LCP < 2,5s
- [ ] FID <100ms
- [ ] CLS < 0,1
- [] TTFB <600ms
- [ ] TTI < 3,8s

## Ferramentas de desempenho

### Ferramentas de medição
- **Lighthouse** - Auditoria de desempenho abrangente
- **WebPageTest** - Análise detalhada em cascata
- **Chrome DevTools** - Perfil de desempenho
- **PageSpeed Insights** - Métricas reais do usuário
- **Extensão Web Vitals** - Monitore os principais sinais vitais da Web

### Ferramentas de análise
- **webpack-bundle-analyzer** - Visualize a composição do pacote
- **source-map-explorer** - Analisar o tamanho do pacote
- **Bundlephobia** - Verifique os tamanhos dos pacotes antes de instalar
- **ImageOptim** - Ferramenta de compactação de imagem

### Ferramentas de monitoramento
- **Google Analytics** - Rastreie os principais sinais vitais da web
- **Sentinela** - Monitoramento de desempenho
- **New Relic** - Monitoramento de desempenho de aplicativos
- **Datadog** - Monitoramento real do usuário

## Habilidades Relacionadas

- `@react-best-practices` - Padrões de desempenho de reação
- `@frontend-dev-guidelines` - Padrões de desenvolvimento frontend
- `@systematic-debugging` - Problemas de desempenho de depuração
- `@senior-architect` - Arquitetura para desempenho

## Recursos Adicionais

- [Desempenho do Web.dev](https://web.dev/performance/)
- [Core Web Vitals](https://web.dev/vitals/)
- [Documentação do Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Guia de desempenho MDN](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Desempenho do Next.js](https://nextjs.org/docs/advanced-features/measuring-performance)
- [Guia de otimização de imagem](https://web.dev/fast/#optimize-your-images)

**Dica profissional:** Concentre-se primeiro nos Core Web Vitals (LCP, FID, CLS) - eles têm o maior impacto na experiência do usuário e nas classificações de SEO!