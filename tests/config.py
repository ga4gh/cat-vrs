from pathlib import Path

root_path = Path(__file__).parent.parent
schema_path = root_path / "schema"
catvar_yaml_path = schema_path / "catvars-source.yaml"
catvar_json_path = schema_path / "catvars.json"
catvar_merged_yaml_path = schema_path / "merged.yaml"

test_path = root_path / 'tests'
fixtures_path = test_path / 'fixtures'


def get_schema_ref(schema_file, schema_class, kw="$defs"):
   return {
      "$ref": schema_path.as_uri() + f"/{schema_file}.json#/{kw}/{schema_class}"
   }