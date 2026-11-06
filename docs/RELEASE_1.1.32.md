# TagRelayLab Server 1.1.32

## Persistent toolbar and map appearance

- Keep the primary map controls in the same order on phone and desktop:
  **More → Administration → Location → Refresh**. Administration is still
  restricted to administrators. Closing the secondary panel never disables
  location, refresh or the administrator shortcut.
- Put account, language, map appearance and direct Nordic/ESP32 firmware links
  in a viewport-level glass panel. It fits the available screen, scrolls
  internally when height is limited and avoids nested header clipping.
- Animate panel entry and exit, including rapid reopen while closing. Outside
  presses and Escape close the panel; keyboard focus returns appropriately.
  Keep the existing administration workspace header and access controls.
- Correct mobile device-drawer dismissal: slide the full sheet downward from
  its current position without fading, shrinking its content or resetting its
  height during the exit. Support a deliberate flick, snap short pulls back,
  handle cancelled touches and reveal the corner reopen button only afterwards.
- Match device reorder controls to the glass interface: centered outline
  chevrons, a paired pill, directional hover and press feedback, visible focus,
  disabled end stops and 44-pixel mobile touch targets. Reordering still moves
  one position at a time and respects reduced-motion preferences.
- Add **Standard, Light, Dark and System** color styles to quick controls and
  Account → Map preferences. Save the choice per account in the current browser;
  System follows the browser color-scheme preference. Logout resets visible
  state and another account does not inherit the previous account's selection.
- These styles recolor the existing OpenStreetMap tiles locally. They are not
  satellite imagery or a new map provider: no API key, new tile service or new
  runtime dependency is required. Marker colors, attribution, zoom and stored
  coordinates remain unchanged.
- Keep six-language labels complete and preserve reduced-motion,
  reduced-transparency, high-contrast and keyboard-focus behavior.

## Checks and update

Responsive checks cover a 320-CSS-pixel phone, 1280-pixel desktop, a reduced
300-pixel height, all six languages and interrupted exit animations. Regression
tests cover persistent controls, safe panel bounds, account-isolated appearance,
system preference, synchronized selectors and storage failures. Checks do not
certify every physical phone/browser combination.

Back up data, pull **1.1.32** and recreate existing services with the same volumes.
Reload browser tabs after updating. Both modular and All-in-One images are
updated, with matching store metadata. No tracker registration, key rotation,
firmware flashing, data migration or ESP32 library upgrade is needed. Provider
and location-processing logic are unchanged. All-in-One still uses a separate
upstream Anisette container. Older version tags remain intact.

See [installation](INSTALLATION.md), the [gallery](screenshots/README.md) and
[licenses and corresponding sources](LICENSING.md).
