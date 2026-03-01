# Chrome DevTools MCP — Setup Guide

## Prerequisites

- **Node.js** v20.19 or newer (LTS)
- **Chrome** (current stable or newer)
- **npm** (comes with Node.js)

## Installation

### Option 1: Antigravity MCP Config (Recommended)

Add to your `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"],
      "env": {
        "CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS": "true"
      },
      "disabled": false
    }
  }
}
```

### Option 2: Connect to Running Chrome

If you want to maintain browser state (cookies, sessions):

1. Start Chrome with remote debugging:

```bash
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-profile-stable
```

2. Configure MCP with `--browserUrl`:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browserUrl",
        "http://127.0.0.1:9222"
      ]
    }
  }
}
```

### Option 3: Headless Mode (CI/CD)

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--headless", "--isolated"]
    }
  }
}
```

## Verification

After adding the config, restart Antigravity. The agent should now have access to 34 new tools under the `chrome-devtools` MCP server.

To verify, ask the agent: "List the available chrome-devtools MCP tools."

## Privacy & Security

| Setting                                        | Description                                 |
| ---------------------------------------------- | ------------------------------------------- |
| `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS=true` | Disables usage statistics sent to Google    |
| `--no-performance-crux`                        | Prevents sending URLs to Google CrUX API    |
| `--isolated`                                   | Uses temporary profile (no persistent data) |

> **Warning**: `chrome-devtools-mcp` exposes browser content to MCP clients. Avoid using it on pages with sensitive data (banking, passwords) unless in `--isolated` mode.

## Troubleshooting

| Issue                      | Solution                                             |
| -------------------------- | ---------------------------------------------------- |
| "Cannot connect to Chrome" | Ensure Chrome is running or use `--autoConnect`      |
| "Port already in use"      | Close other Chrome debugging sessions or change port |
| "Node.js version too old"  | Upgrade to Node.js v20.19+ (`nvm install --lts`)     |
| Tools not appearing        | Restart Antigravity after editing `mcp_config.json`  |

## Official Resources

- **Repository**: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- **npm**: [chrome-devtools-mcp](https://www.npmjs.com/package/chrome-devtools-mcp)
- **License**: Apache-2.0
