# Workflow and tracker contract

## State machine

| Stage | Entry condition | Exit condition |
|---|---|---|
| 0 Setup | Skill invoked | Exact ISMS root and source candidates confirmed |
| 1 Scaffold | Location confirmed | New scaffold created or existing system adopted |
| 2 Discovery | Sources explicitly bound | Relevant observations recorded and triaged |
| 3 Services | Service candidates exist | Each service confirmed, verified, or tracked as unknown |
| 4 Documents | Discovery baseline available | Each document reviewed, paused, skipped, or approved |
| 5 Closeout | Document set reviewed | Structural and consistency validation reported |

Update `STATE.md` after every material step with stage, active document, last completed action, next action, blockers, pause state, and date.

## Tracker ownership

- `SOURCES.md`: portable source identity and scan state. Absolute bindings stay in `.isms-local.json`.
- `FRAMEWORKS.md`: authorized framework profile, source, licence confirmation, and verification state. Identifier profile stays in ignored `.isms-framework-profile.json`.
- `STATUS.md`: add document after first user input. Workflow status never overrides formal metadata.
- `TBD.md`: unknown question or value after first relevant review. Keep source and tracker synchronized.
- `ISSUES.md`: sourced confirmed deficiency. Do not record suspicion.
- `SERVICES.md`: all external-service candidates and verification state.
- `SCHEDULE.md`: recurring action only after source document establishes owner and cadence.
- `findings/`: source observations, not policy or evidence.

## Classification decision

1. Is fact unknown or merely suspected? Track as TBD.
2. Is a present deficiency confirmed from source or user? Track as issue.
3. Is it an uncertain event with security impact? Assess in risk register.
4. Is it approved deviation from policy? Track exception.
5. Did audit or incident establish nonconformity? Use corrective action.

Link related records instead of copying conflicting descriptions.

## Resume and pause

On resume, read state and trackers before source documents. Verify local source bindings still exist. If repository commit changed since scan, identify targeted rediscovery before relying on old findings.

If recorded schema version is older than bundled version, run migration dry-run and explain changes. Never silently migrate or rewrite controlled content.

On pause, finish current atomic edit, synchronize trackers, record exact next question or action, and state whether user input blocks progress.

## Approval

Use formal states `draft`, `approved`, and `retired`. Ask approver explicitly. Do not approve when document contradicts current practice or contains blocking unknowns. An open issue is allowed only when document truthfully discloses it and links approved treatment.
