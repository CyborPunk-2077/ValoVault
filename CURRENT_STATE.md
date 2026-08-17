# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 03 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next objective:** Phase 08 Pass 04 — metric scorecards + calibration evidence ledger/queue, with no automatic or invented thresholds.

## Continuation rule

ValoVault is mid-development. Do **not** restart it, replay completed phases, or redesign established architecture merely because older snapshots exist. Continue from the newest verified checkpoint. Classification, planned runtime bindings, preview media and research do **not** imply realtime readiness or fidelity.

Permanent loop: **inspect → implement → test → fix → verify → update CURRENT_STATE.md → complete ZIP/GitHub checkpoint → continue**.

## Canonical architecture

- `apps/catalog/` — local-first searchable VALORANT catalog and realtime model path when a validated local model exists.
- `apps/lab/` — browser Weapon Lab / fallback realtime integration surface.
- `apps/control/` — durable local control-plane UI.
- `tools/backend/server.py` — single localhost backend/static server and durable workflow API.
- `tools/pipeline/` — FModel / ValorantPorting / Blender export/conversion flow.
- `tools/asset-indexer/` — local export discovery, provenance and readiness evidence.
- `tools/catalog/` + `tools/classifier/` — patch-aware catalog normalization, conservative classification/onboarding, family/theme research propagation, knowledge graph and research worklists.
- `tools/manifest/` + `data/onboarding/` — manifests/import plans/planned runtime bindings. Planned is not validated.
- `data/skin-recipes/` + `tools/recipes/` — reusable premium-family technical capability recipes.
- `unreal/WeaponLab/` — UE5 high-fidelity first-person target.
- `tools/fidelity/` + `reference/` + `data/scenarios/` — fidelity lab, comparators, Reaver Vandal reference-action contracts and Phase-08 orchestration.

## Preserved decisions

- Local-first; proprietary realtime assets come from the user's own local export workflow and are not bundled as public assets.
- No fake `READY` state.
- No PNG-transform pseudo-3D as the final inspector.
- UE5 remains the high-fidelity authority; browser lab is inspection/POC/fallback.
- Base Vandal → Reaver Vandal remains the first premium vertical-slice sequence.
- Family/theme evidence may propagate only with conflict guardrails.
- Offline/local asset work only; never interact with running VALORANT, Vanguard, protected memory or multiplayer traffic.
- Fidelity evidence is immutable source material. Derived working copies must retain SHA-256 provenance to originals.

## Completed through Phase 07

Recovered foundation + Backend Build v2, asset indexing/manifests, Windows integration progression, universal UE runtime scaffold, representative premium-family recipes, catalog-scale classification/onboarding/research intelligence, browser→local catalog sync, and the durable Phase-07 control plane are preserved.

## Phase 08 Pass 01 — complete

- versioned fidelity-run schema;
- Reaver Vandal 10-action canonical run spec;
- deterministic orchestration of existing frame/event/audio/anchor/recoil/weapon-metric tools;
- SHA-256 input provenance;
- explicit `BLOCKED` result for missing captures;
- machine-readable `run.json` + `summary.html`;
- durable `fidelity-run` backend job + `/api/control/fidelity/latest`;
- no invented calibration thresholds.

## Phase 08 Pass 02 — complete

- observed reference/candidate capture-session manifests and canonical capture index;
- deterministic, non-destructive normalization/alignment preflight;
- durable `capture-index` and `fidelity-preflight` jobs + control APIs/UI stages;
- original captures are never mutated;
- packaged no-capture fixture: 0/44 reference + 0/44 candidate channels, preflight `BLOCKED` with 88 blockers and zero destructive operations.

## Phase 08 Pass 03 — complete

Added:

- `packages/shared-schema/capture-queue.schema.json`;
- `packages/shared-schema/fidelity-working-set.schema.json`;
- `tools/fidelity/capture_queue.py`;
- `tools/fidelity/prepare_working_copy.py`;
- canonical `data/control-plane/capture-queue.json`;
- canonical `data/control-plane/fidelity-working-set.json`;
- durable jobs `capture-queue` and `fidelity-prepare`;
- GET `/api/control/capture-queue` and `/api/control/fidelity/working-set`;
- POST `/api/control/capture-queue` and `/api/control/fidelity-prepare`;
- capture/scenario queue + derived-working-set control-plane stages/blockers;
- deterministic derived working-copy preparation with source/derived SHA-256 provenance;
- unsupported transforms block rather than silently approximating temporal/FPS/resolution/audio normalization.

Packaged fixture truth:

- reference observed channels: **0 / 44**;
- candidate observed channels: **0 / 44**;
- preflight verdict: **BLOCKED** with **88** blockers;
- capture/scenario queue: **10 actions**, **10 pending**, **0 ready**, all **NEED_BOTH**;
- derived working-set verdict: **BLOCKED**;
- derived copied files: **0**;
- fidelity run remains **BLOCKED** by missing real evidence.

## Verification — 2026-08-18

- `pytest -q tests tools/asset-indexer/tests`: **69 passed**;
- Phase 04 universal UE static audit: **PASS**;
- Phase 05 representative-family audit: **PASS**;
- Phase 06 catalog/onboarding audit: **PASS**;
- Phase 07 control-plane audit: **PASS**;
- Phase 08 fidelity workflow audit: **PASS**;
- Phase 08 Pass-02 capture/preflight audit: **PASS**;
- Phase 08 Pass-03 working-copy/queue audit: **PASS**;
- Python compileall: **PASS**;
- catalog/data/bridge/research/browser-lab/control JS syntax: **PASS**;
- localhost `/api/health`: **PASS**;
- live durable capture-queue POST/GET: **PASS**;
- live durable fidelity-prepare POST/GET: **PASS**.

## Current blockers / target-PC gates

- `ExportRoots.NotConfigured` — no real FModel/ValorantPorting/Blender export roots here.
- `Classification.ResearchQueue` — 2 fixture classifications still require evidence.
- `Blender.NotConfigured`.
- `WeaponLab.NotConfigured` — no compiled UE Weapon Lab executable here.
- `Fidelity.CapturesMissing` — 44 reference + 44 candidate channels absent in this environment.
- `Fidelity.PreflightBlocked` — 88 absent/invalid capture inputs.
- `Fidelity.CaptureQueuePending` — 10/10 canonical actions still need reference and candidate capture evidence.
- `Fidelity.WorkingSetBlocked` — preflight is not ready, so no derived working files are produced.
- Real UE UHT/UBT compile/runtime validation, real current-game reference capture and defensible thresholds remain target-PC work.

## Exact next objective — Phase 08 Pass 04

1. Build deterministic per-action/per-metric scorecard structures around existing comparator outputs.
2. Add a persistent calibration-evidence ledger recording observed samples, environment/provenance and reviewer decisions.
3. Add a calibration queue that clearly separates insufficient evidence from reviewable evidence.
4. Never infer or invent acceptance thresholds from absent data; thresholds remain unset until defensible real calibration evidence exists.
5. Surface scorecard/calibration state through the durable control plane.
6. Keep Base Vandal → Reaver Vandal as the first end-to-end calibration target.
7. Test/audit/checkpoint before broader fidelity scaling.

## Durable recovery / GitHub status

Repository: `CyborPunk-2077/ValoVault`.

Important correction: the current GitHub `main` direct file tree is **not yet a complete browsable mirror of the recovered source tree**. Do not claim otherwise until a path/hash audit proves a complete direct-source mirror.

Deterministic GitHub recovery path:

1. recover the Phase-08 Pass-01 active-source checkpoint from `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`;
2. Base64-decode + XZ-decompress + apply `checkpoints/phase-08-pass-02/ValoVault_PHASE_08_PASS_02.patch.xz.b64`;
3. Base64-decode + XZ-decompress + apply `checkpoints/phase-08-pass-03/ValoVault_PHASE_08_PASS_03.patch.xz.b64`;
4. read this `CURRENT_STATE.md`;
5. run the verification gate above before editing.

The authoritative complete filesystem backup for this checkpoint is `ValoVault_PHASE_08_PASS_03_COMPLETE.zip`, SHA-256 `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`.