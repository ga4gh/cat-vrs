"""
Auto-generate examples/README.md from compiled JSON examples.
Run via the Makefile; do not invoke directly.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def main():
    json_dir = Path("json")
    output_file = Path("README.md")

    if not json_dir.is_dir():
        print(f"Error: '{json_dir}' directory not found.", file=sys.stderr)
        sys.exit(1)

    # Map each constraint type to a sorted list of (name, filename) tuples
    constraint_to_examples = defaultdict(list)

    for json_file in sorted(json_dir.glob("*.json")):
        with json_file.open() as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Warning: could not parse {json_file}: {e}", file=sys.stderr)
                continue

        name = data.get("name")
        constraints = data.get("constraints", [])

        if not name:
            print(f"Warning: no 'name' field in {json_file}, skipping.", file=sys.stderr)
            continue

        for constraint in constraints:
            constraint_type = constraint.get("type")
            if constraint_type:
                constraint_to_examples[constraint_type].append((name, json_file.name))

    # Sort examples within each constraint alphabetically by name
    for constraint_type in constraint_to_examples:
        constraint_to_examples[constraint_type].sort(key=lambda x: x[0])

    # Build Markdown
    lines = [
        "# Examples - Categorical Variant Representation Specification",
        "",
        (
            "This README is automatically generated from the [Makefile](./Makefile) and [an accompanying Python script](./generate_readme.py). "
            "Please edit examples in YAML. "
            "When ready to compile, run the Makefile to generate both the JSON versions and this README. "
            "From this directory:\n"
            "\n"
            "```bash\n"
            ""
            "make all\n"
            "```"
            ""
        ),
        "",
        "## Examples by Constraint",
        "",
        "A Constraint is a rule or set of rules that must be satisfied for a CategoricalVariant to be considered valid. Constraint sub classes are only used in CategoricalVariant objects.",
        "",
        "| Constraint | Representative Example(s) |",
        "| --- | --- |",
    ]

    for constraint_type in sorted(constraint_to_examples):
        examples = constraint_to_examples[constraint_type]
        links = ", ".join(
            f"[{name}](json/{filename})" for name, filename in examples
        )
        lines.append(f"| {constraint_type} | {links} |")

    lines.append("| None | [t(2;15)(q23.1;q25.3)](json/describedVariant-ex1.json) |")
    lines.append("")  # trailing newline

    output_file.write_text("\n".join(lines))
    print(f"Generated {output_file}")


if __name__ == "__main__":
    main()
