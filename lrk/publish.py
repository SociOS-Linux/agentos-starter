from __future__ import annotations
from typing import Iterable, Dict, Any, Optional

from .attest import build_hash_manifest, append_journal_hash


def build_publication_bundle(
    *,
    bundle_id: str,
    artifacts: Iterable[str],
    previous_hash: str = "0000",
    creator_sig: Optional[str] = None,
    twin_sig: Optional[str] = None,
    bundle_sigs: Optional[list[str]] = None,
) -> Dict[str, Any]:
    arts = list(artifacts)
    manifest = build_hash_manifest(arts)
    journal = {
        "previous": previous_hash,
        "current": append_journal_hash(previous_hash, manifest),
    }
    witness = {}
    if creator_sig:
        witness["creator"] = creator_sig
    if twin_sig:
        witness["twin"] = twin_sig

    return {
        "bundleId": bundle_id,
        "artifacts": arts,
        "manifest": manifest,
        "journal": journal,
        "witness": witness,
        "signatures": bundle_sigs or [],
    }
