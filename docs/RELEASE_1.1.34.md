# TagRelayLab Server 1.1.34

This maintenance release fixes a Google Find Hub provider failure that
could interrupt position updates even when the device list and EID renewal
worked normally.

- The Firebase Cloud Messaging listener now accepts both padded and
  unpadded Base64url values for Web Push encryption parameters.
- Previously, a valid notification without padding could stop the listener
  with `Incorrect padding`. Position requests then timed out and returned
  HTTP 500.

No account migration, tracker re-registration, new keys or firmware
flashing are needed. Update the existing installation with the same
volumes and click **Refresh**. Check for a successful Google position
fetch and, when a new report is available, a newer report timestamp.
This fix does not change which sightings Google's network collects.

See the [installation guide](INSTALLATION.md) for both Docker layouts.
