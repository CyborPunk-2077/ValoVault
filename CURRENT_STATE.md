# ValoVault — CURRENT STATE

**Canonical development checkpoint:** Phase 08 in progress — **Pass 02 complete and verified**  
**Checkpoint date:** 2026-08-18  
**Next objective:** Phase 08 Pass 03 — deterministic derived-working-copy normalization/alignment execution + capture/scenario queue orchestration.

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

Added:

- `packages/shared-schema/capture-session.schema.json`;
- `packages/shared-schema/fidelity-preflight.schema.json`;
- `tools/fidelity/capture_sessions.py`;
- `tools/fidelity/preflight.py`;
- canonical `data/control-plane/capture-index.json`;
- per-role generated capture-session manifests under `data/control-plane/capture-sessions/`;
- canonical `data/control-plane/fidelity-preflight.json`;
- durable jobs `capture-index` and `fidelity-preflight`;
- GET `/api/control/captures` and `/api/control/fidelity/preflight`;
- POST `/api/control/capture-index` and `/api/control/fidelity-preflight`;
- control-plane capture/preflight stages and blockers;
- non-destructive normalization/alignment planning only — original capture evidence is never mutated.

Packaged fixture truth remains intentionally blocked because no real local captures are bundled:

- reference observed channels: **0 / 44**;
- candidate observed channels: **0 / 44**;
- preflight verdict: **BLOCKED**;
- preflight blockers: **88**;
- destructive operations: **0**;
- fidelity run: **BLOCKED by 88 missing inputs**.

## Verification — 2026-08-18

- `pytest -q tests tools/asset-indexer/tests`: **65 passed**;
- Phase 04 universal UE static audit: **PASS**;
- Phase 05 representative-family audit: **PASS**;
- Phase 06 catalog/onboarding audit: **PASS**;
- Phase 07 control-plane audit: **PASS**;
- Phase 08 fidelity workflow audit: **PASS**;
- Phase 08 Pass-02 capture/preflight audit: **PASS**;
- Python compileall: **PASS**;
- catalog/data/bridge/research/browser-lab/control JS syntax: **PASS**;
- localhost `/api/health`: **PASS**;
- live durable capture-index POST/GET: **PASS**;
- live durable fidelity-preflight POST/GET: **PASS**.

## Current blockers / target-PC gates

- `ExportRoots.NotConfigured` — no real FModel/ValorantPorting/Blender export roots here.
- `Classification.ResearchQueue` — 2 fixture classifications still require evidence.
- `Blender.NotConfigured`.
- `WeaponLab.NotConfigured` — no compiled UE Weapon Lab executable here.
- `Fidelity.CapturesMissing` — 44 reference + 44 candidate channels absent in this environment.
- `Fidelity.PreflightBlocked` — 88 absent/invalid capture inputs.
- `Fidelity.MissingInputs` — latest canonical run remains blocked by the same 88 missing inputs.
- Real UE UHT/UBT compile/runtime validation, real current-game reference capture and defensible thresholds remain target-PC work.

## Exact next objective — Phase 08 Pass 03

1. Execute Pass-02 normalization plans **only into derived working-copy directories**.
2. Preserve SHA-256 provenance from every derived output back to its original capture.
3. Produce deterministic frame/audio/timeline alignment outputs suitable for the existing comparators.
4. Add capture/scenario queue manifests so target-PC work can be resumed/retried per action.
5. Surface queue/preparation state through the durable control plane.
6. Never synthesize missing capture evidence and do not invent thresholds.
7. Test/audit/checkpoint again before scorecard/calibration work.

## Durable recovery / GitHub status

Repository: `CyborPunk-2077/ValoVault`.

Important correction: the current GitHub `main` direct file tree is **not yet a complete browsable mirror of the recovered source tree**. It contains handoff/checkpoint artifacts and the historical prototypes. Do not claim otherwise until a path/hash audit proves a complete direct-source mirror.

A deterministic GitHub recovery path is nevertheless preserved:

1. recover the Phase-08 Pass-01 active-source checkpoint from `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`;
2. decode `checkpoints/phase-08-pass-02/ValoVault_PHASE_08_PASS_02.patch.xz.b64` with Base64;
3. decompress XZ and apply the resulting Pass-02 patch to the Pass-01 tree;
4. use this `CURRENT_STATE.md` as the exact continuation handoff;
5. run the verification gate above before major edits.

The authoritative complete filesystem backup for this checkpoint is `ValoVault_PHASE_08_PASS_02_COMPLETE.zip`, SHA-256 `8f3b794ea63904bbc4302d8cb322bb6455dd4c935f0553f18ebdc228c6e42f72`.