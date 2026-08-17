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
- Files: 458; CRC PASS.
- Verification: 65 tests; Phase 04/05/06/07/08/08-pass02 audits; Python/JS syntax; localhost capture-index + preflight jobs/API.
- Fixture truth: 0/44 reference + 0/44 candidate observed; preflight BLOCKED with 88 blockers and zero destructive operations.

## Phase 08 Pass 03 — 2026-08-18

- Exact source delta from Pass 02: `checkpoints/phase-08-pass-03/ValoVault_PHASE_08_PASS_03.patch.xz.b64`
- Complete filesystem checkpoint supplied to the user: `ValoVault_PHASE_08_PASS_03_COMPLETE.zip`
- Complete ZIP SHA-256: `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`
- Complete ZIP files: 468
- ZIP CRC: PASS
- Verification: **69 tests passed**; Phase 04/05/06/07/08/08-pass02/08-pass03 audits passed; Python/JS syntax passed; localhost durable `capture-queue` + `fidelity-prepare` job/API smoke passed.
- Fixture truth: capture queue has 10 actions, 10 pending, 0 ready, all `NEED_BOTH`; derived working set is `BLOCKED` with 0 copied files because real capture evidence/preflight is absent.
- Pass-03 invariant: source capture evidence is never mutated; derived copies retain SHA-256 provenance; unsupported transforms block rather than silently approximate.
- Next objective: Phase 08 Pass 04 — scorecards + calibration evidence ledger/queue, without automatic or invented thresholds.

### Recover current Pass 03 from GitHub

1. Extract the Pass-01 active-source checkpoint.
2. Base64-decode and XZ-decompress the Pass-02 patch, then apply it.
3. Base64-decode and XZ-decompress the Pass-03 patch, then apply it.
4. Read root `CURRENT_STATE.md`.
5. Run the recorded verification gate before editing.

## Remote direct-source mirror warning

The current `main` direct file tree is **not yet a proven complete browsable mirror of the recovered source tree**. The checkpoint artifacts above are the deterministic GitHub recovery path until a full path/hash audit proves otherwise. Do not silently treat the root handoff/prototype tree as the whole project.