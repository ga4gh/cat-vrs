# Documentation Workflow Migration Plan

**Goal:** Let content developers focus on writing — not ReST syntax or build issues.

**Base branch:** `v1` (development)
**Date:** 2026-06-07

---

## Summary of Changes

| Step | What | Effort | Impact |
|------|------|--------|--------|
| 1 | Add `sphinx-autobuild` for live preview | Small | High |
| 2 | Add doc build check to CI | Small | Medium |
| 3 | Migrate RST to MyST Markdown | Medium | High |
| 4 | Add prose linting with Vale (optional) | Small-Medium | Medium |

---

## Current State (v1 branch)

- **74 hand-authored RST files** across `docs/source/`
- Sphinx 8.1.3 with `sphinx-rtd-theme` 3.0.2 and `sphinx_toolbox` 3.9.0
- Python 3.12 (both RTD and CI)
- Single requirements file: `.requirements.txt` (used by both RTD and local dev)
- `conf.py` already excludes `def/**` (generated schema definition files)
- CI: `cqa.yaml` (pre-commit hooks including `update-json-def-files` and
  `update-example-files`) + `tests.yml` (pytest) — but no doc build check
- Local preview: `make watch` uses `entr` (no browser live-reload)

### RST file breakdown

| Directory | Count | Description |
|-----------|-------|-------------|
| `docs/source/` (top-level) | 6 | index, introduction, how_cat_vrs_works, getting_involved, quickstart |
| `docs/source/concepts/` | 3 | CategoricalVariant, Constraint, additional |
| `docs/source/concepts/Constraints/` | 8 | 7 constraint types + index |
| `docs/source/concepts/Recipes/` | 6 | 5 recipe types + index |
| `docs/source/concepts/imported/` | 24 | VRS/gks-core imported concepts + index |
| `docs/source/examples/` | 18 | Example walkthroughs + index |
| `docs/source/impl-guide/` | 1 | index |
| `docs/source/releases/` | 2 | 1.0 release notes + index |
| `docs/source/appendices/` | 4 | design decisions, hyperintensional, roadmap + index |
| **Total** | **74** | |

---

## Step 1: Add `sphinx-autobuild` for Live Preview

**Problem:** The current `make watch` target uses `entr` (which must be installed
separately) and does not auto-refresh the browser. Content developers must
manually reload after every change.

**Solution:** Replace with `sphinx-autobuild`, which watches source files and
serves a live-reloading local site.

### Changes

**`.requirements.txt`** — add to the ReadtheDocs section:
```
sphinx-autobuild
```

**`docs/Makefile`** — replace the `watch` target:
```makefile
# Replace:
#   watch:
#       while true; do find "$(SOURCEDIR)" -name \*.rst | entr -dn make html; done

# With:
livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
```

### Usage

```bash
cd docs
make livehtml
# Open http://127.0.0.1:8000 — auto-refreshes on save
```

---

## Step 2: Add Doc Build Check to CI

**Problem:** Neither `cqa.yaml` nor `tests.yml` builds the docs. Broken
cross-references, bad directives, or syntax errors are only caught when
ReadTheDocs builds — often after merge.

**Solution:** Add a `docs` job to CI that runs `sphinx-build -W` (warnings as
errors).

### Changes

**`.github/workflows/docs.yml`** — new file:
```yaml
name: docs

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r .requirements.txt

      - name: Build docs (warnings as errors)
        run: |
          sphinx-build -W -b html docs/source docs/build/html
```

### What this catches

- Broken cross-references (`:ref:`, `:doc:`, etc.)
- Malformed directives or roles
- Missing included files
- Duplicate labels
- Any Sphinx warning that would otherwise be silently ignored

---

## Step 3: Migrate RST to MyST Markdown

**Problem:** ReST syntax is unfamiliar to most content developers. Headings use
underline characters (`====`), cross-references use `` :ref:`label` ``, links
use ```Link text <url>`__`` , and directives use `.. directive::`. This is a
constant source of build errors and slows down content work.

**Solution:** Use [MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/),
a Markdown superset for Sphinx. Content developers write familiar Markdown while
retaining full Sphinx power.

### 3a. Install and configure MyST

**`.requirements.txt`** — add to the ReadtheDocs section:
```
myst-parser
```

**`docs/source/conf.py`** — update extensions:
```python
extensions = ["sphinx.ext.todo", "sphinx_toolbox.collapse", "myst_parser"]
```

Add MyST configuration:
```python
# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",      # ::: directive syntax (alternative to ```)
    "deflist",          # definition lists
    "substitution",     # |substitution| support
    "fieldlist",        # field lists
]
# Allow both .rst and .md source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst',
}
```

Update `exclude_patterns` to exclude this plan file:
```python
exclude_patterns = ["def/**", "MIGRATION_PLAN.md"]
```

### 3b. Convert RST files to Markdown

Use the `rst-to-myst` tool for automated conversion:

```bash
pip install rst-to-myst

# Convert all hand-authored RST files (74 total)
find docs/source -name '*.rst' | while read f; do
    rst2myst convert "$f"
done
```

**Files to convert (74 total across these directories):**

- `docs/source/*.rst` — 6 top-level pages
- `docs/source/concepts/*.rst` — 3 concept pages
- `docs/source/concepts/Constraints/*.rst` — 8 constraint pages
- `docs/source/concepts/Recipes/*.rst` — 6 recipe pages
- `docs/source/concepts/imported/*.rst` — 24 imported concept pages
- `docs/source/examples/*.rst` — 18 example pages
- `docs/source/impl-guide/*.rst` — 1 page
- `docs/source/releases/*.rst` — 2 pages
- `docs/source/appendices/*.rst` — 4 pages

**Post-conversion manual review checklist:**

- [ ] Toctree directives converted correctly
- [ ] Cross-references (`:ref:`, `:doc:`) work
- [ ] Image directives render properly
- [ ] Tables render correctly
- [ ] `.. todo::` directives converted to `` ```{todo} `` blocks
- [ ] `.. collapse::` blocks converted correctly
- [ ] `.. include::` directives for `def/` files still work
- [ ] Example pages with code blocks render correctly
- [ ] CI doc build (step 2) passes with zero warnings

### 3c. Migrate `rst_epilog` substitutions

The current `docs/source/rst_epilog` file defines RST link targets and
substitutions. These need to be converted to MyST equivalents.

**Current content:**
```rst
.. _civic: https://civicdb.org/
.. _clingen allele registry: http://reg.clinicalgenome.org/...
.. _clinvar: https://www.ncbi.nlm.nih.gov/clinvar/
.. _dbsnp: https://www.ncbi.nlm.nih.gov/snp/
.. _hgvs: https://varnomen.hgvs.org/
.. _VRS Variation: https://vrs.ga4gh.org/en/latest/...
.. _VRS SequenceLocation: https://vrs.ga4gh.org/en/latest/...

.. |catvrs_discussion| replace:: `Cat-VRS Discussion <...>`__
.. |catvrs| replace:: `Cat-VRS <...>`__
.. |catvrs_yaml| replace:: `Cat-VRS YAML <...>`__
.. |recipes_yaml| replace:: `Cat-VRS Recipes YAML <...>`__
.. |catvrs_json| replace:: `Cat-VRS JSON <...>`__

.. |eg| replace:: *e.g.,*
.. |ie| replace:: *i.e.,*
```

**MyST approach — use `myst_substitutions` in `conf.py`:**
```python
myst_substitutions = {
    "catvrs_discussion": "[Cat-VRS Discussion](https://github.com/ga4gh/cat-vrs/discussions)",
    "catvrs": "[Cat-VRS](https://cat-vrs.readthedocs.io/en/latest/)",
    "catvrs_yaml": "[Cat-VRS YAML](https://github.com/ga4gh/cat-vrs/tree/1.0/schema/cat-vrs/cat-vrs-source.yaml)",
    "recipes_yaml": "[Cat-VRS Recipes YAML](https://github.com/ga4gh/cat-vrs/tree/1.0/schema/cat-vrs/recipes-source.yaml)",
    "catvrs_json": "[Cat-VRS JSON](https://github.com/ga4gh/cat-vrs/tree/1.0/schema/cat-vrs/json)",
    "eg": "*e.g.,*",
    "ie": "*i.e.,*",
}
```

Note: The named link targets (`.. _civic:` etc.) don't have a direct MyST
`rst_epilog` equivalent. Options:
1. Keep `rst_epilog` — it still works for `.md` files when MyST is configured
2. Convert them to regular inline Markdown links in the files that use them
3. Define them in a shared `links.md` file included via `myst_substitutions`

**Recommendation:** Start with option 1 (keep `rst_epilog` working alongside
MyST) then clean up later. Sphinx's `rst_epilog` applies to MyST files too when
using `myst_parser`.

### 3d. Update `sphinx-autobuild` watch patterns

After migration, `sphinx-autobuild` watches `.md` files by default — verify this
works.

### 3e. Coexistence with generated RST

The schema build (`y2t` via `ga4gh.gks.metaschema`) generates `.rst` definition
files in the `def/` directory. These remain as RST — `conf.py` already excludes
them from direct processing via `exclude_patterns = ["def/**"]` but they are
still available for `.. include::` directives. Sphinx handles mixed `.rst` + `.md`
projects natively. Only hand-authored content files need to be Markdown.

---

## Step 4: Prose Linting with Vale (Optional)

**Problem:** Inconsistent terminology, passive voice, and style drift across 74+
content files. Especially important for a GA4GH specification where precise
language matters.

**Solution:** Add [Vale](https://vale.sh/) for automated prose quality checks.

### Changes

**`.vale.ini`** — new file at repo root:
```ini
StylesPath = .vale/styles
MinAlertLevel = suggestion

Packages = Google, write-good

[docs/source/*.md]
BasedOnStyles = Vale, Google, write-good

[docs/source/*.rst]
BasedOnStyles = Vale, Google, write-good
```

**`.github/workflows/cqa.yaml`** — add a Vale job:
```yaml
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: errata-ai/vale-action@v2
        with:
          files: docs/source/
```

**Custom vocabulary:** Create `.vale/styles/config/vocabularies/CatVRS/accept.txt`
with project-specific terms (Cat-VRS, GA4GH, CatVar, VRS, allele, etc.) so Vale
doesn't flag them.

---

## Quick-Reference: What Changes Where

| File | Steps |
|------|-------|
| `.requirements.txt` | 1, 3a |
| `docs/Makefile` | 1 |
| `docs/source/conf.py` | 3a, 3c |
| `docs/source/*.rst` (74 files) | 3b (convert to `.md`) |
| `docs/source/rst_epilog` | 3c (keep or migrate) |
| `.github/workflows/docs.yml` | 2 (new) |
| `.vale.ini` | 4 (new, optional) |

---

## Recommended Order of Execution

1. **Step 1 (sphinx-autobuild)** — immediate quality-of-life improvement, no risk
2. **Step 2 (CI doc build)** — catches current RST issues before migration
3. **Step 3 (MyST migration)** — the main event; do on a dedicated branch
   - 3a: Install and configure (quick)
   - 3b: Batch-convert files with `rst-to-myst` (automated)
   - 3c: Migrate epilog substitutions
   - 3d-3e: Verify and clean up
4. **Step 4 (Vale)** — add after migration stabilizes

Steps 1 and 2 can be done in parallel as independent PRs. Step 3 should be its
own branch and PR. Step 4 can follow at any time.

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| `rst-to-myst` doesn't convert all directives perfectly | Manual review checklist in step 3b; CI doc build (step 2) catches errors |
| `sphinx_toolbox.collapse` may not work in MyST | Test early; MyST supports `{directive}` syntax for all Sphinx directives |
| `rst_epilog` substitutions don't work in `.md` files | MyST parser does support `rst_epilog`; test and fall back to `myst_substitutions` |
| `.. include::` of `def/*.rst` files from `.md` pages | MyST supports `{include}` directive; test with generated def files |
| ReadTheDocs build differs from local build | CI step 2 mirrors the RTD build; uses same `.requirements.txt` and Python 3.12 |
| Other GA4GH repos reference specific `.rst` URLs | RTD redirects can handle old URLs; or keep URL paths the same (MyST files can use the same names) |

---

## Syntax Cheat Sheet for Content Developers (Post-Migration)

| What | RST (before) | MyST Markdown (after) |
|------|--------------|----------------------|
| Heading | `Title\n=====` | `# Title` |
| Bold | `**bold**` | `**bold**` |
| Italic | `*italic*` | `*italic*` |
| Link | `` `text <url>`__ `` | `[text](url)` |
| Cross-ref | `` :doc:`path` `` | `` {doc}`path` `` |
| Image | `.. image:: path` | `![alt](path)` or `` ```{image} path `` |
| Directive | `.. note::` | `` ```{note} `` |
| Toctree | `.. toctree::` | `` ```{toctree} `` |
| Substitution | `\|name\|` | `{{name}}` |
| Code block | `.. code-block:: json` | ` ```json ` |
| TODO | `.. todo::` | `` ```{todo} `` |
| Collapse | `.. collapse:: title` | `` ```{collapse} title `` |
| Include | `.. include:: path` | `` ```{include} path `` |
