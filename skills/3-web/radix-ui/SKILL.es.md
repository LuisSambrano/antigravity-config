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

# Sistema de diseño de interfaz de usuario Radix

Cree sistemas de diseño accesibles y listos para producción utilizando las primitivas de la interfaz de usuario de Radix con control de personalización total y sin opiniones de estilo.

## Descripción general

Radix UI proporciona componentes accesibles y sin estilo (primitivos) que puede personalizar para que coincidan con cualquier sistema de diseño. Esta habilidad lo guía en la creación de bibliotecas de componentes escalables con Radix UI, enfocándose en el diseño que prioriza la accesibilidad, la arquitectura temática y los patrones componibles.

**Fortalezas clave:**
- **Sin cabeza por diseño**: control total del estilo sin tener que luchar contra los valores predeterminados
- **Accesibilidad integrada**: compatible con WAI-ARIA, navegación con teclado, compatibilidad con lector de pantalla
- **Primitivas componibles**: cree componentes complejos a partir de bloques de construcción simples
- **Independiente del marco**: funciona con React, pero los estilos funcionan en cualquier lugar

## Cuándo utilizar esta habilidad

- Creación de un sistema de diseño personalizado desde cero.
- Creación de bibliotecas de componentes de interfaz de usuario accesibles
- Implementación de componentes interactivos complejos (Diálogo, Menú desplegable, Pestañas, etc.)
- Migración de bibliotecas de componentes con estilo a primitivas sin estilo
- Configuración de sistemas de tematización con variables CSS o Tailwind
- Necesita control total sobre el comportamiento y el estilo de los componentes.
- Creación de aplicaciones que requieren cumplimiento con WCAG 2.1 AA/AAA

## No uses esta habilidad cuando

- Necesita componentes prediseñados listos para usar (use shadcn/ui, Mantine, etc.)
- Creación de páginas estáticas simples sin interactividad.
- El proyecto no utiliza React 16.8+ (Radix requiere ganchos)
- Necesita componentes para marcos distintos a React

## Principios básicos

### 1. Accesibilidad primero

Cada primitiva de Radix se construye con la accesibilidad como base:

- **Navegación con teclado**: soporte completo de teclado (Tab, teclas de flecha, Enter, Escape)
- **Lectores de pantalla**: atributos ARIA adecuados y regiones en vivo
- **Gestión de enfoque**: captura y restauración automática de enfoque
- **Estados discapacitados**: manejo adecuado de discapacitados y aria-discapacitados

**Regla**: Nunca anules las funciones de accesibilidad. Mejorar, no reemplazar.

### 2. Arquitectura sin cabeza

Radix proporciona **comportamiento**, tú proporcionas **apariencia**:

// ✅ Radix te da comportamiento, le agregas estilo
<Diálogo.Raíz>
  <Dialog.Trigger className="tus-estilos-de-botones" />
  <Dialog.Content className="tus-estilos-modales" />
</Dialog.Root>
```

### 3. Composición sobre configuración

Construya componentes complejos a partir de primitivas simples:

## Empezando

### Instalación

# O instalar varios a la vez
npm install @radix-ui/react-{diálogo, menú desplegable, pestañas, información sobre herramientas}

# Para estilo (opcional pero común)
npm install clsx tailwind-merge clase-varianza-autoridad
```

### Patrón de componentes básicos

Cada componente de Radix sigue este patrón:

función de exportación MyDialog() {
  regresar (
    <Diálogo.Raíz>
      {/* Activar el diálogo */}
      <Dialog.Trigger asChild>
        <button className="trigger-styles">Abrir</button>
      </Dialog.Trigger>

      {/* El portal se representa fuera de la jerarquía DOM */}
      <Portal.de.diálogo>
        {/* Superposición (fondo) */}
        <Dialog.Overlay className="estilos de superposición" />
        
        {/* Contenido (modal) */}
        <Dialog.Content className="estilos de contenido">
          <Dialog.Title>Título</Dialog.Title>
          <Dialog.Description>Descripción</Dialog.Description>
          
          {/* Tu contenido aquí */}
          
          <Diálogo.Cerrar como hijo>
            <botón>Cerrar</botón>
          </Dialog.Close>
        </Dialog.Contenido>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

## Estrategias de temática

### Estrategia 1: Variables CSS (agnósticas del marco)

**Mejor para**: Máxima portabilidad, compatible con SSR

[tema-datos="oscuro"] {
  --color-primario: 220 90% 66%;
  --color-superficie: 222 47% 11%;
}
```

### Estrategia 2: Viento de cola + CVA (Autoridad de variación de clase)

**Mejor para**: proyectos Tailwind, componentes con muchas variantes

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

botón constanteVariantes = cva(
  // estilos básicos
  "elementos en línea-flexibles-centro justificar-centro fuente-md redondeada-colores-de transición medios foco-visible: contorno-ninguno deshabilitado: puntero-eventos-ninguno deshabilitado: opacidad-50",
  {
    variantes: {
      variante: {
        predeterminado: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructivo: "bg-destructivo texto-destructivo-primer plano hover:bg-destructivo/90",
        esquema: "borde borde-entrada bg-fondo hover:bg-acento",
        fantasma: "hover:bg-accent hover:text-accent-foreground",
      },
      tamaño: {
        predeterminado: "h-10 px-4 py-2",
        sm: "h-9 redondeado-md px-3",
        lg: "h-11 redondeado-md px-8",
        icono: "h-10 w-10",
      },
    },
    Variantes predeterminadas: {
      variante: "predeterminado",
      tamaño: "predeterminado",
    },
  }
);

interfaz ButtonProps extiende VariantProps<typeof buttonVariants> {
  niños: React.ReactNode;
}

Botón de función de exportación ({variante, tamaño, hijos}: ButtonProps) {
  regresar (
    <nombre de clase del botón={cn(buttonVariants({ variante, tamaño }))}>
      {niños}
    </botón>
  );
}
```

### Estrategia 3: Puntadas (CSS-in-JS)

**Mejor para**: temas en tiempo de ejecución, estilos con alcance

const Contenido con estilo = con estilo (Contenido de diálogo, {
  color de fondo: '$superficie',
  borderRadius: '$md',
  relleno: '$6',
  
  variantes: {
    tamaño: {
      pequeño: { ancho: '300px' },
      medio: { ancho: '500px' },
      grande: { ancho: '700px' },
    },
  },
  
  Variantes predeterminadas: {
    tamaño: 'mediano',
  },
});
```

## Patrones de componentes

### Patrón 1: componentes compuestos con contexto

**Caso de uso**: compartir estado entre partes primitivas

función de exportación CustomSelect({ elementos, marcador de posición, onValueChange }) {
  regresar (
    <Seleccionar.Root onValueChange={onValueChange}>
      <Select.Trigger className="select-trigger">
        <Select.Value placeholder={placeholder} />
        <Seleccionar.Icono>
          <ChevronDownIcon/>
        </Seleccionar.Icono>
      </Seleccionar.Trigger>

      <Seleccionar.Portal>
        <Seleccionar.Contenido className="seleccionar-contenido">
          <Seleccionar.Vista>
            {elementos.mapa((elemento) => (
              <Seleccionar.elemento 
                clave = {elemento.valor} 
                valor={elemento.valor}
                className="seleccionar-elemento"
              >
                <Select.ItemText>{item.label}</Select.ItemText>
                <Seleccionar.Indicador de elemento>
                  <Icono de verificación />
                </Select.ItemIndicator>
              </Seleccionar.Artículo>
            ))}
          </Seleccionar.Vista>
        </Seleccionar.Contenido>
      </Seleccionar.Portal>
    </Seleccionar.Raíz>
  );
}
```

### Patrón 2: Componentes polimórficos con `asChild`

**Caso de uso**: renderizar como elementos diferentes sin perder comportamiento

// ✅ Renderizar como componente personalizado
<Menú desplegable.Elemento como hijo>
  <YourCustomButton icon={<Icon />}>Acción</YourCustomButton>
</DropdownMenu.Item>
```

**Por qué es importante `asChild`**: evita problemas de botones/vínculos anidados en el árbol de accesibilidad.

### Patrón 3: controlado versus no controlado

// Controlado (Tú gestionas el estado)
const [activeTab, setActiveTab] = useState('tab1');

<Tabs.Valor raíz={activeTab} onValueChange={setActiveTab}>
  <Tabs.Trigger value="tab1">Pestaña 1</Tabs.Trigger>
</Tabs.Root>
```

**Regla**: Úselo controlado cuando necesite sincronizar con un estado externo (URL, Redux, etc.).

### Patrón 4: Animación con Framer Motion

función de exportación AnimatedDialog({ abrir, onOpenChange }) {
  regresar (
    <Dialog.Root open={open} onOpenChange={onOpenChange}>
      <Dialog.Portal forceMount>
        <AnimarPresencia>
          {abrir && (
            <>
              <Diálogo.Superponer como hijo>
                <movimiento.div
                  inicial={{ opacidad: 0 }}
                  animar={{ opacidad: 1 }}
                  salida = {{ opacidad: 0 }}
                  className="superposición de diálogo"
                />
              </Dialog.Overlay>
              
              <Diálogo.Contenido como hijo>
                <movimiento.div
                  inicial={{ opacidad: 0, escala: 0,95 }}
                  animar = {{ opacidad: 1, escala: 1 }}
                  salida = {{ opacidad: 0, escala: 0,95 }}
                  className="contenido de diálogo"
                >
                  {/* Contenido */}
                </movimiento.div>
              </Dialog.Contenido>
            </>
          )}
        </AnimatePresencia>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

## Referencia de primitivas comunes

### Diálogo (modal)

### Menú desplegable

### Pestañas

### Información sobre herramientas

### popover

## Lista de verificación de accesibilidad

### Cada componente debe tener:

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

- [] **Gestión de enfoque**: indicadores de enfoque visibles en todos los elementos interactivos
- [] **Navegación con el teclado**: compatibilidad total con el teclado (Tab, Flechas, Intro, Esc)
- [] **Etiquetas ARIA**: etiquetas significativas para lectores de pantalla
- [ ] **Contraste de color**: mínimo WCAG AA (4,5:1 para texto, 3:1 para interfaz de usuario)
- [] **Estados de error**: borra los mensajes de error con `aria-invalid` y `aria-describedby`
- [] **Estados de carga**: `aria-busy` adecuado durante operaciones asíncronas

### Específico del cuadro de diálogo:
- [] `Dialog.Title` está presente (obligatorio para lectores de pantalla)
- [] `Dialog.Description` proporciona contexto
- [] Enfoque atrapado dentro del modal cuando está abierto
- [] La tecla Escape cierra el diálogo
- [] El enfoque vuelve al disparador al cerrar

### Menú desplegable específico:
- [] Las teclas de flecha navegan por los elementos
- [] La búsqueda de escritura anticipada funciona
- [] Comportamiento de ajuste del primer/último artículo
- [] Estado seleccionado indicado visualmente y con ARIA

## Mejores prácticas

### ✅ Haz esto

1. **Utilice siempre `asChild` para evitar divs contenedores**
   ```tsx
   <Dialog.Trigger asChild>
     <botón>Abrir</botón>
   </Dialog.Trigger>
   ```

2. **Proporcionar HTML semántico**
   ```tsx
   <Diálogo.Contenido como hijo>
     <artículo rol="diálogo" aria-labelledby="título">
       {/* contenido */}
     </artículo>
   </Dialog.Contenido>
   ```

3. **Utilice variables CSS para la temática**
   ```css
   .contenido de diálogo {
     fondo: hsl(var(--superficie));
     color: hsl(var(--en-superficie));
   }
   ```

4. **Componga primitivas para componentes complejos**
   ```tsx
   función CommandPalette() {
     regresar (
       <Diálogo.Raíz>
         <Diálogo.Contenido>
           <Combobox /> {/* Radix Combobox dentro del cuadro de diálogo */}
         </Dialog.Contenido>
       </Dialog.Root>
     );
   }
   ```

### ❌ No hagas esto

1. **No te saltes las partes de accesibilidad**
   ```tsx
   // ❌ Falta título y descripción
   <Diálogo.Contenido>
     <div>Contenido</div>
   </Dialog.Contenido>
   ```

2. **No luches contra los primitivos**
   ```tsx
   // ❌ Anular el comportamiento interno
   <Dialog.Content onClick={(e) => e.stopPropagation()}>
   ```

3. **No mezcles controlado y no controlado**
   ```tsx
   // ❌ Gestión estatal inconsistente
   <Tabs.Root defaultValue="tab1" valor={activeTab}>
   ```

4. **No ignores la navegación con el teclado**
   ```tsx
   // ❌ Deshabilitar el comportamiento del teclado
   <DropdownMenu.Item onKeyDown={(e) => e.preventDefault()}>
   ```

## Ejemplos del mundo real

### Ejemplo 1: Paleta de comandos (diálogo combinado)

función de exportación CommandPalette() {
  const [abierto, setOpen] = useState(false);

  utilizarEfecto(() => {
    constante abajo = (e: KeyboardEvent) => {
      if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setOpen((abrir) => !abrir);
      }
    };
    document.addEventListener('keydown', abajo);
    return () => document.removeEventListener('keydown', abajo);
  }, []);

  regresar (
    <Dialog.Root open={open} onOpenChange={setOpen}>
      <Portal.de.diálogo>
        <Dialog.Overlay className="inserto fijo-0 bg-negro/50" />
        <Dialog.Content className="fijo izquierda-1/2 superior-1/2 -translate-x-1/2 -translate-y-1/2">
          <Comando>
            <Command.Input placeholder="Escriba un comando..." />
            <Lista.de.comandos>
              <Command.Empty>No se encontraron resultados.</Command.Empty>
              <Command.Group encabezado="Sugerencias">
                <Command.Item>Calendario</Command.Item>
                <Command.Item>Buscar emoji</Command.Item>
              </Comando.Grupo>
            </Command.List>
          </Comando>
        </Dialog.Contenido>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

### Ejemplo 2: Menú desplegable con iconos

función de exportación MenúAcciones() {
  regresar (
    <Menú desplegable.Raíz>
      <Menú desplegable.Activar como hijo>
        <botón className="icono-botón" aria-label="Acciones">
          <PuntosHorizontalIcon />
        </botón>
      </DropdownMenu.Trigger>

      <Menú desplegable.Portal>
        <DropdownMenu.Content className="dropdown-content" align="end">
          <DropdownMenu.Item className="elemento-desplegable">
            Editar
          </DropdownMenu.Item>
          <DropdownMenu.Item className="elemento-desplegable">
            Duplicar
          </DropdownMenu.Item>
          <DropdownMenu.Separator className="separador-desplegable" />
          <DropdownMenu.Item className="elemento desplegable texto-rojo-500">
            Eliminar
          </DropdownMenu.Item>
        </DropdownMenu.Contenido>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}
```

### Ejemplo 3: formulario con Radix Select + formulario React Hook

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

interfaz FormData {
  país: cadena;
}

función de exportación CountryForm() {
  const {control, handleSubmit} = useForm<FormData>();

  regresar (
    <formulario onSubmit={handleSubmit((datos) => console.log(datos))}>
      <Controlador
        nombre="país"
        controlar={controlar}
        renderizar = {({ campo }) => (
          <Select.Root onValueChange={field.onChange} valor={field.value}>
            <Select.Trigger className="select-trigger">
              <Select.Value placeholder="Seleccione un país" />
              <Seleccionar.Icono />
            </Seleccionar.Trigger>
            
            <Seleccionar.Portal>
              <Seleccionar.Contenido className="seleccionar-contenido">
                <Seleccionar.Vista>
                  <Select.Item value="us">Estados Unidos</Select.Item>
                  <Select.Item value="ca">Canadá</Select.Item>
                  <Select.Item value="uk">Reino Unido</Select.Item>
                </Seleccionar.Vista>
              </Seleccionar.Contenido>
            </Seleccionar.Portal>
          </Seleccionar.Raíz>
        )}
      />
      <botón tipo="enviar">Enviar</botón>
    </formulario>
  );
}
```

## Solución de problemas

### Problema: el cuadro de diálogo no se cierra con la tecla Escape

**Causa**: evento `onEscapeKeyDown` impedido o estado `abierto` no sincronizado

**Solución**:
```tsx
<Dialog.Root open={open} onOpenChange={setOpen}>
  {/* No evitar el valor predeterminado al escapar */}
</Dialog.Root>
```

### Problema: la posición del menú desplegable está desactivada

**Causa**: El contenedor principal tiene "desbordamiento: oculto" o se transforma

**Solución**:
```tsx
// Usa Portal para renderizar el contenedor de desbordamiento externo
<Menú desplegable.Portal>
  <Menú desplegable.Contenido />
</DropdownMenu.Portal>
```

### Problema: las animaciones no funcionan

**Causa**: El contenido del portal se desmonta inmediatamente

**Solución**:
```tsx
// Usa forceMount + AnimatePresence
<Dialog.Portal forceMount>
  <AnimarPresencia>
    {abrir && <Diálogo.Contenido />}
  </AnimatePresencia>
</Dialog.Portal>
```

### Problema: errores de TypeScript con `asChild`

**Causa**: Problemas de inferencia de tipos con componentes polimórficos

**Solución**:
```tsx
// Escribe explícitamente tu componente
<Dialog.Trigger asChild>
  <botón tipo="botón">Abrir</botón>
</Dialog.Trigger>
```

## Optimización del rendimiento

### 1. División de código

### 2. Reutilización del contenedor del portal

### 3. Memorización

## Integración con herramientas populares

### shadcn/ui (Construido en Radix)

shadcn/ui es una colección de componentes de copiar y pegar creados con Radix + Tailwind.

**Cuándo usar shadcn vs raw Radix**:
- Utilice shadcn: creación rápida de prototipos, diseños estándar
- Utilice Radix sin procesar: personalización total, diseños únicos

### Temas Radix (sistema de estilo oficial)

función aplicación() {
  regresar (
    <Tema acentoColor="carmesí" grisColor="arena">
      <Botón>Haz clic en mí</Botón>
    </Tema>
  );
}
```

## Habilidades relacionadas

- `@tailwind-design-system` - Patrones de integración Tailwind + Radix
- `@react-patterns` - Patrones de composición de React
- `@frontend-design` - Arquitectura general del frontend
- `@accessibility-compliance` - Pruebas de cumplimiento de WCAG

## Recursos

### Documentación oficial
- [Documentos de la interfaz de usuario de Radix] (https://www.radix-ui.com/primitives)
- [Colores Radix] (https://www.radix-ui.com/colors) - Sistema de color accesible
- [Iconos de Radix] (https://www.radix-ui.com/icons) - Biblioteca de iconos

### Recursos comunitarios
- [shadcn/ui](https://ui.shadcn.com) - Colección de componentes
- [Radix UI Discord] (https://discord.com/invite/7Xb99uG) - Soporte de la comunidad
- [Documentación CVA](https://cva.style/docs) - Gestión de variantes

### Ejemplos
- [Zona de juegos Radix] (https://www.radix-ui.com/primitives/docs/overview/introduction#try-it-out)
- [Fuente shadcn/ui](https://github.com/shadcn-ui/ui) - Ejemplos de producción

## Referencia rápida

### Instalación
```golpecito
npm install @radix-ui/react-{nombre-primitivo}
```

### Patrón básico
```tsx
<Raíz.primitiva>
  <Primitivo.Trigger />
  <Portal.primitivo>
    <Contenido.primitivo />
  </Primitivo.Portal>
</Primitivo.Root>
```

### Accesorios clave
- `asChild` - Representar como elemento hijo
- `defaultValue` - Valor predeterminado no controlado
- `value` / `onValueChange` - Estado controlado
- `open` / `onOpenChange` - Estado abierto
- `side` / `align` - Posicionamiento

**Recuerda**: Radix te da **comportamiento**, tú le das **belleza**. La accesibilidad está integrada y la personalización es ilimitada.