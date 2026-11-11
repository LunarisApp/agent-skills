---
name: build-lunaris-extension
description: Build, modify, or troubleshoot Lunaris extensions using the public TypeScript/React SDK, including resource storage, sandbox integration, and marketplace packaging. Use for community extensions and bundled Lunaris resource views or tools.
---

# Build Lunaris extensions

Deliver an extension that builds against its selected SDK and works in its intended Lunaris host. Implement in the user's extension project; use the Lunaris and extensions repositories as references unless host changes are requested.

## Establish the contract

Locate the target project's instructions, package scripts, lockfile, manifest, and entry point. Locate available Lunaris SDK source and the separate extensions repository using [source map](references/source-map.md). Read the installed SDK exports/types for exact signatures; local source, starter docs, and published packages may represent different releases.

Choose the integration from the requested behavior:

- **Standalone tool:** register a standalone view with an explicit `target.launcher` when users should open it from navigation. Use declared workspace KV if it needs workspace preferences.
- **Persistent content:** define a resource type and a resource view. Read [resources and storage](references/resources.md) before implementing persistence or migrations.
- **Another view of existing content:** target its resource type/schema and declare only the storage slots the view consumes.
- **Bundled extension:** follow the app's `extensions/AGENTS.md`, package/descriptor conventions, and local registry. Read the bundled section in [source map](references/source-map.md).

Keep SDK package version, manifest host `api` range, sandbox protocol, extension release version, and resource schema version separate. Confirm the selected SDK is available and the target host supports its emitted protocol. Preserve an existing project's compatible baseline unless the requested feature needs an upgrade.

## Scaffold or extend

For a new community project, use `@lunarisapp/create-extension` in a new or empty directory, or copy the checked-out extensions repository's `template/`. Inspect the generated files before adapting them. Update manifest identity, package metadata, and contribution IDs together. Use the user's namespace; preserve existing IDs when modifying an extension.

The manifest holds identity, discovery metadata, API compatibility, permissions, and dependency/conflict ranges. Register behavior in the default-exported `definePlugin({ manifest, activate })`. Unknown manifest fields are rejected. Keep contribution IDs within the manifest namespace. Dependency ranges refer to extension release versions; service contract versions are separate.

Register contributions during activation; registration closes when activation returns. Put activation side effects in `effects.add` so they start after the atomic registration commit, and supply cleanup for subscriptions or other persistent effects.

Import public SDK entry points, `@lunarisapp/ui` exports, local files, and declared third-party dependencies. Keep private `/internal`, host `/sandbox`, and `@repo/*` imports out of extension implementations. Use shared public contracts for integrations with other extensions.

## Implement the feature

Use [host capabilities](references/host-capabilities.md) when adding commands, search, collaboration presence, network access, downloads, workers, services, or locales. Verify capability signatures and permission checks against the selected SDK.

Community extensions run in opaque-origin iframes. Build through `defineLunarisPluginConfig` from `@lunarisapp/plugin-sdk/vite`; include CSS in the extension bundle. Host DOM, host translation providers, origin storage, and direct network access are unavailable. Keep browser-only initialization inside render/effect lifecycles so build-time registration validation can run.

Implement loading, empty, failure, and read-only behavior using host capability state. Keep local content usable when optional network services fail. Use keyboard-operable controls and layouts that fit narrow panes.

## Verify and deliver

Run the project's typecheck, relevant behavior tests, and build. Use the SDK's `preparePluginActivation` for lifecycle/registration tests when appropriate; registrar mocks alone miss host validation. For stored data changes, test historical payloads and failed migrations. Run applicable bundled registry/import-boundary checks for app extensions.

Inspect build output and runtime metadata. A successful build proves packaging and registration, not host persistence or collaboration. Exercise the packaged artifact in a test workspace when host access is available: open/create, edit and reopen, read-only access, relevant offline/collaboration behavior, disposal, and upgrade from a prior schema. Report any installed-host checks that could not run.

For artifact packaging, test marketplace installation, or release work, read [packaging and installation](references/release.md). Creating a skill or building an extension does not itself authorize publishing a marketplace or changing a live workspace.

Finish with the implementation location, selected compatibility, checks performed, and the next concrete install/run step. State any SDK or host limitation that prevents the requested behavior.
