---
name: radix-ui
description: Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-grade UI libraries.
risk: safe
source: self
---

---

```tsx
// ❌ Don't fight pre-styled components
<Button className="override-everything" />

```tsx
// Primitive components compose naturally
<Tabs.Root>
  <Tabs.List>
    <Tabs.Trigger value="tab1">Tab 1</Tabs.Trigger>
    <Tabs.Trigger value="tab2">Tab 2</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="tab1">Content 1</Tabs.Content>
  <Tabs.Content value="tab2">Content 2</Tabs.Content>
</Tabs.Root>
```

---

```bash
# Install individual primitives (recommended)
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu

```tsx
import * as Dialog from '@radix-ui/react-dialog';

---

```css
/* globals.css */
:root {
  --color-primary: 220 90% 56%;
  --color-surface: 0 0% 100%;
  --radius-base: 0.5rem;
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}

```tsx
// Component.tsx
<Dialog.Content 
  className="
    bg-[hsl(var(--color-surface))]
    rounded-[var(--radius-base)]
    shadow-[var(--shadow-lg)]
  "
/>
```

```tsx
// button.tsx
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

# Sistema de design de interface do usuário Radix

Crie sistemas de design acessíveis e prontos para produção usando as primitivas de UI Radix com controle total de personalização e zero opiniões de estilo.

## Visão geral

Radix UI fornece componentes acessíveis e sem estilo (primitivos) que você pode personalizar para corresponder a qualquer sistema de design. Esta habilidade orienta você na construção de bibliotecas de componentes escalonáveis ​​com Radix UI, com foco no design que prioriza a acessibilidade, arquitetura de temas e padrões combináveis.

**Principais pontos fortes:**
- **Sem cabeça por design**: controle total de estilo sem combater os padrões
**Acessibilidade integrada**: compatível com WAI-ARIA, navegação por teclado, suporte para leitor de tela
- **Primitivas combináveis**: crie componentes complexos a partir de blocos de construção simples
- **Framework agnóstico**: Funciona com React, mas estilos funcionam em qualquer lugar

## Quando usar esta habilidade

- Criação de um sistema de design personalizado do zero
- Construindo bibliotecas de componentes de UI acessíveis
- Implementação de componentes interativos complexos (Dialog, Dropdown, Tabs, etc.)
- Migração de bibliotecas de componentes estilizados para primitivos sem estilo
- Configuração de sistemas temáticos com variáveis CSS ou Tailwind
- Precisa de controle total sobre o comportamento e estilo dos componentes
- Criação de aplicativos que exigem conformidade com WCAG 2.1 AA/AAA

## Não use esta habilidade quando

- Você precisa de componentes pré-estilizados prontos para uso (use shadcn/ui, Mantine, etc.)
- Construindo páginas estáticas simples sem interatividade
- O projeto não usa React 16.8+ (Radix requer ganchos)
- Você precisa de componentes para estruturas diferentes do React

## Princípios Fundamentais

### 1. Acessibilidade em primeiro lugar

Cada primitiva Radix é construída tendo a acessibilidade como base:

- **Navegação pelo teclado**: suporte completo ao teclado (Tab, teclas de seta, Enter, Escape)
- **Leitores de tela**: atributos ARIA adequados e regiões ativas
- **Gerenciamento de foco**: captura e restauração automática de foco
- **Estados desativados**: Tratamento adequado de desativado e desativado por aria

**Regra**: nunca substitua os recursos de acessibilidade. Melhore, não substitua.

### 2. Arquitetura sem cabeça

Radix fornece **comportamento**, você fornece **aparência**:

// ✅ Radix oferece comportamento, você adiciona estilo
<Dialog.Root>
  <Dialog.Trigger className="estilos de seu botão" />
  <Dialog.Content className="seus estilos modais" />
</Dialog.Root>
```

### 3. Composição sobre configuração

Construa componentes complexos a partir de primitivos simples:

## Primeiros passos

### Instalação

# Ou instale vários de uma vez
npm install @radix-ui/react-{dialog, menu suspenso, guias, dica de ferramenta}

# Para estilização (opcional, mas comum)
npm install clsx tailwind-merge autoridade de variação de classe
```

### Padrão de Componente Básico

Cada componente Radix segue este padrão:

função de exportação MyDialog() {
  retornar (
    <Dialog.Root>
      {/* Acione a caixa de diálogo */}
      <Dialog.Trigger asChild>
        <button className="trigger-styles">Abrir</button>
      </Dialog.Trigger>

      {/* O portal é renderizado fora da hierarquia do DOM */}
      <Dialog.Portal>
        {/* Sobreposição (pano de fundo) */}
        <Dialog.Overlay className="estilos de sobreposição" />
        
        {/* Conteúdo (modal) */}
        <Dialog.Content className="estilos de conteúdo">
          <Dialog.Title>Título</Dialog.Title>
          <Dialog.Description>Descrição</Dialog.Description>
          
          {/* Seu conteúdo aqui */}
          
          <Dialog.Fechar asChild>
            <botão>Fechar</button>
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

## Estratégias temáticas

### Estratégia 1: Variáveis CSS (Framework-Agnostic)

**Ideal para**: Máxima portabilidade, compatível com SSR

[data-theme="escuro"] {
  --cor primária: 220 90% 66%;
  --superfície colorida: 222 47% 11%;
}
```

### Estratégia 2: Tailwind + CVA (Autoridade de Variação de Classe)

**Ideal para**: projetos Tailwind, componentes com muitas variantes

```tsx
import { styled } from '@stitches/react';
import * as Dialog from '@radix-ui/react-dialog';

---

```tsx
// Select.tsx
import * as Select from '@radix-ui/react-select';
import { CheckIcon, ChevronDownIcon } from '@radix-ui/react-icons';

```tsx
// ✅ Render as Next.js Link but keep Radix behavior
<Dialog.Trigger asChild>
  <Link href="/settings">Open Settings</Link>
</Dialog.Trigger>

```tsx
// Uncontrolled (Radix manages state)
<Tabs.Root defaultValue="tab1">
  <Tabs.Trigger value="tab1">Tab 1</Tabs.Trigger>
</Tabs.Root>

```tsx
import * as Dialog from '@radix-ui/react-dialog';
import { motion, AnimatePresence } from 'framer-motion';

---

```tsx
<Dialog.Root> {/* State container */}
  <Dialog.Trigger /> {/* Opens dialog */}
  <Dialog.Portal> {/* Renders in portal */}
    <Dialog.Overlay /> {/* Backdrop */}
    <Dialog.Content> {/* Modal content */}
      <Dialog.Title /> {/* Required for a11y */}
      <Dialog.Description /> {/* Required for a11y */}
      <Dialog.Close /> {/* Closes dialog */}
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

```tsx
<DropdownMenu.Root>
  <DropdownMenu.Trigger />
  <DropdownMenu.Portal>
    <DropdownMenu.Content>
      <DropdownMenu.Item />
      <DropdownMenu.Separator />
      <DropdownMenu.CheckboxItem />
      <DropdownMenu.RadioGroup>
        <DropdownMenu.RadioItem />
      </DropdownMenu.RadioGroup>
      <DropdownMenu.Sub> {/* Nested menus */}
        <DropdownMenu.SubTrigger />
        <DropdownMenu.SubContent />
      </DropdownMenu.Sub>
    </DropdownMenu.Content>
  </DropdownMenu.Portal>
</DropdownMenu.Root>
```

```tsx
<Tabs.Root defaultValue="tab1">
  <Tabs.List>
    <Tabs.Trigger value="tab1" />
    <Tabs.Trigger value="tab2" />
  </Tabs.List>
  <Tabs.Content value="tab1" />
  <Tabs.Content value="tab2" />
</Tabs.Root>
```

```tsx
<Tooltip.Provider delayDuration={200}>
  <Tooltip.Root>
    <Tooltip.Trigger />
    <Tooltip.Portal>
      <Tooltip.Content side="top" align="center">
        Tooltip text
        <Tooltip.Arrow />
      </Tooltip.Content>
    </Tooltip.Portal>
  </Tooltip.Root>
</Tooltip.Provider>
```

```tsx
<Popover.Root>
  <Popover.Trigger />
  <Popover.Portal>
    <Popover.Content side="bottom" align="start">
      Content
      <Popover.Arrow />
      <Popover.Close />
    </Popover.Content>
  </Popover.Portal>
</Popover.Root>
```

---

const buttonVariantes = cva(
  //Estilos básicos
  "inline-flex items-center justificar-center arredondado-md fonte-médio transição-cores foco-visível:contorno-nenhum desativado:ponteiro-eventos-nenhum desativado:opacidade-50",
  {
    variantes: {
      variante: {
        padrão: "bg-primary text-primary-foreground hover:bg-primary/90",
        destrutivo: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        esboço: "border border-input bg-background hover:bg-accent",
        fantasma: "hover:bg-accent hover:text-accent-foreground",
      },
      tamanho: {
        padrão: "h-10 px-4 py-2",
        sm: "h-9 arredondado-md px-3",
        lg: "h-11 arredondado-md px-8",
        ícone: "h-10 w-10",
      },
    },
    Variantes padrão: {
      variante: "padrão",
      tamanho: "padrão",
    },
  }
);

interface ButtonProps estende VariantProps<typeof buttonVariants> {
  filhos: React.ReactNode;
}

função de exportação Button({ variante, tamanho, filhos }: ButtonProps) {
  retornar (
    <button className={cn(buttonVariants({variant, size }))}>
      {crianças}
    </button>
  );
}
```

### Estratégia 3: Pontos (CSS-in-JS)

**Ideal para**: temas de tempo de execução, estilos com escopo

const StyledContent = styled(Dialog.Content, {
  cor de fundo: '$superfície',
  borderRadius: '$md',
  preenchimento: '$ 6',
  
  variantes: {
    tamanho: {
      pequeno: {largura: '300px'},
      médio: {largura: '500px'},
      grande: {largura: '700px'},
    },
  },
  
  Variantes padrão: {
    tamanho: 'médio',
  },
});
```

## Padrões de componentes

### Padrão 1: Componentes compostos com contexto

**Caso de uso**: Compartilhe estado entre partes primitivas

função de exportação CustomSelect({itens, espaço reservado, onValueChange }) {
  retornar (
    <Select.Root onValueChange={onValueChange}>
      <Select.Trigger className="select-trigger">
        <Select.Value placeholder={placeholder} />
        <Selecionar.Ícone>
          <ChevronDownIcon />
        </Select.Icon>
      </Select.Trigger>

      <Selecionar.Portal>
        <Select.Content className="select-content">
          <Selecionar.Viewport>
            {items.map((item) => (
              <Selecionar.Item 
                chave={item.valor} 
                valor={item.valor}
                className="selecionar item"
              >
                <Select.ItemText>{item.label}</Select.ItemText>
                <Select.ItemIndicator>
                  <CheckIcon />
                </Select.ItemIndicator>
              </Select.Item>
            ))}
          </Select.Viewport>
        </Select.Content>
      </Select.Portal>
    </Select.Root>
  );
}
```

### Padrão 2: Componentes Polimórficos com `asChild`

**Caso de uso**: renderize como elementos diferentes sem perder comportamento

// ✅ Renderizar como componente personalizado
<DropdownMenu.Item asChild>
  <YourCustomButton icon={<Icon />}>Ação</YourCustomButton>
</DropdownMenu.Item>
```

**Por que `asChild` é importante**: Evita problemas de botões/links aninhados na árvore de acessibilidade.

### Padrão 3: Controlado vs Não Controlado

// Controlado (você gerencia o estado)
const [activeTab, setActiveTab] = useState('tab1');

<Tabs.Root valor={activeTab} onValueChange={setActiveTab}>
  <Tabs.Trigger value="tab1">Guia 1</Tabs.Trigger>
</Tabs.Root>
```

**Regra**: Use controlado quando precisar sincronizar com estado externo (URL, Redux, etc.).

### Padrão 4: Animação com Framer Motion

função de exportação AnimatedDialog({ open, onOpenChange }) {
  retornar (
    <Dialog.Root open={open} onOpenChange={onOpenChange}>
      <Dialog.Portal forceMount>
        <AnimatePresença>
          {abrir && (
            <>
              <Dialog.Overlay asChild>
                <motion.div
                  inicial={{ opacidade: 0 }}
                  animar={{ opacidade: 1 }}
                  saída={{ opacidade: 0 }}
                  className="sobreposição de diálogo"
                />
              </Dialog.Overlay>
              
              <Dialog.Content asChild>
                <motion.div
                  inicial={{ opacidade: 0, escala: 0,95 }}
                  animate={{ opacidade: 1, escala: 1 }}
                  saída={{ opacidade: 0, escala: 0,95 }}
                  className="dialog-content"
                >
                  {/* Conteúdo */}
                </motion.div>
              </Dialog.Content>
            </>
          )}
        </AnimatePresence>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

## Referência de Primitivos Comuns

### Caixa de diálogo (modal)

### Menu suspenso

### Guias

### Dica de ferramenta

### Popover

## Lista de verificação de acessibilidade

### Cada componente deve ter:

---

---

```tsx
import * as Dialog from '@radix-ui/react-dialog';
import { Command } from 'cmdk';

```tsx
import * as DropdownMenu from '@radix-ui/react-dropdown-menu';
import { DotsHorizontalIcon } from '@radix-ui/react-icons';

```tsx
import * as Select from '@radix-ui/react-select';
import { useForm, Controller } from 'react-hook-form';

- [ ] **Gerenciamento de foco**: indicadores de foco visíveis em todos os elementos interativos
- [] **Navegação pelo teclado**: suporte completo ao teclado (Tab, Setas, Enter, Esc)
- [ ] **Rótulos ARIA**: rótulos significativos para leitores de tela
- [ ] **Contraste de cores**: WCAG AA mínimo (4,5:1 para texto, 3:1 para UI)
- [ ] **Estados de erro**: Limpe mensagens de erro com `aria-invalid` e `aria-describedby`
- [ ] **Estados de carregamento**: `aria-busy` adequado durante operações assíncronas

### Específico da caixa de diálogo:
- [ ] `Dialog.Title` está presente (obrigatório para leitores de tela)
- [] `Dialog.Description` fornece contexto
- [] Foco preso dentro do modal quando aberto
- [] Tecla Escape fecha a caixa de diálogo
- [] O foco retorna ao disparo no fechamento

### Específico do menu suspenso:
- [] As teclas de seta navegam pelos itens
- [] A pesquisa por digitação antecipada funciona
- [] Comportamento de empacotamento do primeiro/último item
- [] Estado selecionado indicado visualmente e com ARIA

## Melhores práticas

### ✅ Faça isso

1. **Sempre use `asChild` para evitar divs wrapper**
   ```tsx
   <Dialog.Trigger asChild>
     <botão>Abrir</button>
   </Dialog.Trigger>
   ```

2. **Forneça HTML semântico**
   ```tsx
   <Dialog.Content asChild>
     <artigo role="dialog" aria-labelledby="title">
       {/* conteúdo */}
     </artigo>
   </Dialog.Content>
   ```

3. **Use variáveis CSS para temas**
   ```css
   .dialog-content {
     plano de fundo: hsl(var(--superfície));
     cor: hsl(var(--na-superfície));
   }
   ```

4. **Compor primitivas para componentes complexos**
   ```tsx
   function CommandPalette() {
     retornar (
       <Dialog.Root>
         <Dialog.Conteúdo>
           <Combobox /> {/* Radix Combobox dentro da caixa de diálogo */}
         </Dialog.Content>
       </Dialog.Root>
     );
   }
   ```

### ❌ Não faça isso

1. **Não pule as partes de acessibilidade**
   ```tsx
   // ❌ Título e descrição ausentes
   <Dialog.Conteúdo>
     <div>Conteúdo</div>
   </Dialog.Content>
   ```

2. **Não lute contra os primitivos**
   ```tsx
   // ❌ Substituindo o comportamento interno
   <Dialog.Content onClick={(e) => e.stopPropagation()}>
   ```

3. **Não misture controlado e descontrolado**
   ```tsx
   // ❌ Gerenciamento de estado inconsistente
   <Tabs.Root defaultValue="tab1" value={activeTab}>
   ```

4. **Não ignore a navegação pelo teclado**
   ```tsx
   // ❌ Desativando o comportamento do teclado
   <DropdownMenu.Item onKeyDown={(e) => e.preventDefault()}>
   ```

## Exemplos do mundo real

### Exemplo 1: Paleta de comandos (caixa de diálogo combinada)

função de exportação CommandPalette() {
  const [abrir, setOpen] = useState(false);

  useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setOpen((abrir) => !abrir);
      }
    };
    document.addEventListener('keydown', para baixo);
    return () => document.removeEventListener('keydown', para baixo);
  }, []);

  retornar (
    <Dialog.Root open={open} onOpenChange={setOpen}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/50" />
        <Dialog.Content className="fixo left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">
          <Comando>
            <Command.Input placeholder="Digite um comando..." />
            <Comando.Lista>
              <Command.Empty>Nenhum resultado encontrado.</Command.Empty>
              <Command.Group header="Sugestões">
                <Command.Item>Calendário</Command.Item>
                <Command.Item>Pesquisar Emoji</Command.Item>
              </Command.Group>
            </Command.List>
          </Command>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Exemplo 2: Menu suspenso com ícones

função de exportação ActionsMenu() {
  retornar (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        <button className="icon-button" aria-label="Ações">
          <PontosHorizontalIcon />
        </button>
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content className="dropdown-content" align="end">
          <DropdownMenu.Item className="dropdown-item">
            Editar
          </DropdownMenu.Item>
          <DropdownMenu.Item className="dropdown-item">
            Duplicar
          </DropdownMenu.Item>
          <DropdownMenu.Separator className="dropdown-separator" />
          <DropdownMenu.Item className="dropdown-item text-red-500">
            Excluir
          </DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}
```

### Exemplo 3: Formulário com Radix Select + React Hook Form

---

---

```tsx
// Lazy load heavy primitives
const Dialog = lazy(() => import('@radix-ui/react-dialog'));
const DropdownMenu = lazy(() => import('@radix-ui/react-dropdown-menu'));
```

```tsx
// Create portal container once
<Tooltip.Provider>
  {/* All tooltips share portal container */}
  <Tooltip.Root>...</Tooltip.Root>
  <Tooltip.Root>...</Tooltip.Root>
</Tooltip.Provider>
```

```tsx
// Memoize expensive render functions
const SelectItems = memo(({ items }) => (
  items.map((item) => <Select.Item key={item.value} value={item.value} />)
));
```

---

```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add dialog
```

```tsx
import { Theme, Button, Dialog } from '@radix-ui/themes';

---

---

---

---

interfaceFormData{
  país: string;
}

função de exportação CountryForm() {
  const { controle, handleSubmit } = useForm<FormData>();

  retornar (
    <formulário onSubmit={handleSubmit((dados) => console.log(dados))}>
      <Controlador
        nome="país"
        controle={controle}
        render={({ campo }) => (
          <Select.Root onValueChange={field.onChange} valor={field.value}>
            <Select.Trigger className="select-trigger">
              <Select.Value placeholder="Selecione um país" />
              <Selecionar.Ícone />
            </Select.Trigger>
            
            <Selecionar.Portal>
              <Select.Content className="select-content">
                <Selecionar.Viewport>
                  <Select.Item value="us">Estados Unidos</Select.Item>
                  <Select.Item value="ca">Canadá</Select.Item>
                  <Select.Item value="uk">Reino Unido</Select.Item>
                </Select.Viewport>
              </Select.Content>
            </Select.Portal>
          </Select.Root>
        )}
      />
      <button type="submit">Enviar</button>
    </form>
  );
}
```

## Solução de problemas

### Problema: a caixa de diálogo não fecha com a tecla Escape

**Causa**: evento `onEscapeKeyDown` evitado ou estado `open` não sincronizado

**Solução**:
```tsx
<Dialog.Root open={open} onOpenChange={setOpen}>
  {/* Não evita o padrão no escape */}
</Dialog.Root>
```

### Problema: o posicionamento do menu suspenso está desativado

**Causa**: o contêiner pai tem `overflow: hidden` ou transformação

**Solução**:
```tsx
// Use o Portal para renderizar fora do contêiner de overflow
<DropdownMenu.Portal>
  <DropdownMenu.Content />
</DropdownMenu.Portal>
```

### Problema: as animações não funcionam

**Causa**: o conteúdo do portal é desmontado imediatamente

**Solução**:
```tsx
//Use forceMount + AnimatePresence
<Dialog.Portal forceMount>
  <AnimatePresença>
    {abrir && <Dialog.Content />}
  </AnimatePresence>
</Dialog.Portal>
```

### Problema: erros de TypeScript com `asChild`

**Causa**: problemas de inferência de tipo com componentes polimórficos

**Solução**:
```tsx
// Digite explicitamente seu componente
<Dialog.Trigger asChild>
  <button type="button">Abrir</button>
</Dialog.Trigger>
```

## Otimização de desempenho

### 1. Divisão de código

### 2. Reutilização do contêiner do portal

### 3. Memoização

## Integração com ferramentas populares

### shadcn/ui (construído em Radix)

shadcn/ui é uma coleção de componentes de copiar e colar criados com Radix + Tailwind.

**Quando usar shadcn vs Radix bruto**:
- Use shadcn: prototipagem rápida, designs padrão
- Use Radix bruto: personalização total, designs exclusivos

### Temas Radix (sistema de estilo oficial)

função Aplicativo() {
  retornar (
    <Theme acentuaColor="crimson" greyColor="sand">
      <Button>Clique em mim</Button>
    </Tema>
  );
}
```

## Habilidades Relacionadas

- `@tailwind-design-system` - Padrões de integração Tailwind + Radix
- `@react-patterns` - Padrões de composição de reação
- `@frontend-design` - Arquitetura geral do frontend
- `@accessibility-compliance` - teste de conformidade WCAG

## Recursos

### Documentação Oficial
- [Documentos da UI do Radix](https://www.radix-ui.com/primitives)
- [Radix Colors](https://www.radix-ui.com/colors) - Sistema de cores acessível
- [Ícones Radix](https://www.radix-ui.com/icons) - Biblioteca de ícones

### Recursos da comunidade
- [shadcn/ui](https://ui.shadcn.com) - Coleção de componentes
- [Radix UI Discord](https://discord.com/invite/7Xb99uG) - Suporte da comunidade
- [Documentação CVA](https://cva.style/docs) - Gerenciamento de variantes

### Exemplos
- [Radix Playground](https://www.radix-ui.com/primitives/docs/overview/introduction#try-it-out)
- [fonte shadcn/ui](https://github.com/shadcn-ui/ui) - Exemplos de produção

## Referência rápida

### Instalação
```bash
npm install @radix-ui/react-{nome-primitivo}
```

### Padrão Básico
```tsx
<Primitivo.Root>
  <Primitivo.Trigger />
  <Primitivo.Portal>
    <Primitivo.Conteúdo />
  </Primitive.Portal>
</Primitive.Root>
```

### Principais acessórios
- `asChild` - Renderiza como elemento filho
- `defaultValue` - Padrão não controlado
- `value` / `onValueChange` - Estado controlado
- `open` / `onOpenChange` - Estado aberto
- `side` / `align` - Posicionamento

**Lembre-se**: Radix lhe dá **comportamento**, você dá **beleza**. A acessibilidade é integrada e a personalização é ilimitada.