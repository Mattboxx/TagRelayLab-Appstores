# TagRelayLab Server 1.1.36

- Map refresh runs in the background instead of waiting on one long browser
  request. The map keeps its saved positions while providers respond. Short
  status requests retry after transient connection failures.
- Apple connection testing now distinguishes a successful sample with no
  reports from the number of configured devices. It samples one Apple tracker
  over the last day. An empty response is not a connection failure.
- Keeps the Google notification compatibility fixes from 1.1.35.

Update using the [installation guide](INSTALLATION.md) and keep your existing
volumes. No changes to tracker identities, firmware or credentials are needed.
