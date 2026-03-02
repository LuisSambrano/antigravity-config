---
name: vibecode-ui
description: "UI/UX implementation guidelines specializing in Glassmorphism and high-performance Web Interfaces. Enforces Next.js 14+ architectural standards and WCAG accessibility compliance."
---

---

---

---

---

---

# Estrutura Vibecode UI/UX Pro Max

Esta habilidade combina a filosofia do design "Vibecode" com os padrões de engenharia do "Next Level Builder".

## � Biblioteca de Dados Extendida (Modo Completo)

Esta habilidade tem acesso a uma base de dados de regras detalhadas em `./data/`.
Antes de realizar tarefas completas, **consulte os arquivos CSV relevantes** em `~/playground/.agent/skills/vibecode-ui/data/`:

- `ux-guidelines.csv`: Lista de verificação UX exaustiva (mais de 100 regras).
- `styles.csv`: Definições detalhadas de 67 estilos visuais.
- `stacks/`: Guias específicos para frameworks (Next.js, Vue, Flutter, etc.).
- `ui-reasoning.csv`: Lógica para decidir qual padrão usar dependendo do tipo de produto.

**Instrução de ativação**: Se o usuário quiser uma pilha específica (ej: "Astro") ou um estilo incomum (ej: "Neubrutalism"), LEE o arquivo CSV correspondente primeiro.

## �📋 Las 5 Dimensões do Design (Estética)

Ao gerar CUALQUIER UI, você deve cumprir estas 5 regras visuais:

### 1. **PATRÓN Y DISEÑO**

- **SaaS**: Herói + Prova Social + CTA (Valor primeiro).
- **Luxo/E-commerce**: Hero Slider + Galería Inmersiva.
- **Dashboard**: Bento Grid + Densidade de Dados.

### 2. **ESTILO (Luxo Morfismo de Vidro)**

- `filtro de pano de fundo: desfoque (12px)`
- `bg-white/5` (Modo Escuro) o `bg-black/5` (Modo Claro).
- Bordas sutiles: `border-white/10`.
- **Sombra Interior**: `shadow-[inset_0_1px_0_0_rgba(255,255,255,0.1)]`.

### 3. **COR E TEMA**

- **Paleta**: Luxury Dark (`#0A0A0A`, `#1C1917`, Dourado `#CA8A04`).
- **Gradiente**: Aurora Beams (usar imagens ou gradientes radiais CSS).

### 4. **ANIMACIONES (El Alma)**

- **Entrada**: `initial={{ opacidade: 0, y: 20 }}` -> `animate={{ opacidade: 1, y: 0 }}`.
- **Scroll**: escalonar crianças com `framer-motion`.
- **Micro**: Escala `1.02` em foco.

## � Módulos Avançados (Google Antigravity)

Integração de capacidades de alto nível bloqueadas em seu repositório local:

### **Módulo 3D (Experiência Web)**

- **Herramienta Preferida**: `Spline` para cenas rápidas ("Gorgeous" com baixo esforço) ou `React Three Fiber` para interatividade completa.
- **Desempenho**: Modelos GLB comprimidos (Draco). NUNCA bloqueie o thread principal.
- **Regla de Oro**: Se o 3D não suportar valor narrativo ou estético, use uma imagem/vídeo otimizado.

### **Módulo de Design Intencional (Frontend Design)**

- **Mandato Anti-Genérico**: Evita layouts predecíveis de Tailwind. "Rompe la grilla" intencionalmente com assimetria e superposições.
- **Índice DFII**: Avalia cada design: ¿É memorável? Você tem um visual único?
- **Tipografía Estructural**: Usa fontes de exibição expressivas, sem apenas fontes do sistema.

## �🛠️ Padrões de Engenharia (Next.js 15+ / React)

Regras restritas extraídas de `ui-ux-pro-max`:

### **Roteamento e renderização**

1. **Componentes de servidor por defeito**: Mantenha a lógica no servidor. Apenas use `'use client'` nas horas (botões, entradas).
2. **App Router**: Estrutura `app/(marketing)/page.tsx` para grupos de rotas.
3. **Carregando**: Usa `loading.tsx` e `<Suspense>` para streaming de UI.

### **Desempenho e imagens**

1. **Próximo/Imagem**: OBRIGATÓRIO. Nunca usa `<img>`.
2. **Dimensões**: Sempre defina `largura/altura` ou use `preenchimento` com um aspecto relativo.
3. **Fontes**: Use `next/font` (Inter/JetBrains Mono) para evitar CLS (Cumulative Layout Shift).

### **Busca de dados**

1. **Ações do servidor**: Ações do servidor dos EUA para alterações (formulários), sem rotas API antigas.
2. **Direct Fetch**: Faça a busca de dados diretamente nos componentes do servidor (`await fetch()`).

## 🛡️ Garantia de UX e acessibilidade

Antes de entregar o código, verifique:

### **Interação**

- [ ] **Touch Targets**: Mínimo 44x44px em dispositivos móveis.
- [ ] **Feedback**: Estados de carga (Spinners/Skeletons) para ações > 300ms.
- [ ] **Erros**: Mensagens de erro claras e próximas à entrada falhada.

### **Acessibilidade**

- [ ] **Contraste**: O texto cinza claro sobre fundo escuro deve ser legível (`text-neutral-400` no mínimo).
- [ ] **Focus**: Nunca sai `outline` sem colocar um substituto (`ring-2 ring-accent`).
- [ ] **Etiquetas**: Todas as entradas devem ter `label` ou `aria-label`.

## 🚫 Anti-Patrones (Proibido)

- ❌ **Função Flash over**: Animações que duram > 500ms.
- ❌ **Layout Shift**: as imagens não são dimensionadas para exibir o conteúdo.
- ❌ **Perfuração de props**: Passar props mais de 3 níveis (usa Composição ou Contexto).
- ❌ **Div Soup**: Divs anidados innecesariamente. Use `Fragment` (`<>`) ou Grid/Flex inteligentemente.

**Indicação de Prompt**:
"Gerar um painel de vendas" ->

1. **Estilo**: Bento Grid, Glassmorphism, Dark Mode.
2. **Tecnologia**: Next.js App Router, componentes de servidor para dados, recargas para gráficos.
3. **UX**: Esqueletos ao carregar, dicas de ferramentas em gráficos.