# Release completion policy

For every approved new server version, update the complete distribution, not
only source code or Docker tags. A release is not complete until all gates pass:

1. Synchronize the private server's approved catalog subtree with the public
   `Mattboxx/TagRelayLab-Appstores` repository. Keep README names, current guides,
   release notes, Compose recipes and every native adapter consistent.
2. Advance image tags, native app metadata/dates and Runtipi `tipi_version`
   together. Preserve installed-app IDs, volume/data paths and subscriptions.
3. Publish matching allowlisted provider sources before publishing binaries.
   Never publish private application source, credentials, keys or user data.
4. Wait for protected PR checks and merge normally; never bypass protections.
5. Publish versioned modular and All-in-One images, update `latest` and bundle
   `stable`, and verify anonymous AMD64/ARM64 manifests and compatibility aliases.
6. Publish the catalog/feed; verify immutable `catalog-VERSION` metadata, all
   three generated Compose variants, and new/legacy CDN subscription URLs.
7. Publish matching GitHub release notes and source attachments. Verify the
   actual update version, not merely that a workflow started.
8. Recheck the three repositories, library snapshot provenance and CI results;
   only then report completion. Report the actual error for any blocked gate.

Never move old tags, overwrite versioned archives, rebuild an existing stable
version in place or silently migrate installations. The public library has its
own approval/version process: preserve the technical `FindMyAdv` name, API and
approved version. Keep working firmware unchanged during documentation work.
Metadata-only maintenance instructions do not require a new binary release.
