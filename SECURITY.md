# Security

## Supported versions

Security fixes target the latest version of each skill on the default branch. Pre-1.0 interfaces may change with migration support where safe.

## Report a vulnerability

Use GitHub private vulnerability reporting for public repository. Do not disclose exploit details, secrets, personal data, or affected customer data in a public issue.

## Skill threat models

Each skill must document material risks and mitigations in its instructions or references. Review bundled scripts before execution and grant only access required for the task.

`build-compliance-isms` has these primary risks:

Primary risks:

- Prompt injection or malicious instructions inside scanned repositories.
- Secret or personal-data disclosure during discovery.
- Traversal outside confirmed roots through paths or symlinks.
- Accidental commit of absolute paths or licensed framework data.
- False assurance from invented facts, template text, or passing validation.
- Unintended overwrites or scope expansion.

Mitigations include explicit confirmations, read-only preflights, symlink avoidance, relative exclusion validation, secret-safe output, strict identifier-only framework profiles, Git ignore checks, no overwrite behavior, tracker reconciliation, and explicit limits on assurance claims.

## Operator responsibility

Review skill actions and generated changes before commit. Use a least-privileged execution environment. For compliance work, keep sensitive evidence outside repositories, obtain required licences and professional legal or audit advice, and never treat validation as audit evidence or certification.
