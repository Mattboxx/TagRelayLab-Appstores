# TagRelayLab Server 1.1.26

This release makes large saved-device lists usable sooner and aligns the three
related projects under the TagRelayLab name.

## Changes

- Devices appear progressively in pages of 50, without loading every history.
- History loads on selection or when History mode is explicitly enabled, with
  bounded concurrency and protection against previous-account responses.
- Every visit starts in Latest; the history-range preference remains separate.
- Google analysis no longer holds the shared ingestion lock during computation.
  The last reliable position stays available while an update is pending; raw
  outliers are never promoted to reliable positions as a loading shortcut.
- The mobile device-list button is restored after sign-in/session restoration.
- Current README titles distinguish TagRelayLab Server, TagRelayLab Appstores
  and TagRelayLab ESP32 Library. Technical FindMyAdv names and app IDs remain.

## Verification and limits

Regressions cover paging, lazy history, session isolation, concurrent ingestion
and reliable/raw separation. Desktop/mobile browser checks use 150 synthetic
devices. A local benchmark with 60,000 saved points measured a 68,039-byte first
summary page versus a 31,367,254-byte full-list response; real server timings
depend on hardware and data. CI additionally tests simulated-provider restart
and stable-image startup.

No live account or hardware validation is implied. Firmware bytes, tracker
identities, raw reports and existing immutable releases are unchanged.

## Update

Back up data, pull `1.1.26`, recreate the same services with the same volumes,
and reload browser tabs. Do not reinstall or regenerate identities. `latest`
tracks this release after publication. All-in-One still uses two containers:
the server bundle and external Anisette.

See [installation](INSTALLATION.md), [user guide](USER_GUIDE.en.md) and
[licensing/source offer](LICENSING.md).
