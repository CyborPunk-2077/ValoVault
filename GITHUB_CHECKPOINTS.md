# ValoVault GitHub Checkpoints

GitHub is the durable continuation source for ValoVault. The newest verified checkpoint on `main`, together with root `CURRENT_STATE.md`, is authoritative.

## Recovery procedure for a fresh coding agent

1. Read root `CURRENT_STATE.md` first.
2. Locate the newest checkpoint in `checkpoints/`.
3. Verify its SHA-256 against this registry / `CURRENT_STATE.md`.
4. Extract it into a clean working directory.
5. Run the existing verification commands recorded in `CURRENT_STATE.md` before major edits.
6. Continue from the exact next objective; do not replay older phases.

## Checkpoints

### Phase 08 Pass 01 — 2026-08-17

- GitHub archive: `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`
- SHA-256: `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`
- Active source files represented: 424 Git-trackable files at packaging time.
- Full disaster-recovery ZIP (outside GitHub archive): `ValoVault_PHASE_08_PASS_01.zip`
- Full ZIP SHA-256: `8ef331ec0a22413cc19295553ecc07eb7e4091b9a0dcf0960febcb3c4946500c`
- Verification at checkpoint: 61 tests passed; Phase 04/05/06/07/08 audits passed.
- Next objective: Phase 08 Pass 02 — capture-session manifests/indexing + normalization/alignment preflight.

The GitHub source archive intentionally excludes redundant historical nested ZIPs and ignored local/proprietary/runtime/cache outputs. Those remain in the separately verified complete checkpoint ZIP. No active source code required for continuation is excluded.
