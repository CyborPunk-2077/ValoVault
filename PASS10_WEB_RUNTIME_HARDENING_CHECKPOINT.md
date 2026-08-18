# ValoVault — Pass 10 Local-First Web Runtime Hardening

Date: 2026-08-18

This checkpoint continues the Pass-10 product-completion lane without creating Pass 11 or changing Reaver fidelity semantics.

## Closed product gap

The Browser Weapon Lab, Catalog inline 3D preview and browser shells had hidden remote executable/style dependencies. Runtime CDN execution has been removed.

- Browser Weapon Lab resolves Three.js only from local pinned vendor paths.
- `config/web-vendor.json` pins official Three.js r180 files by exact upstream Git blob SHA-1.
- Explicit vendor setup verifies every Git blob before atomic promotion and records SHA-256/size in `VENDOR_LOCK.json`.
- Catalog Google model-viewer dependency was replaced by a minimal ValoVault-owned local Three.js GLB/animation viewer.
- Google Fonts runtime stylesheets/preconnects were removed from Catalog, Research and Control shells.
- `audit_web_runtime.py` prevents remote script/stylesheet/import-map dependencies from silently returning.
- Missing local Three.js vendor files gate Browser 3D only; Catalog/Control continue with image/media previews.

## Verified state

- 138 pytest tests PASS.
- 26 release self-test checks PASS.
- Every existing audit through Phase 08 Pass 10 PASS.
- Python compileall and relevant JavaScript syntax PASS.
- Web runtime audit: 0 remote executable/style/import-map findings.
- Local app doctor: PASS / 18 checks / 0 required blockers / 5 optional environment/capability warnings.
- Reaver target-PC execution kit remains 83 allowlisted payload files / 0 violations.
- Browser screenshot QA remains environment-gated; no visual PASS is claimed.
- Real Reaver evidence remains intentionally unexecuted; no readiness/fidelity/certification claim is fabricated.

## Durable artifacts

### Exact complete checkpoint
`ValoVault_PASS10_WEB_RUNTIME_HARDENED_COMPLETE.zip`
- SHA-256: `aadb95b42bcf1651d0e97de9238f501982b6a3d94880f90c444fd8a7d0913570`
- 3,143,428 bytes
- 601 ZIP files
- CRC + package/checkpoint manifests PASS

### Recovery Vault
`ValoVault_RECOVERY_VAULT_ALL_HISTORY.zip`
- SHA-256: `383ba485bce895e56049af6e7044c2c6cdf9e3cba465505c8074875ec1504862`
- 41,959,088 bytes
- 33 candidates → 26 unique artifacts / 7 duplicate copies elided
- CRC PASS

### Reaver target kit
`ValoVault_REAVER_TARGET_PC_EXECUTION_KIT.zip`
- SHA-256: `7d817f9d06a17148c9575b3ef792d22b1bb8e3f172b7bce618faf5334874d760`
- 83 allowlisted payload files / 0 violations

## Continuation

Do not ask the user to execute the real target-PC evidence workflow yet. Continue only concrete product/usability/security/distribution gaps that can be verified without proprietary evidence. The next identified independent gap is localhost backend write/CORS hardening.
