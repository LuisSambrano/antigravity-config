---
name: agent-browser
description: Control Electron desktop applications (Slack, Discord, Notion, VS Code) using Vercel's agent-browser via Chrome DevTools Protocol (CDP).
---

# AGENT-BROWSER (VERCEL LABS)

**Version**: 1.0.0
**Status**: ACTIVE
**Category**: 10-tools

---

## 🎯 Purpose

This skill utilizes Vercel Labs' `agent-browser` CLI to allow autonomous AI agents to interact with and control desktop applications built on Electron (Slack, Discord, Notion, Figma, VS Code, Spotify) or WebView2. It circumvents the need for complex APIs or OAuth, allowing the agent to "see" and "click" the UI directly via the Chrome DevTools Protocol (CDP).

---

## 🚀 Installation & Invocation

To use this tool, the AI Agent must execute the following CLI command:

```bash
npx skills add vercel-labs/agent-browser --skill electron
```

---

## ⚙️ How It Works (DOM Snapshot + Refs)

Instead of passing the entire bloated HTML of a desktop application (which consumes massive context limits), `agent-browser` extracts a **Snapshot + Refs** representation. This is a clean, compressed snapshot of only the interactive elements on the screen.

1.  **Read State**: The agent views the clean snapshot.
2.  **Action**: The agent executes a click or types text targeting a specific "Ref" ID.
3.  **Update**: The browser immediately reflects the action without API latency.

---

## 🔗 Connection Protocol (CDP)

To control an Electron app, it must be launched with remote debugging enabled.

### 1. Launch the Target Application

The user must launch their Electron app from the terminal with the `--remote-debugging-port` flag.

**Examples:**

```bash
# MacOS Examples
/Applications/Notion.app/Contents/MacOS/Notion --remote-debugging-port=9222
/Applications/Slack.app/Contents/MacOS/Slack --remote-debugging-port=9222
/Applications/Discord.app/Contents/MacOS/Discord --remote-debugging-port=9222
```

### 2. Connect the Agent

Once the port (e.g., `9222`) is active, instruct the agent to connect via the `--cdp` flag using `agent-browser`.

```bash
# Using the CLI to connect to the active CDP port
agent-browser --cdp 9222
# Or full WebSocket URL if remote
agent-browser --cdp http://localhost:9222
```

---

## 🛡️ Security Considerations

- **Zero OAuth**: No tokens are stored; interaction happens at the UI level.
- **Local Execution**: Ensure CDP ports (like 9222) are never exposed to public networks, as they grant full remote execution control over the application.

---

## 🧠 Prompting Strategy

When tasking an agent with `agent-browser`, use explicit instructions:

> "Use `agent-browser` connected to CDP port `9222`. Read the latest messages in the active Slack channel, summarize them, and type a response clicking the 'Send' button."
