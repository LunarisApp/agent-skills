# Validation levels

## Scaffold

Require complete document inventory, metadata, unique IDs, local links, ignored local state, and no reference-company or machine-specific content. If an organization-authorized framework profile is bound, require exact identifier agreement between profile, SoA, and crosswalk. Without one, report detailed coverage as unavailable; approval validation must fail.

Scaffold placeholders are allowed. Empty trackers are expected.

## Review

Apply scaffold checks plus tracker synchronization. `STATUS.md` counts must match open TBDs and issues for each visited document. Verify source bindings, exclusions, current repository availability, service fact state, schedule semantics, and local-state schema.

Warnings identify stale discovery commits or missing local bindings. Refresh or explicitly defer them before relying on findings.

## Approval

Apply review checks plus approved formal status for scaffolded controlled documents and material source, service, issue, schedule, and framework records. Workflow state, visited status, TBD working tracker, discovery findings, and records index do not require approval. Require no unresolved plain-value TBDs, no blocking tracker items, and owner/disposition for every issue. Verify disclosed open issues link to approved treatment.

## Manual consistency review

Compare scope, source list, system description, assets, data flows, services, regions, roles, risk, treatment, SoA, crosswalk, policies, procedures, schedules, and evidence expectations. Resolve contradictions; automated checks cannot establish legal sufficiency, control operation, or certification readiness.

Never interpret a passing validator as audit evidence or assurance opinion.
