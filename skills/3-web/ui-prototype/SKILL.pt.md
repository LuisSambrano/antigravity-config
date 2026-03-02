---
name: ui-prototype
description: UI/UX prototyping workflow using generate_image tool. Use when the user wants to design mockups, wireframes, or visual prototypes before coding.
---

# Prototipagem UI/UX com generate_image

Crie modelos visuais e repita os designs de UI antes de escrever o código.

## Quando usar

- O usuário diz "diseña una UI", "crea un mockup", "prototipa esto"
- Antes de construir componentes de UI complexos
- Quando o usuário deseja visualizar um layout antes de codificar

## Fluxo de trabalho

### 1. Entenda os requisitos

- Qual é a finalidade da página/componente?
- Quem é o público-alvo?
- Qual é o estilo de design? (glassmorfismo, mínimo, brutalista, etc.)
- Primeiro o celular ou o desktop?

### 2. Gerar maquete inicial

Use `generate_image` com um prompt detalhado descrevendo:

- Estrutura de layout (cabeçalho, barra lateral, área de conteúdo, rodapé)
- Paleta de cores e estilo
- Principais elementos da UI (botões, cartões, formulários, tabelas)
- Preferências de tipografia
- Modo escuro/claro

### 3. Iterar no feedback

Refine o design com base no feedback do usuário usando chamadas `generate_image` de acompanhamento com ajustes.

### 4. Extrair tokens de design

A partir da maquete aprovada, defina:

- Variáveis ​​de cores (propriedades personalizadas CSS)
- Escala de espaçamento
- Escala de tipografia
- Raio da borda, sombras
- Padrões de componentes

### 5. Implementar

Traduza o modelo aprovado em código usando os tokens de design estabelecidos.

## Dicas imediatas

- Seja específico sobre o layout ("grade de 3 colunas com barra lateral")
- Sistemas de design conhecidos de referência ("inspirado em Linear/Notion/Vercel")
- Especifique as cores exatas quando possível ("use o plano de fundo #0A0A0A")
- Incluir exemplos de conteúdo, não Lorem Ipsum
- Especifique o modo escuro com efeitos de vidro se estiver usando morfismo de vidro

## Antipadrões

- ❌ Gerando antes de entender os requisitos
- ❌ Codificar antes de obter a aprovação do modelo
- ❌ Usando texto de espaço reservado em modelos finais
- ❌ Ignorando a capacidade de resposta móvel em protótipos