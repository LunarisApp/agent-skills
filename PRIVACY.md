# Privacy

This repository contains agent instructions and bundled resources. Review each skill before use. Agent-platform processing remains governed by the user's chosen product, configuration, and terms.

Skills must document network access, telemetry, credential use, or sensitive-data handling they introduce. Current `build-compliance-isms` script runs locally and contains no telemetry or network client. It does not send repository or ISMS data to a service by itself.

Discovery reads explicitly confirmed Git repositories. Generated findings may contain repository name, sanitized remote, branch, commit ID, dirty-state indicator, dependency names, manifest names, relative paths, and inferred service candidates.

That skill intentionally excludes common dependency, cache, build, binary, and generated directories; does not follow symlinks; enforces file and package-manifest size limits; and instructs agents not to deliberately inspect or record secret values, customer content, personal data, contracts, screenshots, database exports, or credentials. User-defined exclusions can further reduce scope.

Absolute source paths and authorized framework profile stay in `.isms-local.json` and `.isms-framework-profile.json`, both gitignored. Validate ignore status before committing. Review all findings and trackers for organizationally sensitive metadata.

Removing local files does not erase committed Git history, Codex conversation history, external backups, or previously exported data.
