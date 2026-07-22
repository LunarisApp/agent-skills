# External-service verification

## Inventory fields

For each service, determine purpose, owner, data categories, account ownership, sign-in and recovery, actual plan, regions, relevant capabilities/defaults, data retention, subprocessor role, contract/DPA status, source, verification date, and fact state.

## Fact states

- `discovered`: repository or public-product evidence suggests service use.
- `confirmed`: organization confirms service, purpose, account, or configuration.
- `verified`: current primary documentation or actual-plan information supports claim.

Do not upgrade `discovered` to `confirmed` by inference. Do not upgrade `confirmed` to `verified` without source.

## Plan-tier rule

Never assume feature availability from another tier, general marketing page, industry convention, or memory. Ask user for exact plan. Verify against plan-specific documentation where public. For dashboard-only facts, ask user to report configuration or provide a safe redacted source; never request credentials.

Distinguish:

- service default from organization-selected policy target;
- available capability from enabled capability;
- contracted term from marketing statement;
- global edge presence from data-storage region;
- supplier retention from organization deletion workflow.

## Triage

Unknown service or plan fact becomes TBD. Confirmed missing MFA, personal account dependency, disclosure mismatch, unsupported region claim, missing contract, or unavailable required capability becomes issue only after user or source confirmation. Link material supplier exposure to risk assessment.
