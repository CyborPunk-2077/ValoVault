# ValoVault — Current State

**Checkpoint status:** Phase 08 in progress — pass 01 fidelity workflow complete and checkpointed  
**Checkpoint date:** 2026-08-17  
**Canonical project root:** this repository (`skin-vault-lab/`)  
**Next implementation objective:** Phase 08 pass 02 — capture-session indexing + normalization/alignment preflight, preserving target-PC reality gates

## 1. Continuation rule

ValoVault is an existing mid-development project. Continue from this tree. Do **not** restart it, replay completed phases, or replace established architecture merely because an older snapshot exists.

The newest verified implementation in this tree is the source of truth. Historical ZIPs and the prior-chat transcript are retained only for recovery/audit under `docs/recovery/source-snapshots/`.

Before every new major phase or after 1–2 substantial implementation passes:

1. inspect the actual current files;
2. run relevant tests/audits;
3. fix regressions rather than restarting work;
4. update this file;
5. create and verify a complete recoverable project ZIP;
6. commit/push a stable milestone if Git/GitHub is configured;
7. only then begin another major phase.

If a command hangs, inspect what actually completed, terminate only that command, verify partial writes, repair if necessary, and resume with shorter commands. Never restart a whole phase solely because one command hung.

## 2. Current milestone

**Phase 07 is COMPLETE and verified. Phase 08 is IN PROGRESS; pass 01 is complete and verified.**

Phase 08 pass 01 builds directly on the Phase-07 durable control plane and existing fidelity comparators. It does not replace Phase 01–07 systems. It adds the deterministic fidelity-run orchestration layer required before real target-PC calibration work.

Current deterministic packaged fixture state:

- catalog skins: **17**;
- technically classified: **15**;
- deliberately research-blocked: **2**;
- locally matched realtime asset manifests: **0**;
- browser/Web 3D models verified ready: **0**;
- Unreal validated runtime bindings: **0**;
- active durable jobs at checkpoint: **0**;
- latest fidelity verdict: **BLOCKED**;
- default Reaver fidelity actions: **10**;
- explicit missing reference/candidate inputs: **88**.

Zero realtime readiness is expected in this environment because the actual local exported VALORANT assets, Blender target configuration, and compiled UE Weapon Lab are not present. Do not turn planned/classified state into `READY` to make dashboards look complete.

## 3. Canonical architecture — preserve this

1. **Catalog UI — `apps/catalog/`**
   - searchable local-first VALORANT weapon/skin/chroma/level/media catalog;
   - true GLB/glTF viewer path when a validated local realtime model exists;
   - explicit fallback to official preview media when realtime clips/assets are absent;
   - developer intelligence link/mode;
   - browser/UE Weapon Lab launch flow.

2. **Browser Weapon Lab — `apps/lab/`**
   - restored from the completed Backend Build v2 path;
   - browser realtime integration target and fallback lab;
   - not the final high-fidelity renderer.

3. **UE5 Weapon Lab — `unreal/WeaponLab/`**
   - high-fidelity first-person target;
   - universal runtime scaffold from Phase 04 + representative-family systems from Phase 05;
   - actual UHT/UBT compile and real content binding remain target-PC dependent.

4. **Unified local backend — `tools/backend/server.py`**
   - single localhost product/backend entry point;
   - serves catalog, browser lab and control plane;
   - owns local configuration, selection, asset scans/conversion orchestration, catalog sync, control-plane APIs and eventual Weapon Lab launch integration.

5. **Asset extraction/import pipeline**
   - `tools/pipeline/`: FModel / ValorantPorting / Blender export synchronization and conversion flow;
   - `tools/asset-indexer/`: discovers/matches local exports to catalog skin UUIDs and records provenance/readiness evidence;
   - `tools/importer/`: import/content planning;
   - local asset provenance must remain separate from public catalog metadata and from fidelity claims.

6. **Catalog intelligence — `tools/catalog/` + `tools/classifier/`**
   - patch-aware catalog snapshots;
   - classification vs presentation fingerprints;
   - conservative family/archetype/capability routing;
   - theme/family propagation with conflict guardrails;
   - knowledge graph;
   - technical-signature clusters;
   - research campaigns/packs/query worklists;
   - safe reviewed research overrides + persistent ledger;
   - browser → local `/api/catalog-sync` materialization path.

7. **Manifest/onboarding/runtime planning**
   - `tools/manifest/` + `data/onboarding/`;
   - Manifest V2 skeletons;
   - provenance/evidence;
   - centralized readiness evaluation;
   - generic import plans;
   - deterministic Unreal content plans;
   - planned runtime registry entries;
   - `PLANNED_NOT_VALIDATED` is **not** runtime readiness.

8. **Skin recipe/capability layer — `data/skin-recipes/` + `tools/recipes/`**
   - reusable technical-family behavior recipes;
   - representative hard-family coverage from Phase 05;
   - do not implement every premium skin from scratch if an existing capability can be generalized.

9. **Control plane — `apps/control/` + `tools/control_plane/`**
   - durable jobs persisted at `data/control-plane/jobs.json`;
   - interrupted-job recovery/retry;
   - catalog refresh, asset rescan, Blender conversion, cache index and readiness reconcile operations;
   - truthful blockers/status;
   - observed readiness only from actual files/validated registry state.

10. **Fidelity laboratory — `tools/fidelity/` + `reference/` + `data/scenarios/`**
    - existing frame, event, anchor, audio timing, recoil, weapon-metric and sequence comparison utilities;
    - Reaver Vandal reference action manifests already exist;
    - Phase 08 pass 01 now wraps these tools in a versioned deterministic workflow/job layer; pass 02 should add capture-session indexing and normalization/alignment preflight rather than replace the comparison tools.

## 4. Major decisions that must be preserved

- **Local-first architecture.** Public catalog metadata may be fetched/cached, but realtime proprietary assets are discovered from the user's own local export workflow and are not bundled as if they were ours.
- **No fake readiness.** Classification, technical analogy, planned runtime bindings and preview media do not imply realtime readiness or 1:1 fidelity.
- **No PNG-transform pseudo-3D as the final inspector.** The original prototype is preserved only as history/reference under `prototype/`.
- **UE5 is the high-fidelity target.** Browser/WebGL/WebGPU remains a valuable inspection/POC/fallback surface, not the fidelity authority.
- **Base Vandal → Reaver Vandal sequence remains the core validation strategy.** First make the base Vandal end-to-end functional, then make Reaver Vandal the first premium vertical slice before broad premium scaling.
- **Family/theme research once, propagate carefully.** Shared collection/theme evidence may reduce repeated research, but conflicting sibling evidence must remain explicit and unknown behavior must stay unknown.
- **Architecture before scale.** Hard skin-specific solutions should become reusable capabilities before catalog-wide expansion.
- **Never touch a running VALORANT process, Vanguard, protected memory or multiplayer traffic.** Asset research/import and fidelity work remain offline/local.

## 5. Completed systems / phases

### Recovered foundation / early builds

- Original Build 1 preserved at `prototype/valorant-skin-vault.html` and historical copies under recovery snapshots.
- Incomplete Build 2 preserved as historical evidence rather than treated as canonical architecture.
- Completed Backend Build v2 paths were recovered after an older phase fork had accidentally dropped them, including `apps/lab/`, `tools/backend/`, `tools/pipeline/`, config and unified launchers.

### Phase 02

- Local asset backend / export indexing foundations and manifest/readiness infrastructure retained.

### Phase 03

- Local asset-index/registry pipeline progression retained and regression-tested.

### Phase 04

- Universal UE Weapon Lab runtime scaffold retained.
- Runtime/state/fidelity contracts retained.
- Static Unreal audit currently passes.

### Phase 05

- Representative premium-family recipes/capabilities retained.
- Family stress architecture retained.
- Static representative-family audit currently passes.

### Phase 06

- Canonical catalog-scale onboarding/classification branch retained.
- Later useful Phase-06 divergent-branch capabilities were selectively recovered without replacing the stronger canonical branch.
- Patch-aware catalog normalization, knowledge graph, research campaigns, developer intelligence console, family profiles/member deltas, family consistency, technical analog advisories and live browser→local sync are present.
- Deterministic generated fixture currently contains 17 skins / 13 families; 2 remain deliberately research-blocked.

### Phase 07

- Durable local control-plane jobs;
- restart/interruption recovery;
- truthful readiness reconciler;
- non-destructive browser cache audit;
- workflow/blocker status aggregation;
- unified backend control APIs;
- `apps/control/` operational dashboard.

### Phase 08 — pass 01 complete

- versioned fidelity-run JSON Schema;
- canonical Reaver Vandal 10-action fidelity run spec;
- deterministic orchestration around the existing frame/event/audio/anchor/recoil/weapon-metric tools;
- SHA-256 provenance for resolved run inputs;
- explicit `BLOCKED` result for missing captures;
- optional thresholds with no invented default calibration limits;
- machine-readable `run.json` + human `summary.html`;
- durable backend `fidelity-run` job;
- `/api/control/fidelity/latest`;
- control-plane fidelity stage/metric/action;
- Phase-08 tests and audit.

## 6. Current working functionality

Environment-independent and currently verified:

- deterministic catalog snapshot/regeneration;
- patch diff = no changes on repeat fixture run;
- catalog health audit;
- conservative classification/onboarding;
- family profiles, consistency, technical analogs and research campaigns;
- knowledge graph generation;
- planned Unreal registry generation with no false readiness;
- local readiness/cache/status reconciliation;
- durable control-plane job storage/retry semantics;
- unified localhost backend health/status API;
- catalog/browser-lab/control-plane JavaScript syntax;
- Python package compilation;
- Phase 04/05/06/07/08 static audits;
- versioned Reaver fidelity run orchestration;
- truthful missing-input/provenance reporting;
- durable HTTP fidelity job + latest-result endpoint.

## 7. Partial / environment-dependent functionality

These systems exist but cannot be truthfully called complete until run on the target machine with the relevant dependencies/content:

- live full-current public catalog refresh and upstream-source reconciliation;
- real FModel / ValorantPorting / Blender export root scan;
- actual source-model → GLB conversion using installed Blender;
- real per-skin mesh/material/skeleton/animation/audio/VFX discovery;
- browser inspector readiness using those local assets;
- actual UE DataAsset/content generation against a real UE project install;
- UE UHT/UBT compile and runtime launch;
- real first-person model binding and animation/event validation;
- Reaver Vandal realtime vertical slice;
- real current-game reference capture and perceptual calibration;
- Phase-08 capture-session indexing and normalization/alignment preflight;
- defensible metric thresholds derived from real calibration evidence.

## 8. Deferred functionality

- exact/current first-person screen-space calibration;
- current recoil/camera calibration;
- animated shader/material reconstruction against real content;
- Niagara/VFX and audio parity against real content;
- kill feedback/finishers after the core Reaver vertical slice;
- catalog-wide premium-skin fidelity scaling after Base Vandal + Reaver prove the pipeline;
- any public/distribution packaging decision involving locally extracted proprietary assets;
- Phase-08 PASS/FAIL fidelity claims until real inputs and defensible thresholds exist.

## 9. Verification status at this checkpoint

Fresh verification on 2026-08-17:

- deterministic Phase-06 fixture regeneration: **PASS**;
- catalog repeat delta: **0 added / 0 removed / 0 changed**;
- catalog health: **0 errors / 0 warnings**;
- classifier audit: **PASS**;
- generated graph: **207 nodes / 382 edges**;
- family profiles: **13**;
- family consistency issues surfaced: **2**;
- research campaigns: **2**;
- `pytest -q tests tools/asset-indexer/tests`: **61 passed**;
- Phase-04 universal UE static audit: **PASS**;
- Phase-05 representative-family audit: **PASS**;
- Phase-06 catalog/onboarding truthfulness audit: **PASS**;
- Phase-07 control-plane audit: **PASS**;
- Phase-08 fidelity workflow audit: **PASS**;
- Python `compileall`: **PASS**;
- Node syntax checks for catalog/data/bridge/research/browser-lab/control-plane: **PASS**;
- unified backend localhost `/api/health`: **PASS**;
- unified backend localhost `/api/control/status`: **PASS**;
- `POST /api/control/fidelity-run`: **PASS**;
- durable fidelity job terminal state: **done**;
- durable fidelity result: **BLOCKED** (expected);
- `GET /api/control/fidelity/latest`: **PASS**;
- default Reaver run: **10 actions / 88 missing inputs / 0 invented thresholds**.

One full `verify_phase7.py` invocation exceeded the shell execution timeout **after** completing fixture regeneration, readiness/cache/status and all 57 tests. Per the project hang-recovery rule, the completed work was inspected and the remaining short audits were run individually; they all passed. The verifier was not blindly restarted.

## 10. Known blockers right now

Current control-plane blockers are truthful and expected:

1. `ExportRoots.NotConfigured` — no local FModel/ValorantPorting/Blender export root configured in this sandbox.
2. `Classification.ResearchQueue` — 2 fixture skin classifications still intentionally require evidence.
3. `Blender.NotConfigured` — no target Blender executable configured.
4. `WeaponLab.NotConfigured` — no compiled UE Weapon Lab executable configured.
5. Real reference captures/local VALORANT-derived assets are absent, so fidelity cannot be claimed.
6. `Fidelity.MissingInputs` — the latest Reaver fidelity run is explicitly blocked by 88 missing local reference/candidate inputs.

## 11. Exact next implementation objective

**Phase 08 pass 02 — add capture-session manifests/indexing and deterministic normalization/alignment preflight around the pass-01 orchestrator.**

Do not rewrite the comparators or invent fidelity thresholds. The next safe unit should:

1. define a versioned capture-session manifest for reference and candidate recordings;
2. index capture sessions by skin/action/FPS/resolution/source/provenance;
3. validate that reference and candidate sessions are comparable before running metrics;
4. surface FPS/resolution/duration/action mismatches as explicit preflight blockers;
5. add normalization/alignment planning without silently resampling or cropping evidence;
6. integrate capture-session/preflight state with the existing durable `fidelity-run` job and control UI;
7. add tests/audit;
8. update `CURRENT_STATE.md` and checkpoint again before another large pass.

Target-PC work (real captures, UE runtime output, actual calibration thresholds) remains deferred until those inputs exist.

## 12. Exact stopping point of latest development pass

The latest implementation pass stopped **after Phase 08 pass 01 was fully integrated and verified**.

What exists at the stop point:

- `packages/shared-schema/fidelity-run.schema.json`;
- `data/fidelity/reaver-vandal-core-v1.json`;
- `tools/fidelity/orchestrate_run.py`;
- durable backend/control-plane `fidelity-run` integration;
- canonical latest default run at `data/control-plane/fidelity-latest.json`;
- latest verdict `BLOCKED` with 88 explicit missing capture inputs;
- 61 tests + Phase 4/5/6/7/8 audits passing;
- finished job history cleaned before checkpoint.

The next coding agent should begin with **capture-session/preflight infrastructure**, not redo the orchestrator, Phase 07, classification, or earlier runtime work.

## 13. Recovery assets

Historical source snapshots, original prototypes, the master build prompt and prior-chat transcript are preserved under:

`docs/recovery/source-snapshots/`

They are recovery evidence, not authority over this newer verified tree. If a historical snapshot conflicts with this tree, preserve the newer verified implementation unless concrete file/test evidence proves a regression.

## 14. Git / remote status

Durable GitHub remote is configured and writable through the connected GitHub integration:

- repository: `CyborPunk-2077/ValoVault`;
- canonical latest branch: `main`;
- milestone branch convention: `milestone/phase-XX[-pass-YY]`;
- first recovered durable milestone: **Phase 08 Pass 01**;
- durable source checkpoint: `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`;
- source checkpoint SHA-256: `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`.

The repository previously contained only the two original prototype HTML files from the historical initial commit. Because the current connected environment does not expose an authenticated local `gh` CLI for a normal bulk Git push, the first recovered milestone is stored on GitHub as: **root handoff/state documents + a verified compressed active-source checkpoint**. The archive contains every Git-trackable active project file; redundant historical nested ZIPs and ignored local/runtime/cache output remain in the separately verified full checkpoint ZIP.

A fresh coding agent can continue entirely from GitHub by reading this file, fetching the latest archive under `checkpoints/`, verifying its SHA-256, extracting it, and continuing at the exact stopping point above. When a normal authenticated Git push path is available, mirroring the extracted active source tree directly into GitHub is desirable but must not block checkpointing.

After every major phase or 1–2 substantial implementation passes: verify the tree, update this file, create the complete ZIP, publish a new verified GitHub source checkpoint and state docs to `main`, and pin the same commit with a milestone branch.
