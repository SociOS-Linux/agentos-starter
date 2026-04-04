# Executor Interface (patched)

## Purpose
A provider that can **apply changes** to a repo/worktree and run commands/tests.

## Required capabilities
- `plan(task, session_handle=None)` -> structured plan + required tools
- `apply(patch|instructions, session_handle=None)` -> repo modifications (git diff-able)
- `run(cmd, cwd, env, session_handle=None, surface=None)` -> command execution with captured stdout/stderr/exit code
- `report(session_handle=None)` -> JSON report compatible with `SessionReceipt`, including provenance, tool calls, execution surface, and artifact refs

## Hard constraints
- Must be runnable in a sandboxed context (non-root, constrained FS)
- Must never store secrets in logs
- Must emit stable artifact refs for review/promotion/reversal flows

## Example providers
OpenCode, Aider, Continue, Goose.
