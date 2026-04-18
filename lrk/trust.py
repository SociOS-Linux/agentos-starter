from __future__ import annotations
from typing import Any, Dict


def witness_policy_ok(bundle: Dict[str, Any], scope: str) -> bool:
    witness = bundle.get("witness", {})
    if scope == "review-grade":
        return True
    if scope == "governance-grade":
        return bool(witness.get("creator")) and bool(witness.get("twin"))
    return False
