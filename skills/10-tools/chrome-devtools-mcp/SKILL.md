---
name: chrome-devtools-mcp
description: Chrome DevTools MCP integration for ultra-fast UI testing, debugging, and performance auditing. Replaces slow visual emulation (browser_subagent) with direct Chrome DevTools Protocol (CDP) access via the official Google Chrome MCP server. Use when testing web pages, debugging network/console errors, or running performance audits.
---

# Chrome DevTools MCP — Ultra-Fast Testing & Debugging

Direct Chrome DevTools Protocol (CDP) integration for AI coding agents. Replaces slow visual emulation with instant DOM inspection, network monitoring, and browser automation via the official [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) server by Google Chrome.

## Why This Exists

Traditional AI browser testing (`browser_subagent`) emulates clicks element-by-element, takes heavy screenshots (~5MB each), and introduces timing errors from CSS animations and delayed renders. This skill connects the agent directly to Chrome's engine via CDP, making all operations near-instant.

| Method                | DOM Read                   | Form Fill               | Screenshot             | Network Inspection |
| --------------------- | -------------------------- | ----------------------- | ---------------------- | ------------------ |
| `browser_subagent`    | ~3-5s (screenshot + parse) | ~5-10s (click-by-click) | ~2-3s (5MB risk)       | ❌ Not available   |
| `chrome-devtools-mcp` | ~instant                   | ~instant                | ~instant (lightweight) | ✅ Full access     |

## Prerequisites

- **Node.js** v20.19 or newer (LTS)
- **Chrome** stable (M144+ for `--autoConnect`, any version for `--browserUrl`)
- **npm** (comes with Node.js)

## Installation

Add to your Antigravity MCP config (`~/.gemini/antigravity/mcp_config.json`):

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

### Alternative: Connect to Running Chrome

For maintaining browser state (cookies, authenticated sessions):

```bash
# Start Chrome with remote debugging
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-devtools-mcp-profile
```

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
      ],
      "env": { "CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS": "true" }
    }
  }
}
```

## Decision Tree: When to Use What

```
Need to interact with a browser?
│
├─ READ data (DOM, Network, Console, a11y)?
│   └─ ✅ chrome-devtools MCP (evaluate_script, list_network_requests)
│
├─ AUTOMATE actions (clicks, forms, navigation)?
│   └─ ✅ chrome-devtools MCP (click, fill, fill_form, navigate_page)
│
├─ AUDIT performance?
│   └─ ✅ chrome-devtools MCP (performance_start_trace, lighthouse_audit)
│
├─ VERIFY visual design?
│   ├─ Can verify via DOM/CSS? → ✅ chrome-devtools MCP (evaluate_script)
│   └─ Need a visual capture?  → ✅ chrome-devtools MCP → take_screenshot
│
└─ RECORD a visual demo for the user?
    └─ 🔄 browser_subagent (ONLY valid use case)
```

## Available Tools (34)

### Input Automation

`click` · `drag` · `fill` · `fill_form` · `handle_dialog` · `hover` · `press_key` · `type_text` · `upload_file`

### Navigation

`navigate_page` · `new_page` · `close_page` · `list_pages` · `select_page` · `wait_for`

### Emulation

`emulate` · `resize_page`

### Performance

`performance_start_trace` · `performance_stop_trace` · `performance_analyze_insight` · `take_memory_snapshot`

### Network

`list_network_requests` · `get_network_request`

### Debugging

`evaluate_script` · `list_console_messages` · `get_console_message` · `take_screenshot` · `take_snapshot` · `lighthouse_audit`

## Operational Protocols

### Protocol 1: UI Testing

```
1. navigate_page → dev server URL
2. wait_for → key element selector
3. evaluate_script → verify content/state
4. fill_form → fill forms if applicable
5. click → interact with buttons/links
6. list_console_messages → verify 0 errors
7. list_network_requests → verify OK responses
```

### Protocol 2: Debugging

```
1. navigate_page → problematic URL
2. list_console_messages → find errors/warnings
3. list_network_requests → find failed requests
4. get_network_request → inspect specific request
5. evaluate_script → inspect app state
```

### Protocol 3: Performance Audit

```
1. navigate_page → URL to audit
2. lighthouse_audit → full audit
3. performance_start_trace → detailed trace
4. [simulated user interactions]
5. performance_stop_trace → trace data
6. performance_analyze_insight → bottleneck analysis
```

### Protocol 4: Responsive Testing

```
1. navigate_page → URL to test
2. resize_page → 375x667 (mobile)
3. take_screenshot or evaluate_script → verify layout
4. resize_page → 768x1024 (tablet)
5. resize_page → 1440x900 (desktop)
```

## Configuration Flags

| Flag                    | Default  | Description                                                         |
| ----------------------- | -------- | ------------------------------------------------------------------- |
| `--autoConnect`         | `false`  | Auto-connect to running Chrome (M144+)                              |
| `--browserUrl`          | -        | Connect to specific Chrome instance (e.g., `http://127.0.0.1:9222`) |
| `--headless`            | `false`  | Run without visible UI                                              |
| `--slim`                | `false`  | Only 3 tools (navigation, JS execution, screenshots)                |
| `--isolated`            | `false`  | Uses temporary user-data-dir                                        |
| `--viewport`            | auto     | Initial viewport size (e.g., `1280x720`)                            |
| `--channel`             | `stable` | Chrome channel (`stable`, `canary`, `beta`, `dev`)                  |
| `--no-performance-crux` | -        | Disables URL tracking via Google CrUX API                           |
| `--no-usage-statistics` | -        | Disables usage statistics                                           |

## Privacy & Security

| Setting                                        | Description                                 |
| ---------------------------------------------- | ------------------------------------------- |
| `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS=true` | Disables usage stats sent to Google         |
| `--no-performance-crux`                        | Prevents sending URLs to CrUX API           |
| `--isolated`                                   | Uses temporary profile (no persistent data) |

> **Warning**: `chrome-devtools-mcp` exposes browser content to MCP clients. Avoid using it on pages with sensitive data unless in `--isolated` mode.

## Known Limitations

1. **No video recordings** — For recorded visual demos, use `browser_subagent`
2. **Requires Chrome open** — If Chrome is not running, tools may fail
3. **M144+ for autoConnect** — Older Chrome versions need `--browserUrl` with manual remote debugging

## References

- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [chrome-devtools-mcp on npm](https://www.npmjs.com/package/chrome-devtools-mcp)
- **License**: Apache-2.0
