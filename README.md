# Cat-VRS

[A terminology and data model for describing categorical variation concepts](https://vrsatile.readthedocs.io/en/latest/catvars/index.html), built on top of the
[GA4GH Variation Representation Specification (VRS)](https://vrs.ga4gh.org).

![image](docs/source/images/cat-vrs-transparent-bg.png)

## Using the schema

The schema is available in the [schema/](./schema/) directory, in both reStructuredText
(RST) and JSON versions. It conforms to JSON Schema Draft 2020-12. For a list of
libraries that support JSON schema, see
[JSONSchema>Implementations](https://json-schema.org/tools).

## Installing for development

Fork the repo at <https://github.com/ga4gh/cat-vrs>.

    git clone --recurse-submodules git@github.com:YOUR_GITHUB_ID/cat-vrs.git
    cd cat-vrs
    make devready
    source venv/3.12/bin/activate

If you already cloned the repo, but forgot to include `--recurse-submodules` you can run:

    git submodule update --init --recursive

## Contributing to the schema

Cat-VRS uses [cat-vrs-source.yaml](./schema/cat-vrs/cat-vrs-source.yaml) as the source
document for JSON Schema.

To create the corresponding def and json files after making changes to the source
document, from the root directory:

    cd schema
    make all

## Contributing to the docs

The Cat-VRS specification documentation is written in reStructuredText and located in
[docs/source](docs/source/). Commits to this repo are built automatically at
<https://vrsatile.readthedocs.io/en/latest/catvars/index.html#>.

To build documentation locally, you must install [entr](https://eradman.com/entrproject/):

    brew install entr

Then from the root directory:

    cd docs
    make clean watch &

Then, open [docs/build/html/index.html](./docs/build/html/index.html). The above make
command should build docs when source changes. (Some types of changes require recleaning and building.)
