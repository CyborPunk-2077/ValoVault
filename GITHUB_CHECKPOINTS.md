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
- Live backend: threshold-governance, token-free threshold-application-plan and calibrated-replay-plan jobs/API PASS.
- Safety: no apply API; CLI application is token-bound, backed up, stale/duplicate-safe and reversible.
- Fixture: 0 reviewed patches/applications; calibrated replay `NO_APPLIED_THRESHOLD_VERSION`; canonical thresholds `{}`.

## Phase 08 Pass 07 — 2026-08-18
- Canonical complete checkpoint: `ValoVault_PHASE_08_PASS_07_COMPLETE.zip`
- ChatGPT Library: `/ValoVault Checkpoints/ValoVault_PHASE_08_PASS_07_COMPLETE.zip`
- SHA-256: `ec898b86f5ac52359abd46053e5033b106b1fb09bb106bf2b4bea02744c2c19e`
- ZIP files: **525**
- Checkpoint-manifest entries: **524**
- Package-manifest entries: **523**
- ZIP CRC + every recorded manifest SHA/size: **PASS**
- Verification: **96 tests passed**; Phase 04/05/06/07 + Phase 08 + Pass-02/03/04/05/06/07 audits PASS; Python/JS syntax PASS.
- Added replay-bound threshold-policy promotion governance, immutable promoted/retired policy registry, deterministic 10-action Reaver target-PC certification handoff, and machine-readable vertical-slice certification gate.
- Live backend: token-free promotion preview, target-PC handoff, and certification jobs/API PASS.
- Safety: `/api/control/threshold-promote` and `/api/control/threshold-retire` return **404**; actual promote/retire operations remain explicit CLI-only reviewer actions.
- Synthetic PASS replay → token-bound promotion → append-only retirement: PASS; FAIL replay and stale-spec promotion rejection: PASS.
- Fixture truth: promotion preview `NO_REPLAY_MEASUREMENT`; active threshold policies 0; target-PC handoff 10/10 actions; vertical-slice certification `BLOCKED` with 9 real blockers; canonical thresholds `{}`.
- Portability issue discovered: historical control/capture artifacts contain machine-specific absolute paths from older temporary workspaces. These must be reconciled/rebased before real target-PC evidence is trusted.
- Next objective: **Phase 08 Pass 08 — portable target-PC return ingestion + path reconciliation/rebasing**, still Reaver-only.

## Strict authority split

- **Chat owns roadmap reasoning, improvement choices, phase sequencing, and the canonical next implementation prompt.**
- **GitHub owns durable source/history/checkpoint metadata/milestones.**
- `CURRENT_STATE.md` is a concise recovery handoff, not the entire product strategy.

## Recovery rule

Prefer the newest complete checkpoint whose SHA/CRC/manifests have been verified. GitHub `main` is **not yet proven to be a complete path/hash mirror** of the recovered filesystem, so do not claim it is. The complete verified ZIP is the authoritative filesystem disaster-recovery source until that direct-tree audit exists.
