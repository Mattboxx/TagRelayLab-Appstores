# Security policy

For the server, providers or Docker catalog, use GitHub's
[private vulnerability reporting form](https://github.com/Mattboxx/TagRelayLab-Appstores/security/advisories/new).
The application source repository is private; this public catalog is the
available confidential reporting entry point. For the standalone ESP32 library,
use its [private reporting form](https://github.com/Mattboxx/TagRelayLab-ESP32-Library/security/advisories/new).

Never put account credentials, tracker identities, exact positions, private keys,
`secrets.json`, `.env`, personalized firmware or complete container logs in public
issues. Include the affected version/digest and a minimal reproduction with
synthetic data. Ordinary installation questions belong in public issues, with
all sensitive details removed.

Security fixes target the latest stable release. Old immutable image tags are
retained for rollback, not recommended for new deployments. The volunteer
project handles reports on a best-effort basis without a guaranteed response
deadline; coordinate fixes and disclosure privately.
