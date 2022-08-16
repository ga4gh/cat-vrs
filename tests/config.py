from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
vod_yaml_path = schema_dir / "vod-source.yaml"
vod_json_path = schema_dir / "vod.json"
vod_merged_yaml_path = schema_dir / "merged.yaml"

