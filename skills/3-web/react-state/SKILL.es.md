---
name: react-state
description: Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state management solutions.
---

```
Small app, simple state → Zustand or Jotai
Large app, complex state → Redux Toolkit
Heavy server interaction → React Query + light client state
Atomic/granular updates → Jotai
```

```typescript
// store/useStore.ts
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

```typescript
// store/index.ts
import { configureStore } from '@reduxjs/toolkit'
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux'
import userReducer from './slices/userSlice'
import cartReducer from './slices/cartSlice'

```typescript
// store/slices/userSlice.ts
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit'

```typescript
// store/slices/createUserSlice.ts
import { StateCreator } from 'zustand'

# Reaccionar gestión del estado

Guía completa de los patrones modernos de gestión del estado de React, desde el estado de los componentes locales hasta los almacenes globales y la sincronización del estado del servidor.

## No uses esta habilidad cuando

- La tarea no está relacionada con la gestión del estado de reacción.
- Necesita un dominio o herramienta diferente fuera de este alcance.

## Instrucciones

- Aclarar objetivos, limitaciones y aportes requeridos.
- Aplicar las mejores prácticas relevantes y validar los resultados.
- Proporcionar pasos procesables y verificación.
- Si se requieren ejemplos detallados, abra `resources/implementation-playbook.md`.

## Usa esta habilidad cuando

- Configurar la gestión del estado global en una aplicación React
- Elegir entre Redux Toolkit, Zustand o Jotai
- Administrar el estado del servidor con React Query o SWR
- Implementación de actualizaciones optimistas.
- Depuración de problemas relacionados con el estado.
- Migración de Redux heredado a patrones modernos

## Conceptos básicos

### 1. Categorías estatales

| Tipo | Descripción | Soluciones |
|------|-------------|-----------|
| **Estado local** | Estado de la interfaz de usuario específico del componente | useState, useReducer |
| **Estado global** | Compartido entre componentes | Kit de herramientas Redux, Zustand, Jotai |
| **Estado del servidor** | Datos remotos, almacenamiento en caché | Consulta de reacción, SWR, consulta RTK |
| **Estado de la URL** | Parámetros de ruta, buscar | Reaccionar enrutador, nuqs |
| **Estado del formulario** | Valores de entrada, validación | Forma de gancho React, Formik |

### 2. Criterios de selección

## Inicio rápido

### Zustand (el más simple)

interfaz AppState {
  usuario: Usuario | nulo
  tema: 'luz' | 'oscuro'
  setUser: (usuario: Usuario | nulo) => nulo
  toggleTheme: () => vacío
}

exportar constante useStore = crear<AppState>()(
  herramientas de desarrollo (
    persistir (
      (conjunto) => ({
        usuario: nulo,
        tema: 'luz',
        setUser: (usuario) => set({ usuario }),
        toggleTheme: () => set((estado) => ({
          tema: estado.tema === 'luz'? 'oscuro': 'claro'
        })),
      }),
      { nombre: 'almacenamiento de aplicaciones' }
    )
  )
)

// Uso en el componente
Encabezado de función() {
  const {usuario, tema, toggleTheme} = useStore()
  regresar (
    <nombre de clase de encabezado={tema}>
      {usuario?.nombre}
      <button onClick={toggleTheme}>Alternar tema</button>
    </encabezado>
  )
}
```

## Patrones

### Patrón 1: Kit de herramientas Redux con TypeScript

exportar tienda constante = configurarStore({
  reductor: {
    usuario: usuarioReductor,
    carrito: cartReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableComprobación: {
        acciones ignoradas: ['persist/PERSIST'],
      },
    }),
})

tipo de exportación RootState = ReturnType<tipo de tienda.getState>
tipo de exportación AppDispatch = tipo de store.dispatch

// Ganchos escritos
exportar const useAppDispatch: () => AppDispatch = useDispatch
exportar constante useAppSelector: TypedUseSelectorHook<RootState> = useSelector
```

interfaz Usuario {
  identificación: cadena
  correo electrónico: cadena
  nombre: cadena
}

interfaz Estado de usuario {
  actual: Usuario | nulo
  estado: 'inactivo' | 'cargando' | 'tuvo éxito' | 'fallido'
  error: cadena | nulo
}

const estado inicial: Estado de usuario = {
  actual: nulo,
  estado: 'inactivo',
  error: nulo,
}

exportar const fetchUser = createAsyncThunk(
  'usuario/buscarUsuario',
  async (userId: cadena, {rechazarConValor}) => {
    prueba {
      respuesta constante = esperar a buscar(`/api/users/${userId}`)
      if (!response.ok) arroja un nuevo error ('No se pudo recuperar el usuario')
      regresar espera respuesta.json()
    } captura (error) {
      devolver rechazarConValor((error como Error).mensaje)
    }
  }
)

const rebanada de usuario = crear rebanada ({
  nombre: 'usuario',
  estado inicial,
  reductores: {
    setUser: (estado, acción: PayloadAction<Usuario>) => {
      estado.actual = acción.carga útil
      state.status = 'exitoso'
    },
    clearUser: (estado) => {
      estado.actual = nulo
      estado.status = 'inactivo'
    },
  },
  extraReducers: (constructor) => {
    constructor
      .addCase(fetchUser.pending, (estado) => {
        estado.status = 'cargando'
        estado.error = nulo
      })
      .addCase(fetchUser.fulfilled, (estado, acción) => {
        state.status = 'exitoso'
        estado.actual = acción.carga útil
      })
      .addCase(fetchUser.rejected, (estado, acción) => {
        estado.status = 'fallido'
        state.error = action.payload como cadena
      })
  },
})

exportar const {setUser, clearUser} = userSlice.actions
exportar userSlice.reducer predeterminado
```

### Patrón 2: Zustand con rebanadas (escalable)

interfaz de exportación UserSlice {
  usuario: Usuario | nulo
  está autenticado: booleano
  iniciar sesión: (credenciales: Credenciales) => Promesa<void>
  cerrar sesión: () => nulo
}

```typescript
// atoms/userAtoms.ts
import { atom } from 'jotai'
import { atomWithStorage } from 'jotai/utils'

```typescript
// hooks/useUsers.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

```typescript
// Zustand for client state
const useUIStore = create<UIState>((set) => ({
  sidebarOpen: true,
  modal: null,
  toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
  openModal: (modal) => set({ modal }),
  closeModal: () => set({ modal: null }),
}))

exportar const createUserSlice: StateCreator<
  UserSlice y CartSlice, // Tipo de tienda combinado
  [],
  [],
  Rebanada de usuario
> = (establecer, obtener) => ({
  usuario: nulo,
  está autenticado: falso,
  iniciar sesión: asíncrono (credenciales) => {
    usuario constante = esperar authApi.login (credenciales)
    set({ usuario, está autenticado: verdadero })
  },
  cerrar sesión: () => {
    set({ usuario: nulo, está autenticado: falso })
    // Puede acceder a otros sectores
    // obtener().clearCart()
  },
})

// tienda/index.ts
importar {crear} desde 'zustand'
importar {createUserSlice, UserSlice} desde './slices/createUserSlice'
importar {createCartSlice, CartSlice} desde './slices/createCartSlice'

escriba StoreState = UserSlice y CartSlice

exportar const useStore = crear<StoreState>()((...args) => ({
  ...createUserSlice(...argumentos),
  ...createCartSlice(...argumentos),
}))

// Suscripciones selectivas (evita rerenderizaciones innecesarias)
exportar const useUser = () => useStore((estado) => estado.usuario)
exportar const useCart = () => useStore((estado) => estado.cart)
```

### Patrón 3: Jotai para el estado atómico

// átomo básico
exportar const userAtom = atom<Usuario | nulo>(nulo)

// Átomo derivado (calculado)
exportar const isAuthenticatedAtom = atom((get) => get(userAtom)!== null)

// Átomo con persistencia de almacenamiento local
exportar const themeAtom = atomWithStorage<'light' | 'oscuro'>('tema', 'claro')

// átomo asíncrono
exportar const userProfileAtom = atom(async (get) => {
  usuario constante = get(userAtom)
  si (!usuario) devuelve nulo
  respuesta constante = await fetch(`/api/users/${user.id}/profile`)
  devolver respuesta.json()
})

// átomo de solo escritura (acción)
exportar const logoutAtom = atom(null, (get, set) => {
  establecer (usuarioAtom, nulo)
  set(carritoAtom, [])
  almacenamiento local.removeItem('token')
})

// uso
función Perfil() {
  constante [usuario] = useAtom(usuarioAtom)
  const [, cerrar sesión] = useAtom(cerrar sesiónAtom)
  const [perfil] = useAtom(userProfileAtom) // Suspenso habilitado

  regresar (
    <Reserva de suspenso={<Esqueleto />}>
      <ProfileContent perfil={perfil} onLogout={cerrar sesión} />
    </Suspenso>
  )
}
```

### Patrón 4: Consulta de reacción para el estado del servidor

// Consultar fábrica de claves
exportar claves de usuario constantes = {
  todos: ['usuarios'] como constante,
  listas: () => [...userKeys.all, 'lista'] como constante,
  lista: (filtros: UserFilters) => [...userKeys.lists(), filtros] como constante,
  detalles: () => [...userKeys.all, 'detalle'] como constante,
  detalle: (id: cadena) => [...userKeys.details(), id] como constante,
}

// buscar gancho
función de exportación useUsers(filtros: UserFilters) {
  devolver useQuery({
    queryKey: userKeys.list (filtros),
    queryFn: () => fetchUsers(filtros),
    StaleTime: 5 * 60 * 1000, // 5 minutos
    gcTime: 30 * 60 * 1000, // 30 minutos (antes cacheTime)
  })
}

// Gancho de usuario único
función de exportación useUsuario (id: cadena) {
  devolver useQuery({
    queryKey: claves de usuario.detalle(id),
    consultaFn: () => fetchUser(id),
    habilitado: !!id, // No buscar si no hay identificación
  })
}

// Mutación con actualización optimista
función de exportación useUpdateUser() {
  const consultaClient = useQueryClient()

  devolver useMutación({
    mutaciónFn: actualizarUsuario,
    onMutate: asíncrono (nuevo usuario) => {
      // Cancelar recuperaciones salientes
      await queryClient.cancelQueries({ queryKey: userKeys.detail(newUser.id) })

      // Instantánea del valor anterior
      const usuario anterior = queryClient.getQueryData(userKeys.detail(newUser.id))

      // Actualización optimista
      queryClient.setQueryData(userKeys.detail(nuevoUsuario.id), nuevoUsuario)

      devolver {usuario anterior}
    },
    onError: (err, nuevoUsuario, contexto) => {
      // Revertir en caso de error
      queryClient.setQueryData(
        userKeys.detail(nuevoUsuario.id),
        ¿contexto?.usuarioanterior
      )
    },
    onSettled: (datos, error, variables) => {
      // Recuperar después de la mutación
      queryClient.invalidateQueries({ queryKey: userKeys.detail(variables.id) })
    },
  })
}
```

### Patrón 5: Combinación de estado de cliente + servidor

// Reaccionar consulta para el estado del servidor
función Panel() {
  const {barra lateral abierta, alternar barra lateral } = useUIStore()
  const {datos: usuarios, isLoading} = useUsers({ activo: verdadero})
  const {datos: estadísticas} = usarEstadísticas()

  si (isLoading) devuelve <DashboardSkeleton />

  regresar (
    <div className={sidebarOpen? 'con barra lateral': ''}>
      <Barra lateral abierta={barra lateral abierta} onToggle={toggleSidebar} />
      <principal>
        <StatsCards estadísticas={estadísticas} />
        <Usuarios de UserTable={usuarios} />
      </principal>
    </div>
  )
}
```

## Mejores prácticas

```typescript
// Before (legacy Redux)
const ADD_TODO = 'ADD_TODO'
const addTodo = (text) => ({ type: ADD_TODO, payload: text })
function todosReducer(state = [], action) {
  switch (action.type) {
    case ADD_TODO:
      return [...state, { text: action.payload, completed: false }]
    default:
      return state
  }
}

### Qué hacer
- **Colocar estado** - Mantener el estado lo más cerca posible de donde se usa
- **Usar selectores** - Evite rerenderizaciones innecesarias con suscripciones selectivas
- **Normalizar datos** - Aplanar estructuras anidadas para actualizaciones más fáciles
- **Escriba todo** - La cobertura completa de TypeScript evita errores de tiempo de ejecución
- **Preocupaciones separadas** - Estado del servidor (React Query) frente al estado del cliente (Zustand)

### Lo que no se debe hacer
- **No globalices demasiado** - No todo tiene que estar en un estado global
- **No duplique el estado del servidor** - Deje que React Query lo administre
- **No mutar directamente** - Utilice siempre actualizaciones inmutables
- **No almacenar datos derivados** - Calcúlelos en su lugar
- **No mezcle paradigmas** - Elija una solución principal por categoría

## Guías de migración

### De Legacy Redux a RTK

// Después (Kit de herramientas Redux)
const todosSlice = crearSlice({
  nombre: 'todos',
  estado inicial: [],
  reductores: {
    addTodo: (estado, acción: PayloadAction<cadena>) => {
      // Immer permite "mutaciones"
      state.push({ texto: acción.payload, completado: falso })
    },
  },
})
```

## Recursos

- [Documentación del kit de herramientas de Redux] (https://redux-toolkit.js.org/)
- [Zustand GitHub](https://github.com/pmndrs/zustand)
- [Documentación de Jotai](https://jotai.org/)
- [Consulta de TanStack] (https://tanstack.com/query)