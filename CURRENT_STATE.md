# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 10 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next implementation prompt:** must be authored in the active ValoVault chat. Do not infer Pass 11 solely from this file.

## Strict continuation authority

- **The active ValoVault chat owns roadmap reasoning, improvements, phase sequencing and the exact next implementation/master prompt.**
- **GitHub owns durable source/history/checkpoint metadata/milestones.**
- This file is a concise recovery handoff, not the full project strategy.
- Before each substantial pass, state the canonical prompt in chat first.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/Git checkpoint → continue**.

Truth boundary: **classification ≠ assets ≠ runtime readiness ≠ fidelity ≠ calibrated replay ≠ promoted policy ≠ certification**.

## Product invariants

Local-first; UE5 Weapon Lab remains fidelity authority; browser lab is fallback/inspection; FModel/ValorantPorting/Blender local extraction; Base Vandal → Reaver Vandal first premium vertical slice; immutable evidence/provenance; no fake READY/PASS; no running VALORANT/Vanguard/protected-memory/multiplayer interaction; no broader premium scaling until the real Reaver round trip succeeds.

## Completed stack

Phase 08 Passes 01–09 remain complete: deterministic fidelity; capture/index/preflight/working set; scorecards/calibration/evidence cohorts/human threshold decisions; reversible threshold governance; calibrated replay; PASS-only promotion; target-PC handoff/certification; portable return reconciliation/root rebinding; execution-kit/environment doctor/safe return bundle.

### Phase 08 Pass 10 — complete

Added:
- `packages/shared-schema/target-pc-session.schema.json`;
- `packages/shared-schema/target-pc-execution-receipt.schema.json`;
- `tools/fidelity/target_pc_session.py`;
- canonical `data/control-plane/target-pc-session-plan.json`;
- durable non-mutating `target-pc-session-plan` job + GET plan/receipt APIs;
- Pass-09 safe-return receipt validation/inclusion;
- Pass-10 tests/audit/report/verification.

Session contract:
- **10 required target-PC steps**;
- exactly **2 MANUAL_EVIDENCE_REQUIRED** capture gates;
- **9 receiver-only** reconciliation/calibration/certification steps;
- session bound to handoff session ID, fidelity-spec SHA, execution-kit manifest SHA, machine identity and nonce;
- automatic steps are offline ValoVault tooling only; runner never launches/inspects/controls VALORANT/Vanguard;
- interrupted RUNNING steps recover to `INTERRUPTED`, requiring explicit retry; completed work is not replayed;
- manual evidence records owned root + reviewer/rationale + counts/bytes/directory SHA, never copied proprietary evidence;
- `close` is rejected until every required target step is complete;
- execution receipt is SHA-256 hash-bound safe metadata. It proves workflow provenance only and does not make remote fidelity/readiness truth authoritative;
- backend/browser cannot run steps, record manual evidence or close sessions.

## Current packaged truth

- catalog 17; classification research blockers 2;
- realtime/Web3D/Unreal validated: 0 / 0 / 0;
- captures 0/44 reference + 0/44 candidate; preflight BLOCKED / 88; queue 10 pending; working/fidelity blocked;
- calibration/threshold/policy evidence empty; canonical Reaver thresholds `{}`;
- handoff 10/10; return reconciliation BLOCKED / 2; certification BLOCKED / 9;
- environment doctor BLOCKED / 3 (export roots, Blender, Weapon Lab);
- execution-kit plan READY / **77 files / 0 violations**;
- session plan READY / **10 target / 2 manual / 9 receiver-only**;
- active target-PC session: none; execution receipt: none; active durable jobs: 0.

## Verification

- **118 pytest tests passed**;
- every audit from Phase 04 through Phase 08 Pass 10: PASS;
- Python compileall + relevant JS syntax: PASS;
- live session-plan job/API: PASS;
- session mutation API probes: 404 as required;
- synthetic full session through hash-bound receipt + safe return: PASS;
- interruption/retry/resume, stale spec/kit, incomplete close and receipt-tamper tests: PASS.

## Decision point for the active chat

The workflow is now sufficient to package, validate, resume and return a Reaver target-PC session without trusting remote truth or automating the game. The active chat must choose what comes next. The strongest options are:

1. **first-real-run readiness/release freeze** — prepare an operator-grade Reaver release bundle/checklist and stop adding abstractions until the user executes it on the actual target PC; or
2. **durability cleanup** — repair/audit the GitHub direct-source mirror before handing the repository to Claude Code.

Do not silently choose either path from this file.

## Durable recovery

Use the newest complete verified ZIP recorded in `GITHUB_CHECKPOINTS.md` and persisted in `/ValoVault Checkpoints/` in ChatGPT Library. GitHub remains the durable history/handoff layer, but its direct `main` tree is not yet proven path/hash-complete.
