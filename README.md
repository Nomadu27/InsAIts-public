# InsAIts

**Runtime security for AI agents. Catches what your AI misses.**

[![PyPI](https://img.shields.io/pypi/v/insa-its?color=cyan&label=PyPI)](https://pypi.org/project/insa-its/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://pypi.org/project/insa-its/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![100% Local](https://img.shields.io/badge/Data-100%25%20Local-brightgreen)](#what-insaits-does-not-do)
[![Website](https://img.shields.io/badge/Website-Live-cyan)](https://nomadu27.github.io/InsAIts-public/)

**[Website](https://nomadu27.github.io/InsAIts-public/)** | **[PyPI](https://pypi.org/project/insa-its/)** | **[YouTube](https://www.youtube.com/@insAIts1407)**

---

## What It Does

InsAIts monitors AI-to-AI communication in real-time. It watches every tool call, every response, and every agent-to-agent message for security anomalies -- credential leaks, hallucination chains, prompt injection attempts, unauthorized writes, and 19 more anomaly types. When it catches something, it intervenes immediately by injecting corrective instructions into the agent's context, before the damage reaches your codebase.

It runs as a Claude Code hook. You install it, and it works silently in the background. No configuration needed.

![InsAIts Dashboard](assets/dashboard-hero.png)

---

## Verified Numbers

These are real numbers from real sessions, not benchmarks:

| Metric | Value | Context |
|--------|-------|---------|
| Longest continuous session | **8+ hours** | Two terminals, March 22 2026 |
| First burst duration | **9 hours 16 minutes** | Single session with minimal interruptions |
| Anomalies caught and corrected | **682** | Across multi-terminal session |
| Anomaly types | **23** | Credential exposure, hallucination, drift, injection, and more |
| OWASP coverage | **MCP Top 10** | ASI01-ASI10, with CVE references |
| Data sent to cloud | **0 bytes** | Everything runs locally |

---

## Features & How to Use Them

### Live Dashboard (16+ panels)
Open your browser at `http://localhost:5001` after starting `insaits-dashboard`. You get:
- **Threat Index** -- overall security score for your session, updated in real-time
- **Anomaly Feed** -- live stream of detected issues with severity levels and details
- **Agent Intelligence Scores** -- each agent scored independently (trust level, stability, anomaly rate)
- **Blast Radius** -- how much of your session is affected by anomalies
- **Intervention Log** -- shows when InsAIts corrected an agent and what happened next
- **Circuit Breaker** -- manually pause/resume AI execution if things go wrong
- **OWASP Panel** -- full MCP Top 10 + Agentic AI Top 10 compliance view with CVE references

### Real-Time Anomaly Detection (23 types)
InsAIts catches issues as they happen, not after. Categories include:
- **Credential exposure** -- API keys, tokens, passwords appearing in AI messages
- **Hallucination chains** -- one agent fabricates a fact, another treats it as truth
- **Prompt injection** -- attempts to override system instructions
- **Semantic drift** -- meaning gradually shifting across agent messages
- **Tool poisoning** -- tool descriptions changing between calls
- **Phantom citations** -- fabricated URLs, DOIs, paper references
- **Data exfiltration** -- base64/hex encoded data being piped to external services
- **Unauthorized file writes** -- agents writing to files they should not touch

### Active Intervention
InsAIts does not just alert -- it acts. When a critical anomaly is detected:
1. The agent receives a corrective instruction injected into its context
2. The intervention is logged with before/after details
3. You can review all interventions in the dashboard

### Stealth Mode
Toggle stealth on/off from the dashboard. In stealth mode, InsAIts monitors without the AI knowing. Useful for security auditing where you want to observe natural agent behavior.

### Inter-Session Dialog
Run multiple AI agents in different terminals? InsAIts lets them communicate:
- Send messages between terminals from the dashboard
- Coordinate work across agents (file locks, task assignment)
- See the full dialog thread in the dashboard

### Session Guardian
For long sessions (hours), InsAIts automatically:
- Saves work snapshots every 25 tool calls
- Detects context compression (when Claude forgets earlier work)
- Injects a resume anchor with your progress so the AI picks up where it left off
- Emergency-saves on crash so nothing is lost

### Behavioral Fingerprinting
Each agent gets a behavioral profile. InsAIts detects when an agent starts behaving differently from its baseline -- which can indicate a compromised tool, prompt injection, or model degradation.

### Pattern Learning
After each session, InsAIts can learn from what it saw. It identifies recurring patterns specific to your project, reducing false positives and catching real issues faster.

![Dashboard Panels](assets/dashboard-panels.png)

---

## Install

```bash
pip install insa-its[full]
```

That is it. No API keys. No cloud account. No configuration files.

**Minimal install** (no local embeddings, no terminal dashboard):
```bash
pip install insa-its
```

---

## Quick Start — Step by Step

### Step 1: Install

```bash
pip install insa-its[full]
```

### Step 2: Start the Collector

Open a terminal and run:
```bash
insaits-collector
```
This starts the central event hub on **port 5003**. It collects events from all AI sessions, manages the dialog bus, and provides the data API for the dashboard.

### Step 3: Start the Dashboard

Open a **second terminal** and run:
```bash
insaits-dashboard
```
This starts the web dashboard on **port 5001**. Open [http://localhost:5001](http://localhost:5001) in your browser to see real-time monitoring.

### Step 4: Start using AI

That is it. Start Claude Code, Cursor, or any AI tool in your project. InsAIts will detect and monitor tool calls, agent spawns, and message flows automatically.

### Available Commands

| Command | What it does | Port |
|---------|-------------|------|
| `insaits-collector` | Central event stream hub, session registry, dialog bus | 5003 |
| `insaits-dashboard` | Real-time web dashboard with 16+ security panels | 5001 |
| `insaits-tui` | Terminal UI dashboard (for VS Code split terminal) | - |

You can also run as Python modules:
```bash
python -m insa_its.collector
python -m insa_its.web
```

### Claude Code Integration (Optional)

To enable deep Claude Code monitoring, add this to your project's `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "python -c \"from insa_its.hooks import run_hook; run_hook()\"",
        "timeout": 10000
      }
    ]
  }
}
```

Then add this to your project's `CLAUDE.md` so Claude reads the Guardian work log:

```markdown
## PHASE_GUARDIAN — Session Continuity
When you see a `[InsAIts Resume Anchor]` in a tool result, trust it.
It is your work journal from the Guardian. Use it to pick up where
you left off without re-reading everything.
```

### Python API

```python
from insa_its import insAItsMonitor

monitor = insAItsMonitor()

result = monitor.send_message(
    text="Here is the API key: sk-abc123secret",
    sender_id="agent1",
    llm_id="gpt-4o"
)

for anomaly in result["anomalies"]:
    print(f"[{anomaly.severity}] {anomaly.type}: {anomaly.details}")
```

See [example.py](example.py) for the complete working example.

---

## Demo

[![InsAIts Dashboard Demo](https://img.youtube.com/vi/sxTxlOPcRmI/maxresdefault.jpg)](https://www.youtube.com/watch?v=sxTxlOPcRmI&list=PLdSaNvpK_XOdsWyYw5vJnp7OS0Du9VIWt)

> Click the image above to watch the dashboard in action.

---

## What InsAIts Does NOT Do

- **No cloud calls.** Zero. Every byte of processing happens on your machine.
- **No telemetry.** We do not track usage, sessions, errors, or anything else.
- **No data leaves your machine.** Your code, your prompts, your AI responses -- they stay on your disk. Period.
- **No API keys required.** Install and use. That is the entire setup.

---

## Attribution

InsAIts was built during live sessions with Claude Code. The integration was contributed to the [everything-claude-code](https://github.com/anthropics/everything-claude-code) repository as [PR #370](https://github.com/anthropics/everything-claude-code/pull/370), confirmed by Affaan (Anthropic).

---

## Links

- [PyPI Package](https://pypi.org/project/insa-its/) -- `pip install insa-its`
- [Website](https://nomadu27.github.io/InsAIts-public/)
- [YouTube Playlist](https://www.youtube.com/watch?v=sxTxlOPcRmI&list=PLdSaNvpK_XOdsWyYw5vJnp7OS0Du9VIWt)
- [YouTube Channel](https://www.youtube.com/@insAIts1407)

---

## About

InsAIts is developed by **Steddy Nova SRL / YuyAI**. The source code is in a private repository. The package is fully functional via PyPI.

Contact: info@yuyai.pro

Licensed under [Apache 2.0](LICENSE).
