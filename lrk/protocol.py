from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

try:
    import yaml
    _YAML_IMPORT_ERROR = None
except ModuleNotFoundError as exc:
    yaml = None
    _YAML_IMPORT_ERROR = exc


def load_protocol_bindings(path: str) -> Dict[str, Any]:
    if yaml is None:
        raise RuntimeError(
            "load_protocol_bindings requires the third-party 'PyYAML' package. "
            "Install it with 'pip install PyYAML'."
        ) from _YAML_IMPORT_ERROR

    loaded = yaml.safe_load(Path(path).read_text())
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError("Protocol bindings file must contain a YAML mapping at top level.")

    return loaded


def resolve_tritrpc_binding(path: str) -> Dict[str, Any]:
    data = load_protocol_bindings(path)
    return data.get("protocol_bindings", {}).get("tritrpc", {})
