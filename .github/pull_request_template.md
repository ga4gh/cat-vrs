## Link to the corresponding Issue.

## Summary of the Pull Request.

## Pull Request checklist:

### Required
- [ ] Does the title of this Pull Request reference the corresponding Issue?
- [ ] Is the branch validating against pre-commit hooks? Run `pre-commit run --all-files` from the root directory.
- [ ] Is the branch passing tests? Run `pytest tests/` from the root directory.

### If the schema or examples were contributed to:
- [ ] Were the schema `def/` and `json/` files recompiled and committed? Run `cd schema; make all` from the root directory.
- [ ] Have tests been created or updated?
- [ ] Have schema changes been documented (update existing files or create new ones in `docs/source/`)?
- [ ] If new `.rst` files were created, have they been registered in the documentation structure?
- [ ] Has documentation been regenerated and committed? Run `cd docs; make clean watch &` from the root directory to compile documentation.
