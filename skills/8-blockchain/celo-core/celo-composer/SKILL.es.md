---
name: celo-composer
description: Scaffold Celo dApps with Celo Composer. Use when starting new Celo projects, creating MiniPay apps, or setting up development environments.
license: Apache-2.0
metadata:
  author: celo-org
  version: "1.0.0"
---

```bash
npx @celo/celo-composer@latest create
```

```bash
npx @celo/celo-composer@latest create my-celo-app
```

```bash
npx @celo/celo-composer@latest create my-celo-app \
  --template basic \
  --wallet-provider rainbowkit \
  --contracts hardhat
```

```bash
npx @celo/celo-composer@latest create my-celo-app --yes
```

```bash
npx @celo/celo-composer@latest create -t minipay
```

```bash
npx @celo/celo-composer@latest create -t farcaster-miniapp
```

```
my-celo-app/
├── apps/
│   ├── web/              # Next.js application
│   │   ├── app/          # App router pages
│   │   ├── components/   # React components
│   │   └── ...
│   └── contracts/        # Smart contracts (if selected)
│       ├── contracts/    # Solidity files
│       ├── scripts/      # Deployment scripts
│       └── test/         # Contract tests
├── packages/
│   ├── ui/               # Shared UI components
│   └── utils/            # Shared utilities
├── pnpm-workspace.yaml   # Workspace configuration
├── turbo.json            # Turborepo configuration
└── package.json
```

```bash
cd my-celo-app

```bash
# Navigate to contracts
cd apps/contracts

```bash
# Navigate to contracts
cd apps/contracts

```bash
# Required for wallet connection
NEXT_PUBLIC_WC_PROJECT_ID=your_walletconnect_project_id

```bash
PRIVATE_KEY=your_private_key
CELOSCAN_API_KEY=your_celoscan_api_key
```

```tsx
// apps/web/app/my-page/page.tsx
export default function MyPage() {
  return <div>My Custom Page</div>;
}
```

```tsx
// apps/web/components/MyComponent.tsx
export function MyComponent() {
  return <div>My Component</div>;
}
```

# Celo Composer

This skill covers using Celo Composer to scaffold Celo dApps with pre-configured templates.

## When to Use

- Starting a new Celo project
- Creating a MiniPay Mini App
- Setting up a Farcaster Miniapp
- Need pre-configured Next.js + Web3 setup

## Quick Start

### Interactive Mode

Follow the prompts to select your options.

### With Project Name

### Non-Interactive (Flags)

### Quick Start with Defaults

## Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `basic` | Standard Next.js 14+ dApp | General web3 applications |
| `minipay` | Mobile-first MiniPay app | MiniPay Mini Apps |
| `farcaster-miniapp` | Farcaster SDK + Frame | Farcaster integrations |
| `ai-chat` | Standalone chat application | AI-powered dApps |

### Create MiniPay App

### Create Farcaster Miniapp

## Configuration Options

### Wallet Providers

| Provider | Description |
|----------|-------------|
| `rainbowkit` | Popular wallet connection UI (default) |
| `thirdweb` | thirdweb Connect SDK |
| `none` | No wallet provider |

### Smart Contracts

| Option | Description |
|--------|-------------|
| `hardhat` | Hardhat development environment (default) |
| `foundry` | Foundry development environment |
| `none` | No smart contracts |

## Project Structure

## Running the Project

# Install dependencies
pnpm install

# Start development server
pnpm dev

# Build for production
pnpm build
```

## Tech Stack

- **Framework:** Next.js 14+ with App Router
- **Styling:** Tailwind CSS
- **Components:** shadcn/ui
- **Monorepo:** Turborepo + PNPM workspaces
- **Language:** TypeScript
- **Web3:** viem + wagmi (or thirdweb)

## Requirements

- Node.js 18.0.0 or higher
- PNPM (recommended) or npm/yarn

## Working with Contracts

If you selected Hardhat or Foundry:

### Hardhat

# Compile
npx hardhat compile

# Test
npx hardhat test

# Deploy to Celo Sepolia
npx hardhat run scripts/deploy.ts --network celoSepolia
```

### Foundry

# Build
forge build

# Test
forge test

# Deploy to Celo Sepolia
forge script script/Deploy.s.sol --rpc-url https://forno.celo-sepolia.celo-testnet.org --broadcast
```

## Environment Variables

Create `.env.local` in `apps/web/`:

# Optional: Alchemy API key
NEXT_PUBLIC_ALCHEMY_API_KEY=your_alchemy_key
```

Create `.env` in `apps/contracts/`:

## Customization

### Adding New Pages

Create files in `apps/web/app/`:

### Adding Components

Add to `apps/web/components/` or shared `packages/ui/`:

## Additional Resources

- [templates.md](references/templates.md) - Detailed template documentation


