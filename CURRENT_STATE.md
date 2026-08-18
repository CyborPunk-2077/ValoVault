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

## Preserved product decisions

Local-first; UE5 Weapon Lab remains fidelity authority; browser lab is fallback/inspection; FModel/ValorantPorting/Blender local extraction; Base Vandal → Reaver Vandal first premium vertical slice; immutable evidence/provenance; no fake READY/PASS; no running VALORANT/Vanguard/protected-memory/multiplayer interaction; no broader premium scaling until the real Reaver round trip succeeds.

## Completed Phase 08 stack

Passes 01–09 remain complete: deterministic fidelity; capture/index/preflight/working set; scorecards/calibration/evidence cohorts/human threshold decisions; reversible threshold governance; calibrated replay; PASS-only promotion; target-PC handoff/certification; portable return reconciliation/root rebinding; execution-kit/environment doctor/safe return bundle.

### Pass 10 — complete

Added:
- `packages/shared-schema/target-pc-session.schema.json`;
- `packages/shared-schema/target-pc-execution-receipt.schema.json`;
- `tools/fidelity/target_pc_session.py`;
- canonical `data/control-plane/target-pc-session-plan.json`;
- durable non-mutating `target-pc-session-plan` job + GET plan/receipt APIs;
- Pass-09 return-package receipt validation/inclusion;
- Pass-10 tests/audit/report/verification.

Session contract:
- 10 required target-PC steps;
- exactly 2 `MANUAL_EVIDENCE_REQUIRED` capture gates;
- 9 receiver-only downstream reconciliation/calibration/certification steps;
- session bound to handoff session ID, fidelity-spec SHA, execution-kit manifest SHA, machine identity and nonce;
- offline automatic steps only; runner never launches/inspects/controls VALORANT/Vanguard;
- interrupted RUNNING step becomes `INTERRUPTED`, requiring explicit retry; completed work is not replayed;
- manual evidence records root + reviewer/rationale + counts/bytes/directory SHA, never copied proprietary files;
- close rejected until all required target steps are complete;
- execution receipt is SHA-256 hash-bound safe metadata; receipt proves workflow provenance only and is not remote fidelity truth;
- browser/backend cannot run steps, record evidence or close sessions.

## Current packaged truth
- catalog 17; classification research blockers 2;
- local realtime/Web3D/Unreal validated: 0 / 0 / 0;
- captures 0/44 + 0/44; preflight BLOCKED / 88; queue 10 pending; working/fidelity blocked;
- calibration/threshold/policy evidence remains empty; canonical Reaver thresholds `{}`;
- target-PC handoff 10/10; return reconciliation BLOCKED / 2; certification BLOCKED / 9;
- environment doctor BLOCKED / 3 (export roots, Blender, Weapon Lab);
- execution-kit plan READY / **80 files / 0 violations**;
- target-PC session plan READY / **10 target / 2 manual / 9 receiver-only**;
- active target-PC session: none; execution receipt: none; active durable jobs: 0.

## Verification
- **121 pytest tests passed**;
- every audit from Phase 04 through Phase 08 Pass 10: PASS;
- Python compileall + relevant JS syntax: PASS;
- live session-plan job/API: PASS;
- session mutation API probes: 404 as required;
- synthetic full session through hash-bound receipt + safe return: PASS;
- interruption/retry/resume, stale spec/kit, incomplete close and receipt tampering tests: PASS.

## Direction correction after Pass 10 — Reaver closure lock

The active chat reviewed the project direction and chose the first-real-run path. The core architecture remains valid, but further speculative control-plane/fidelity abstraction is now frozen. See `docs/EXECUTION_STRATEGY.md` in the current complete checkpoint.

Until the first real Reaver round trip succeeds, new engineering work is allowed only for a real-run blocker, operator-friction reduction, regression fix, or durability/recovery improvement. Do not broaden to other premium families.

Workflow hardening added after Pass 10 without changing product semantics:
- root `START_HERE.md`;
- `TARGET_PC_START_HERE.md` shipped inside the target-PC execution kit;
- `tools/fidelity/configure_target_pc.py` for one-command local tool/root configuration;
- `prepare-reaver-release.ps1` / `.sh` to build + verify the one target-PC execution ZIP;
- `tools/recovery/build_recovery_vault.py` for one deduplicated historical recovery vault.

**Next product action:** prepare and execute the first real Reaver target-PC run. Fix only blockers that the real run actually exposes.

## Durable recovery

Newest complete verified filesystem checkpoint: `ValoVault_PASS10_WORKFLOW_HARDENED_COMPLETE.zip`, SHA-256 `f2b6220ac514152c5c06e7ea4507bcf5350a95ac5dc35f75486b0e3ebd15fd0a`.

Deduplicated history bundle: `ValoVault_RECOVERY_VAULT_ALL_HISTORY.zip`, SHA-256 `8ed7223bc479e7ccfe54e77f6824f47ffcf2693af07ad1f2d844fd0052e617e0` (28 discovered copies → 22 unique artifacts; CRC PASS).

GitHub remains the durable history/handoff layer but its direct `main` tree is not yet proven path/hash-complete. Prefer the complete verified ZIP / Recovery Vault for exact filesystem recovery until a normal authenticated Git mirror is available.