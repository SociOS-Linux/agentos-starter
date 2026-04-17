from __future__ import annotations
from pathlib import Path
from typing import Dict, Any
import yaml


def load_protocol_bindings(path: str) -> Dict[str, Any]:
    return yaml.safe_load(Path(path).read_text())


def resolve_tritrpc_binding(path: str) -> Dict[str, Any]:
    data = load_protocol_bindings(path)
    return data.get("protocol_bindings", {}).get("tritrpc", {})
