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

# Gerenciamento de estado de reação

Guia abrangente para padrões modernos de gerenciamento de estado do React, desde o estado do componente local até armazenamentos globais e sincronização do estado do servidor.

## Não use esta habilidade quando

- A tarefa não está relacionada ao gerenciamento do estado de reação
- Você precisa de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça metas, restrições e insumos necessários.
- Aplicar as melhores práticas relevantes e validar os resultados.
- Fornece etapas acionáveis ​​e verificação.
- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Use esta habilidade quando

- Configurando o gerenciamento global de estado em um aplicativo React
- Escolhendo entre Redux Toolkit, Zustand ou Jotai
- Gerenciando o estado do servidor com React Query ou SWR
- Implementação de atualizações otimistas
- Depuração de problemas relacionados ao estado
- Migrando do Redux legado para padrões modernos

## Conceitos Básicos

### 1. Categorias de estado

| Tipo | Descrição | Soluções |
|------|-------------|-----------|
| **Estado Local** | Específico do componente, estado da UI | useState, useReducer |
| **Estado Global** | Compartilhado entre componentes | Kit de ferramentas Redux, Zustand, Jotai |
| **Estado do servidor** | Dados remotos, cache | Consulta React, SWR, Consulta RTK |
| **Estado do URL** | Parâmetros de rota, pesquisa | Roteador React, nuqs |
| **Estado do formulário** | Valores de entrada, validação | Formulário de gancho React, Formik |

### 2. Critérios de seleção

## Início rápido

### Zustand (mais simples)

interface AppState {
  usuário: Usuário | nulo
  tema: 'luz' | 'escuro'
  setUser: (usuário: Usuário | nulo) => void
  toggleTheme: () => vazio
}

exportar const useStore = create<AppState>()(
  ferramentas de desenvolvimento (
    persistir (
      (conjunto) => ({
        usuário: nulo,
        tema: 'luz',
        setUser: (usuário) => set({usuário}),
        toggleTheme: () => set((estado) => ({
          tema: state.theme === 'luz'? 'escuro': 'claro'
        })),
      }),
      { nome: 'armazenamento de aplicativo' }
    )
  )
)

//Uso no componente
função Cabeçalho() {
  const {usuário, tema, toggleTheme} = useStore()
  retornar (
    <header className={tema}>
      {usuário?.nome}
      <button onClick={toggleTheme}>Alternar tema</button>
    </header>
  )
}
```

## Padrões

### Padrão 1: Redux Toolkit com TypeScript

exportar const store = configureStore({
  redutor: {
    usuário: userReducer,
    carrinho: carrinhoRedutor,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        Ações ignoradas: ['persistir/PERSIST'],
      },
    }),
})

tipo de exportação RootState = ReturnType<typeof store.getState>
tipo de exportação AppDispatch = typeof store.dispatch

//ganchos digitados
exportar const useAppDispatch: () => AppDispatch = useDispatch
exportar const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
```

interface Usuário {
  identificação: string
  e-mail: string
  nome: string
}

interface EstadoUsuário {
  atual: Usuário | nulo
  status: 'inativo' | 'carregando' | 'sucesso' | 'falhou'
  erro: string | nulo
}

const estadoinicial: EstadoUsuário = {
  atual: nulo,
  status: 'inativo',
  erro: nulo,
}

exportar const fetchUser = createAsyncThunk(
  'usuário/fetchUser',
  assíncrono (userId: string, {rejectWithValue}) => {
    tente {
      resposta const = aguardar busca(`/api/users/${userId}`)
      if (!response.ok) throw new Error('Falha ao buscar usuário')
      retornar aguardar resposta.json()
    } pegar (erro) {
      retornar rejeitarWithValue((erro como erro).mensagem)
    }
  }
)

const userSlice = createSlice({
  nome: 'usuário',
  estado inicial,
  redutores: {
    setUser: (estado, ação: PayloadAction<Usuário>) => {
      estado.atual=ação.payload
      estado.status = 'sucesso'
    },
    clearUser: (estado) => {
      estado.atual = nulo
      estado.status = 'inativo'
    },
  },
  extraReducers: (construtor) => {
    construtor
      .addCase(fetchUser.pending, (estado) => {
        estado.status = 'carregando'
        estado.error=nulo
      })
      .addCase(fetchUser.fulfilled, (estado, ação) => {
        estado.status = 'sucesso'
        estado.atual=ação.payload
      })
      .addCase(fetchUser.rejected, (estado, ação) => {
        estado.status = 'falhou'
        state.error = action.payload como string
      })
  },
})

exportar const {setUser, clearUser} = userSlice.actions
exportar userSlice.reducer padrão
```

### Padrão 2: Zustand com fatias (escalável)

interface de exportação UserSlice {
  usuário: Usuário | nulo
  isAuthenticated: booleano
  login: (credenciais: Credenciais) => Promessa<void>
  sair: () => vazio
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
  UserSlice & CartSlice, // Tipo de armazenamento combinado
  [],
  [],
  UserSlice
> = (definir, obter) => ({
  usuário: nulo,
  isAutenticado: falso,
  login: assíncrono (credenciais) => {
    const usuário = aguarda authApi.login (credenciais)
    set({usuário, isAuthenticated: true })
  },
  sair: () => {
    set({usuário: null, isAuthenticated: false })
    //Pode acessar outras fatias
    //get().clearCart()
  },
})

//loja/index.ts
importar {criar} de 'zustand'
importar {createUserSlice, UserSlice} de './slices/createUserSlice'
importar {createCartSlice, CartSlice} de './slices/createCartSlice'

digite StoreState = UserSlice e CartSlice

exportar const useStore = create<StoreState>()((...args) => ({
  ...createUserSlice(...args),
  ...createCartSlice(...args),
}))

// Assinaturas seletivas (evita novas renderizações desnecessárias)
exportar const useUser = () => useStore((state) => state.user)
exportar const useCart = () => useStore((estado) => estado.cart)
```

### Padrão 3: Jotai para Estado Atômico

//Átomo básico
exportar const userAtom = átomo<Usuário | nulo>(nulo)

//Átomo derivado (computado)
exportar const isAuthenticatedAtom = atom((get) => get(userAtom) !== null)

// Atom com persistência localStorage
exportar const temaAtom = atomWithStorage<'light' | 'escuro'>('tema', 'claro')

//Átomo assíncrono
exportar const userProfileAtom = atom(async (get) => {
  const usuário = get(userAtom)
  se (!usuário) retornar nulo
  resposta const = aguardar busca(`/api/users/${user.id}/profile`)
  retornar resposta.json()
})

//Átomo somente gravação (ação)
exportar const logoutAtom = átomo(null, (get, set) => {
  definir(userAtom,nulo)
  set(carrinhoAtom, [])
  localStorage.removeItem('token')
})

// Uso
função Perfil() {
  const [usuário] = useAtom(userAtom)
  const [, sair] = useAtom(logoutAtom)
  const [perfil] = useAtom(userProfileAtom) // habilitado para suspense

  retornar (
    <Suspense fallback={<Esqueleto />}>
      <ProfileContent profile={perfil} onLogout={logout} />
    </Suspenso>
  )
}
```

### Padrão 4: Consulta de reação para estado do servidor

//Consulta fábrica de chaves
exportar const userKeys = {
  todos: ['usuários'] como const,
  listas: () => [...userKeys.all, 'lista'] como const,
  lista: (filtros: UserFilters) => [...userKeys.lists(), filtros] como const,
  detalhes: () => [...userKeys.all, 'detalhe'] como const,
  detalhe: (id: string) => [...userKeys.details(), id] como const,
}

//Busca o gancho
função de exportação useUsers(filtros: UserFilters) {
  return useQuery({
    queryKey: userKeys.list (filtros),
    queryFn: () => fetchUsers(filtros),
    staleTime: 5 * 60 * 1000, // 5 minutos
    gcTime: 30 * 60 * 1000, // 30 minutos (anteriormente cacheTime)
  })
}

// Gancho de usuário único
função de exportação useUser(id: string) {
  return useQuery({
    queryKey: userKeys.detail(id),
    queryFn: () => fetchUser(id),
    enabled: !!id, // Não busca se não houver id
  })
}

// Mutação com atualização otimista
função de exportação useUpdateUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutaçãoFn: updateUser,
    onMutate: assíncrono (newUser) => {
      //Cancela buscas de saída
      aguarde queryClient.cancelQueries({ queryKey: userKeys.detail(newUser.id) })

      // Valor anterior do instantâneo
      const anteriorUser = queryClient.getQueryData(userKeys.detail(newUser.id))

      // Atualizar de forma otimista
      queryClient.setQueryData(userKeys.detail(newUser.id), newUser)

      return {usuárioanterior}
    },
    onError: (err, newUser, contexto) => {
      //Reversão em caso de erro
      queryClient.setQueryData(
        userKeys.detail(newUser.id),
        contexto?.anteriorUser
      )
    },
    onSettled: (dados, erro, variáveis) => {
      //Rebusca após mutação
      queryClient.invalidateQueries({ queryKey: userKeys.detail(variables.id) })
    },
  })
}
```

### Padrão 5: Combinando Estado do Cliente + Servidor

//Reagir consulta para estado do servidor
function Painel() {
  const { sidebarOpen, toggleSidebar } = useUIStore()
  const {dados: usuários, isLoading } = useUsers({ ativo: verdadeiro })
  const {dados: estatísticas} = useStats()

  if (isLoading) retornar <DashboardSkeleton />

  retornar (
    <div className={barra lateralOpen ? 'com barra lateral': ''}>
      <Barra lateral aberta={sidebarOpen} onToggle={toggleSidebar} />
      <principal>
        <StatsCards estatísticas={estatísticas} />
        <UserTable usuários={usuários} />
      </principal>
    </div>
  )
}
```

## Melhores práticas

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

### O que fazer
- **Colocar estado** - Mantenha o estado o mais próximo possível de onde é usado
- **Use seletores** - Evite novas renderizações desnecessárias com assinaturas seletivas
- **Normalizar dados** - Achatar estruturas aninhadas para atualizações mais fáceis
- **Digite tudo** - A cobertura completa do TypeScript evita erros de tempo de execução
- **Preocupações separadas** - Estado do servidor (React Query) versus estado do cliente (Zustand)

### O que não fazer
- **Não globalize demais** - Nem tudo precisa estar em um estado global
- **Não duplique o estado do servidor** - Deixe o React Query gerenciá-lo
- **Não mude diretamente** - Sempre use atualizações imutáveis
- **Não armazene dados derivados** - Em vez disso, calcule-os
- **Não misture paradigmas** - Escolha uma solução primária por categoria

## Guias de migração

### Do Legacy Redux ao RTK

//Depois (kit de ferramentas Redux)
const todosSlice = createSlice({
  nome: 'todos',
  estadoinicial: [],
  redutores: {
    addTodo: (estado, ação: PayloadAction<string>) => {
      //Immer permite "mutações"
      state.push({texto: action.payload, concluído: false })
    },
  },
})
```

## Recursos

- [Documentação do Redux Toolkit](https://redux-toolkit.js.org/)
- [Zustand GitHub](https://github.com/pmndrs/zustand)
- [Documentação Jotai](https://jotai.org/)
- [Consulta TanStack](https://tanstack.com/query)