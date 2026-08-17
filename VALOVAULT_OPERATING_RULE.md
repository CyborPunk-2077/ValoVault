# ValoVault Permanent Development Rule

This project must never depend on one conversation or one temporary working directory as its only recoverable copy.

Permanent loop:

**inspect → implement → test → fix → verify → update `CURRENT_STATE.md` → complete ZIP / Git checkpoint → continue**

Rules:

- Continue from the newest verified implementation; never restart ValoVault because an older snapshot exists.
- Do not recreate completed phases or redesign established architecture solely for checkpointing.
- After every major phase or 1–2 substantial implementation passes: test, update `CURRENT_STATE.md`, create and verify a complete project ZIP, provide it to the user, push/update GitHub when available, and pin a milestone branch or equivalent durable checkpoint.
- A checkpoint ZIP contains the whole recoverable project, excluding only disposable dependency/cache/build output and secrets.
- If a command hangs: inspect what completed, terminate only that command, verify partial writes, repair if needed, use a shorter equivalent, and resume. Do not replay an entire phase.
- Before a conversation becomes too long: finish the current safe implementation unit, test it, update state, checkpoint, and explicitly recommend moving to a fresh ValoVault chat.
- A fresh chat continues from the latest repository/complete checkpoint + `CURRENT_STATE.md` + necessary artifacts, never from memory alone.
- At all times ask: **If this conversation disappeared right now, could another competent coding agent continue from saved artifacts without losing meaningful work?** If not, checkpoint before more major implementation.

## Authority split — strict

- **The active ValoVault chat is the authoritative planning/continuation brain.** It owns product intent, architecture reasoning, what to improve next, phase sequencing, and the exact next implementation/master prompt.
- **GitHub is the durable execution/checkpoint layer.** It stores code/history/checkpoint metadata/milestones and is used to recover exact implementation state; it does not decide the roadmap by itself.
- `CURRENT_STATE.md` is the concise machine handoff/recovery index. It must accurately record the exact stop point and immediate next objective, but it is **not a replacement for the richer planning context established in chat**.
- Before starting each new substantial pass, explicitly formulate the canonical next prompt in chat from the full accumulated ValoVault context, then execute that prompt against the newest verified checkpoint.
- When moving to a fresh chat: recover the newest implementation from GitHub/complete checkpoint, read `CURRENT_STATE.md` and this operating rule, preserve established product intent/architecture, and then continue the roadmap rather than inventing a new one.
