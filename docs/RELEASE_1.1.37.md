# TagRelayLab Server 1.1.37

- The refresh button stops spinning when the server accepts the job. The
  map status shows which provider is being queried or whether results are
  being saved, plus elapsed time. A mobile notice confirms that the
  update was started even when the device panel is closed.
- The map starts loading saved devices without waiting for the administrator
  account list. Provider polling still runs in the background; an upstream
  service that is slow to respond can delay new reports without blocking
  access to the map.
- Retains the Google notification and Apple connectivity diagnostics fixes.

Update using the [installation guide](INSTALLATION.md), keeping your existing
data volumes, identities and credentials. No firmware changes are needed.
