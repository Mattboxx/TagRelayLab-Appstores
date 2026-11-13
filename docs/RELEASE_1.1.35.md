# TagRelayLab Server 1.1.35

Supersedes the 1.1.34 Google Find Hub notification compatibility fix.
In addition to accepting unpadded Base64url, the provider now reads the
named `dh` and `salt` parameters separately from other Web Push header
parameters. Previously the extra fields could corrupt the decoded public
key, shut down the FCM listener and cause position requests to time out.
Messages for unrelated subtypes and malformed encryption parameters no
longer stop delivery of subsequent valid notifications.

Update using the [installation guide](INSTALLATION.md), keep existing
volumes, and click **Refresh**. No account reset, tracker re-registration,
key changes or firmware changes are needed. The fix does not cause Google's
network to generate new sightings.
