# ValoVault GitHub Checkpoints

GitHub is the durable continuation index for ValoVault. Always read root `CURRENT_STATE.md` first.

## Phase 08 Pass 01

- Active-source checkpoint: `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`
- SHA-256: `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`
- Verification at checkpoint: 61 tests; Phase 04/05/06/07/08 audits passed.

## Phase 08 Pass 02 — 2026-08-18

- Exact source delta from Pass 01: `checkpoints/phase-08-pass-02/ValoVault_PHASE_08_PASS_02.patch.xz.b64`
- Complete filesystem checkpoint supplied to the user: `ValoVault_PHASE_08_PASS_02_COMPLETE.zip`
- Complete ZIP SHA-256: `8f3b794ea63904bbc4302d8cb322bb6455dd4c935f0553f18ebdc228c6e42f72`
- Complete ZIP files: 458
- ZIP CRC: PASS
- Verification: 65 tests; Phase 04/05/06/07/08/08-pass02 audits passed; Python/JS syntax passed; localhost capture-index + fidelity-preflight durable job/API smoke passed.
- Fixture truth: 0/44 reference and 0/44 candidate channels observed; preflight BLOCKED with 88 blockers and 0 destructive operations.
- Next objective: Phase 08 Pass 03 — derived-working-copy normalization/alignment execution + capture/scenario queue orchestration.

### Recover Pass 02 from GitHub

1. Extract the Pass-01 active-source checkpoint.
2. Base64-decode the Pass-02 `.patch.xz.b64` file.
3. XZ-decompress it to a unified patch.
4. Apply that patch to the Pass-01 project tree.
5. Read root `CURRENT_STATE.md`.
6. Run the recorded verification gate before editing.

## Remote direct-source mirror warning

The current `main` direct file tree is **not yet a proven complete browsable mirror of the recovered source tree**. The checkpoint artifacts above are the deterministic GitHub recovery path until a full path/hash audit proves otherwise. Do not silently treat the prototype-only/root handoff tree as the whole project.