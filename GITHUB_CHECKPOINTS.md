# ValoVault GitHub Checkpoints

GitHub is the durable continuation index for ValoVault. Always read root `CURRENT_STATE.md` first.

## Phase 08 Pass 01

- Active-source checkpoint: `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`
- SHA-256: `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`
- Verification: 61 tests; Phase 04/05/06/07/08 audits passed.

## Phase 08 Pass 02 — 2026-08-18

- Exact source delta: `checkpoints/phase-08-pass-02/ValoVault_PHASE_08_PASS_02.patch.xz.b64`
- Complete ZIP: `ValoVault_PHASE_08_PASS_02_COMPLETE.zip`
- ZIP SHA-256: `8f3b794ea63904bbc4302d8cb322bb6455dd4c935f0553f18ebdc228c6e42f72`
- Verification: 65 tests; Pass-02 audit; Python/JS; capture-index/preflight localhost jobs/API.

## Phase 08 Pass 03 — 2026-08-18

- Exact source delta from Pass 02: `checkpoints/phase-08-pass-03/ValoVault_PHASE_08_PASS_03.patch.xz.b64`
- Complete ZIP: `ValoVault_PHASE_08_PASS_03_COMPLETE.zip`
- ZIP SHA-256: `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`
- Verification: 69 tests; Pass-03 audit; durable capture-queue/fidelity-prepare smoke.
- Fixture truth: 10 pending actions, all `NEED_BOTH`; derived working set BLOCKED with 0 copied files.

## Phase 08 Pass 04 — 2026-08-18

- Exact source delta from Pass 03: `checkpoints/phase-08-pass-04/ValoVault_PHASE_08_PASS_04.patch.xz.b64`
- Patch XZ SHA-256: `39b37109af94e1b9da6d4cc8c9965359f2edd4f0f51e2df2e06a4eb46dc3b858`
- Base64 artifact SHA-256: `ee55353bf733d58c5af7cfd0f6dea1e1d6f69642992212a7dbf4ced36864b271`
- Complete filesystem checkpoint: `ValoVault_PHASE_08_PASS_04_COMPLETE.zip`
- Complete ZIP SHA-256: `7390f9c42d0cca55cf1066f480b4f4090c51f825af6095c0c745215133476e85`
- ZIP files: 482; checkpoint manifest entries: 481; CRC + every manifest hash: PASS.
- Verification: **75 tests passed**; Phase 04/05/06/07/08/08-pass02/08-pass03/08-pass04 audits passed; Python/JS syntax passed; localhost durable scorecard/evidence/calibration jobs/API passed.
- Fixture truth: 44 scorecard channel slots, 0 observed metrics, aggregate score null, 0 evidence entries, 88 pending calibration items, 0 thresholds, 0 automatic threshold proposals.
- Pass-04 recovery patch was test-applied to a fresh Pass-03 tree and produced a path/hash-identical 482-file tree.
- Next objective: Phase 08 Pass 05 — evidence cohorts/distribution summaries + explicit human threshold-decision packets; never auto-apply thresholds.

### Recover current Pass 04 from GitHub

1. Extract the Pass-01 active-source checkpoint.
2. Base64-decode and XZ-decompress Pass 02, then `git apply` it from the project root.
3. Apply Pass 03 the same way.
4. Apply Pass 04 the same way.
5. Read root `CURRENT_STATE.md`.
6. Run the recorded verification gate before editing.

## Remote direct-source mirror warning

The current `main` direct file tree is **not yet a proven complete browsable mirror of the recovered source tree**. The checkpoint artifacts above are the deterministic GitHub recovery path until a complete path/hash audit proves otherwise. Do not silently treat the root handoff/prototype tree as the entire project.
