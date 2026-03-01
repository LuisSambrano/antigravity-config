---
name: chrome-devtools
description: |
  Skill that automatically prioritizes the chrome-devtools-mcp server over visual emulation (browser_subagent) for UI testing, network/console debugging, and performance audits. Uses the Chrome DevTools Protocol (CDP) directly, eliminating the friction of screenshots and emulated clicks.
---

# Chrome DevTools MCP — Ultra-fast Testing & Debugging

## 📌 When to Activate (Automatic Trigger)

This skill activates automatically when the agent needs to:

1. **Test a web interface** (verify elements exist, forms work, user flows are correct)
2. **Debug errors** (browser console, network requests, CORS, JS errors)
3. **Audit performance** (LCP, CLS, TBT, Lighthouse)
4. **Validate accessibility** (DOM inspection, ARIA attributes)
5. **Fill and submit forms** programmatically
6. **Execute JavaScript** in the context of the page

## 🔴 CRITICAL RULE: CDP-First, Visual-Second

```
Do I need to interact with a browser?
│
├─ Is it to READ data (DOM, Network, Console, accessibility)?
│   └─ ✅ USE chrome-devtools MCP (evaluate_script, list_network_requests, list_console_messages)
│
├─ Is it to AUTOMATE actions (clicks, forms, navigation)?
│   └─ ✅ USE chrome-devtools MCP (click, fill, fill_form, navigate_page, press_key)
│
├─ Is it to AUDIT performance?
│   └─ ✅ USE chrome-devtools MCP (performance_start_trace, lighthouse_audit)
│
├─ Is it to VERIFY that something LOOKS right (design, colors, layout)?
│   ├─ Can I verify via DOM/CSS?
│   │   └─ ✅ USE chrome-devtools MCP (evaluate_script to read computed styles)
│   └─ Do I really need a visual screenshot for the user?
│       └─ ⚠️ USE chrome-devtools MCP → take_screenshot (1 single shot, no subagent)
│
└─ Is it a visual demonstration for the user or a recording?
    └─ 🔄 USE browser_subagent (ONLY valid case — see "handling-browser-5mb-limit" Skill)
```

**NEVER** use `browser_subagent` to:

- Read page content (use `evaluate_script` or `take_snapshot`)
- Verify if an element exists (use `wait_for` or `evaluate_script`)
- Fill out forms (use `fill` or `fill_form`)
- Navigate between pages (use `navigate_page`)
- Inspect network/console (use `list_network_requests`, `list_console_messages`)

## 🛠️ Available Tools (34 tools)

### Input Automation

| Tool            | Description                      |
| --------------- | -------------------------------- |
| `click`         | Click on a DOM element           |
| `drag`          | Drag an element                  |
| `fill`          | Fill a specific input            |
| `fill_form`     | Fill multiple fields in a form   |
| `handle_dialog` | Handle alerts/confirms/prompts   |
| `hover`         | Hover over an element            |
| `press_key`     | Press a key (Enter, Tab, etc.)   |
| `type_text`     | Type text character by character |
| `upload_file`   | Upload a file to a file input    |

### Navigation

| Tool            | Description                             |
| --------------- | --------------------------------------- |
| `navigate_page` | Navigate to a URL                       |
| `new_page`      | Open a new tab                          |
| `close_page`    | Close a tab                             |
| `list_pages`    | List all open tabs                      |
| `select_page`   | Switch to another tab                   |
| `wait_for`      | Wait for a selector/condition to be met |

### Emulation

| Tool          | Description                       |
| ------------- | --------------------------------- |
| `emulate`     | Emulate a device (mobile, tablet) |
| `resize_page` | Change viewport size              |

### Performance

| Tool                          | Description                 |
| ----------------------------- | --------------------------- |
| `performance_start_trace`     | Start a performance trace   |
| `performance_stop_trace`      | Stop trace and get data     |
| `performance_analyze_insight` | Analyze trace insights      |
| `take_memory_snapshot`        | Take a heap memory snapshot |

### Network

| Tool                    | Description                       |
| ----------------------- | --------------------------------- |
| `list_network_requests` | List all requests                 |
| `get_network_request`   | Get details of a specific request |

### Debugging

| Tool                    | Description                           |
| ----------------------- | ------------------------------------- |
| `evaluate_script`       | Execute JS on the page                |
| `list_console_messages` | List console messages                 |
| `get_console_message`   | Get details of a specific message     |
| `take_screenshot`       | Capture screenshot (without subagent) |
| `take_snapshot`         | Take a full DOM snapshot              |
| `lighthouse_audit`      | Full Lighthouse audit                 |

## 📋 Operation Protocols

### Protocol 1: UI Testing

```
1. navigate_page → Dev server URL
2. wait_for → Key element selector
3. evaluate_script → Verify content/state
4. fill_form → Fill forms if applicable
5. click → Interact with buttons/links
6. list_console_messages → Verify 0 errors
7. list_network_requests → Verify OK responses
```

### Protocol 2: Debugging

```
1. navigate_page → Problematic URL
2. list_console_messages → Look for errors/warnings
3. list_network_requests → Look for failed requests
4. get_network_request → Inspect specific request
5. evaluate_script → Inspect app state
```

### Protocol 3: Performance Audit

```
1. navigate_page → URL to audit
2. lighthouse_audit → Full audit
3. performance_start_trace → Detailed trace
4. [Simulated user interactions]
5. performance_stop_trace → Trace data
6. performance_analyze_insight → Bottleneck analysis
```

### Protocol 4: Responsive Testing

```
1. navigate_page → URL to test
2. resize_page → 375x667 (mobile)
3. take_screenshot or evaluate_script → Verify layout
4. resize_page → 768x1024 (tablet)
5. resize_page → 1440x900 (desktop)
```

## 🔗 Integration with Other Skills

- **`handling-browser-5mb-limit`**: If you need a visual capture, use `take_screenshot` from this MCP instead of the `browser_subagent`, eliminating the risk of exceeding the 5MB limit.
- **Pre-Delivery Gate**: Use `lighthouse_audit` to verify Performance ≥ 90 and Accessibility ≥ 95 before delivery.

## ⚠️ Known Limitations

1. **Does not generate recordings/videos**: For recorded video demos, use `browser_subagent`.
2. **Does not emulate visual human interaction**: If the user wants to SEE what the flow looks like step-by-step like a human, use `browser_subagent`.
3. **Requires Chrome to be open**: If Chrome is not running, some tools may fail.

---

**Remember**: This MCP is your primary tool. The `browser_subagent` is your fallback for visual evidence. Speed > Captures.
