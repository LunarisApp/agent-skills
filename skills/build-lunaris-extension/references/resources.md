# Resources and storage

Read the selected SDK's resource/view types and storage migration guide alongside the nearest example. A resource type owns durable data; a view owns presentation. Navigate by `resourceId`, not a backing Yjs document ID or a view instance ID.

## Design the payload

Declare a fixed map of named slots on the resource type:

- `yjs`: collaboratively edited structured content.
- `key-value`: synced values such as resource settings.
- `file`: zero or one backing file per fixed slot.

Use multiple fixed slots where needed. Dynamic file collections are not supported by a single file slot. Workspace-wide preferences require `defineWorkspaceStorage` and `contributions.workspaceStorage` during activation; they are scoped to the registering extension. KV is synced data, not secret storage.

Define a stable `resourceTypeId`, schema ID, `currentVersion` starting at 1, Standard Schema validators in `versions`, and a `schema.read` that projects the logical payload across slots. Declare `defaultViewId` and hierarchy creation/visibility as required. Initialize durable defaults through slot initialization or scoped resource creation, once; a loading renderer must never replace existing data with defaults.

Resource views declare `target: { kind: "resource", resourceTypeIds, schemas }` and `storageRequirements`, mapping each required slot name to its kind. The host matches type, schema range, and slots before opening. It passes only the handles requested. Use `storageRequirements: {}` for a storage-free resource view. A `statusBar` belongs to its resource view; standalone views cannot declare one.

## Read and edit

Use `useYjsStorage`, `useKeyValue`, and `useStoredFile` with supplied opaque handles. Wait for Yjs hydration and handle errors/missing documents before constructing an editor. Honor `useOrganizationAccess` write state; request the manifest permissions enforced by the selected hooks. Yjs/KV hooks currently require both `content.read` and `content.write`, including read-looking uses. Use read-context capabilities for genuinely read-only traversal where suitable.

Await KV mutation promises and surface failures; validate saved JSON at runtime. Keep independent settings in independent keys. Use `Y.Text` or an editor binding for character-level text collaboration instead of replacing a whole string field. Keep editor instances stable and observe shared Yjs structures reactively. Apply user edits through the collaborative model; avoid replacing the whole persisted snapshot on each remote update. Host persistence acknowledgment differs from network acknowledgment; use the supported persistence wait API when a workflow needs durable completion.

For children or lists, each `PluginResource` has its own slot handles. Mount a stable child component for each child's storage hooks. Use `useWorkspaceResourcesMap`, `useWorkspaceChildrenMap`, and semantic read contexts instead of SQL, private tables, backing object keys, or another extension's private namespace.

Use `useFileStorage` for host-mediated file upload, replacement, and download. Its mutation hook currently requires both file permissions. Distinguish available file metadata from uncached/offline bytes. Scoped `createInWorkspace` capabilities support atomic resource/slot creation; avoid assembling host persistence manually.

## Evolve saved content

Resource type ID, schema ID, slot names, and slot kinds are immutable contracts. Add a slot with a schema-version bump; represent a rename or kind change as a new slot plus migration. Supply a pure migration for every adjacent version, validators for all historical versions, and `schema.write(payload, context)` to apply validated migrated data to staged storage. Update initializers for newly created resources and view schema ranges/requirements alongside the migration.

The host stages migration writes and commits with a version compare-and-set; failed, corrupt, or unsupported-newer payloads are quarantined without mutation. Test historical fixtures, already-current data, failed validation, and preservation of original payloads. Extension release versions change for releases; resource schema versions change only when the stored contract changes.
