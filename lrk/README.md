# lrk (starter package)

Starter package for the Living Root Kit / semantic layer.

## Scope

This package should provide:
- metric extraction primitives
- truth/B11-style surface assembly helpers
- proof-of-life parsing helpers
- model registry and publication scaffolding
- protocol binding references to the canonical external `SocioProphet/TriTRPC` repo

It should **not** own:
- the immutable substrate
- the canonical schema family
- the authoritative TriTRPC wire format
- the full integrated runtime graph

## Suggested package layout

- `metrics.py`
- `surfaces.py`
- `pol.py`
- `registry.py`
- `delta.py`
- `invariants.py`
- `publish.py`
- `trust.py`
