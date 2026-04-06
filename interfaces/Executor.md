# Executor Interface

## Purpose
A provider that can **apply changes** to a repo or worktree and run commands or tests.

## Required capabilities
- `plan(task, sessionHandle=None)` -> structured plan plus required tools
- `apply(patch|instructions, sessionHandle=None)` -> repo modifications that remain git-diff-able
- `run(cmd, cwd, env, sessionHandle=None, surface=None)` -> command execution with captured stdout, stderr, and exit code
- `report(sessionHandle=None)` -> JSON report compatible with `SessionReceipt`, including provenance, tool calls, execution surface, and artifact refs

## Hard constraints
- Must be runnable in a sandboxed context (non-root, constrained FS)
- Must never store secrets in logs
- Must emit stable artifact refs for review, promotion, and reversal flows

## Example providers
OpenCode, Aider, Continue, Goose.
