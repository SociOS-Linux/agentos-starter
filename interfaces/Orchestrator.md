# Orchestrator Interface

## Purpose
Coordinate **multiple executors** across multiple repos or worktrees with role separation.

## Required capabilities
- `spawn(role, workspace, mode='ask', toolBudget=None, memoryScope=None, skillRefs=None, surface=None)` -> returns session handle
- `assign(sessionHandle, task, completionCriteria)` -> tracked work item
- `collect(sessionHandle=None)` -> unify reports, diffs, and gate results
- `gate(stage, sessionHandle=None)` -> pass or fail decision based on evidence
- `defer(sessionHandle, pendingDecision)` -> persist a paused decision point
- `resume(sessionHandle, executionDecision)` -> resume with explicit execution decision

## Example providers
Gastown (primary). AIWG provides stage-gate semantics, not workspace spawning.
