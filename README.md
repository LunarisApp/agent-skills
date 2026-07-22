# Lunaris Agent Skills

Public collection of standalone agent skills maintained by Lunaris. Each directory under `skills/` is independently usable and contains its own instructions and resources.

## Skills

| Skill | Purpose | Requirements |
|---|---|---|
| [`build-compliance-isms`](skills/build-compliance-isms/SKILL.md) | Build or resume a lean ISO 27001 and SOC 2 Security documentation program. | Python 3.10+, Git |

## Installation

Copy or install only the desired directory under `skills/` using the skill mechanism supported by your agent. Keep the directory name unchanged.

Example invocation:

```text
Use $build-compliance-isms to start or continue my ISMS documentation program.
```

Review each skill before use. Skills can inspect repositories, execute bundled scripts, or create files when their documented workflow and user authorization allow it.

## Development

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

Run the agent platform's official skill validator for every changed skill when available.

## Privacy

See [PRIVACY.md](PRIVACY.md). Individual skills may add stricter handling requirements.

## Licence

Repository content is licensed under [Apache License 2.0](LICENSE) unless a file states otherwise. See [CHANGELOG.md](CHANGELOG.md) and [SECURITY.md](SECURITY.md).
