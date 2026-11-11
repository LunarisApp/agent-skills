# Behavioral evaluation scenarios

Run these in isolated scratch projects with the indicated SDK/repository available. Inspect resulting code, build output, and the agent's report. Remote publication and live workspace changes are outside these evaluations.

| Request | Observable success |
| --- | --- |
| Build a standalone unit converter from the community starter. | Explicit launcher, namespaced IDs, no unnecessary content permissions, included styles, passing typecheck/build; no invented resource storage or private imports. |
| Add persistent review cards with a synced boolean setting. | Resource type with initialized KV slot and schema validator, matching view requirements; reopen does not reset content; malformed payload test fails validation. |
| Add a setting slot to a version-1 collaborative resource. | Schema bump and adjacent migration, historical fixture preserved, failure leaves original payload intact; no in-place slot rename or kind change. |
| Add an export larger than 64 MiB while retaining old host support. | Agent checks actual SDK/host capabilities; explicitly handles missing saveChunks and reports incompatible size when fallback cannot work; no false success from optional chaining. |
| Prepare a new marketplace release with unrelated extensions already indexed. | Artifact/runtime metadata and byte hashes match built files; other index entries survive; artifact commit pin precedes index commit when committing is authorized; no remote publication. |
| Add a built-in Kanban view in the app checkout. | Package-owned implementation and lazy descriptor, registry imports descriptor, applicable package and boundary checks pass. |

For every scenario, check that SDK/package/API/protocol numbers are independently resolved from supplied evidence. A source checkout version alone must not be reported as a published-package or deployed-host guarantee.
