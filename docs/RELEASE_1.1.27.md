# TagRelayLab Server 1.1.27

This maintenance release completes the current three-repository consistency audit.

## Changes

- Use TagRelayLab for both the installed web-app name and short name.
- Align current deployment/network instructions, fresh-install folder examples,
  canonical links and confidential security-reporting instructions.
- Keep optional Italian localization documentation collapsed under English.
- Correct the manual release recovery workflow's GHCR namespace handling and
  verify the same All-in-One image set as the normal release workflow.
- Match the downloadable FindMyAdv API reference to its actual defaults and
  out-of-range interval fallback; implementation, API and version 1.1.0 are unchanged.
  Both server snapshots match public revision
  `82c4f264bb4423060d29cbd573a9b852fe519772`, including provenance hashes.
- Add read-only consistency checks and negative regressions for stale/surplus
  files, staged deletions, binary corruption, broken anchors and version drift.

## Preserved behavior

Progressive device loading, on-demand histories, Latest on each visit, reliable
Google positions and account isolation from 1.1.26 remain. No tracker identities,
keys, raw reports, firmware bytes, installation IDs or data paths are changed.
Old release/image/catalog tags remain immutable. This is not new hardware,
certification or live-account validation.

## Update

Back up data, pull `1.1.27`, recreate the same services with their existing
volumes and reload browser tabs. Do not reinstall or regenerate identities.
All-in-One still uses two containers, including separate upstream Anisette.
Library source snapshots remain distinct from the original immutable 1.1.0 tag.

See [installation](INSTALLATION.md), [security reporting](../SECURITY.md) and
[licensing/source offer](LICENSING.md).
