# Phase 08 Pass 03 checkpoint

Pass 03 advances ValoVault from observed capture/preflight planning to deterministic derived-working-copy preparation plus resumable capture/scenario queues.

Authoritative complete ZIP supplied to the user:

- `ValoVault_PHASE_08_PASS_03_COMPLETE.zip`
- SHA-256: `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`
- files: 468
- CRC: PASS

GitHub recovery path:

1. Extract `../ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`.
2. Apply the decoded/decompressed Pass-02 patch.
3. Base64-decode `ValoVault_PHASE_08_PASS_03.patch.xz.b64`, XZ-decompress it and apply the resulting unified diff.
4. Read root `CURRENT_STATE.md`.
5. Run `pytest -q tests tools/asset-indexer/tests` plus the Phase 04/05/06/07/08/08-pass02/08-pass03 audits.

Verified Pass-03 result: 69 tests passed. Packaged fixture: 10 queue actions, 10 pending, 0 ready, all `NEED_BOTH`; derived working set `BLOCKED`, zero copied files. Original evidence is never mutated and derived outputs retain SHA-256 provenance when produced.

Next objective: Phase 08 Pass 04 — metric scorecards plus calibration-evidence ledger/queue, without automatic/invented thresholds.