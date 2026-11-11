# Packaging and installation

Building, preparing artifacts, publishing, and installing are separate outcomes. Complete local build and validation within the requested scope; perform remote publication or workspace changes only when authorized.

## Build output

Use `defineLunarisPluginConfig` from `/vite`. The build emits normalized `dist/manifest.json`, self-contained IIFE `main.js`, optional `styles.css`, and optional raster icon. Newer SDK builds emit `runtime.json`. The helper enforces imports, registration, asset limits, and release-tag compatibility. Preserve a starter's necessary compatibility configuration until verified against the selected SDK; investigate validation failures before adding global shims or bypassing checks.

Read runtime metadata into the release descriptor. Protocol 6 fallback is for known legacy builds without metadata; never label a newer executable protocol 6 merely to pass an older registry. The inspected executable limit is 10 MiB including inline workers and license notices. Typecheck/build alone do not create `release.json` or `marketplace.json`.

## Official registry tooling

In the extensions repository, inspect `registry/README.md` and script options before running. From its root after building the chosen extension:

```sh
EXTENSION_DIST=extensions/example/dist bun registry/build-artifact.ts
```

Replace `example` with the real package. The tool creates `artifacts/<extension-id>/<version>/release.json` and executable assets. `--check` compares a build with its committed artifact. Existing versions are immutable by default; normally increment the extension release version.

For authorized GitHub publication, commit artifacts first, then run `bun registry/update-marketplace.ts` and commit the index separately. The index descriptor URL contains the full artifact commit SHA. Rewriting/squashing that artifact commit breaks the pin; finalize artifact history before generating the index and regenerate pins after an authorized history rewrite. Push the referenced artifact commit as part of publication.

Replacement releases require explicit replacement intent; inspect the tools' `--overwrite` flow for both artifact and index so descriptor byte length, SHA-256, URL, API, and runtime all change together. Installed clients keep their persisted pins; replacing the index is not a reload mechanism.

## Other marketplaces

Use the SDK `/marketplace` validators and developer publishing guide when packaging without registry tooling. A root schema-version-1 `marketplace.json` indexes extensions and versions; each version pins the exact descriptor URL, byte length, and SHA-256. The descriptor pins scripts, styles, and icons the same way, and includes matching manifest/API/runtime metadata. Asset URLs may be relative to the descriptor. Compute hashes from final bytes, including JSON whitespace/newlines.

Preserve historical versions and unrelated entries when merging an index. Host every descriptor/asset at immutable public HTTPS URLs with correct media types and browser CORS on the index, descriptors, scripts, styles, and icons. A GitHub repository URL resolves its root marketplace; non-GitHub hosts use the complete HTTPS manifest URL.

## Test installation

A Vite preview is useful for isolated UI but supplies no Lunaris storage/authorization runtime. Test a packaged release through a test marketplace and workspace. At the inspected host revision, an eligible organization owner enables **Developer mode** in organization **Settings → General**, adds the repository/manifest under **Marketplaces**, then installs through workspace **Settings → Manage extensions**, reviewing source and permissions through **Trust and install**. Verify current UI if it differs.

Test launcher/resource creation, persisted edits after reopening/restart, relevant two-client collaboration and offline convergence, read-only access, disposal on close/disable, and upgrade of historical payloads. Test browser CORS and Desktop transport for network/export features. Verify the oldest host combination advertised by the manifest. Report installed checks as unverified when no suitable host or authorized test marketplace is available.
