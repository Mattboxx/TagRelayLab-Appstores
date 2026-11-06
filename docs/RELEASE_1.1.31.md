# TagRelayLab Server 1.1.31

## Glass sign-in and complete mobile device settings

- Redesign sign-in and first-run setup with a black background, the map's
  layered glass material, restrained sky-blue reflections and animated buttons.
  A small, purely decorative street pattern recalls the map without showing
  real positions. Remove the large circular background effect.
- Keep form labels and keyboard focus visible, preserve password-manager
  autocomplete, and allow short/landscape screens to scroll to every field.
  Entry and button motion respect reduced-motion preferences. No new image
  download or runtime dependency is introduced.
- Make all original-device settings reachable from a unified view: the device
  settings button opens an original member, and a labelled selector switches
  between each original and the unified view. Keys, firmware tools, ownership,
  MQTT and other existing actions remain available. Polling preserves the
  selector, and logging out clears its device names.
- Keep the mobile settings frame within the visible viewport and scroll its
  content internally. Account and user dialogs prevent scroll chaining to the
  background while retaining inner scrolling and usable range controls.
- Use an accessible icon-only Setup control so translated labels cannot widen
  or overlap the toolbar. Language changes update its label and tooltip.
- Replace the unified-view chain icon with a consistent layered outline.
- Match Show hidden to the glass controls with an animated checkmark and touch
  feedback, preserving native checkbox semantics and the saved preference.

## Checks and installation

Regression coverage includes direct access to original settings, safe member
labels, account isolation, nested dialogs, touch/wheel scroll boundaries and
range controls, alongside the existing history, translation and location tests.
Responsive sign-in checks include 320/390 px phone layouts and desktop.
These checks do not certify every physical iPhone or browser version.

Back up your data, pull **1.1.31** and recreate the existing services with the
same volumes. Reload existing browser tabs after updating. No new tracker
registration, key rotation, firmware flashing or data migration is needed.
Provider logic, location processing, firmware bytes and FindMyAdv remain unchanged.
Both modular and All-in-One distributions are updated; All-in-One still needs
the separate upstream Anisette container. Older version tags are not replaced.

See [installation](INSTALLATION.md), the [gallery](screenshots/README.md) and
[licenses and source offers](LICENSING.md).
