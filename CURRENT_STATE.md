# ValoVault — CURRENT STATE

**Canonical checkpoint:** Phase 08 in progress — **Pass 06 complete and verified**  
**Date:** 2026-08-18  
**Next objective:** Phase 08 Pass 07 — explicit threshold-version promotion governance + reproducible target-PC calibration/replay certification handoff for the Base Vandal → Reaver Vandal vertical slice.

## Strict continuation authority

- **The active ValoVault chat owns roadmap reasoning, improvements, phase sequencing and the exact next implementation/master prompt.**
- **GitHub owns durable source/history/checkpoint metadata/milestones.**
- This file is the concise recovery handoff, not the whole product-strategy context.
- Before every substantial pass, formulate the canonical prompt in chat first, then execute it against the newest verified checkpoint.
- Never restart completed phases because an older snapshot exists.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/Git checkpoint → continue**.

Truth boundary: **classification ≠ assets ≠ runtime readiness ≠ fidelity ≠ calibrated promotion**.

## Architecture that must remain intact

Local-first catalog; FModel/ValorantPorting/Blender local export pipeline; browser Weapon Lab fallback; UE5 `unreal/WeaponLab/` as high-fidelity authority; Base Vandal → Reaver Vandal as first premium vertical slice; immutable capture evidence + derived SHA provenance; no fake READY; no interaction with running VALORANT/Vanguard/protected memory/multiplayer traffic.

## Phase 08 status

Passes 01–05 remain complete: deterministic fidelity orchestration; capture-session/preflight; resumable capture queue + derived working set; raw scorecards/evidence/calibration queue; ACCEPTED-evidence cohorts + explicit human threshold-decision packets.

### Pass 06 — complete

Added reviewed-threshold governance and calibrated replay safety:

- `tools/fidelity/threshold_governance.py`
- `tools/fidelity/threshold_application.py`
- `tools/fidelity/calibrated_replay.py`
- threshold-governance/application/replay schemas and canonical ledgers/plans
- durable jobs: `threshold-governance`, `threshold-application-plan`, `calibrated-replay-plan`
- GET APIs for governance/application preview/application ledger/calibrated replay
- POST APIs only for the three **non-mutating** jobs
- control UI actions: `VALIDATE THRESHOLDS`, `PREVIEW APPLICATION`, `PLAN CALIBRATED REPLAY`
- deliberately **no** `/api/control/threshold-apply` endpoint

Reviewed patches are validated against exact spec SHA, reviewer/rationale, finite rules, action/channel/metric contracts, ACCEPTED evidence and matching provenance-locked cohorts.

The control-plane application preview is token-free and non-mutating. Explicit application is CLI-only: a one-time token is bound to the exact plan; a byte-for-byte spec backup is created before modification; stale or consumed plans are rejected; only reviewed action-local thresholds change; rollback requires reviewer+rationale and restores the verified backup.

Calibrated replay recognizes only an active non-rolled-back `APPLIED_FOR_REPLAY` event with the exact applied spec SHA and a provenance-locked READY working set. Replay measurement never auto-promotes thresholds.

## Packaged fixture truth

- catalog: 17 skins; research blockers: 2
- local realtime asset matches / Web3D ready / Unreal validated: 0 / 0 / 0
- capture channels: 0/44 reference + 0/44 candidate
- preflight: BLOCKED / 88 blockers
- capture queue: 10 pending / 0 ready
- fidelity run: BLOCKED / 88 missing inputs
- scorecard observed metrics: 0; aggregate score: null
- calibration evidence: 0; calibration queue: 88 NEEDS_MEASUREMENT
- accepted cohorts: 0
- threshold decision packets: 88 NO_ACCEPTED_EVIDENCE
- numeric threshold suggestions: 0
- reviewed threshold patches bundled: 0
- governance reviewed/invalid/stale: 0/0/0
- application preview: `NO_REVIEWED_PATCH`, 0 operations, applicationAllowed=false
- active threshold applications: 0; backups bundled: 0
- calibrated replay: `NO_APPLIED_THRESHOLD_VERSION`, replayAllowed=false, promotionAllowed=false
- canonical Reaver root/action thresholds: `{}` / none
- active jobs: 0

## Verification

- **89 pytest tests passed** (`tests` + `tools/asset-indexer/tests`)
- Phase 04, 05, 06, 07, Phase 08 and Pass-02/03/04/05/06 audits: PASS
- Python compileall: PASS
- catalog/data/bridge/research/browser-lab/control JS syntax: PASS
- localhost threshold-governance job/API: PASS
- localhost threshold-application-plan preview job/API: PASS
- localhost calibrated-replay-plan job/API: PASS
- POST `/api/control/threshold-apply`: **404 as required**
- valid reviewed patch → preview → wrong-token rejection → backup → apply → replay blocked/ready/measured → duplicate-use rejection → byte-exact rollback: PASS
- stale spec / unaccepted evidence / missing cohort provenance / invalid rule rejection: PASS

## Exact next direction — Phase 08 Pass 07

The active chat must produce the full Pass-07 prompt before implementation. Intended scope: explicit replay-bound threshold **promotion governance**, immutable threshold-policy version registry/retirement history, and a reproducible target-PC calibration/replay/certification handoff for the 10-action Reaver vertical slice. A machine-readable vertical-slice certification gate must remain BLOCKED in this no-assets/no-captures fixture. Broader premium-skin scaling remains blocked until Reaver has real local asset/runtime/fidelity evidence.

## Durable checkpoint

Authoritative complete filesystem checkpoint:

- `ValoVault_PHASE_08_PASS_06_COMPLETE.zip`
- SHA-256: `cad9769249e4131cfd4ebe13bb371f0aa9e2db76f58a3cc3cbda720579532518`
- ZIP files: 509
- checkpoint manifest entries: 508
- package manifest entries: 507
- CRC + manifest hashes: PASS
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_06_COMPLETE.zip`

Repository: `CyborPunk-2077/ValoVault`.

**Remote warning:** GitHub `main` is still not proven to be a complete path/hash mirror of the full recovered filesystem. GitHub remains the durable history/handoff layer, while the verified complete ZIP is the authoritative disaster-recovery filesystem checkpoint until a full direct-tree audit proves otherwise.
