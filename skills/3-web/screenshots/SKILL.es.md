---
name: screenshots
description: "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation."
source: "https://github.com/Shpigford/skills/tree/main/screenshots"
risk: safe
---

# Capturas de pantalla

Genere capturas de pantalla con calidad de marketing de su aplicación utilizando Playwright directamente. Las capturas de pantalla se capturan con una resolución HiDPI real (2x retina) usando `deviceScaleFactor: 2`.

## Cuándo utilizar esta habilidad

Utilice esta habilidad cuando:
- El usuario quiere crear capturas de pantalla para Product Hunt.
- Creación de capturas de pantalla para redes sociales.
- Generación de imágenes para páginas de destino.
- Creación de capturas de pantalla de documentación.
- El usuario solicita capturas de pantalla de la aplicación con calidad de marketing.

## Requisitos previos

El dramaturgo debe estar disponible. Compruébalo:
```golpecito
dramaturgo de npx --versión 2>/dev/null || npm ls dramaturgo 2>/dev/null | dramaturgo grep
```

Si no lo encuentra, informe al usuario:
> Se requiere dramaturgo. Instálelo con: `npm install -D playwright` o `npm install -D @playwright/test`

## Paso 1: determinar la URL de la aplicación

Si se proporciona `$1`, utilícelo como URL de la aplicación.

Si no se proporciona ninguna URL:
1. Compruebe si es probable que se esté ejecutando un servidor de desarrollo buscando los scripts `package.json`
2. Utilice `AskUserQuestion` para pedirle al usuario la URL u ofrecerle ayuda para iniciar el servidor de desarrollo.

URL predeterminadas comunes para sugerir:
- `http://localhost:3000` (Next.js, Crear aplicación React, Rails)
- `http://localhost:5173` (Vite)
- `http://localhost:4000` (Phoenix)
- `http://localhost:8080` (Vue CLI, genérico)

## Paso 2: Reúna los requisitos

Utilice `AskUserQuestion` con las siguientes preguntas:

**Pregunta 1: recuento de capturas de pantalla**
- Encabezado: "Contar"
- Pregunta: "¿Cuántas capturas de pantalla necesitas?"
- Opciones:
  - "3-5" - Conjunto rápido de funciones clave
  - "5-10" - Cobertura completa de funciones
  - "10+" - Paquete de marketing completo

**Pregunta 2: Propósito**
- Encabezado: "Propósito"
- Pregunta: "¿Para qué se utilizarán estas capturas de pantalla?"
- Opciones:
  - "Búsqueda de productos": fotografías de héroes y funciones destacadas
  - "Redes sociales" - Demostraciones de funciones llamativas
  - "Página de destino" - Secciones de marketing y beneficios
  - "Documentación" - Referencia de UI y tutoriales

**Pregunta 3: Autenticación**
- Encabezado: "Autenticación"
- Pregunta: "¿La aplicación requiere iniciar sesión para acceder a las funciones que desea capturar?"
- Opciones:
  - "No es necesario iniciar sesión" - Sólo páginas públicas
  - "Sí, proporcionaré las credenciales" - Primero debes iniciar sesión

Si el usuario selecciona "Sí, proporcionaré credenciales", haga preguntas de seguimiento:
- "¿Cuál es la URL de la página de inicio de sesión?" (por ejemplo, `/iniciar sesión`, `/iniciar sesión`)
- "¿Cuál es el correo electrónico/nombre de usuario?"
- "¿Cuál es la contraseña?"

El script detectará automáticamente los campos del formulario de inicio de sesión utilizando los localizadores inteligentes de Playwright.

## Paso 3: Analizar la base de código en busca de funciones

Explore a fondo el código base para comprender la aplicación e identificar oportunidades de captura de pantalla.

### 3.1: Lea la documentación primero

**Empieza siempre leyendo estos archivos** para entender lo que hace la aplicación:

1. **README.md** (y cualquier archivo README en los subdirectorios): lea el archivo README completo para comprender:
   - Qué es la aplicación y qué problema resuelve.
   - Funciones y capacidades clave
   - Capturas de pantalla o descripciones de funciones ya documentadas.

2. **CHANGELOG.md** o **HISTORY.md**: funciones recientes que vale la pena destacar

3. Directorio **docs/**: cualquier documentación adicional sobre funciones

### 3.2: Analizar rutas para buscar páginas

Lea la configuración de enrutamiento para descubrir todas las páginas disponibles:

| Marco | Archivo para leer | Qué buscar |
|-----------|--------------|------------------|
| **Enrutador de aplicaciones Next.js** | estructura de directorios `app/` | Cada carpeta con `page.tsx` es una ruta |
| **Enrutador de páginas Next.js** | directorio `páginas/` | Cada archivo es una ruta |
| **Rieles** | `config/rutas.rb` | Lea el archivo completo para todas las rutas |
| **Reaccionar enrutador** | Busque `createBrowserRouter` o `<Ruta` | Definiciones de rutas con caminos |
| **Enrutador Vue** | `src/router/index.js` o `router.js` | Matriz de rutas con definiciones de ruta |
| **Kit esbelto** | directorio `src/rutas/` | Cada carpeta con `+page.svelte` es una ruta |
| **Remezcla** | directorio `aplicación/rutas/` | Enrutamiento basado en archivos |
| **Laravel** | `rutas/web.php` | Definiciones de ruta |
| **Django** | Archivos `urls.py` | Patrones de URL |
| **Expreso** | Busque `app.get`, `router.get` | Manejadores de ruta |

**Importante**: Lea estos archivos, no se limite a comprobar si existen. Las definiciones de ruta le indican qué páginas están disponibles para capturas de pantalla.

### 3.3: Identificar componentes clave

Busque componentes que representen características que se pueden capturar en capturas de pantalla:

- Componentes del tablero
- Secciones de funciones con interfaz de usuario distinta
- Formularios y entradas interactivas.
- Visualizaciones de datos (cuadros, gráficos, tablas)
- Modales y diálogos.
- Navegación y barras laterales.
- Paneles de configuración
- Secciones de perfil de usuario

### 3.4: Verificación de activos de marketing

```bash
mkdir -p screenshots
```

```javascript
import { chromium } from 'playwright';

```bash
node screenshot-script.mjs
```

Busque contenido de marketing existente que indique características clave:
- Componentes de la página de destino (a menudo en `componentes/landing/` o `componentes/marketing/`)
- Componentes de la lista de características
- Tablas de precios
- Secciones de testimonios

### 3.5: Crear lista de funciones

Cree una lista completa de funciones descubiertas con:
- Nombre de la función (de README o nombre del componente)
- Ruta URL (desde rutas)
- Selector de CSS en el que centrarse (desde la estructura del componente)
- Estado de la interfaz de usuario requerido (iniciar sesión, datos completos, apertura modal, pestaña específica seleccionada)

## Paso 4: Planificar capturas de pantalla con el usuario

Presente las funciones descubiertas al usuario y pídale que confirme o modifique la lista.

Utilice `AskUserQuestion`:
- Encabezado: "Características"
- Pregunta: "Encontré estas características en tu código base. ¿Cuál te gustaría tomar una captura de pantalla?"
- Opciones: Enumere 3 o 4 características clave descubiertas, además de "Déjeme elegir algunas específicas".

Si el usuario quiere preguntas específicas, haga preguntas de seguimiento para aclarar exactamente qué capturar.

## Paso 5: Crear directorio de capturas de pantalla

## Paso 6: generar y ejecutar el script de dramaturgo

Cree un script Node.js que utilice Playwright con la configuración HiDPI adecuada. El guión debería:

1. **Utilice `deviceScaleFactor: 2`** para obtener una resolución de retina real
2. **Establezca la ventana gráfica en 1440x900** (produce imágenes de 2880x1800 píxeles)
3. **Manejar la autenticación** si se proporcionaron las credenciales
4. **Navega a cada página** y captura capturas de pantalla

### Plantilla de secuencia de comandos

Escriba este script en un archivo temporal (por ejemplo, `screenshot-script.mjs`) y ejecútelo:

const BASE_URL = '[APP_URL]';
const SCREENSHOTS_DIR = './capturas de pantalla';

// Configuración de autenticación (si es necesario)
constante AUTH = {
  necesario: [verdadero|falso],
  URL de inicio de sesión: '[LOGIN_URL]',
  correo electrónico: '[CORREO ELECTRÓNICO]',
  contraseña: '[CONTRASEÑA]',
};

// Capturas de pantalla para capturar
const CAPTURAS DE PANTALLA = [
  { nombre: '01-nombre-de-función', url: '/ruta', esperarPara: '[selector-opcional]' },
  { nombre: '02-otra-característica', url: '/otra-ruta' },
  // ... agrega todas las capturas de pantalla planificadas
];

función asíncrona principal() {
  navegador constante = esperar chromium.launch();

  // Crear contexto con configuración HiDPI
  contexto constante = esperar navegador.newContext({
    ventana gráfica: {ancho: 1440, alto: 900},
    deviceScaleFactor: 2, // Esta es la clave para capturas de pantalla reales de retina
  });

  página constante = espera contexto.newPage();

  // Manejar la autenticación si es necesario
  si (AUTH.necesaria) {
    console.log('Iniciando sesión...');
    espere página.goto(AUTH.loginUrl);

    // Inicio de sesión inteligente: pruebe varios patrones comunes para el campo de correo electrónico/nombre de usuario
    const emailField = página.locator([
      'entrada[tipo="correo electrónico"]',
      'entrada[nombre="correo electrónico"]',
      'entrada[id="correo electrónico"]',
      'entrada[placeholder*="correo electrónico" i]',
      'entrada[nombre="nombre de usuario"]',
      'entrada[id="nombre de usuario"]',
      'entrada[tipo="texto"]',
    ].join(', ')).primero();
    espere emailField.fill(AUTH.email);

    // Inicio de sesión inteligente: pruebe varios patrones comunes para el campo de contraseña
    const campocontraseña = página.localizador([
      'entrada[tipo="contraseña"]',
      'entrada[nombre="contraseña"]',
      'entrada[id="contraseña"]',
    ].join(', ')).primero();
    espere contraseñaField.fill(AUTH.contraseña);

    // Inicio de sesión inteligente: pruebe varios patrones comunes para el botón de envío
    const enviarBotón = página.localizador([
      'botón[tipo="enviar"]',
      'entrada[tipo="enviar"]',
      'botón:has-text("Iniciar sesión")',
      'botón:has-text("Iniciar sesión")',
      'botón:tiene-texto("Iniciar sesión")',
      'botón:tiene-texto("Enviar")',
    ].join(', ')).primero();
    espere enviarButton.click();

    espere página.waitForLoadState('networkidle');
    console.log('Inicio de sesión completo');
  }

  // Captura cada captura de pantalla
  para (toma constante de CAPTURAS DE PANTALLA) {
    console.log(`Capturando: ${shot.name}`);
    espere página.goto(`${BASE_URL}${shot.url}`);
    espere página.waitForLoadState('networkidle');

    // Opcional: esperar por un elemento específico
    si (disparo.esperar) {
      espera página.waitForSelector(shot.waitFor);
    }

    // Opcional: realizar acciones antes de la captura de pantalla
    si (disparo.acciones) {
      para (acción constante de shot.actions) {
        si (acción.clic) espera página.clic(acción.clic);
        si (acción.relleno) espera página.relleno (acción.relleno.selector, acción.relleno.valor);
        si (action.wait) espera página.waitForTimeout(action.wait);
      }
    }

    espera página.captura de pantalla ({
      ruta: `${SCREENSHOTS_DIR}/${shot.name}.png`,
      página completa: toma.página completa || falso,
    });
    console.log(` Guardado: ${shot.name}.png`);
  }

  espere navegador.close();
  console.log('¡Listo!');
}

main().catch(consola.error);
```

### Ejecutando el script

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

Después de ejecutar, limpie el script temporal:
```golpecito
rm captura de pantalla-script.mjs
```

## Paso 7: Opciones avanzadas de captura de pantalla

### Capturas de pantalla centradas en elementos

Para capturar un elemento específico en lugar de la ventana gráfica completa:

### Capturas de pantalla de página completa

Para contenido desplazable, capture la página completa:

### Esperando animaciones

Si la página tiene animaciones, espera a que se completen:

### Hacer clic en elementos antes de la captura de pantalla

Para capturar un estado modal, desplegable o flotante:

### Capturas de pantalla en modo oscuro

Si la aplicación admite el modo oscuro:

## Paso 8: Convención de nomenclatura de archivos

Utilice nombres de archivo descriptivos, tipo kebab, con prefijos numéricos para realizar pedidos:

| Característica | Nombre de archivo |
|---------|----------|
| Descripción general del panel | `01-panel-descripción general.png` |
| Gestión de enlaces | `02-enlace-bandeja de entrada.png` |
| Editor de edición | `03-edición-editor.png` |
| Análisis | `04-analítica.png` |
| Configuración | `05-configuración.png` |

## Paso 9: Verificar y resumir

Después de realizar todas las capturas de pantalla, verifique los resultados:

Proporcionar un resumen al usuario:

1. Enumere todos los archivos generados con sus rutas.
2. Confirme la resolución (debe ser 2880x1800 para retina 2x en una ventana gráfica de 1440x900)
3. Mencione el tamaño total de los archivos
4. Sugerir acciones de seguimiento.

Salida de ejemplo:
```
Se generaron 5 capturas de pantalla de marketing:

capturas de pantalla/
├── 01-dashboard-overview.png (1,2 MB, 2880x1800 @ 2x)
├── 02-link-inbox.png (456 KB, 2880x1800 @ 2x)
├── 03-edición-editor.png (890 KB, 2880x1800 @ 2x)
├── 04-analytics.png (567 KB, 2880x1800 @ 2x)
└── 05-configuraciones.png (234 KB, 2880x1800 @ 2x)

Todas las capturas de pantalla tienen verdadera calidad de retina (2x deviceScaleFactor) y están listas para su uso en marketing.
```

## Manejo de errores

- **Dramaturgo no encontrado**: Sugerir `npm install -D dramaturgo`
- **La página no se carga**: compruebe si el servidor de desarrollo se está ejecutando, sugiera iniciarlo
- **Error de inicio de sesión**: los localizadores inteligentes prueban patrones comunes pero pueden fallar en formularios de inicio de sesión inusuales. Si el inicio de sesión falla, analice el HTML de la página de inicio de sesión para encontrar los selectores correctos y personalizar el script.
- **Elemento no encontrado**: verifique el selector de CSS, ofrezca tomar una captura de pantalla de página completa en su lugar
- **Captura de pantalla fallida**: verifique el espacio en disco, verifique los permisos de escritura en el directorio de capturas de pantalla

## Consejos para obtener mejores resultados

1. **Estado limpio de la interfaz de usuario**: utilice datos de demostración/semillas para obtener contenido realista
2. **Tamaño consistente**: use la misma ventana gráfica para todas las capturas de pantalla
3. **Esperar contenido**: utilice `waitForLoadState('networkidle')` para garantizar que se cargue todo el contenido.
4. **Ocultar herramientas de desarrollo**: asegúrese de que no haya extensiones de navegador ni superposiciones de desarrollo visibles
5. **Variantes del modo oscuro**: considere capturar tanto el modo claro como el oscuro si es compatible