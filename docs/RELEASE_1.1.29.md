# TagRelayLab Server 1.1.29

## A consistent interface

- Share neutral controls across the map, device settings, account/user dialogs,
  administration, programming tools and license page. Danger and warning colors
  remain meaningful.
- Replace decorative action emojis with local outline SVGs while retaining
  translated labels, accessible names, field locks and hidden admin controls.
- Keep device key labels visible independently of placeholders; preserve six
  languages and the system's motion, contrast and transparency preferences.
- Refine the devices drawer's grip and close button: a compact 32 px visual
  control retains a 44 px touch target.
- Match the application and store icons to the neutral glass style.
- Guard accidental mobile document zoom in settings and dialogs, while keeping
  Leaflet's own pinch, double-tap and button zoom separate.

## A lighter map refresh

Unchanged reports reuse their existing Leaflet markers and paths. A changed
tracker rebuilds only its own layers; an unchanged bounding box no longer
recenters the map on every poll. During pan/zoom, glass backdrops temporarily
use a neutral tint instead of repeatedly blurring the moving map.

A regression test with 200 trackers and 2,000 points verifies that an unchanged
refresh adds/removes zero layers and does not repeat fitBounds. This is a
renderer test, not an FPS guarantee for every phone. Reports and stored history
are not reduced or deleted.

## Update

Back up data, pull 1.1.29 and recreate the existing services with the same volumes.
Reload browser tabs. No re-registration, firmware flashing, identity migration,
or library upgrade is required. The 1.1.28 and earlier versioned tags are preserved.
All-in-One still uses the separate upstream Anisette container.

See [installation](INSTALLATION.md), [screenshots](screenshots/README.md) and
[licensing and corresponding sources](LICENSING.md).
