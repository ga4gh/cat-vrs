from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
catvar_yaml_path = schema_dir / "catvars-source.yaml"
catvar_json_path = schema_dir / "catvars.json"
catvar_merged_yaml_path = schema_dir / "merged.yaml"

