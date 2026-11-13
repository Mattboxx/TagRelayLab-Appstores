# TagRelayLab Server 1.1.38

The administrator Setup page can download a Windows assistant for the Google
account. Extract the ZIP and double-click `Start Google Setup.cmd`. It uses
Chrome and Python 3.12; if Python is missing, the launcher offers to install it
through Windows Package Manager. The assistant verifies the pinned upstream
source archive before running the desktop login.

Sign in only in the Google window. The assistant creates `secrets.json` beside
the launcher; return to Setup and import it. No automatic upload, account
migration, tracker re-registration or firmware changes are required.
Non-Windows systems can continue to use the upstream desktop guide.

See the [installation guide](INSTALLATION.md).
