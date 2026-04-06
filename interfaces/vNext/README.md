# Agent-plane vNext Interfaces

These additive interface drafts exist to align AgentOS with the merged `SourceOS-Linux/sourceos-spec` agent-plane schema family without destabilizing the current baseline interfaces prematurely.

## Files

- `MemoryAPI.md`
- `Orchestrator.md`
- `Executor.md`

## Why additive first

The baseline interfaces remain intentionally minimal.
The `vNext` drafts capture the runtime-law semantics now represented upstream in the schema layer:
- session-oriented orchestration
- defer / resume decision flow
- authored vs learned memory separation
- execution surface awareness
- receipt-compatible executor reporting

## Migration path

1. Review the `vNext` drafts against the merged schema family.
2. Replace the baseline interface files once the naming and field shapes settle.
3. Remove `interfaces/vNext/` after the canonical baseline is updated.

## Non-goal

`interfaces/vNext/` is not intended to become a permanent second interface surface.
