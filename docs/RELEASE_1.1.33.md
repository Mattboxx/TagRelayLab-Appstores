# TagRelayLab Server 1.1.33

## History first, clear map preferences and smoother touch controls

- Verify the session behind a neutral loading state during page navigation.
  Show the login form only after the server confirms authentication is needed,
  eliminating the temporary sign-in flash for already signed-in users.
- The device settings icon now opens detailed position history first, with
  **Device details and settings** collapsed and ready to expand.
- Unified views show the combined/original-device selector above the history.
  Changing it synchronizes the history and settings target without merging,
  deleting or replacing any device, key or position.
- Put **Default source** and **Map appearance** only in the three-dot More menu.
  Preserve existing account-scoped browser preferences; remove the duplicates
  from the Account dialog.
- Keep reorder buttons square on tablet layouts, overriding inherited minimum
  heights. Touch-capable devices get 44-pixel controls, centered outline icons,
  disabled end stops and the existing glass feedback.
- Rework mobile drawer input around captured pointers and one paint per frame.
  Downward drags translate the fixed-size sheet without repeated height writes.
  Short pulls snap back, deliberate pulls/flicks dismiss, upward pulls expand,
  and direction changes, cancelled contacts and regrabs preserve continuity.
- Use one cancellable animation owner for drawer opening, settling and closing.
  Disable competing CSS entry animations that could restart after a drag,
  especially on browsers without discrete display transitions. Enlarge the grip's
  touch area and preserve reduced-motion behavior and normal list scrolling.

## Update

Back up data, pull **1.1.33** and recreate services with the same volumes. Reload
open browser tabs. Modular and All-in-One distributions have matching store
metadata and documentation. No firmware flashing, re-registration, key rotation
or data migration is needed; providers and location-processing logic are unchanged.
Anisette remains a separate upstream container. Previous stable tags are intact.

Responsive browser checks and automated tests cover phone/tablet proportions,
history/member selection, preference placement, frame coalescing, pointer capture,
snap/flick, regrab, cancellation and motion preferences. These are not a claim
of testing every physical iPad or Safari release.

See [installation](INSTALLATION.md), the [gallery](screenshots/README.md) and
[licenses and corresponding sources](LICENSING.md).
