# Lunaris Agent Skills

Public collection of standalone agent skills maintained by Lunaris. Each directory under `skills/` is independently usable and contains its own instructions and resources.

## Skills

| Skill | Purpose | Requirements |
|---|---|---|
| [`build-lunaris-extension`](skills/build-lunaris-extension/SKILL.md) | Build and test Lunaris extensions with the public SDK. | Bun, TypeScript/React project, compatible Lunaris host for integration checks |

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
