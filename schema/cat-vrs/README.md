# Adding Standalone examples into `examples-source.yaml`
[![Read the Docs](https://img.shields.io/readthedocs/vr-spec/1.1)](https://cat-vrs.readthedocs.io/en/latest/)


## Rationale

Prior [to issue #133](https://github.com/ga4gh/cat-vrs/issues/133), Cat-VRS examples were standalone `.yaml` files in the `../../examples directory`.

In order to integrate the examples into the existing `.yaml` to `.JSON` pipeline via the Meta-Schema Processor (MSP) and in turn incorporate JSON examples into [the support documentation](https://cat-vrs.readthedocs.io/en/latest/) for Cat-VRS, it was decided to instead relocate these examples into a single `examples-source.yaml` file in this current directory.


## How-To

When a `make` command is executed, the MSP searches for files with a `-source.yaml` tail, and then parses out the yaml into `.rst` and `.JSON` files in the `def` and `json` directories, respectively.  Therefore, if it sees a new `-source.yaml` file for the examples complete with the expected metadata, it will parse out each example into JSON representations, and write the respective files.

We created an `examples-source.yaml` file, headed with the following metadata, adapted from `recipes-source.yaml`.

    $schema: "https://json-schema.org/draft/2020-12/schema"
    $id: "https://w3id.org/ga4gh/schema/cat-vrs/1.0.0/examples-source.yaml"
    title: GA4GH-Cat-VRS-examples
    type: object

    imports:
      cat-vrs: ./cat-vrs-source.yaml

    namespaces:
      gks.core: /ga4gh/schema/gks-core/1.0.0/json/
      vrs: /ga4gh/schema/vrs/2.0.1/json/

    $defs:

The yaml contents of existing examples could then be copied into this new `examples-source.yaml` file, indented to nest the example under `$defs:`.  In order for each example to be interpreted correctly by the MSP, some additional metadata must be prepended for each example.

First, a name must be created for the example, under which the rest of the example yaml code is nested:

    canonicalAllele-ex1:
        [rest of example yaml code]

Second, the MSP expects data classes and recipes to specify a maturity status and description:

    canonicalAllele-ex1:
        maturity: [status]
        description: >-
            [a description]
        [rest of example yaml code]

With this additional information, the MSP correctly reads in the examples and generates appropriate .JSON for each example.
