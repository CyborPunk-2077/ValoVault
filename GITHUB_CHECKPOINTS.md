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
- Persisted in ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_06_COMPLETE.zip`
- Complete ZIP SHA-256: `cad9769249e4131cfd4ebe13bb371f0aa9e2db76f58a3cc3cbda720579532518`
- ZIP files: **509**
- Checkpoint-manifest entries: **508**
- Package-manifest entries: **507**
- ZIP CRC + every recorded manifest SHA/size: **PASS**
- Verification: **89 tests passed**; Phase 04/05/06/07/08 + Pass-02/03/04/05/06 audits passed; Python/JS syntax passed.
- Live backend: `threshold-governance`, token-free `threshold-application-plan`, and `calibrated-replay-plan` durable jobs/API all PASS.
- Safety proof: POST `/api/control/threshold-apply` returns **404**; threshold application is CLI-only, explicit-token-bound, backed up before mutation, stale/duplicate plans rejected, and rollback is byte-exact.
- Fixture truth: reviewed patches 0; governance reviewed/invalid/stale 0/0/0; application plan `NO_REVIEWED_PATCH`; active applications 0; calibrated replay `NO_APPLIED_THRESHOLD_VERSION`; canonical Reaver thresholds `{}`.
- Next direction: Phase 08 Pass 07 — replay-bound threshold promotion governance + version registry + target-PC calibration/replay certification handoff.

## Strict authority split

- **Chat owns roadmap reasoning and the canonical next implementation prompt.**
- **GitHub owns durable source/history/checkpoint metadata/milestones.**
- `CURRENT_STATE.md` is the concise recovery handoff, not the entire product strategy.

## Recovery rule

Prefer the newest complete checkpoint whose SHA/CRC/manifests have been verified. GitHub `main` is **not yet proven to be a complete path/hash mirror** of the recovered filesystem, so do not claim it is. The complete verified ZIP is the authoritative filesystem disaster-recovery source until that direct-tree audit exists.
