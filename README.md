# InsAIts

**Runtime security for AI agents. Catches what your AI misses.**

[![PyPI v4.8.0](https://img.shields.io/badge/PyPI-v4.8.0-cyan)](https://pypi.org/project/insa-its/)
[![Downloads](https://img.shields.io/badge/downloads-13.45k-brightgreen)](https://pypi.org/project/insa-its/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://pypi.org/project/insa-its/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![100% Local](https://img.shields.io/badge/Data-100%25%20Local-brightgreen)](#what-insaits-does-not-do)
[![Tests](https://img.shields.io/badge/Tests-1946%20passing-brightgreen)](#verified-numbers)
[![Trial](https://img.shields.io/badge/Trial-14%20days%20full-yellow)](#pricing)
[![Website](https://img.shields.io/badge/Website-Live-cyan)](https://nomadu27.github.io/InsAIts-public/)

**[Website](https://nomadu27.github.io/InsAIts-public/)** | **[PyPI](https://pypi.org/project/insa-its/)** | **[YouTube](https://www.youtube.com/@insAIts1407)**

---

## What It Does

InsAIts monitors AI-to-AI communication in real-time. It watches every tool call, every response, and every agent-to-agent message for security anomalies — credential leaks, hallucination chains, prompt injection attempts, unauthorized writes, rogue subagent behavior, and 25+ more anomaly types. When it catches something critical, it intervenes immediately by injecting corrective instructions into the agent's context, before the damage reaches your codebase.

It runs as a Claude Code hook. You install it, and it works silently in the background. No configuration needed.

![InsAIts Dashboard](assets/dashboard-v4.4.3-security-hero.png)

---

## Verified Numbers

These are real numbers from real sessions, not benchmarks:

| Metric | Value | Context |
|--------|-------|---------|
| **PyPI downloads** | **12,260+** | Total installs of `insa-its` |
| SDK version | **4.8.0** | Latest release on PyPI |
| Anomaly detectors | **30** | Full TRS-weighted detector suite (see [full list](#real-time-anomaly-detection-30-detectors)) |
| OWASP coverage | **MCP Top 10 + Agentic AI Top 10** | ASI01–ASI10, with CVE references |
| Tests passing | **1,946** | API (566) + SDK (1380), full detector + integration + E2E |
| Longest continuous session | **9h 16min** | Single session, minimal interruptions |
| Anomalies caught and corrected | **682+** | Across multi-terminal sessions |
| Trial length | **14 days** | Full feature access, no card required |
| Data sent to cloud | **0 bytes** | Everything runs locally |

### Ecosystem adoption
InsAIts is the security core of the **AgentShield** runtime, a fork of Everything Claude Code ecosystem,. AgentShield is our `feat/insaits-security-hook` branch of `everything-claude-code` — same codebase, rebranded downstream. If you use AgentShield, you're running InsAIts.

---

## Pricing

All detection is open source. You pay for productivity, longer sessions, premium detectors, and team features.

| Tier | Monthly | Lifetime | What unlocks |
|------|--------:|---------:|--------------|
| **Trial** | free | 14 days | Full feature access, no card |
| **Starter** | **€10** | **€99** | All 30 detectors, all Phase 3 reliability gates, Session Vault, full dashboard, work-checkpoint continuity |
| **Pro** | **€49** | **€299** | Starter + L3 subagent anchors, Session-SAE behavioral anomaly detection, inter-session dialog, RABE export, Decipher engine, cloud embeddings, priority support |
| **Enterprise** | from €200 | custom | SOC2-ready audit export, multi-seat, white-label dashboard, dedicated support |

### Activate

- [**Starter €10/month**](https://buy.stripe.com/eVq7sLdsbgItgTqaaIb3q0a)
- [**Pro €49/month**](https://buy.stripe.com/bJefZhewffEpeLieqYb3q01)
- [**Starter Lifetime €99**](https://buy.stripe.com/eVq4gzfAjcsd6eMfv2b3q09)
- [**Pro Lifetime €299**](https://buy.stripe.com/3cI8wPfAjak5bz61Ecb3q04)

After payment, your key arrives by email. Set `INSAITS_LICENSE_KEY` before starting the collector. **Passive mode** (expired trial, no key): detection still runs, anomalies still appear on the dashboard — injection/intervention is what unlocks when you activate.

Enterprise: `info@yuyai.pro`.

---

## What's New in v4.8.0

- **Subagent observability (L2 Layer)** — full visibility into subagent tool calls with parent-agent linkage, scope-drift guard, and rogue-intent detection. The dashboard now shows every subagent call with its parent Agent ID and assigned-prompt digest.
- **Work-checkpoint continuity** — Guardian Session Vault now captures task progress snapshots every 50 tool calls. Recover from context compression without losing track of what you were doing.
- **Lean observability** — token-optimization pass: doc-only demotions, escalation gates, and smart injection budgeting save ~1,200–1,800 tokens per clean session.
- **Session-SAE (Pro/Enterprise)** — autoencoder-based behavioral anomaly detector catches session-pattern drift that rule-based detectors miss.
- **False-positive fixes (FP1–FP5)** — implementer-verb whitelist, adaptive subagent TTL, JSON-crash fix on set/frozenset encoding, `cwd`-audit every entry.
- **Truth-first dashboard** — feed semantics match what actually fires. No more "SAFE" header while CRITICAL events sit in the feed.

Full technical notes live on the API repo releases page.

---

## Features

### Live Dashboard (20+ panels)
Open your browser at `http://localhost:5001` after starting `insaits-dashboard`. You get:
- **Threat Readiness Score** — TRS v2 with cooldown, variety gate, and time-weighted signals
- **Anomaly Feed** — live stream of detected issues with severity levels and details
- **Agent Intelligence Scores** — each agent scored independently (trust level, stability, anomaly rate)
- **Blast Radius** — severity-weighted impact measurement across your session
- **Intervention Log** — shows when InsAIts corrected an agent and what happened next
- **Circuit Breaker** — manually pause/resume AI execution with one-click toggle
- **OWASP Panel** — full MCP Top 10 + Agentic AI Top 10 compliance view with CVE references
- **Agent Communication Map** — visual graph of agent-to-agent message flows
- **Subagent Drill-Down** — per-subagent tool-call traces with rogue-intent flags
- **RABE Analysis** — Risk-Adjusted Behavioral Entropy tracking per session
- **Session Vault** — full session state, snapshots, work-journal checkpoints
- **Token Budget** — live injection cost tracking (MEASURED vs ESTIMATED vs OVERHEAD)

### Real-Time Anomaly Detection (30 detectors)
InsAIts catches issues as they happen, not after. Full detector list (TRS-weighted):

**Security-critical (OWASP MCP Top 10):**
- Credential exposure, prompt injection, tool poisoning, data exfiltration
- Shadow server, unauthorized access, unauthorized write, exfiltration pattern
- Entropy covert channel

**Behavioral / integrity:**
- Rogue agent, hallucination chain, memory poisoning, information flow
- Phantom citation, chain tampering, semantic drift, agent probing pattern
- Signature match (known-bad patterns)

**Communication quality:**
- Shorthand emergence, context collapse, truncated output
- Uncertainty propagation, governance gap

**Advanced / adaptive:**
- Behavioral fingerprint, tool call frequency anomaly, tool description divergence

**Session health predictors:**
- Context exhaustion predicted, edit spiral predicted, scope drift predicted

**Pro/Enterprise tier:**
- Session-SAE (session pattern anomaly) — autoencoder behavioral detector

### Active Intervention — Rogue-Only Blocking
InsAIts does not just alert — it acts. But **only rogue-agent behavior can block**:
- `_BLOCKING_SEVERITIES = {"CRITICAL"}` — only CRITICAL severity ever gates the next tool call
- `tool_type_mismatch`, `compliance_bypass_attempt`, `checklist_without_execution` → HIGH warnings, **non-blocking**
- Rogue-intent detection (subagent scope drift, agent probing) → HIGH/MEDIUM, alert-only
- Infrastructure DENY only on retry-storm or circuit-breaker — not on agent behavior
- Layer-respect: L1/L2/L3 anchor injections honor per-layer enable toggles, anomaly-delta gates, and shorthand gates

### Stealth Mode
Toggle stealth on/off from the dashboard. In stealth mode, InsAIts monitors without the AI knowing. Useful for security auditing where you want to observe natural agent behavior.

### Inter-Session Dialog
Run multiple AI agents in different terminals? InsAIts lets them communicate:
- Send messages between terminals from the dashboard
- Coordinate work across agents (file locks, task assignment)
- See the full dialog thread in the dashboard

### Session Guardian — Work-Checkpoint Continuity
For long sessions (hours), InsAIts automatically:
- Saves work snapshots every 50 tool calls (v4.8.0.2)
- Detects context compression (when Claude forgets earlier work)
- Injects a resume anchor with your progress so the AI picks up where it left off
- Captures task-progress checkpoints in the Session Vault
- Emergency-saves on crash so nothing is lost

### Behavioral Fingerprinting
Each agent gets a behavioral profile. InsAIts detects when an agent starts behaving differently from its baseline — which can indicate a compromised tool, prompt injection, or model degradation.

### LangChain and CrewAI Integrations
Drop-in integrations for popular agent frameworks. Monitor LangChain chains, CrewAI crews, and LangGraph workflows with the same anomaly detection and intervention engine.

### Pattern Learning
After each session, InsAIts can learn from what it saw. It identifies recurring patterns specific to your project, reducing false positives and catching real issues faster. In v4.8, patterns feed an SQLite intelligence store shared across sessions.

---

## Install

```bash
pip install insa-its[full]
```

### Claude Code hook setup

Add this to your `.claude/settings.json`:

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
- **No data leaves your machine.** Your code, your prompts, your AI responses — they stay on your disk. Period.
- **No API keys required.** Install and use. That is the entire setup.

---

## Attribution

InsAIts was built during live sessions with Claude Code. The integration was contributed to the [everything-claude-code](https://github.com/anthropics/everything-claude-code) repository as [PR #370](https://github.com/anthropics/everything-claude-code/pull/370), confirmed by Affaan (Anthropic).

---

## Links

- [PyPI Package](https://pypi.org/project/insa-its/) — `pip install insa-its`
- [Website](https://nomadu27.github.io/InsAIts-public/)
- [YouTube Playlist](https://www.youtube.com/watch?v=sxTxlOPcRmI&list=PLdSaNvpK_XOdsWyYw5vJnp7OS0Du9VIWt)
- [YouTube Channel](https://www.youtube.com/@insAIts1407)

---

## About

InsAIts is developed by **Steddy Nova SRL / YuyAI**. The source code is in a private repository. The package is fully functional via PyPI.

Contact: info@yuyai.pro

Licensed under [Apache 2.0](LICENSE).
