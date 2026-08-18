# ValoVault — Pass 10 Localhost Security Hardening

Date: 2026-08-18

This checkpoint is an independent product/security hardening unit after Phase 08 Pass 10. It does not create Pass 11 and does not change asset/readiness/fidelity/certification truth.

## Closed gap

ValoVault's local HTTP services were already loopback-bound but previously emitted wildcard CORS. The current unified backend and documented legacy bridge now share a strict localhost browser boundary:

- loopback Host only (`127.0.0.1`, `localhost`, `::1`);
- foreign browser Origin rejected;
- `Sec-Fetch-Site: cross-site` rejected;
- mutating endpoints require `application/json`;
- wildcard CORS removed;
- validated loopback origins are echoed only for the active server port;
- local CLI clients may omit Origin/Sec-Fetch headers;
- no-sniff/referrer/CORP headers added.

Live HTTP smoke verified authorized and rejected paths. Test-created finished jobs were cleared before the checkpoint.

## Verification

- 142 pytest tests PASS;
- 26 release self-test checks PASS;
- all existing audits through Phase 08 Pass 10 PASS;
- Python compileall PASS;
- relevant JavaScript syntax PASS;
- durable jobs 0;
- Reaver target kit 83 allowlisted payload files / 0 violations.

## Durable artifacts

### Exact complete checkpoint
`ValoVault_PASS10_LOCALHOST_SECURITY_HARDENED_COMPLETE.zip`
- SHA-256 `9d7c0d1fa2669cc5ac6b2aab59554883e1c791de4257770518824db02baa94b1`
- 3,147,639 bytes
- 605 files
- CRC + embedded manifests PASS

### Recovery Vault
`ValoVault_RECOVERY_VAULT_ALL_HISTORY.zip`
- SHA-256 `7e61ec98b545ad9e006840e3c9ee4911f2369c9685e56f72deacf9866c7add5e`
- 44,984,585 bytes
- 34 candidates → 27 unique artifacts / 7 duplicates elided
- CRC PASS

### Reaver target kit
`ValoVault_REAVER_TARGET_PC_EXECUTION_KIT.zip`
- SHA-256 `b7eb9865eb1db8a2eeb1d3033742e8344073903167e372d44de9d67a81c75043`
- 83 allowlisted payload files / 0 violations

## Continuation

Do not ask the user for real target-PC evidence yet. Continue only concrete independent product/usability/data/distribution/security work that can be verified without proprietary evidence. Do not invent another fidelity phase.
