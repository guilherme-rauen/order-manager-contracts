#!/usr/bin/env python3
"""JSON Schema (YAML) → Pydantic v2 models via datamodel-code-generator.

Resolves $ref across YAML files before generation, so primitives are
inlined from their canonical source (single source of truth).

Processes:
- docs/interfaces/schemas/*.data.yaml → event data models
- docs/interfaces/schemas/primitives/*.yaml → primitive type models
- docs/interfaces/schemas/envelope.yaml → CloudEvents envelope model
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "docs/interfaces/schemas"
PRIMITIVES_DIR = SCHEMAS_DIR / "primitives"
OUT_DIR = ROOT / "generated/python/order_manager_contracts/generated"
VENV_PY = ROOT / "generated/python/.venv/bin/python"


def resolve_python() -> Path:
    env = os.environ.get("PYTHON_BIN")
    if env:
        return Path(env)
    if VENV_PY.exists():
        return VENV_PY
    return Path(sys.executable).resolve()


def to_class_name(kebab: str) -> str:
    return "".join(word.capitalize() for word in kebab.split("-"))


def to_snake(kebab: str) -> str:
    return kebab.replace("-", "_")


def resolve_refs(schema_path: Path) -> dict:
    """Recursively resolve $ref pointers in a YAML schema to produce a self-contained dict."""
    import yaml  # type: ignore[import-untyped]

    with schema_path.open() as f:
        schema = yaml.safe_load(f)

    def _resolve(obj: object, base_dir: Path) -> object:
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref_path = base_dir / obj["$ref"]
                with ref_path.open() as rf:
                    resolved = yaml.safe_load(rf)
                # Remove meta keys from inlined ref
                resolved.pop("$schema", None)
                resolved.pop("$id", None)
                return _resolve(resolved, ref_path.parent)
            return {k: _resolve(v, base_dir) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_resolve(item, base_dir) for item in obj]
        return obj

    resolved = _resolve(schema, schema_path.parent)
    if isinstance(resolved, dict):
        return resolved
    msg = f"Schema at {schema_path} did not resolve to a dict"
    raise TypeError(msg)


def generate_model(
    py: Path,
    schema_path: Path,
    out_file: Path,
    class_name: str,
) -> None:
    # Resolve $ref and write a temporary self-contained JSON file
    resolved = resolve_refs(schema_path)
    resolved.pop("$schema", None)
    resolved.pop("$id", None)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False,
    ) as tmp:
        json.dump(resolved, tmp)
        tmp_path = tmp.name

    try:
        header = f"# Auto-generated from {schema_path.name} — do not edit."
        cmd = [
            str(py),
            "-m",
            "datamodel_code_generator",
            "--input",
            tmp_path,
            "--input-file-type",
            "jsonschema",
            "--output",
            str(out_file),
            "--output-model-type",
            "pydantic_v2.BaseModel",
            "--snake-case-field",
            "--use-annotated",
            "--use-standard-collections",
            "--target-python-version",
            "3.13",
            "--disable-timestamp",
            "--custom-file-header",
            header,
            "--use-title-as-name",
            "--class-name",
            class_name,
        ]
        print("[generate:python]", " ".join(cmd))
        subprocess.check_call(cmd, cwd=str(ROOT))
        print(f"[generate:python] wrote {out_file}")
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def main() -> None:
    py = resolve_python()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "__init__.py").write_text(
        '"""Codegen output — do not edit."""\n',
        encoding="utf-8",
    )

    # 1. Envelope
    generate_model(
        py,
        SCHEMAS_DIR / "envelope.yaml",
        OUT_DIR / "envelope.py",
        "Envelope",
    )

    # 2. Event data schemas (*.data.yaml)
    for schema_file in sorted(SCHEMAS_DIR.glob("*.data.yaml")):
        base_name = schema_file.name.removesuffix(".data.yaml")
        class_name = to_class_name(base_name) + "Data"
        out_file = OUT_DIR / f"{to_snake(base_name)}_data.py"
        generate_model(py, schema_file, out_file, class_name)

    # 3. Primitive schemas
    for schema_file in sorted(PRIMITIVES_DIR.glob("*.yaml")):
        base_name = schema_file.name.removesuffix(".yaml")
        class_name = to_class_name(base_name)
        out_file = OUT_DIR / f"{to_snake(base_name)}.py"
        generate_model(py, schema_file, out_file, class_name)

    print("[generate:python] done")


if __name__ == "__main__":
    main()
