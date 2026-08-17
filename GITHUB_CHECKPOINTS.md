# ValoVault GitHub Checkpoints

GitHub is the durable execution/history/checkpoint index for ValoVault. The active ValoVault chat remains the authoritative planning/roadmap/next-prompt layer. Always read `CURRENT_STATE.md` and `VALOVAULT_OPERATING_RULE.md` before continuing.

## Phase 08 Pass 01
- Active-source checkpoint: `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`
- SHA-256: `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`
- Verification: 61 tests; Phase 04/05/06/07/08 audits passed.

## Phase 08 Pass 02
- Exact source delta: `checkpoints/phase-08-pass-02/ValoVault_PHASE_08_PASS_02.patch.xz.b64`
- Complete ZIP SHA-256: `8f3b794ea63904bbc4302d8cb322bb6455dd4c935f0553f18ebdc228c6e42f72`
- Verification: 65 tests + Pass-02 audit/API smoke.

## Phase 08 Pass 03
- Exact source delta: `checkpoints/phase-08-pass-03/ValoVault_PHASE_08_PASS_03.patch.xz.b64`
- Complete ZIP SHA-256: `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`
- Verification: 69 tests + Pass-03 audit/API smoke.

## Phase 08 Pass 04
- Exact source delta: `checkpoints/phase-08-pass-04/ValoVault_PHASE_08_PASS_04.patch.xz.b64`
- Complete ZIP SHA-256: `7390f9c42d0cca55cf1066f480b4f4090c51f825af6095c0c745215133476e85`
- ZIP files: 482; CRC/manifest hashes PASS.
- Verification: 75 tests + Pass-04 audit/API smoke.

## Phase 08 Pass 05
- Complete checkpoint: `ValoVault_PHASE_08_PASS_05_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_05_COMPLETE.zip`
- SHA-256: `c3f06e1991781e91678d9db32625dd7f4feda7c9754f0c55853b1232888fe387`
- ZIP files: 494; CRC/manifest hashes PASS.
- Verification: 84 tests + all audits through Pass 05.
- Fixture: 0 accepted cohorts; 88 `NO_ACCEPTED_EVIDENCE` packets; 0 numeric threshold suggestions; canonical thresholds `{}`.
- Pass-05 GitHub patch transport was not independently proven complete; use the complete verified ZIP for exact recovery.

## Phase 08 Pass 06 — 2026-08-18
- Canonical complete checkpoint: `ValoVault_PHASE_08_PASS_06_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_06_COMPLETE.zip`
- SHA-256: `cad9769249e4131cfd4ebe13bb371f0aa9e2db76f58a3cc3cbda720579532518`
- ZIP files: 509; checkpoint entries: 508; package entries: 507; CRC/manifest hashes PASS.
- Verification: 89 tests; all audits through Pass 06; Python/JS syntax PASS.
- Safety: threshold application remains CLI-only, token-bound, backed up and reversible.

## Phase 08 Pass 07 — 2026-08-18
- Canonical complete checkpoint: `ValoVault_PHASE_08_PASS_07_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_07_COMPLETE.zip`
- SHA-256: `ec898b86f5ac52359abd46053e5033b106b1fb09bb106bf2b4bea02744c2c19e`
- ZIP files: 525; checkpoint entries: 524; package entries: 523; CRC/manifest hashes PASS.
- Verification: 96 tests; all audits through Pass 07; Python/JS syntax PASS.
- Added PASS-only threshold policy promotion, target-PC handoff and truthful Reaver certification gate.

## Phase 08 Pass 08 — 2026-08-18
- Canonical complete checkpoint: `ValoVault_PHASE_08_PASS_08_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_08_COMPLETE.zip`
- SHA-256: `51f926369649e070b1b6efcfd3f3eb69261b3f1dfdbfe65516ea964aec5b7952`
- ZIP files: 536; checkpoint entries: 535; package entries: 534; CRC/manifest hashes PASS.
- Verification: 104 tests; all audits through Pass 08; Python/JS syntax PASS.
- Added portable target-PC return manifest/rebinding/reconciliation and local truth regeneration.

## Phase 08 Pass 09 — 2026-08-18
- Canonical complete checkpoint: `ValoVault_PHASE_08_PASS_09_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_09_COMPLETE.zip`
- SHA-256: `9f3ef8b3c90c55b9a8626285d2b7c2eda7eded2b9be77ad9d7058f354e850696`
- ZIP files: **546**
- Checkpoint-manifest entries: **545**
- Package-manifest entries: **544**
- ZIP CRC + every recorded manifest SHA/size: **PASS**
- Verification: **110 tests passed**; Phase 04/05/06/07 + Phase 08 + Pass-02/03/04/05/06/07/08/09 audits PASS; Python/JS syntax PASS.
- Added target-PC environment doctor, safe 74-file execution-kit plan/build/verify, safe non-proprietary return-package build/verify, and receiver verification feeding directly into Pass-08 reconciliation/local truth regeneration.
- Live backend exposes only the non-mutating `target-pc-doctor` job plus doctor/execution-plan GETs. Package build endpoints deliberately return 404.
- Actual proof execution kit: 74 files, SHA-256 `e0cbc509e6be773f999c76f391dcb98e0b3f4d577c61af88004ade203cf4a9d3`.
- Actual proof safe return bundle: 15 manifested metadata files, SHA-256 `077411e4ed6fc764b34082fd651f1ed6522d3dd915c3b1b872cf224f85d3073d`.
- Synthetic Windows-root two-machine round trip and local truth regeneration: PASS; capture/audio/model leakage rejection: PASS.
- Fixture truth: environment doctor BLOCKED / 3 real target-machine blockers; execution kit plan READY / 74 / 0 violations; no real captures/assets; certification remains BLOCKED; canonical thresholds `{}`.
- Next implementation prompt must be authored in chat. Current real gap: resumable target-PC session execution/receipt state machine, not broader premium scaling.

## Strict authority split

- **Chat owns roadmap reasoning, improvement choices, phase sequencing, and the canonical next implementation prompt.**
- **GitHub owns durable source/history/checkpoint metadata/milestones.**
- `CURRENT_STATE.md` is a concise recovery handoff, not the entire product strategy.

## Recovery rule

Prefer the newest complete checkpoint whose SHA/CRC/manifests have been verified. GitHub `main` is **not yet proven to be a complete path/hash mirror** of the recovered filesystem, so do not claim it is. The complete verified ZIP is the authoritative filesystem disaster-recovery source until that direct-tree audit exists.
