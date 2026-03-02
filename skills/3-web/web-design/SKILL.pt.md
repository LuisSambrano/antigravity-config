---
name: web-design
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

# Diretrizes para interface da Web

Revise os arquivos para conformidade com as Diretrizes de Interface da Web.

## Como funciona

1. Obtenha as diretrizes mais recentes no URL de origem abaixo
2. Leia os arquivos especificados (ou solicite ao usuário os arquivos/padrão)
3. Verifique todas as regras nas diretrizes buscadas
4. Resultados de saída no formato conciso `file:line`

## Fonte das Diretrizes

Obtenha novas diretrizes antes de cada revisão:

Use o WebFetch para recuperar as regras mais recentes. O conteúdo obtido contém todas as regras e instruções de formato de saída.

## Uso

Quando um usuário fornece um argumento de arquivo ou padrão:
1. Obtenha as diretrizes do URL de origem acima
2. Leia os arquivos especificados
3. Aplique todas as regras das diretrizes obtidas
4. Resultados de resultados usando o formato especificado nas diretrizes

Se nenhum arquivo for especificado, pergunte ao usuário quais arquivos revisar.