# LRK Runtime Starter Note

This note anchors the LRK / Semantic Holography starter integration in `agentos-starter`.

## Role of this repo

`agentos-starter` is the scaffold layer for the Linux-side LRK runtime starter package.

It is the correct home for:
- local-first LRK package structure
- starter collectors and emitters
- invariant and delta helpers
- publication and trust scaffolding
- protocol binding references to the external canonical TriTRPC repo

It is **not** the canonical contract registry and it should not redefine transport semantics already governed by `SocioProphet/TriTRPC`.

## Follow-on work

- land LRK package files
- land collector and invariant CLIs
- land publication/trust helpers
- align naming to upstream TruthSurface / DeltaSurface semantics where applicable
