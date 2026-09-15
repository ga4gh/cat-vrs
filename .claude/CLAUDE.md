# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

The GA4GH **Categorical Variation Representation Specification (Cat-VRS)** — a **schema +
documentation** repo, not an application. Deliverables are JSON Schema files, generated
`.rst` class docs, and a Sphinx site (https://cat-vrs.readthedocs.io). Built on top of VRS,
which is built on GKM-Core.

## Source-of-truth pipeline (understand this first)

Everything is generated from **`*-source.yaml`**. **Never hand-edit generated artifacts** —
edit the source YAML and regenerate.

- **Sources** (this repo owns two): `schema/cat-vrs/cat-vrs-source.yaml` (the model) and
  `schema/cat-vrs/recipes-source.yaml` (pre-defined categorical variants).
- **Generated:** `schema/cat-vrs/json/*` (split JSON Schema, one file/class, no extension)
  and `schema/cat-vrs/def/*.rst` (per-class doc includes).
- **Generator = the MSP** (metaschema processor): the `ga4gh.gkm.metaschema` pip package
  (renamed from `ga4gh.gks.metaschema`), pinned in `.requirements.txt` (currently
  `== 0.4.5`, PyPI). Its console scripts `source2classes`, `source2splitjs`, `y2t` are
  invoked by `schema/cat-vrs/Makefile`. Not vendored here — see
  [ga4gh/gks-metaschema](https://github.com/ga4gh/gks-metaschema).

Regenerate:
```bash
cd schema && make all        # builds schema/cat-vrs (only dir with a Makefile)
cd schema && make clean      # wipes build/ json/ def/ — regenerate after
```
A **pre-commit hook** (`pre-commit-hooks/update-json-def-files.sh`) runs `make all` and
auto-stages regenerated `json/`+`def/` on commit of any `*-source.yaml`. Run
`pre-commit install`.

## Submodule chain & schema/ layout

```
cat-vrs → submodules/vrs (ga4gh/vrs) → submodules/gkm-core (ga4gh/gkm-core)
```
Cat-VRS imports **both** vrs and gkm-core. Under `schema/`, the imported dirs are **real
folders holding symlinks ONLY to the imported `*-source.yaml` (for `imports:`) and `json/`
(for `$ref` resolution) — never to the submodule's `def/`:**

- `schema/vrs/{vrs-source.yaml, json}` → into `submodules/vrs/schema/vrs/...`
- `schema/gkm-core/{gkm-core-source.yaml, json}` → into the nested gkm-core

**Cat-VRS owns its imported-class docs locally**: `y2t` generates `def/*.rst` for imported
vrs/gkm-core classes into `schema/cat-vrs/def/`, and `schema/cat-vrs/prune.mk` keeps **all**
`def/*` while pruning only stray `json/*`. Docs `.. include::` these via
`docs/source/def/cat-vrs/` — there is **no** `docs/source/def/{vrs,gkm-core}` symlink.

**GOTCHA — keep the `json/` symlinks:** `tests/config.py` resolves imported `$ref`s by
reading `schema/<module>/json/<Class>` straight off disk. Removing `schema/vrs/json` or
`schema/gkm-core/json` breaks tests.

Always clone `--recurse-submodules`, or `make all` can't resolve imports.

## Cross-schema references (`$refCurie`)

The MSP (0.4.x) is strict: a bare `$ref: SomeClass` to another schema is an error. Use
`$refCurie: <namespace>:<Class>` with a matching `namespaces:` entry. In particular
`recipes-source.yaml` references cat-vrs's own classes across files and therefore declares a
`cat-vrs:` namespace and uses `$refCurie: cat-vrs:CategoricalVariant` (etc.). `vrs:` and
`gkm.core:` namespaces likewise back `$refCurie: vrs:...` / `gkm.core:...`. `inherits:` uses
the import alias (`gkm-core:Entity`, `Constraint`).

## 0.4.x convention & the anyOf/oneOf gotcha

- Abstract classes: `abstract: true`, left **open** (no `additionalProperties`/
  `unevaluatedProperties`). Concrete classes: **closed** (processor injects
  `type: object`/closure — drop explicit `type: object` from concrete sources).
- No `extends:`; no `heritableProperties`/`heritableRequired` — use plain
  `properties`/`required` on the base; a subtype just re-declares a narrowed property.
- **anyOf vs oneOf:** VRS deliberately renders its abstract bases (e.g. `vrs:Location`,
  `vrs:Variation`) as **open** subtype unions for third-party extension, so such a base can
  also validate an object of another branch. Any Cat-VRS union that mixes an abstract
  imported base with another object type (e.g. `AdjacencyConstraint.adjoinedElements`:
  `Location` + `MappableConcept`) must use **`anyOf`, not `oneOf`** — otherwise validation
  fails with "matches more than one schema".

## Bumping vrs / gkm-core / the MSP

```bash
git submodule update --remote submodules/vrs      # tracks .gitmodules branch (2.1.1-ballot.2026-09)
git -C submodules/vrs submodule update --init --recursive   # nested gkm-core, from INSIDE vrs
```
- GOTCHA: `--remote` uses the branch in LOCAL `.git/config`, which can be stale — if it
  checks out the wrong commit, reset to the `branch =` in `.gitmodules` and re-sync.
- GOTCHA: running `git submodule update` (no `--remote`) from the superproject reverts vrs to
  the recorded pointer; init the nested gkm-core **from inside vrs** to avoid reverting it.
- After a bump, verify `$id` tokens via the symlinks (`schema/vrs/vrs-source.yaml`,
  `schema/gkm-core/gkm-core-source.yaml`) and regenerate. Retarget the `vrs`/`gkm.core`/
  `cat-vrs` namespace version strings + Cat-VRS `$id` in both source files if versions moved.
- MSP version lives only in `.requirements.txt`; `pip install -r .requirements.txt --pre`.

## Setup

```bash
make devready && source venv/3.12/bin/activate
pre-commit install
```

## Tests

`make test` → `pytest tests/`. One `test_examples()` loops `tests/test_definitions.yaml`,
validating each `examples/yaml/*` against a class (each example is listed once per
definition it should satisfy). **Positive-only** — no negative/"should-reject" cases yet.
When adding an example: add its yaml, a docs page, and a `test_definitions.yaml` entry.

## Docs

Sphinx/rST under `docs/source/`; must build **warning-free** (`cd docs && make html`, or
`make clean watch`). Notes:
- Imported-class stubs live in `docs/source/concepts/imported/*.rst` (label + title +
  `.. include:: ../../def/cat-vrs/<Class>.rst`). VRS stubs carry a note linking the latest
  vrs.ga4gh.org page; **GKM-Core stubs get no such note** (no public spec). Classify by the
  stub's include target, not by guesswork.
- `docs/source/appendices/maturity_model.rst` is a **real file** (not a submodule symlink) so
  this repo owns the `.. _maturity-model:` label.
- `docs/source/rst_epilog` defines substitutions the MSP admonitions need (`|maturity-model|`,
  `|indent|`). Add substitutions here if a build reports one undefined.
- Undefined `:ref:` labels usually mean a referenced imported class lacks a stub — add one.

## CI

- `tests.yml` — `pytest tests/` (checks out `submodules: recursive`).
- `cqa.yaml` — runs pre-commit hooks incl. `update-json-def-files`. **Must** check out
  `submodules: recursive` (else `make all` can't resolve imports), and the hook **skips
  import-only dirs** (`schema/vrs`, `schema/gkm-core` have no Makefile — `make` there errors).

## Versioning & release notes

- Ballot `$id` tokens look like `cat-vrs/1.1.1-ballot.2026-09.1`; deps track the matching
  vrs/gkm-core ballot tokens.
- **Maturity/semver:** a breaking change to a **trial use** class → *minor*; changes to
  **draft** classes or non-breaking changes → *patch*. (e.g. the `oneOf`→`anyOf` above is
  non-breaking + draft → patch.)
- `docs/source/releases/`: the `1.1` page lists sub-releases **most-recent-first**
  (1.1.1 above 1.1.0). Release notes **preview the finalized version** — drop `-ballot.2026-09`
  tokens so they read as they will at release.

## Golden workflow for any schema/docs change

1. Edit the **source YAML** (never generated files).
2. `cd schema && make all`  → regenerates json/def.
3. `make test` (expect all examples to validate) and `cd docs && make html` (expect 0 warnings).
4. Review the diff; commit **source + regenerated json/def together**. Ballot branches PR into `v1`.
