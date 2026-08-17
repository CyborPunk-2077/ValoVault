# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 04 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next objective:** Phase 08 Pass 05 — calibration cohorts/distribution summaries + explicit human threshold-decision packets, with no automatic threshold application.

## Continuation rule

ValoVault is mid-development. Do **not** restart it, replay completed phases, or redesign established architecture because older snapshots exist. Continue from the newest verified checkpoint. Classification, planned runtime bindings, preview media and research do **not** imply realtime readiness or fidelity.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/GitHub checkpoint → continue**.

## Preserved architecture / truth boundaries

- local-first catalog + asset pipeline;
- `apps/catalog/`, browser `apps/lab/`, and operational `apps/control/`;
- unified local backend `tools/backend/server.py`;
- FModel / ValorantPorting / Blender local extraction/conversion pipeline;
- conservative classification/onboarding and research intelligence;
- UE5 `unreal/WeaponLab/` as high-fidelity authority;
- Base Vandal → Reaver Vandal as the first premium vertical slice;
- proprietary realtime assets remain local and are never bundled/claimed READY merely from metadata;
- fidelity evidence is immutable source material; derived working copies retain SHA-256 provenance;
- offline/local work only; never interact with a running VALORANT process, Vanguard, protected memory, or multiplayer traffic.

## Phase 08 Passes 01–03 — complete

Pass 01 added versioned deterministic fidelity-run orchestration around the existing frame/event/audio/anchor/recoil/weapon-metric comparators, explicit missing-input blocking, SHA-256 provenance, durable `fidelity-run` jobs, and no default thresholds.

Pass 02 added observed reference/candidate capture manifests/indexing and non-destructive normalization/alignment preflight. The packaged fixture has 0/44 reference and 0/44 candidate channels and preflight is truthfully BLOCKED by 88 missing inputs.

Pass 03 added resumable per-action capture/scenario queues and immutable-provenance derived working-set preparation. The fixture has 10 pending actions, all `NEED_BOTH`, and the working set is BLOCKED with 0 copied files.

## Phase 08 Pass 04 — complete

Added:

- `packages/shared-schema/fidelity-scorecards.schema.json`;
- `packages/shared-schema/calibration-evidence-ledger.schema.json`;
- `packages/shared-schema/calibration-queue.schema.json`;
- `tools/fidelity/metric_contracts.py` — comparator metric semantics only; **not thresholds**;
- `tools/fidelity/build_scorecards.py` — per-action/per-channel raw scorecards;
- `tools/fidelity/calibration_ledger.py` — deterministic/deduplicated measurement evidence + explicit review state;
- `tools/fidelity/calibration_queue.py` — metric-level states `NEEDS_MEASUREMENT`, `NEEDS_REVIEW`, `READY_FOR_HUMAN_DECISION`, `THRESHOLD_DEFINED`;
- canonical `data/control-plane/fidelity-scorecards.json`;
- canonical `data/calibration/evidence-ledger.json`;
- canonical `data/control-plane/calibration-queue.json`;
- durable jobs/APIs `fidelity-scorecards`, `calibration-evidence`, `calibration-queue`;
- control-plane scorecard/evidence/calibration stages and blockers;
- latent Pass-02/03 backend error-path bug fixed: undefined `_fail_job` calls now use durable `_finish_job(..., error=...)`.

### Pass-04 truth state

The no-capture fixture remains deliberately uncalibrated:

- scorecard actions: **10**;
- scorecard channel slots: **44**;
- measured channels: **0**;
- observed calibration metrics: **0**;
- aggregate score: **null**;
- evidence ledger entries: **0**;
- calibration metric items: **88**;
- pending calibration items: **88**, all `NEEDS_MEASUREMENT`;
- thresholds defined: **0**;
- automatic thresholds/proposals created: **0**;
- canonical Reaver spec still has `thresholds: {}`;
- fidelity run remains **BLOCKED** by 88 missing local reference/candidate inputs.

Scorecards expose raw measurements only. Metric direction/unit semantics are not acceptance thresholds. Evidence collection never creates thresholds. The calibration queue may eventually mark reviewed evidence `READY_FOR_HUMAN_DECISION`, but it never derives or writes a threshold automatically.

## Verification — 2026-08-18

- `pytest -q tests tools/asset-indexer/tests`: **75 passed**;
- Phase 04 universal UE static audit: **PASS**;
- Phase 05 representative-family audit: **PASS**;
- Phase 06 catalog/onboarding audit: **PASS**;
- Phase 07 control-plane audit: **PASS**;
- Phase 08 fidelity workflow audit: **PASS**;
- Phase 08 Pass-02 capture/preflight audit: **PASS**;
- Phase 08 Pass-03 working-set/queue audit: **PASS**;
- Phase 08 Pass-04 scorecard/calibration audit: **PASS**;
- Python compileall: **PASS**;
- catalog/data/bridge/research/browser-lab/control JS syntax: **PASS**;
- localhost `/api/health`: **PASS**;
- live durable `fidelity-scorecards` POST/job/GET: **PASS**;
- live durable `calibration-evidence` POST/job/GET: **PASS**;
- live durable `calibration-queue` POST/job/GET: **PASS**;
- finished job history cleared; active jobs: **0**.

## Current blockers / target-PC gates

- `ExportRoots.NotConfigured`;
- `Classification.ResearchQueue` — 2 fixture classifications still need evidence;
- `Blender.NotConfigured`;
- `WeaponLab.NotConfigured`;
- `Fidelity.CapturesMissing` — all 44 reference + 44 candidate channel inputs absent here;
- `Fidelity.PreflightBlocked` — 88 capture/input blockers;
- `Fidelity.CaptureQueuePending` — 10 canonical actions need both sides;
- `Fidelity.WorkingSetBlocked`;
- `Fidelity.ScorecardsUnmeasured` — no comparator metrics exist, so no score may be synthesized;
- `Fidelity.CalibrationQueuePending` — 88 metric-level calibration decisions await real evidence;
- `Fidelity.MissingInputs` — latest run blocked by the same 88 missing inputs.

Real UE UHT/UBT/runtime validation, real current-game reference capture, and defensible threshold selection remain target-PC work.

## Exact next objective — Phase 08 Pass 05

1. Group **accepted** evidence into provenance-locked cohorts by action/channel/metric and comparable capture conditions.
2. Compute descriptive distributions only when real reviewed evidence exists.
3. Keep sample statistics separate from fidelity acceptance thresholds.
4. Generate human-review threshold-decision packets that cite exact evidence IDs/cohorts/distributions.
5. Require an explicit reviewed decision before producing any threshold patch artifact.
6. Never apply a threshold patch automatically to the canonical Reaver spec.
7. Surface cohort/decision readiness through the durable control plane.
8. Keep the no-capture fixture at zero evidence and zero threshold proposals.
9. Test/audit/checkpoint before broader premium-skin fidelity scaling.

## Durable recovery / GitHub status

Repository: `CyborPunk-2077/ValoVault`.

**Important:** the current GitHub `main` direct file tree is still **not yet proven to be a complete browsable mirror** of the recovered source tree. Do not claim otherwise until a path/hash audit proves it.

Deterministic GitHub recovery path:

1. extract `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`;
2. Base64-decode + XZ-decompress + `git apply` the Pass-02 patch;
3. apply the Pass-03 patch the same way;
4. apply `checkpoints/phase-08-pass-04/ValoVault_PHASE_08_PASS_04.patch.xz.b64` the same way;
5. read this `CURRENT_STATE.md`;
6. run the verification gate before major editing.

The Pass-04 patch was independently test-applied to a fresh Pass-03 tree and produced a **path/hash-identical 482-file Pass-04 tree**.

Authoritative complete filesystem backup: `ValoVault_PHASE_08_PASS_04_COMPLETE.zip`  
SHA-256: `7390f9c42d0cca55cf1066f480b4f4090c51f825af6095c0c745215133476e85`  
ZIP files: **482**; manifest entries: **481**; CRC/hash verification: **PASS**.
