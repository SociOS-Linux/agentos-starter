# Baseline Replacement Checklist

Use this checklist to graduate `interfaces/vNext/*` into the canonical baseline interface files.

## MemoryAPI
- [ ] add `kind` parameter to `put(...)`
- [ ] require citation-aware search filters
- [ ] add `compact(namespace)`
- [ ] add `pin(namespace, key)`
- [ ] keep system-of-record rule unchanged

## Orchestrator
- [ ] change `spawn(...)` to return a session handle
- [ ] include `mode`, `toolBudget`, `memoryScope`, `skillRefs`, and `surface`
- [ ] add `defer(...)`
- [ ] add `resume(...)`

## Executor
- [ ] make `session_handle` explicit across `plan/apply/run/report`
- [ ] add `surface` to `run(...)`
- [ ] make `report(...)` receipt-compatible
- [ ] require stable artifact refs for review/promotion/reversal

## Exit condition
- [ ] baseline interface files updated
- [ ] `interfaces/vNext/` removed or archived after merge
