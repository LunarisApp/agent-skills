# Build Compliance ISMS

`build-compliance-isms` is an agent skill for building a lean information security management system (ISMS) for a founder-led or small SaaS company pursuing ISO/IEC 27001:2022 with Amendment 1:2024 and SOC 2 Security.

> **Expect substantial human effort.** This skill assists and structures the work; it does not make compliance automatic. The organization must invest time to investigate its actual practices, answer questions, make decisions, review and approve documents, remediate gaps, operate controls, and collect evidence. The amount of work depends on the organization's scope, complexity, and current maturity.

## What it is

The skill is a guided, repository-backed documentation workflow. It helps an agent and a human operator:

- discover current security practices from explicitly approved source repositories;
- scaffold a new ISMS or adopt an existing documentation set without overwriting it;
- inventory external services while distinguishing discovered, confirmed, and verified facts;
- work through governance, risk, policies, procedures, control mappings, and readiness documents one at a time;
- record unknowns, confirmed gaps, decisions, owners, and next actions in resumable trackers;
- validate the structure and internal consistency of the resulting document system; and
- keep claims grounded in observed evidence, user confirmation, or clearly labelled plans.

The bundled `isms.py` helper makes repeatable workspace operations deterministic, while the skill's interview workflow leaves business decisions and approvals with the organization.

## What it is not

The skill is not:

- a replacement for qualified legal, compliance, security, or audit advice;
- an auditor, certification body, or guarantee of ISO 27001 certification or SOC 2 attestation;
- proof that documented controls operate effectively;
- a one-click or autonomous route to compliance;
- a tool for conducting an audit, collecting audit evidence, or creating historical operating records;
- an autonomous compliance program that chooses risk appetite, policy values, owners, deadlines, or approvals for the organization;
- an infrastructure or product automation tool—it does not change systems, deploy controls, or remediate findings unless separately requested and authorized; or
- a source of licensed ISO or AICPA normative text. Framework mappings require organization-authorized identifier sources and professional review.

Its intended stopping point is a truthful, internally consistent ISMS documentation set that is ready for organizational approval and further professional validation.

For agent instructions and guardrails, see [SKILL.md](SKILL.md).
