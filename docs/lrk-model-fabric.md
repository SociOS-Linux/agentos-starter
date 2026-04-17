# LRK Model Fabric in AgentOS Starter

This document places the LRK / semantic work in `agentos-starter` as a reference scaffold.

## Purpose

`agentos-starter` is not the immutable substrate and not the canonical contract registry. It is the right place for:

- starter package layout for the LRK model fabric
- collector and publisher stubs that emit truth/B11-style surfaces
- reference service topology for local-first semantic/runtime integration

## Components

### `lrk/`
A starter package for:
- metrics extraction
- surface assembly
- proof-of-life helpers
- model registry / benchmark scaffolding

### Systemd service stubs
- `lrk-surface-collector.service`
- `lrk-model-fabric.service`

These are intentionally small and audit-friendly. Richer integration belongs in `agentos-spine`.
