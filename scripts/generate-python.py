#!/usr/bin/env python3
"""JSON Schema (YAML) → Pydantic v2 models via datamodel-code-generator.

Processes:
- docs/interfaces/schemas/*.data.yaml → event data models
- docs/interfaces/schemas/primitives/*.yaml → primitive type models
- docs/interfaces/schemas/envelope.yaml → CloudEvents envelope model
"""

from __future__ import annotations

import os
import subprocess
import sys
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


def generate_model(
    py: Path,
    schema_path: Path,
    out_file: Path,
    class_name: str,
) -> None:
    cmd = [
        str(py),
        "-m",
        "datamodel_code_generator",
        "--input",
        str(schema_path),
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
        "--class-name",
        class_name,
    ]
    print("[generate:python]", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(ROOT))
    print(f"[generate:python] wrote {out_file}")


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
