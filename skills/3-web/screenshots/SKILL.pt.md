---
name: screenshots
description: "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation."
source: "https://github.com/Shpigford/skills/tree/main/screenshots"
risk: safe
---

# Capturas de tela

Gere capturas de tela do seu aplicativo com qualidade de marketing usando o Playwright diretamente. As capturas de tela são capturadas em resolução HiDPI real (2x retina) usando `deviceScaleFactor: 2`.

## Quando usar esta habilidade

Use esta habilidade quando:
- O usuário deseja criar capturas de tela para o Product Hunt
- Criação de screenshots para mídias sociais
- Geração de imagens para landing pages
- Criação de screenshots de documentação
- O usuário solicita capturas de tela do aplicativo com qualidade de marketing

## Pré-requisitos

O dramaturgo deve estar disponível. Verifique:
```bash
dramaturgo npx --versão 2>/dev/null || npm ls dramaturgo 2>/dev/null | dramaturgo grep
```

Caso não seja encontrado, informe ao usuário:
> É necessário dramaturgo. Instale-o com: `npm install -D playwright` ou `npm install -D @playwright/test`

## Etapa 1: determinar o URL do aplicativo

Se `$1` for fornecido, use-o como URL do aplicativo.

Se nenhum URL for fornecido:
1. Verifique se é provável que um servidor de desenvolvimento esteja em execução procurando scripts `package.json`
2. Use `AskUserQuestion` para pedir a URL ao usuário ou oferecer ajuda para iniciar o servidor de desenvolvimento

URLs padrão comuns para sugerir:
- `http://localhost:3000` (Next.js, Criar aplicativo React, Rails)
- `http://localhost:5173` (Vite)
- `http://localhost:4000` (Phoenix)
- `http://localhost:8080` (Vue CLI, genérico)

## Etapa 2: Reunir requisitos

Use `AskUserQuestion` com as seguintes perguntas:

**Pergunta 1: contagem de capturas de tela**
- Cabeçalho: "Contagem"
- Pergunta: "Quantas capturas de tela você precisa?"
- Opções:
  - "3-5" - Conjunto rápido de recursos principais
  - "5-10" - Cobertura abrangente de recursos
  - "10+" - Pacote completo de marketing

**Pergunta 2: Objetivo**
- Cabeçalho: "Objetivo"
- Pergunta: "Para que servirão essas capturas de tela?"
- Opções:
  - "Product Hunt" - Fotos de heróis e destaques de recursos
  - "Mídia social" - Demonstrações de recursos atraentes
  - "Página de destino" - Seções e benefícios de marketing
  - "Documentação" - Referência da UI e tutoriais

**Pergunta 3: Autenticação**
- Cabeçalho: "Autorização"
- Pergunta: "O aplicativo requer login para acessar os recursos que você deseja capturar a tela?"
- Opções:
  - "Não é necessário fazer login" - Somente páginas públicas
  - "Sim, fornecerei credenciais" - É necessário fazer login primeiro

Se o usuário selecionar "Sim, fornecerei credenciais", faça perguntas de acompanhamento:
- "Qual é o URL da página de login?" (por exemplo, `/login`, `/sign-in`)
- "Qual é o e-mail/nome de usuário?"
- "Qual é a senha?"

O script detectará automaticamente os campos do formulário de login usando os localizadores inteligentes do Playwright.

## Etapa 3: analisar a base de código em busca de recursos

Explore minuciosamente a base de código para entender o aplicativo e identificar oportunidades de captura de tela.

### 3.1: Leia a documentação primeiro

**Sempre comece lendo estes arquivos** para entender o que o aplicativo faz:

1. **README.md** (e quaisquer arquivos README em subdiretórios) - Leia o README completo para entender:
   - O que é o aplicativo e qual problema ele resolve
   - Principais recursos e capacidades
   - Capturas de tela ou descrições de recursos já documentadas

2. **CHANGELOG.md** ou **HISTORY.md** – Recursos recentes que merecem destaque

3. Diretório **docs/** - Qualquer documentação adicional sobre recursos

### 3.2: Analisar rotas para encontrar páginas

Leia a configuração de roteamento para descobrir todas as páginas disponíveis:

| Estrutura | Arquivo para ler | O que procurar |
|-----------|--------------|------------------|
| **Roteador de aplicativo Next.js** | estrutura de diretório `app/` | Cada pasta com `page.tsx` é uma rota |
| **Roteador de páginas Next.js** | diretório `páginas/` | Cada arquivo é uma rota |
| **Trilhos** | `config/rotas.rb` | Leia o arquivo inteiro para todas as rotas |
| **Roteador React** | Procure por `createBrowserRouter` ou `<Route` | Definições de rota com caminhos |
| **Roteador Vue** | `src/router/index.js` ou `router.js` | Matriz de rotas com definições de caminho |
| **SvelteKit** | diretório `src/routes/` | Cada pasta com `+page.svelte` é uma rota |
| **Remix** | diretório `app/routes/` | Roteamento baseado em arquivo |
| **Laravel** | `rotas/web.php` | Definições de rota |
| **Django** | Arquivos `urls.py` | Padrões de URL |
| **Expresso** | Procure por `app.get`, `router.get` | Manipuladores de rota |

**Importante**: Leia realmente esses arquivos, não apenas verifique se eles existem. As definições de rota informam quais páginas estão disponíveis para capturas de tela.

### 3.3: Identificar os principais componentes

Procure componentes que representem recursos de captura de tela:

- Componentes do painel
- Seções de recursos com interface de usuário distinta
- Formulários e entradas interativas
- Visualizações de dados (tabelas, gráficos, tabelas)
- Modais e diálogos
- Navegação e barras laterais
- Painéis de configurações
- Seções de perfil de usuário

### 3.4: Verifique os ativos de marketing

```bash
mkdir -p screenshots
```

```javascript
import { chromium } from 'playwright';

```bash
node screenshot-script.mjs
```

Procure conteúdo de marketing existente que indique os principais recursos:
- Componentes da página de destino (geralmente em `components/landing/` ou `components/marketing/`)
- Componentes da lista de recursos
- Tabelas de preços
- Seções de depoimentos

### 3.5: Lista de recursos de construção

Crie uma lista abrangente de recursos descobertos com:
- Nome do recurso (do README ou nome do componente)
- Caminho da URL (das rotas)
- Seletor CSS para focar (da estrutura do componente)
- Estado da UI necessário (logado, dados preenchidos, modal aberto, guia específica selecionada)

## Etapa 4: planejar capturas de tela com o usuário

Apresente os recursos descobertos ao usuário e peça-lhe para confirmar ou modificar a lista.

Use `AskUserQuestion`:
- Cabeçalho: "Recursos"
- Pergunta: "Encontrei esses recursos em sua base de código. Qual você gostaria de capturar?"
- Opções: liste de 3 a 4 recursos principais descobertos, além de "Deixe-me escolher os específicos"

Se o usuário quiser informações específicas, faça perguntas de acompanhamento para esclarecer exatamente o que capturar.

## Etapa 5: Criar diretório de capturas de tela

## Etapa 6: gerar e executar o script do Playwright

Crie um script Node.js que use Playwright com configurações HiDPI adequadas. O roteiro deve:

1. **Use `deviceScaleFactor: 2`** para resolução real de retina
2. **Defina a janela de visualização para 1440x900** (produz imagens de 2880x1800 pixels)
3. **Tratar da autenticação** se as credenciais foram fornecidas
4. **Navegue até cada página** e faça capturas de tela

### Modelo de roteiro

Escreva este script em um arquivo temporário (por exemplo, `screenshot-script.mjs`) e execute-o:

const BASE_URL = '[APP_URL]';
const SCREENSHOTS_DIR = './capturas de tela';

//Configuração de autenticação (se necessário)
const AUT = {
  necessário: [verdadeiro|falso],
  loginUrl: '[LOGIN_URL]',
  e-mail: '[EMAIL]',
  senha: '[SENHA]',
};

//Capturas de tela para capturar
const CAPTURAS DE TELA = [
  {nome: '01-feature-name', url: '/caminho', waitFor: '[seletor opcional]' },
  {nome: '02-outro-recurso', url: '/outro-caminho' },
  // ... adiciona todas as capturas de tela planejadas
];

função assíncrona main() {
  const navegador = aguarda chromium.launch();

  // Cria contexto com configurações HiDPI
  const contexto = aguardar navegador.newContext({
    janela de visualização: {largura: 1440, altura: 900},
    deviceScaleFactor: 2, // Esta é a chave para capturas de tela verdadeiras da retina
  });

  página const = aguardar context.newPage();

  // Trata a autenticação se necessário
  if (AUTH. necessário) {
    console.log('Efetuando login...');
    aguarde page.goto(AUTH.loginUrl);

    // Login inteligente: experimente vários padrões comuns para o campo email/nome de usuário
    const emailField = page.locator([
      'entrada[tipo="e-mail"]',
      'entrada[nome="e-mail"]',
      'entrada[id="e-mail"]',
      'entrada[placeholder*="e-mail" i]',
      'input[nome="nome de usuário"]',
      'entrada[id="nome de usuário"]',
      'entrada[tipo="texto"]',
    .join(', ')).primeiro();
    aguarde emailField.fill(AUTH.email);

    // Login inteligente: experimente vários padrões comuns para o campo de senha
    const passwordField = page.locator([
      'entrada[tipo="senha"]',
      'entrada[nome="senha"]',
      'entrada[id="senha"]',
    .join(', ')).primeiro();
    aguarde passwordField.fill(AUTH.password);

    // Login inteligente: experimente vários padrões comuns para o botão enviar
    const submitButton = page.locator([
      'botão[type="enviar"]',
      'entrada[tipo="enviar"]',
      'botão: tem-texto("Entrar")',
      'botão: tem-texto("Entrar")',
      'botão:tem-texto("Login")',
      'botão:tem-texto("Enviar")',
    .join(', ')).primeiro();
    aguarde submitButton.click();

    aguarde page.waitForLoadState('networkidle');
    console.log('Login concluído');
  }

  //Captura cada captura de tela
  for (captura constante de CAPTURAS DE TELA) {
    console.log(`Capturando: ${shot.name}`);
    aguarde page.goto(`${BASE_URL}${shot.url}`);
    aguarde page.waitForLoadState('networkidle');

    // Opcional: aguarde por elemento específico
    if (tiro.waitFor) {
      aguarde page.waitForSelector(shot.waitFor);
    }

    // Opcional: execute ações antes da captura de tela
    if (tiro.ações) {
      for (ação const de shot.actions) {
        if (action.click) aguarda page.click(action.click);
        if (action.fill) aguarda page.fill(action.fill.selector, action.fill.value);
        if (action.wait) aguardar page.waitForTimeout(action.wait);
      }
    }

    aguardar página.screenshot({
      caminho: `${SCREENSHOTS_DIR}/${shot.name}.png`,
      fullPage: shot.fullPage || falso,
    });
    console.log(`Salvo: ${shot.name}.png`);
  }

  aguarde navegador.close();
  console.log('Concluído!');
}

main().catch(console.error);
```

### Executando o script

```javascript
const element = await page.locator('[CSS_SELECTOR]');
await element.screenshot({ path: `${SCREENSHOTS_DIR}/element.png` });
```

```javascript
await page.screenshot({
  path: `${SCREENSHOTS_DIR}/full-page.png`,
  fullPage: true
});
```

```javascript
await page.waitForTimeout(500); // Wait 500ms for animations
```

```javascript
await page.click('button.open-modal');
await page.waitForSelector('.modal-content');
await page.screenshot({ path: `${SCREENSHOTS_DIR}/modal.png` });
```

```javascript
// Set dark mode preference
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  colorScheme: 'dark',
});
```

```bash
ls -la screenshots/*.png
sips -g pixelWidth -g pixelHeight screenshots/*.png 2>/dev/null || file screenshots/*.png
```

Após a execução, limpe o script temporário:
```bash
rm screenshot-script.mjs
```

## Etapa 7: opções avançadas de captura de tela

### Capturas de tela focadas em elementos

Para capturar a captura de tela de um elemento específico em vez da janela de visualização completa:

### Capturas de tela de página inteira

Para conteúdo rolável, capture a página inteira:

### Esperando por animações

Se a página tiver animações, espere que elas sejam concluídas:

### Clicando nos elementos antes da captura de tela

Para capturar um estado modal, suspenso ou suspenso:

### Capturas de tela do modo escuro

Se o aplicativo suportar o modo escuro:

## Etapa 8: Convenção de nomenclatura de arquivos

Use nomes de arquivos descritivos, kebab-case, com prefixos numéricos para ordenação:

| Recurso | Nome do arquivo |
|--------|----------|
| Visão geral do painel | `01-dashboard-overview.png` |
| Gerenciamento de links | `02-link-inbox.png` |
| Editor de edição | `03-edição-editor.png` |
| Análise | `04-analítica.png` |
| Configurações | `05-configurações.png` |

## Etapa 9: verificar e resumir

Após capturar todas as capturas de tela, verifique os resultados:

Forneça um resumo ao usuário:

1. Liste todos os arquivos gerados com seus caminhos
2. Confirme a resolução (deve ser 2880x1800 para retina 2x na janela de visualização de 1440x900)
3. Mencione o tamanho total dos arquivos
4. Sugira quaisquer ações de acompanhamento

Exemplo de saída:
```
Gerou 5 capturas de tela de marketing:

capturas de tela/
├── 01-dashboard-overview.png (1,2 MB, 2880x1800 @ 2x)
├── 02-link-inbox.png (456 KB, 2880x1800 @ 2x)
├── 03-edition-editor.png (890 KB, 2880x1800 @ 2x)
├── 04-analytics.png (567 KB, 2880x1800 @ 2x)
└── 05-settings.png (234 KB, 2880x1800 @ 2x)

Todas as capturas de tela têm qualidade retina verdadeira (2x deviceScaleFactor) e estão prontas para uso em marketing.
```

## Tratamento de erros

- **Dramaturgo não encontrado**: Sugira `npm install -D dramaturgo`
- **Página não carregando**: Verifique se o servidor de desenvolvimento está rodando, sugira iniciá-lo
- **Falha no login**: Os localizadores inteligentes tentam padrões comuns, mas podem falhar em formulários de login incomuns. Se o login falhar, analise o HTML da página de login para encontrar os seletores corretos e personalizar o script.
- **Elemento não encontrado**: verifique o seletor CSS e ofereça uma captura de tela inteira da página
- **Falha na captura de tela**: verifique o espaço em disco, verifique as permissões de gravação no diretório de capturas de tela

## Dicas para melhores resultados

1. **Estado de IU limpo**: use dados de demonstração/semente para conteúdo realista
2. **Dimensionamento consistente**: use a mesma janela de visualização para todas as capturas de tela
3. **Aguarde pelo conteúdo**: Use `waitForLoadState('networkidle')` para garantir que todo o conteúdo seja carregado
4. **Ocultar ferramentas de desenvolvimento**: certifique-se de que nenhuma extensão do navegador ou sobreposição de desenvolvimento esteja visível
5. **Variantes do modo escuro**: considere capturar os modos claro e escuro, se compatível