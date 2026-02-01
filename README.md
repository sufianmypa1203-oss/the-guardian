# 🛡️ The Guardian - Safety & Reliability Agent

> **"It is better to ship nothing than to ship something that breaks production."**

A production-grade AI agent persona that enforces **Additive Development** and prevents breaking changes before, during, and after every code change.

## 🎯 What This Does

The Guardian acts as your "Safety Inspector" by:

| Check | What It Does |
|-------|-------------|
| **Pre-Code Verification** | Identifies affected systems before you write code |
| **Signature Protection** | Blocks breaking function signature changes |
| **Feature Flag Enforcement** | Requires flags for all new user-facing features |
| **Rollback Readiness** | Enforces canary rollout (5% → 25% → 50% → 100%) |
| **Post-Change Audit** | Detects destructive patterns after changes |

## 🚀 Quick Start

### Option 1: Copy to your project
```bash
mkdir -p .agent/agents
cp AGENT.md .agent/agents/safety-reliability-agent.md
```

### Option 2: Clone and symlink
```bash
git clone https://github.com/YOUR_USERNAME/the-guardian.git ~/.agents/the-guardian
ln -s ~/.agents/the-guardian/AGENT.md .agent/agents/safety-reliability-agent.md
```

## 🔑 Activation

Say any of these to activate The Guardian:

- `"Is this safe to ship?"`
- `"Audit this change"`
- `"Check for breaking changes"`
- `"Review this PR"`
- `/safe-check`

## 📦 Required Skills

For full power, also install these companion skills:

| Skill | Purpose |
|-------|---------|
| [safe-feature-addition](https://github.com/YOUR_USERNAME/safe-feature-addition) | Core safety audit & feature flag logic |
| codebase-architecture-mapper | Dependency analysis |
| testing-patterns | Verification steps |

## 🧩 Golden Heuristics

1. **Signature Shield** - New parameters MUST have default values
2. **Flag or Fail** - Every new feature needs a feature flag
3. **Additive > Destructive** - Extend, don't rewrite
4. **Rollback Ready** - No deployment without a rollback plan
5. **Three File Rule** - Block 3+ file refactors without justification

## 📄 License

MIT License - Use freely, stay safe! 🛡️
