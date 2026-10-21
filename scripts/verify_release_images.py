"""Verify public release images, architectures and moving tags without Docker/login."""
import argparse
import hashlib
import json
import re
import urllib.request

IMAGES = ("find-my-web", "find-my-apple-provider", "find-my-google-provider",
          "tagrelaylab-server", "apple-google-tracking-server", "find-my-hub")
BUNDLES = IMAGES[3:]
ACCEPT = "application/vnd.oci.image.index.v1+json, application/vnd.docker.distribution.manifest.list.v2+json"


def index(image, tag):
    with urllib.request.urlopen(f"https://ghcr.io/token?service=ghcr.io&scope=repository:mattboxx/{image}:pull", timeout=30) as response:
        token = json.load(response)["token"]
    request = urllib.request.Request(
        f"https://ghcr.io/v2/mattboxx/{image}/manifests/{tag}",
        headers={"Authorization": "Bearer " + token, "Accept": ACCEPT, "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
        digest = "sha256:" + hashlib.sha256(raw).hexdigest()
        if response.headers.get("Docker-Content-Digest", digest) != digest:
            raise ValueError(f"{image}:{tag}: registry digest mismatch")
    return json.loads(raw), digest


def verify(version):
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("A stable semantic version is required")
    canonical = None
    for image in IMAGES:
        expected = None
        for tag in (version, "latest", "stable") if image in BUNDLES else (version, "latest"):
            payload, digest = index(image, tag)
            platforms = {(entry.get("platform", {}).get("os"), entry.get("platform", {}).get("architecture"))
                         for entry in payload.get("manifests", [])}
            if not {("linux", "amd64"), ("linux", "arm64")} <= platforms:
                raise ValueError(f"{image}:{tag}: missing amd64/arm64")
            expected = expected or digest
            if digest != expected:
                raise ValueError(f"{image}:{tag}: moving tag differs from {version}")
        if image in BUNDLES:
            canonical = canonical or expected
            if expected != canonical:
                raise ValueError(f"{image}: bundle compatibility alias mismatch")
        print(f"{image}: {version}, moving tags, amd64/arm64 and anonymous access OK ({expected})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version")
    verify(parser.parse_args().version)
