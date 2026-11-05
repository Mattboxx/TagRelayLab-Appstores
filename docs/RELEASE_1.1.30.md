# TagRelayLab Server 1.1.30

## Clearer glass, consistent navigation

- Keep the main map translucent while panning and zooming. Only administration
  and programming workspaces use a black background, with subtle colored rims,
  recessed fields and restrained reflections for readable text.
- Center the map toolbar, remove its duplicate brand label, and order its
  controls as account, language, firmware, administration, position and refresh.
  Active geolocation has a light sky-blue state; the firmware icon has a muted
  yellow accent. Duplicate refresh requests are guarded.
- Make the firmware menu readable and viewport-aware on small screens. Press
  the lightning button again to close it, with a cancellable return animation.
- Keep a consistent return action at the upper left of administration and
  programming pages. Match language selectors, buttons and touch feedback.
- Refine device-drawer tool sizes and centering, reserve room for its close
  control and enlarge the glass reopen button in the map corner.
- Give support and license links a quiet sky-blue glass treatment.

## Device details and accounts

- Open device settings directly from the device's settings icon. Keep history
  and configuration separate, use an aligned SVG chevron, and prevent the
  device drawer from obscuring the detail panel on compact screens.
- Lay out source/time, coordinates, navigation, map actions and the history
  slider in separate rows. Marker popovers follow the shared visual style and
  retain every report field; unknown accuracy is not shown as zero metres.
- Animate device actions and disclosure sections in both directions, including
  interrupted open/close sequences. Respect reduced-motion preferences and
  retain contrast/transparency fallbacks.
- Separate the user list and account creation form into labelled tabs. Keep
  long names readable, mobile actions stacked and Close outside the scroll
  region; dialogs follow the visible viewport when space is limited.
- Refresh accessible labels when the language changes. Existing six-language
  bundles, account isolation and original device/identity actions remain intact.
- Refresh the application and store icons with one muted glass master.

## Verification and update

Static HTML, CSS, JavaScript and other text assets are precompressed at Docker
build time and negotiated as gzip for compatible clients. Decompression restores
the exact original bytes: no styling, graphics, animation or function is removed.
Original files, ETag revalidation and range requests remain supported. APIs and
personalized exports are excluded; there is no extra runtime compressor or
dependency. The maintainer-only icon master is excluded from the runtime image.

Responsive checks cover 320/390 px phones, 672/1024 px intermediate layouts,
1440 px desktop and 844×390 landscape, plus a 320×380 reduced-height dialog.
Automated coverage includes history ranges, raw/reliable Google separation,
session isolation, animation cancellation and renderer reuse. These checks
are not a guarantee for every physical iPhone, browser or assistive technology.
See the [updated screenshot gallery](screenshots/README.md).

Back up data, pull 1.1.30 and recreate the existing services with the same volumes.
Reload browser tabs after updating. No tracker registration, firmware flashing,
key rotation, data migration or ESP32 library upgrade is required. Provider
and location-processing logic and working firmware are unchanged by this release.
All-in-One still needs the separate upstream Anisette container. Existing
versioned image tags and compatibility names are preserved.

See [installation](INSTALLATION.md) and [licensing/source offers](LICENSING.md).
