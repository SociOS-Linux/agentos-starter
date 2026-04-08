# MemoryAPI Interface (patched)

## System-of-record rule
System-of-record is **git + AIWG artifact directory**. MemoryAPI is a **queryable cache/service**, not authority.

## Required capabilities
- `put(namespace, key, payload, metadata, kind, citationRefs=[], authoritativeRef=None, freshness=None)`
- `get(namespace, key)`
- `search(namespace, query, filters)` -> ranked results + citations to artifacts
- `compact(namespace)` -> summarize/merge stale learned entries into recap form
- `pin(namespace, key)` -> protect high-value entries from compaction
- `export(namespace)` -> for backup/migration
- `import(namespace, dump)` -> for restore/replacement

## Supported kinds
- `rule` -> human-authored durable guidance
- `learned` -> model-discovered note anchored to artifacts/transcripts
- `recap` -> compressed summary artifact

## Required filters
- `kind`
- `workspace`
- `pathPrefix`
- `sessionRef`

## Example providers
Mem0 (primary).
