# ValoVault Permanent Development Rule

This project must never depend on one conversation or one temporary working directory as its only recoverable copy.

Permanent loop:

**inspect → implement → test → fix → verify → update `CURRENT_STATE.md` → complete ZIP / Git checkpoint → continue**

Rules:

- Continue from the newest verified implementation; never restart ValoVault because an older snapshot exists.
- Do not recreate completed phases or redesign established architecture solely for checkpointing.
- After every major phase or 1–2 substantial implementation passes: test, update `CURRENT_STATE.md`, create and verify a complete project ZIP, provide it to the user, push the verified complete source tree to GitHub `main`, and pin the same verified commit with a `milestone/phase-XX[-pass-YY]` branch when GitHub is configured.
- A checkpoint ZIP contains the whole recoverable project, excluding only disposable dependency/cache/build output and secrets.
- If a command hangs: inspect what completed, terminate only that command, verify partial writes, repair if needed, use a shorter equivalent, and resume. Do not replay an entire phase.
- Before a conversation becomes too long: finish the current safe implementation unit, test it, update state, checkpoint, and explicitly recommend moving to a fresh ValoVault chat.
- A fresh chat continues from the latest repository/ZIP + `CURRENT_STATE.md` + necessary artifacts, never from memory alone.
- At all times ask: **If this conversation disappeared right now, could another competent coding agent continue from saved artifacts without losing meaningful work?** If not, checkpoint before more major implementation.
