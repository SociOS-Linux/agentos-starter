# Orchestrator Interface (patched)

## Purpose
Coordinate **multiple executors** across multiple repos/worktrees with role separation.

## Required capabilities
- `spawn(role, workspace, mode='ask', toolBudget=None, memoryScope=None, skillRefs=None, surface=None)` -> returns session handle
- `assign(session_handle, task, completion_criteria)` -> tracked work item
- `collect(session_handle=None)` -> unify reports + diffs + gate results
- `gate(stage, session_handle=None)` -> pass/fail decision based on evidence
- `defer(session_handle, pending_request)` -> persist a paused decision point
- `resume(session_handle, decision)` -> resume with explicit execution decision

## Example providers
Gastown (primary). AIWG provides stage-gate semantics, not workspace spawning.
