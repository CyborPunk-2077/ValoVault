# ValoVault GitHub Checkpoints

GitHub is the durable history/handoff/checkpoint index for ValoVault. The active ValoVault chat owns roadmap reasoning and the exact next implementation prompt. Always read `CURRENT_STATE.md` and `VALOVAULT_OPERATING_RULE.md` before continuing.

For exact filesystem recovery, prefer the newest complete checkpoint whose CRC/manifest/hash verification is recorded here. Do not claim the live GitHub tree is an exact mirror of a later filesystem checkpoint unless that exact tree was independently path/hash audited.

## Historical Phase 08 checkpoints

- **Pass 01** — source checkpoint `checkpoints/ValoVault_PHASE_08_PASS_01_GITHUB_SOURCE.tar.xz`; SHA-256 `f814f36bd28528a35e2ef7fd87aec8a691a7f070cb2350d51948877ab7d607b7`; 61 tests.
- **Pass 02** — complete ZIP SHA-256 `8f3b794ea63904bbc4302d8cb322bb6455dd4c935f0553f18ebdc228c6e42f72`; 65 tests.
- **Pass 03** — complete ZIP SHA-256 `33d81ec46e00b4eb80c8b25a58751c1be5fac8bb88e709a21f50c9bcecb32d13`; 69 tests.
- **Pass 04** — complete ZIP SHA-256 `7390f9c42d0cca55cf1066f480b4f4090c51f825af6095c0c745215133476e85`; 75 tests.
- **Pass 05** — `ValoVault_PHASE_08_PASS_05_COMPLETE.zip`; SHA-256 `c3f06e1991781e91678d9db32625dd7f4feda7c9754f0c55853b1232888fe387`; 84 tests.
- **Pass 06** — `ValoVault_PHASE_08_PASS_06_COMPLETE.zip`; SHA-256 `cad9769249e4131cfd4ebe13bb371f0aa9e2db76f58a3cc3cbda720579532518`; 89 tests.
- **Pass 07** — `ValoVault_PHASE_08_PASS_07_COMPLETE.zip`; SHA-256 `ec898b86f5ac52359abd46053e5033b106b1fb09bb106bf2b4bea02744c2c19e`; 96 tests.
- **Pass 08** — `ValoVault_PHASE_08_PASS_08_COMPLETE.zip`; SHA-256 `51f926369649e070b1b6efcfd3f3eb69261b3f1dfdbfe65516ea964aec5b7952`; 104 tests.
- **Pass 09** — `ValoVault_PHASE_08_PASS_09_COMPLETE.zip`; SHA-256 `9f3ef8b3c90c55b9a8626285d2b7c2eda7eded2b9be77ad9d7058f354e850696`; 110 tests.
- **Pass 10** — `ValoVault_PHASE_08_PASS_10_COMPLETE.zip`; SHA-256 `1bea8efb5eb4d329bdfed4777af0902651833cb3c5e0b1939df231b5dfa96d17`; 118 tests; target-PC resumable session + SHA-bound receipt.

All recorded complete ZIP checkpoints above passed CRC/recorded manifest verification at creation. Historical recovery snapshots/divergent Phase-6 branches remain recovery evidence, not instructions to merge them into current mainline work.

## Post-Pass-10 direction correction

### Workflow hardening
- Reaver closure lock established; no speculative Pass 11 or premium-family fidelity scaling before real Reaver closure.
- Operator/recovery path simplified.
- Verification: 121 tests.
- Milestone: `milestone/pass10-workflow-hardened`.

### Product hardening
- Exact checkpoint: `ValoVault_PASS10_PRODUCT_HARDENED_COMPLETE.zip`
- SHA-256 `aa50b7d84db1f0fa5159426f47c2b884d5b47176ccb595f470ad0e72554c33bc`
- 593 files / CRC + embedded manifests PASS
- Verification: 134 tests.
- Added Reaver operator façade, safe public catalog promotion/provenance, catalog scalability/UI controls, local app doctor/start entrypoint, Recovery Vault hardening and completion matrix.
- Milestone: `milestone/pass10-product-hardened`.

### Local-first web runtime hardening
- Exact checkpoint: `ValoVault_PASS10_WEB_RUNTIME_HARDENED_COMPLETE.zip`
- SHA-256 `aadb95b42bcf1651d0e97de9238f501982b6a3d94880f90c444fd8a7d0913570`
- 601 files / CRC + embedded manifests PASS
- Verification: 138 tests / 26 release checks.
- Runtime CDN scripts/styles removed; pinned official Three.js r180 vendor identities + verified installer; ValoVault local Catalog GLB viewer; web-runtime audit.
- Recovery Vault at that milestone: SHA-256 `383ba485bce895e56049af6e7044c2c6cdf9e3cba465505c8074875ec1504862`.
- Milestone: `milestone/pass10-web-runtime-hardened`.

## Pass 10 localhost security hardening — CURRENT

- Exact checkpoint: `ValoVault_PASS10_LOCALHOST_SECURITY_HARDENED_COMPLETE.zip`
- SHA-256: `9d7c0d1fa2669cc5ac6b2aab59554883e1c791de4257770518824db02baa94b1`
- size: **3,147,639 bytes**
- files: **605**
- CRC + package/checkpoint manifest hashes/sizes: **PASS**
- Verification: **142 pytest tests / 26 release checks PASS**; all audits through Phase 08 Pass 10, Python compileall and relevant JavaScript syntax remain PASS.
- Localhost HTTP hardening: loopback Host only, foreign Origin/cross-site rejection, JSON-only writes, no wildcard CORS, basic response-hardening headers.
- Live smoke: local health 200; foreign read 403; foreign write 403; local non-JSON write 415; local JSON write 202; non-loopback Host 403.
- Durable jobs cleaned to 0 before checkpoint.
- Reaver target kit: SHA-256 `b7eb9865eb1db8a2eeb1d3033742e8344073903167e372d44de9d67a81c75043`; 83 allowlisted payload files / 0 violations.

### Current Recovery Vault

`ValoVault_RECOVERY_VAULT_ALL_HISTORY.zip`
- SHA-256: `7e61ec98b545ad9e006840e3c9ee4911f2369c9685e56f72deacf9866c7add5e`
- size: **44,984,585 bytes**
- 34 candidate artifacts → **27 unique artifacts** / 7 duplicate copies elided
- CRC PASS
- previous Recovery Vault containers are never recursively nested.

## Authority split

- **Chat:** roadmap, improvements, sequencing, exact next prompt.
- **GitHub:** durable history/handoff/index/milestones.
- **Newest complete verified ZIP:** exact filesystem disaster recovery unless a later Git source tree is independently proven complete.
- **Recovery Vault:** one-file historical fallback so the user never has to manually collect old ZIPs.

The user should not be asked to run the real target-PC evidence workflow yet. Continue only concrete independent product/usability/data/distribution/security work that can be verified without proprietary evidence. If no material gap remains, stop adding architecture and preserve the clean checkpoint.
