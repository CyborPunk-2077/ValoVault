# ValoVault — CURRENT STATE

**Canonical development state:** Phase 08 Pass 10 complete + independent product hardening  
**Checkpoint date:** 2026-08-18  
**Roadmap authority:** the active ValoVault chat. Do **not** invent Pass 11 from this file.

## Continuation contract

ValoVault is one continuous mid-development project. Preserve existing architecture/history and continue from the newest verified checkpoint. Permanent loop:

**inspect → implement → test → fix → verify → update state → complete ZIP → Recovery Vault → GitHub handoff → continue**

Truth boundary remains strict:

**classification ≠ assets ≠ runtime readiness ≠ fidelity ≠ calibrated replay ≠ promoted policy ≠ certification**

GitHub is the durable history/handoff index. The newest complete verified ZIP is the exact filesystem disaster-recovery authority unless an exact later Git tree has been independently path/hash audited.

## Preserved product direction

- local-first VALORANT weapon/skin catalog;
- browser Catalog + Control + Browser Weapon Lab;
- UE5 Weapon Lab remains fidelity authority;
- FModel / ValorantPorting / Blender local export pipeline;
- Base Vandal → Reaver Vandal is the first premium vertical slice;
- no fake READY/PASS/CERTIFIED/PROMOTED state;
- no interaction with running VALORANT/Vanguard/protected memory/multiplayer traffic;
- proprietary captures/assets remain local and are never checkpointed;
- no Prime/Kuronami/etc. fidelity/runtime scaling until Reaver closes truthfully.

## Reaver closure lock

The Phase-08/Pass-10 fidelity architecture is mature enough. Do **not** build another general fidelity/control-plane abstraction before the first real Reaver round trip.

Reaver-specific work is allowed only for:
1. a blocker observed during the eventual real target-PC run;
2. operator-friction reduction;
3. regression/truth-boundary fixes;
4. durability/recovery work.

The user should **not** be asked to perform the real target-PC evidence run yet. Continue independent software/product work first.

## Completed Reaver software path

- deterministic fidelity orchestration;
- capture/index/preflight/working set;
- scorecards/calibration/evidence cohorts;
- human threshold decisions + reversible governance;
- calibrated replay + PASS-only policy promotion;
- target-PC handoff + truthful certification gate;
- portable return reconciliation/root rebinding;
- environment doctor + safe execution/return packages;
- resumable target-PC session + SHA-bound execution receipt;
- single target/receiver operator façade;
- one-command release self-test/checkpoint/recovery tooling.

Scoped Reaver software path: **24/24 implemented**. Packaged real evidence/certification fixture remains **0/11** by design. This is not an overall product percentage.

Current Reaver fixture truth:
- catalog 17 / classified 15 / research blockers 2;
- realtime/Web3D/Unreal validated 0 / 0 / 0;
- captures 0/44 reference + 0/44 candidate;
- fidelity preflight BLOCKED / 88 missing inputs;
- canonical thresholds `{}`;
- certification BLOCKED / 9;
- environment doctor BLOCKED / 3 target-machine inputs;
- target-PC session plan 10 target steps / 2 manual evidence gates / 9 receiver-only steps;
- active durable jobs 0.

## Independent product hardening completed after Pass 10

### Operator/recovery hardening
- `START_HERE.md`, `RUN_REAVER.*`, `VALOVAULT_START.*`;
- target-PC configurator + single Reaver operator façade;
- one-command release verification;
- one-command safe complete checkpoint builder;
- deduplicated Recovery Vault with no-self-nesting, temp-write, CRC verification and atomic promotion;
- `PROJECT_COMPLETION_MATRIX.json` anti-loop lane map.

### Public catalog hardening
- safe public catalog manager: **stage → audit → shrink guard → atomic promote → provenance**;
- backend/control refresh routed through safe promotion;
- source/version/health visibility;
- scalable catalog search/filter/sort/lazy-image UI;
- local app doctor distinguishes required blockers from optional machine capabilities.

### Local-first browser runtime hardening
- removed runtime CDN execution from Browser Lab and Catalog;
- removed Google model-viewer and Google Fonts runtime dependencies;
- Catalog uses ValoVault-owned minimal local GLB/animation viewer;
- official Three.js r180 dependency manifest pins exact upstream Git blob SHA-1 values;
- explicit installer verifies blobs, writes SHA-256 lock, and atomically promotes only verified files;
- missing vendor files gate Browser 3D only; Catalog/Control remain available;
- `audit_web_runtime.py` prevents remote executable/style/import-map regressions.

Current container cannot fetch the pinned third-party files, so no fabricated vendor bytes are claimed installed. A network-enabled setup/build machine may run `python tools/dev/vendor_web_dependencies.py install`.

### Localhost backend security hardening
- unified backend and legacy documented bridge remain bound to loopback;
- non-loopback/DNS-rebinding Host values rejected;
- foreign browser Origin and cross-site requests rejected;
- mutating requests require `application/json`;
- wildcard CORS removed; only validated loopback origin/current port is echoed;
- local CLI use without Origin remains supported;
- basic no-sniff/referrer/CORP response hardening added.

Live smoke verified: local health 200; foreign-origin read 403; foreign cross-site write 403; same-origin non-JSON write 415; same-origin JSON write 202; non-loopback Host 403. Smoke-created finished jobs were cleared before checkpointing.

## Verification

Current verified software baseline:
- **142 pytest tests PASS**;
- **26 one-command release checks PASS**;
- every audit from Phase 04 through Phase 08 Pass 10 PASS;
- Python compileall PASS;
- relevant JavaScript syntax PASS;
- web runtime audit PASS / 0 remote executable-style findings;
- Reaver target kit verification PASS / 83 allowlisted payload files / 0 violations;
- durable jobs 0.

Browser screenshot QA remains environment-gated because the available Chromium binary hangs before producing a frame; no visual PASS is claimed.

## Current durable artifacts

### Exact complete filesystem checkpoint — CURRENT
`ValoVault_PASS10_LOCALHOST_SECURITY_HARDENED_COMPLETE.zip`
- SHA-256: `9d7c0d1fa2669cc5ac6b2aab59554883e1c791de4257770518824db02baa94b1`
- size: 3,147,639 bytes
- 605 files
- CRC + embedded package/checkpoint manifest verification PASS

### Deduplicated Recovery Vault — CURRENT
`ValoVault_RECOVERY_VAULT_ALL_HISTORY.zip`
- SHA-256: `7e61ec98b545ad9e006840e3c9ee4911f2369c9685e56f72deacf9866c7add5e`
- size: 44,984,585 bytes
- 34 candidates → 27 unique artifacts / 7 duplicate copies elided
- CRC PASS

### Reaver target-PC kit
`ValoVault_REAVER_TARGET_PC_EXECUTION_KIT.zip`
- SHA-256: `b7eb9865eb1db8a2eeb1d3033742e8344073903167e372d44de9d67a81c75043`
- 83 allowlisted payload files / 0 violations
- **do not ask the user to run it yet**.

## Next engineering direction

Continue only concrete independent product/usability/data/distribution/security gaps that can be verified without proprietary real evidence. Do not create Pass 11, do not expand premium fidelity scope, and do not treat missing target-machine inputs as software TODOs.

If no material independent gap remains, stop adding architecture and preserve the clean checkpoint until the project is mature enough for the user’s eventual real Reaver run.
