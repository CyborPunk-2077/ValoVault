# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 05 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next objective:** Phase 08 Pass 06 — reviewed threshold-patch validation/application governance + calibrated replay planning, while keeping the packaged no-capture fixture threshold-free.

## Continuation rule

ValoVault is mid-development. Do **not** restart it, replay completed phases, or redesign established architecture because older snapshots exist. Continue from this newest verified checkpoint.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/GitHub checkpoint → continue**.

Truth boundary: **classification ≠ local assets ≠ runtime readiness ≠ fidelity**. Planned bindings, previews, classifications and descriptive calibration statistics do not imply `READY`, fidelity PASS, or a valid acceptance threshold.

## Architecture / product decisions to preserve

- Local-first VALORANT catalog and local asset pipeline.
- `apps/catalog/` catalog, `apps/lab/` browser Weapon Lab/fallback, `apps/control/` operational control plane.
- `tools/backend/server.py` unified localhost backend.
- FModel / ValorantPorting / Blender local export/conversion workflow.
- UE5 `unreal/WeaponLab/` remains the high-fidelity authority.
- Base Vandal → Reaver Vandal remains the first premium vertical slice.
- Proprietary realtime assets remain local; repository state never fabricates asset readiness.
- Fidelity source evidence is immutable; derived working copies retain SHA-256 provenance.
- Never interact with a running VALORANT process, Vanguard, protected memory, or multiplayer traffic.

## Phase 08 passes completed

### Pass 01 — deterministic fidelity run

Versioned Reaver Vandal 10-action orchestration around existing comparators, input SHA provenance, explicit missing-input blocking, durable `fidelity-run`, and default `thresholds: {}`.

### Pass 02 — capture sessions + preflight

Observed reference/candidate capture manifests/index plus non-destructive normalization/alignment preflight. Packaged fixture: **0/44 reference + 0/44 candidate channels**, preflight `BLOCKED` with **88** blockers.

### Pass 03 — resumable capture queue + derived working set

10-action resumable capture/scenario queue and derived-working-copy preparation. Packaged fixture: **10 pending / 0 ready / all NEED_BOTH**, working set `BLOCKED`, **0 copied files**.

### Pass 04 — raw scorecards + evidence ledger + calibration queue

Raw per-action/per-channel metric scorecards, immutable/deduplicated evidence observations with review state, and metric-level calibration queue. No vanity aggregate score or automatic threshold creation.

### Pass 05 — provenance cohorts + human threshold decisions

Added:

- `tools/fidelity/calibration_cohorts.py`;
- `tools/fidelity/threshold_decision_packets.py`;
- `tools/fidelity/create_threshold_patch.py`;
- schemas `calibration-cohorts`, `threshold-decision-packets`, `reviewed-threshold-patch`;
- `data/control-plane/calibration-cohorts.json`;
- `data/control-plane/threshold-decision-packets.json`;
- optional capture-condition propagation from scorecards into the calibration ledger;
- durable jobs `calibration-cohorts` and `threshold-decision-packets`;
- GET `/api/control/calibration/cohorts` and `/api/control/calibration/decisions`;
- POST `/api/control/calibration-cohorts` and `/api/control/threshold-decision-packets`;
- control-plane cohort/threshold-decision stages, summaries and blockers;
- control UI actions `BUILD COHORTS` and `BUILD DECISION PACKETS`.

Cohorts include only **ACCEPTED** evidence and are grouped by action/channel/metric + capture-condition fingerprint. They expose descriptive distributions and a provenance-lock SHA. Descriptive distributions are explicitly **not acceptance thresholds**.

Threshold-decision packets cite cohort/evidence/provenance data but always have `suggestedThreshold: null`. When real reviewed evidence exists they may become `HUMAN_DECISION_REQUIRED`; they do not choose a rule.

`create_threshold_patch.py` requires an explicit reviewer, rationale, finite numeric min/max rule, and matching ACCEPTED evidence IDs. It emits a `REVIEWED_NOT_APPLIED` artifact and **never edits the canonical fidelity spec**.

## Packaged fixture truth after Pass 05

- catalog skins: **17**;
- research-blocked classifications: **2**;
- local matched realtime asset manifests: **0**;
- browser/Web 3D ready: **0**;
- Unreal validated bindings: **0**;
- reference capture channels observed: **0 / 44**;
- candidate capture channels observed: **0 / 44**;
- preflight: **BLOCKED / 88 blockers**;
- capture queue: **10 pending / 0 ready**;
- fidelity run: **BLOCKED / 88 missing inputs**;
- scorecard observed metrics: **0**;
- aggregate score: **null**;
- calibration evidence entries: **0**;
- calibration queue: **88 pending / all NEEDS_MEASUREMENT**;
- accepted-evidence cohorts: **0**;
- threshold-decision packets: **88 / all NO_ACCEPTED_EVIDENCE**;
- numeric threshold suggestions: **0**;
- reviewed threshold patches bundled: **0**;
- explicit/default Reaver thresholds: **0 / `{}`**;
- active durable jobs at checkpoint: **0**.

## Verification — 2026-08-18

- `pytest -q tests tools/asset-indexer/tests`: **84 passed**;
- Phase 04 universal UE static audit: **PASS**;
- Phase 05 representative-family audit: **PASS**;
- Phase 06 catalog/onboarding audit: **PASS**;
- Phase 07 control-plane audit: **PASS**;
- Phase 08 fidelity workflow audit: **PASS**;
- Phase 08 Pass-02 audit: **PASS**;
- Phase 08 Pass-03 audit: **PASS**;
- Phase 08 Pass-04 audit: **PASS**;
- Phase 08 Pass-05 audit: **PASS**;
- Python compileall: **PASS**;
- catalog/data/bridge/research/browser-lab/control JavaScript syntax: **PASS**;
- localhost `calibration-cohorts` durable POST/job/GET: **PASS**;
- localhost `threshold-decision-packets` durable POST/job/GET: **PASS**;
- reviewed threshold-patch test proves canonical spec stays byte-for-byte unchanged: **PASS**.

## Current blockers / target-PC gates

- `ExportRoots.NotConfigured`;
- `Classification.ResearchQueue` — 2 fixture classifications require evidence;
- `Blender.NotConfigured`;
- `WeaponLab.NotConfigured`;
- `Fidelity.CapturesMissing`;
- `Fidelity.PreflightBlocked`;
- `Fidelity.CaptureQueuePending`;
- `Fidelity.WorkingSetBlocked`;
- `Fidelity.ScorecardsUnmeasured`;
- `Fidelity.CalibrationQueuePending`;
- `Fidelity.CalibrationCohortsEmpty`;
- `Fidelity.ThresholdDecisionPending`;
- `Fidelity.MissingInputs`.

Real UE UHT/UBT/runtime validation, current-game reference capture, capture-condition review, and defensible human threshold selection remain target-PC work.

## Exact next objective — Phase 08 Pass 06

1. Add a versioned reviewed-threshold decision/application ledger separate from measurement evidence.
2. Validate `REVIEWED_NOT_APPLIED` patch artifacts against canonical spec SHA, accepted evidence IDs and reviewer provenance.
3. Build an explicit **application preview/plan** that shows exact threshold changes and rollback data without mutating the canonical spec.
4. If an application command is added, require an explicit review/confirmation token and make a backed-up/reversible operation; never auto-apply from cohort statistics or decision packets.
5. Add calibrated replay planning so a reviewed threshold version can be rerun against the same provenance-locked working set before being promoted.
6. Keep the packaged fixture at **zero reviewed patches and `thresholds: {}`**.
7. Surface review/application readiness through the durable control plane.
8. Test/audit/checkpoint again before any broader premium-skin fidelity scaling.

## Durable recovery / GitHub / chat authority

Repository: `CyborPunk-2077/ValoVault`.

**Authority split:** the active ValoVault chat owns roadmap reasoning, improvement choices, phase sequencing and the canonical next implementation prompt. GitHub owns durable code/history/checkpoints. This file is the concise recovery handoff, not the entire product-strategy context.

The GitHub `main` direct file tree is **not yet proven to be a complete browsable mirror** of the recovered source tree. Do not claim otherwise until a complete path/hash audit proves it.

For the exact Pass-05 filesystem state, prefer the complete verified checkpoint persisted in the user's ChatGPT Library:

- Library path: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_05_COMPLETE.zip`
- expected SHA-256 is recorded in `GITHUB_CHECKPOINTS.md`

GitHub remains the durable handoff/history layer and has deterministic recovery through Pass 04. Pass-05 patch transport must not be claimed complete until its GitHub artifact is independently hash-verified. A fresh chat should recover the newest complete checkpoint, read this file + `VALOVAULT_OPERATING_RULE.md`, preserve the established architecture/product intent, formulate the next canonical prompt in chat, then continue.
