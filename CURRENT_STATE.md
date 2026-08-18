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
- execution-kit plan READY / **83 files / 0 violations**;
- target-PC session plan READY / **10 target / 2 manual / 9 receiver-only**;
- active target-PC session: none; execution receipt: none; active durable jobs: 0.

## Verification
- **134 pytest tests passed**;
- every audit from Phase 04 through Phase 08 Pass 10: PASS;
- Python compileall + relevant JS syntax: PASS;
- live session-plan job/API: PASS;
- session mutation API probes: 404 as required;
- synthetic full session through hash-bound receipt + safe return: PASS;
- interruption/retry/resume, stale spec/kit, incomplete close and receipt tampering tests: PASS.

## Direction correction after Pass 10 — Reaver closure lock

The active chat reviewed the project direction and chose the first-real-run path. The core architecture remains valid, but further speculative control-plane/fidelity abstraction is now frozen. See `docs/EXECUTION_STRATEGY.md`.

Until the first real Reaver round trip succeeds, new engineering work is allowed only for a real-run blocker, operator-friction reduction, regression fix, or durability/recovery improvement. Do not broaden to other premium families.

Workflow hardening added after Pass 10 without changing product semantics:
- root `START_HERE.md` plus `RUN_REAVER.ps1` / `.sh`;
- `TARGET_PC_START_HERE.md` shipped inside the target-PC execution kit;
- `tools/fidelity/configure_target_pc.py` for one-command local tool/root configuration;
- `tools/fidelity/reaver_operator.py` as the single target/receiver facade;
- target facade auto-progresses through every safe step and pauses only at the two real evidence gates;
- receiver facade verifies/rebinds returned evidence, regenerates local truth, prepares calibration review, applies explicitly reviewed thresholds, runs calibrated replay, promotes PASS-only policy and re-evaluates certification;
- target-machine project/Python/comparator absolute paths are treated as hash-verified non-authoritative provenance and rebound locally instead of creating meaningless operator binding chores;
- `prepare-reaver-release.ps1` / `.sh` builds + verifies the one target-PC execution ZIP;
- `tools/dev/reaver_release_selftest.py` plus `verify-reaver.ps1` / `.sh` replaces the long manual release-verification command list;
- `tools/recovery/build_complete_checkpoint.py` plus `checkpoint-now.ps1` / `.sh` builds and verifies the current safe complete checkpoint;
- `tools/recovery/build_recovery_vault.py` maintains one deduplicated historical Recovery Vault.

Scoped closure status:
- first-Reaver software path: **24 / 24 implemented (100%)**;
- real evidence/certification path in packaged fixture: **0 / 11 satisfied**;
- this is deliberately **not** an overall ValoVault-completion percentage.

**Next engineering direction while the user is not yet testing:** do not create Pass 11 or another fidelity abstraction. Continue independent product-completion work that does not require proprietary local evidence—starting with the public metadata/catalog product path and operator-facing catalog/control polish—while preserving the Reaver closure lock. The next Reaver-specific engineering change must be a blocker observed during the eventual real run.

## Independent product completion — catalog hardening

While real Reaver evidence is deferred, the public catalog path was hardened without changing Phase-08/Reaver semantics.

Added:
- `tools/catalog/catalog_release.py`: stage → audit → shrink guard → atomic promote → provenance state;
- backend/control catalog refresh routed through the safe promoter before onboarding;
- API source/version provenance preserved through fixture replay;
- `data/catalog/public-catalog-state.json` contract for release/health/truth-boundary metadata;
- catalog source/release UI, large-catalog lazy loading, view filters and sorting;
- Control Plane catalog release/health/warning visibility;
- `refresh-public-catalog.ps1` / `.sh`.

Current public API provenance independently verified in chat: release branch `release-13.02`, version `13.02.00.5229475`, engine `5.3.2.0`, build date `2026-08-04T00:12:33Z`. The current container cannot directly resolve the API, so the packaged snapshot remains the deterministic fixture rather than fabricating a full live snapshot. A network-enabled environment can now refresh the full catalog safely in one command.

Verification after this unit: **134 pytest tests**, all existing audits, compileall/JS syntax and the **83-file / 0-violation** Reaver target kit all PASS. Browser screenshot QA remains environment-blocked because the available Chromium binary hangs with DBus/zygote errors before frame capture; this was bounded and not looped.

**Independent usability/distribution hardening also completed:**
- `tools/dev/local_app_doctor.py` distinguishes required app-start blockers from optional real-machine capabilities;
- `VALOVAULT_START.ps1` / `.bat` / `.sh` provide one normal local-app entrypoint;
- `PROJECT_COMPLETION_MATRIX.json` is the anti-loop lane map: software-complete vs environment-gated vs real-evidence-required vs deferred-after-Reaver.

Current local-app doctor: **PASS / 17 checks / 0 required blockers / 4 expected optional warnings** (no promoted live catalog state yet, no export roots, Blender or Weapon Lab executable). Those warnings are machine inputs, not reasons to invent more architecture.

Recovery Vault refresh hardening:
- fixed an in-place refresh recursion bug discovered during this checkpoint: a previous Recovery Vault is now always excluded from candidate payloads;
- new vaults are written to a temporary sibling, CRC-verified, then atomically promoted;
- vault schema v2 explicitly forbids recursively embedding an older Recovery Vault;
- tests cover in-place refresh and duplicate-alias deduplication.

**Next independent direction:** only close concrete product/usability gaps that can be verified without proprietary evidence. Do not create a new fidelity pass and do not ask the user for real Reaver evidence yet.

## Durable recovery

Use the newest complete verified ZIP recorded in `GITHUB_CHECKPOINTS.md`, plus the deduplicated Recovery Vault. The current checkpoint builder excludes secrets/caches/local proprietary evidence automatically and verifies CRC + recorded SHA/size before a checkpoint is accepted. GitHub remains the durable history/handoff layer; do not claim a source tree is a path/hash-complete mirror unless that exact tree has been audited.
