# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 08 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next chat-authored objective:** Phase 08 Pass 09 — portable target-PC execution bundle + environment doctor + safe return-package assembly, still Reaver-only.

## Strict authority split

- **This ValoVault chat is the authoritative planning/continuation brain.** It decides product direction, improvements, phase sequencing and the exact next implementation/master prompt.
- **GitHub is the durable execution/history/checkpoint layer.**
- `CURRENT_STATE.md` is a concise recovery handoff, not the whole strategy context.
- Before every substantial pass, formulate the canonical next prompt in chat first.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/Git checkpoint → continue**.

Truth boundary: **classification ≠ assets ≠ runtime readiness ≠ fidelity ≠ calibrated replay ≠ promoted policy ≠ vertical-slice certification**.

## Architecture/product invariants

Local-first catalog; local FModel/ValorantPorting/Blender asset flow; browser Weapon Lab fallback; UE5 Weapon Lab as fidelity authority; Base Vandal → Reaver Vandal first premium slice; immutable source evidence/derived SHA provenance; no fake READY; no interaction with running VALORANT/Vanguard/protected memory/multiplayer traffic; broader premium scaling remains blocked until the Reaver slice has real evidence.

## Phase 08 Passes 01–07 — complete

Preserved: deterministic fidelity run; observed capture sessions/index/preflight; resumable 10-action queue + derived working set; raw scorecards/evidence/calibration queue; accepted-evidence cohorts + human threshold decision packets; reviewed threshold governance; explicit reversible threshold application; calibrated replay; PASS-only threshold-policy promotion; deterministic Reaver target-PC certification handoff; vertical-slice certification gate. Canonical packaged Reaver thresholds remain `{}`.

## Phase 08 Pass 08 — complete

Added portable target-PC return ingestion/reconciliation:

- `packages/shared-schema/target-pc-return-manifest.schema.json`
- `packages/shared-schema/target-pc-root-bindings.schema.json`
- `packages/shared-schema/target-pc-return-reconciliation.schema.json`
- `tools/fidelity/target_pc_return.py`
- `data/control-plane/target-pc-return-manifest.json`
- `data/control-plane/target-pc-return-reconciliation.json`
- local-only `data/runtime/target-pc-return-bindings.json`
- root-override support in capture sessions/queue/preflight/working-set preparation
- durable job/API/UI: `target-pc-return-reconcile`
- GET `/api/control/target-pc-return/manifest`
- GET `/api/control/target-pc-return/reconciliation`
- Pass-08 tests and audit.

### Return truth model

- Return manifest is bound to exact handoff session ID + fidelity-spec SHA-256.
- Paths are explicitly `PROJECT_RELATIVE`, `LOCAL_ROOT_RELATIVE`, or `MACHINE_ABSOLUTE`.
- Machine-root bindings are explicit reviewed CLI records requiring reviewer+rationale. There is no browser/API root-binding approval path.
- Original source paths and SHA-256 values are immutable provenance. Rebinding records resolved local paths separately.
- Windows drive paths, stale `/mnt/data` paths, unbound absolute paths, missing files, hash/size mismatches and action/channel mismatches are explicit blockers.
- Proprietary capture/assets stay in user-controlled local roots and may not be auto-transported as checkpoint metadata.
- Remote `READY`, `PASS`, `CERTIFIED`, `PROMOTED` claims are ignored/rejected as local truth.
- After valid reconciliation, capture index → queue → preflight → working set can be regenerated from **local observation only** using approved root overrides.

## Packaged fixture truth after Pass 08

- catalog skins: 17; classification research blockers: 2
- local realtime asset matches / Web3D / Unreal validated: 0 / 0 / 0
- observed captures: 0/44 reference + 0/44 candidate
- preflight: BLOCKED / 88 blockers
- capture queue: 10 pending / 0 ready
- working set: BLOCKED / 0 copied files
- fidelity run: BLOCKED / 88 missing inputs
- scorecard observed metrics: 0; aggregate score null
- calibration evidence: 0; calibration queue: 88 NEEDS_MEASUREMENT
- accepted cohorts: 0
- reviewed threshold patches / active applications / promoted policies: 0 / 0 / 0
- calibrated replay: NO_APPLIED_THRESHOLD_VERSION
- target-PC handoff: 10/10 actions
- target-PC return manifest: 0 returned artifacts
- target-PC return reconciliation: **BLOCKED / 2 blockers**
- remote truth claims accepted: 0
- vertical-slice certification: BLOCKED / 9 blockers
- canonical Reaver thresholds: `{}`
- active durable jobs: 0

## Verification

- **104 pytest tests passed**
- Phase 04/05/06/07 + Phase 08 + Pass-02/03/04/05/06/07/08 audits: PASS
- Python compileall: PASS
- catalog/data/bridge/research/browser-lab/control JavaScript syntax: PASS
- live `target-pc-return-reconcile` durable job/API: PASS
- return manifest/reconciliation GET APIs: PASS
- `/api/control/target-pc-return-bindings`: 404 as required
- synthetic Windows D:\\ capture roots → reviewed local rebinding → hash validation → locally regenerated capture index/preflight/working set: PASS
- stale `/mnt/data`, wrong session/spec SHA, missing/hash mismatch, action/channel mismatch, proprietary transport leakage and remote truth import attempts: correctly blocked

## Exact next objective — Phase 08 Pass 09

The active chat owns the full prompt. Current intended direction is to operationalize the already-built handoff/return contracts rather than broaden the skin catalog:

1. build a portable target-PC execution bundle containing only code/contracts/config templates required for the Reaver run;
2. add a target-PC environment doctor that validates Python/tooling, writable roots, configured Blender/UE paths and exact handoff/spec identity without touching a running VALORANT/Vanguard process;
3. add a safe return-package assembler that includes only approved non-proprietary metadata/control artifacts + the Pass-08 return manifest;
4. statically scan the return package for prohibited proprietary asset/capture leakage before packaging;
5. produce package SHA/manifests and a receiver verification command that feeds directly into Pass-08 reconciliation;
6. simulate a complete target-PC round trip with synthetic owned evidence;
7. keep the packaged no-assets fixture BLOCKED and Reaver-only;
8. test/audit/checkpoint before any real target-PC execution or broader premium scaling.

## Durable recovery

The authoritative exact filesystem checkpoint is the newest complete verified ZIP recorded in `GITHUB_CHECKPOINTS.md` and persisted under `/ValoVault Checkpoints/` in the user's ChatGPT Library. GitHub is the durable history/handoff layer but its direct `main` tree is still not proven to be a complete path/hash mirror; do not claim otherwise until audited.
