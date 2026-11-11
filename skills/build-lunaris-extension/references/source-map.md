# Source map

Resolve paths relative to the actual checkouts; this skill has no machine-specific checkout dependency. The repositories are `LunarisApp/lunaris` and `LunarisApp/extensions` on GitHub. Prefer local source or installed package declarations. When unavailable, retrieve only the relevant files from the repository through available GitHub tools. Ask for the target location only if it cannot be established.

## Lunaris application repository

| Path | Consult for |
| --- | --- |
| `packages/plugin-sdk/package.json` and `src/index.ts`, `src/data-index.ts` | Current package version, exports, and public API surface |
| `packages/plugin-sdk/src/manifest.ts` | Host API constants, manifest fields, permission names, validation |
| `packages/plugin-sdk/docs/{resources,views,storage}.md` | Resource contracts and migrations |
| `packages/plugin-sdk/docs/{presence,cross-extension-queries}.md` | Presence/awareness and semantic workspace access |
| `packages/plugin-sdk/docs/migrating-to-0.10.md` | Protocol 7, incremental Yjs replicas, chunked downloads |
| `apps/docs/content/developers/extensions/` | Quickstart, contracts, resources, migrations, host capabilities, testing, publishing |
| `extensions/{kanban,rich-text,file}/src/` | Built-in resource, editing, file, and export examples |
| `internal/workspaces/src/extensions/registry.ts` and `registry.test.ts` | Bundled descriptor wiring and import-boundary checks |

## Extensions repository

| Path | Consult for |
| --- | --- |
| `create-extension/README.md`, `template/` | Scaffolder, minimal package, Vite and TypeScript configuration |
| `extensions/demo/src/` | Validated resource payloads and KV initialization |
| `extensions/excalidraw/src/` | Yjs editing, loading/read-only states, status bar, search |
| `extensions/exporter/src/` | Host-mediated export and service slots |
| `extensions/mini-app/src/` | HTML-tool integration; inspect its security model before adapting |
| `registry/README.md`, `build-artifact.ts`, `update-marketplace.ts` | Immutable artifact packaging and index generation |
| `marketplace.json`, `artifacts/` | Published descriptor/index structure |

Examples are evidence of usage at their SDK version, not permission to reuse private imports or copy an entire app into a new extension. The spreadsheet example was marked an unpublished integration candidate when inspected.

## Compatibility findings

Inspected application revision `6b702cda3fa7319acac7c887d4a6f61bace08cd5` and extensions revision `cc1044ae7bf0f384876fd42dfd65615bbd0967bc`.

At these revisions, the community starter requests SDK `^0.10.0`, host API `^0.9.0`, and protocol 6. Application SDK `package.json` is `0.12.5`; its manifest constants support host APIs `0.9.0` and `0.10.0`. The migration guide introduces protocol 7 at SDK 0.11 and API 0.10 for new capabilities. These are source observations, not a claim that a checkout's version is published or every deployed host supports it. Read the selected build's `runtime.json` and current exports rather than deriving a protocol or API from package semver.

Some older package notes mention `/catalog`; the inspected exports expose `/marketplace` instead. Resolve discrepancies from the selected SDK's exports and implementation.

## Bundled integration

Built-ins use `@extension/<slug>` workspace packages and `lunaris.*` runtime identities. Their `src/descriptor.ts` exports `definePluginDescriptor({ manifest, icon, load: () => import("./index") })`. Descriptor and implementation manifests must agree. The host registry imports descriptors only; each descriptor owns lazy loading.

Keep implementation inside its extension package. Same-package imports, public SDK/UI entry points, and declared dependencies are allowed; other extension implementations and private `@repo/*` packages are excluded. Package export paths used by the host are integration boundaries, not a license for cross-extension implementation imports.

When built-in MCP support is requested, inspect its existing `mcp.ts`, `mcp-contract.ts`, and `mcp-runtime.ts`: declarations stay runtime-neutral, schemas describe contracts, and document logic stays pure. API/Desktop hosts own authorization, persistence, idempotency, and transport. Verify community sandbox support before proposing an equivalent MCP capability there.
