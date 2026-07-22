# Contributing

Keep every skill lean, self-contained, deterministic where needed, and safe for unknown repositories.

Place skills in `skills/<skill-name>/`. Use lowercase hyphenated names matching the `name` in `SKILL.md`. Keep user-facing repository documentation and tests outside skill packages.

Before submitting:

1. Add or update tests under `tests/<skill_name>/`, using underscores in Python package names.
2. Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests -v`.
3. Run the platform's official validator for every changed skill when available.
4. Confirm no secrets, personal data, machine-specific paths, generated evidence, or unsupported claims entered the repository.
5. Document behavior or generated-layout migrations in the repository changelog.

Skill-specific safety rules still apply. For `build-compliance-isms`, do not submit copyrighted standards text or complete proprietary control inventories. Test identifiers must be fictitious unless distribution is authorized.
