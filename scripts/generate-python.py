#!/usr/bin/env python3
"""JSON Schema (YAML) → Pydantic v2 models via datamodel-code-generator."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# Repo root: .../scripts/thisfile.py -> parents[1] == repo
ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "docs/interfaces/schemas/order-created.data.yaml"
OUT_DIR = ROOT / "generated/python/order_manager_contracts/generated"
OUT_FILE = OUT_DIR / "order_created_data.py"
VENV_PY = ROOT / "generated/python/.venv/bin/python"


def resolve_python() -> Path:
    env = os.environ.get("PYTHON_BIN")
    if env:
        return Path(env)
    # Do not .resolve() the venv shim — it points at system Python and loses site-packages.
    if VENV_PY.exists():
        return VENV_PY
    return Path(sys.executable).resolve()


def main() -> None:
    py = resolve_python()
    if not SCHEMA.is_file():
        print(f"[generate:python] missing schema: {SCHEMA}", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "__init__.py").write_text(
        '"""Codegen output — do not edit."""\n',
        encoding="utf-8",
    )

    cmd = [
        str(py),
        "-m",
        "datamodel_code_generator",
        "--input",
        str(SCHEMA),
        "--input-file-type",
        "jsonschema",
        "--output",
        str(OUT_FILE),
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--snake-case-field",
        "--use-annotated",
        "--use-standard-collections",
        "--target-python-version",
        "3.13",
        "--class-name",
        "OrderCreatedData",
    ]
    print("[generate:python]", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(ROOT))
    print("[generate:python] wrote", OUT_FILE)


if __name__ == "__main__":
    main()
