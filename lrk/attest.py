from __future__ import annotations

import hashlib
from typing import Dict, Iterable


def build_hash_manifest(artifacts: Iterable[str]) -> Dict[str, str]:
    return {
        artifact: hashlib.sha256(artifact.encode("utf-8")).hexdigest()
        for artifact in artifacts
    }


def append_journal_hash(previous_hash: str, manifest: Dict[str, str]) -> str:
    parts = [previous_hash]
    for artifact, digest in sorted(manifest.items()):
        parts.append(f"{artifact}:{digest}")
    payload = "\n".join(parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
