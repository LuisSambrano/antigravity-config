---
name: tailwind
description: Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture.
allowed-tools: Read, Write, Edit, Glob, Grep
---

---

---

```
@theme {
  /* Colors - use semantic names */
  --color-primary: oklch(0.7 0.15 250);
  --color-surface: oklch(0.98 0 0);
  --color-surface-dark: oklch(0.15 0 0);
  
  /* Spacing scale */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

---

---

---

---

---

---

# Padrões CSS Tailwind (v4 - 2025)

> CSS utilitário moderno com configuração nativa de CSS.

## 1. Arquitetura Tailwind v4

### O que mudou desde a v3

| v3 (Legado) | v4 (atual) |
|------------|--------------|
| `tailwind.config.js` | Diretiva `@theme` baseada em CSS |
| Plug-in PostCSS | Motor óxido (10x mais rápido) |
| Modo JIT | Nativo, sempre ativo |
| Sistema de plug-ins | Recursos nativos de CSS |
| Diretiva `@apply` | Ainda funciona, desanimado |

### Conceitos Básicos da v4

| Conceito | Descrição |
|--------|-------------|
| **CSS primeiro** | Configuração em CSS, não em JavaScript |
| **Motor Óxido** | Compilador baseado em Rust, muito mais rápido |
| **Aninhamento nativo** | Aninhamento CSS sem PostCSS |
| **Variáveis ​​CSS** | Todos os tokens expostos como `--*` vars |

## 2. Configuração baseada em CSS

### Definição do tema

### Quando estender ou substituir

| Ação | Usar quando |
|--------|----------|
| **Estender** | Adicionando novos valores junto com os padrões |
| **Substituir** | Substituindo totalmente a escala padrão |
| **Tokens semânticos** | Nomenclatura específica do projeto (primário, superfície) |

## 3. Consultas de contêiner (v4 nativo)

### Ponto de interrupção vs contêiner

| Tipo | Responde a |
|------|-------------|
| **Ponto de interrupção** (`md:`) | Largura da janela de visualização |
| **Contêiner** (`@contêiner`) | Largura do elemento pai |

### Uso de consulta de contêiner

| Padrão | Aulas |
|--------|---------|
| Definir contêiner | `@container` no pai |
| Ponto de interrupção do contêiner | `@sm:`, `@md:`, `@lg:` em crianças |
| Recipientes nomeados | `@container/card` para especificidade |

### Quando usar

| Cenário | Usar |
|----------|-----|
| Layouts de nível de página | Pontos de interrupção da janela de visualização |
| Responsivo em nível de componente | Consultas de contêineres |
| Componentes reutilizáveis ​​| Consultas de contêiner (independentes do contexto) |

## 4. Design Responsivo

### Sistema de ponto de interrupção

| Prefixo | Largura mínima | Alvo |
|--------|-----------|--------|
| (nenhum) | 0px | Primeira base móvel |
| `sm:` | 640px | Telefone grande/tablet pequeno |
| `md:` | 768px | Tablet |
| `lg:` | 1024px | Portátil |
| `xl:` | 1280px | Área de Trabalho |
| `2xl:` | 1536px | Área de trabalho grande |

### Princípio Mobile-First

1. Escreva primeiro os estilos móveis (sem prefixo)
2. Adicione substituições de tela maiores com prefixos
3. Exemplo: `w-full md:w-1/2 lg:w-1/3`

## 5. Modo escuro

### Estratégias de configuração

| Método | Comportamento | Usar quando |
|--------|----------|----------|
| `classe` | classe `.dark` alterna | Alternador de tema manual |
| `mídia` | Segue a preferência do sistema | Sem controle do usuário |
| `seletor` | Seletor personalizado (v4) | Temas complexos |

### Padrão de modo escuro

| Elemento | Luz | Escuro |
|--------|-------|------|
| Plano de fundo | `bg-branco` | `escuro:bg-zinco-900` |
| Texto | `texto-zinco-900` | `escuro:text-zinc-100` |
| Fronteiras | `border-zinco-200` | `escuro:border-zinc-700` |

## 6. Padrões de layout modernos

### Padrões Flexbox

| Padrão | Aulas |
|--------|---------|
| Centro (ambos os eixos) | `flex itens-centro justificar-centro` |
| Pilha vertical | `flex flex-col gap-4` |
| Linha horizontal | `flex gap-4` |
| Espaço entre | `flex justificar entre itens-centro` |
| Grade envolvente | `flex flex-wrap gap-4` |

### Padrões de grade

| Padrão | Aulas |
|--------|---------|
| Ajuste automático responsivo | `grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))]` |
| Assimétrico (Bento) | `grid grid-cols-3 grid-rows-2` com vãos |
| Layout da barra lateral | `grade grid-cols-[auto_1fr]` |

> **Observação:** Prefira layouts assimétricos/Bento em vez de grades simétricas de 3 colunas.

## 7. Sistema de cores moderno

### OKLCH versus RGB/HSL

| Formato | Vantagem |
|--------|-----------|
| **OKLCH** | Perceptivamente uniforme, melhor para o design |
| **HSL** | Matiz/saturação intuitiva |
| **RGB** | Compatibilidade herdada |

### Arquitetura de token de cores

| Camada | Exemplo | Finalidade |
|-------|---------|-----|
| **Primitivo** | `--azul-500` | Valores de cores brutas |
| **Semântico** | `--cor-primária` | Nomenclatura baseada em propósito |
| **Componente** | `--botão-bg` | Específico do componente |

## 8. Sistema de tipografia

### Padrão de pilha de fontes

| Tipo | Recomendado |
|------|-------------|
| Sem | `'Inter', 'SF Pro', system-ui, sans-serif` |
| Mono | `'JetBrains Mono', 'Código Fira', monoespaço` |
| Exibir | `'Outfit', 'Poppins', sem serifa` |

### Tipo Escala

| Classe | Tamanho | Usar |
|-------|------|-----|
| `texto-xs` | 0,75rem | Etiquetas, legendas |
| `texto-sm` | 0,875rem | Texto secundário |
| `texto-base` | 1rem | Corpo do texto |
| `texto-lg` | 1,125rem | Texto principal |
| `texto-xl`+ | 1,25rem+ | Títulos |

## 9. Animação e transições

### Animações integradas

---

---

---

---

| Classe | Efeito |
|-------|--------|
| `animar-spin` | Rotação contínua |
| `animar-ping` | Pulso de atenção |
| `animar-pulso` | Pulso de opacidade sutil |
| `animar-salto` | Efeito saltitante |

### Padrões de Transição

| Padrão | Aulas |
|--------|---------|
| Todas as propriedades | `transição-toda a duração-200` |
| Específico | `duração das cores de transição-150` |
| Com flexibilização | `ease-out` ou `ease-in-out` |
| Efeito de foco | `hover:scale-105 transição-transformação` |

## 10. Extração de componentes

### Quando extrair

| Sinal | Ação |
|--------|--------|
| Combo da mesma classe 3+ vezes | Extrair componente |
| Variantes de estado complexo | Extrair componente |
| Elemento do sistema de design | Extrato + documento |

### Métodos de extração

| Método | Usar quando |
|--------|----------|
| **Componente React/Vue** | Dinâmico, JS necessário |
| **@apply em CSS** | Estático, sem necessidade de JS |
| **Tokens de design** | Valores reutilizáveis ​​|

## 11. Antipadrões

| Não | Faça |
|-------|-----|
| Valores arbitrários em todos os lugares | Use a escala do sistema de design |
| `!importante` | Corrija a especificidade adequadamente |
| `estilo=` embutido | Usar utilitários |
| Duplicar listas longas de turmas | Extrair componente |
| Misture a configuração v3 com v4 | Migre totalmente para CSS primeiro |
| Use `@apply` fortemente | Prefira componentes |

## 12. Princípios de Desempenho

| Princípio | Implementação |
|-----------|----------------|
| **Expurgar não utilizado** | Automático em v4 |
| **Evite dinamismo** | Nenhuma classe de string de modelo |
| **Usar Óxido** | Padrão na v4, 10x mais rápido |
| **Construções de cache** | Cache CI/CD |

> **Lembre-se:** Tailwind v4 prioriza CSS. Adote variáveis ​​CSS, consultas de contêiner e recursos nativos. O arquivo de configuração agora é opcional.