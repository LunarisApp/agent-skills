# Host capabilities

Read `apps/docs/content/developers/extensions/host-capabilities.mdx` and the selected SDK types for the requested capability. Request only the manifest permissions required by the actual hooks and operations: `content.read`, `content.write`, `files.read`, `files.write`, `downloads.write`, `network.https` are the inspected permission names.

## UI, commands, and search

- Commands register during activation and use their scoped execute context. React hooks belong in components, not command handlers.
- Resource navigation uses resource identity and schema metadata. Check boolean navigation results before claiming a destination opened.
- Use `contributions.searchIndexer` for content that should appear in the current host search UI. Extract bounded, deterministic plain text from validated payloads; request `content.read`, plus `files.read` for binary reads. The inspected host registers `searchQuery` but does not yet consume it in the search interface; confirm current support before relying on it.
- Register host-visible locale strings with `contributions.locales`; initialize iframe-local translation using `useLocale` and extension dictionaries. The host's React i18n provider and CSS do not cross the iframe boundary. Import required styles explicitly.
- Use the selected SDK's readiness mechanism, such as `ViewReady`/`reportReady`, once the view is usable; inspect examples for the exact contract.

## Network and compute

Use `usePluginFetch()` with `network.https` for unauthenticated HTTPS. Browser CORS still applies; Desktop uses native transport. Credentials default to `omit`. Abort obsolete requests and validate responses before rendering or saving. Keep credentials out of bundles and workspace KV.

Use `useDownloads()` with `downloads.write`; `save` accepts `ArrayBuffer` with a 64 MiB limit at the inspected revision. Newer SDK/hosts optionally expose `saveChunks` with a 256 MiB total. Check availability and execute a fallback or show a host requirement; silent optional chaining cannot count as a successful export. Browser downloads still assemble a Blob.

For CPU-heavy pure work, import a dedicated worker with `?worker&inline`, expose it through `exposePluginWorkerTask`, and invoke via `runPluginWorkerTask` from `/worker`. Inline output preserves the single pinned script. Inputs must be structured-cloneable; transfer lists detach input buffers. Workers have no host bridge, DOM, network, storage, or progress channel. Use cancellation and bounded execution.

## Collaboration presence

Use `useResourcePresence` for other viewers and `useResourceAwareness` for transient pointers/selections; read `packages/plugin-sdk/docs/presence.md` for bounds and lifecycle. These APIs use `content.read`; older hosts and local-only workspaces can return unavailable. Validate received state at runtime and preserve editing when presence fails. Presence is neither a lock nor authorization.

For editor cursors use `useYjsAwareness` on the same storage handle as `useYjsStorage`. Let the host manage identity, sessions, transport, and subscription cleanup. Durable collaboration continues through Yjs persistence, independently of awareness.

## Services and slots

Define provider-owned public contracts with `definePluginService`; register providers during activation. Consumers declare the provider's extension version range in required or optional dependencies. Handle absent optional providers and rebinding when they return.

Use service slots for multiple contributors; the Exporter example demonstrates representation providers. Across the sandbox, methods take one wire value and return one wire value: JSON-compatible data and supported `ArrayBuffer` values. Functions, React elements, DOM nodes, and live Yjs documents cannot cross this boundary. Share a public contract package instead of importing another extension's source.
