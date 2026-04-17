from __future__ import annotations
from typing import Any, Dict


def verify_witness_block(bundle: Dict[str, Any], scope: str) -> bool:
    witness = bundle.get("witness", {})
    sigs = bundle.get("signatures", [])
    if scope == "review-grade":
        return "manifest" in bundle and "journal" in bundle
    if scope == "governance-grade":
        return bool(witness.get("creator")) and bool(witness.get("twin")) and len(sigs) >= 1
    return False
