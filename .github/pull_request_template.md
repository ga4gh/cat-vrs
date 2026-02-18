## Link to the corresponding Issue

## Summary of the Pull Request

## Pull Request checklist

### Required
- [ ] The title of this Pull Request accurately reflects the scope and content of the linked Issue.
- [ ] The branch passes all pre-commit hooks (Run `pre-commit run --all-files` from the root directory).
- [ ] The branch passes all tests (Run `pytest tests/` from the root directory).

### Required if the schema or examples were contributed to
- [ ] The schema `def/` and `json/` files have been recompiled and committed (Run `cd schema; make all` from the root directory).
- [ ] Tests have been created or updated.
- [ ] Schema changes have been documented (existing files updated or new files created in `docs/source/`).
- [ ] Any new schema definition `.rst` files have been registered in the documentation structure.
- [ ] Documentation has been regenerated and committed (Run `cd docs; make clean watch &` from the root directory to compile documentation).
