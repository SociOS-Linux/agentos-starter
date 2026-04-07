# agentos-starter

Bootstrap skeleton for AgentOS interfaces, policy, Linux integration, and registry scaffolding.

## Topology position

- **Role:** starter / scaffold repo for AgentOS-adjacent interfaces, policy, Linux integration, and registry structure.
- **Connects to:**
  - `SociOS-Linux/agentos-spine` — current Linux-side integration/workspace spine where broader assembly and routing belong
  - `SourceOS-Linux/sourceos-spec` — canonical typed contracts, JSON-LD contexts, and shared vocabulary
  - `SociOS-Linux/workstation-contracts` — workstation/CI contract and conformance lane
  - `SociOS-Linux/SourceOS` — immutable substrate that a concrete AgentOS integration may target
- **Not this repo:**
  - workspace controller
  - immutable substrate
  - canonical typed-contract registry
  - public docs site
- **Semantic direction:** this repo should eventually publish a starter-level repo descriptor that references the shared SourceOS/SociOS vocabulary from `sourceos-spec`.
