#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${ROOT}/generated/python"
cd "${PY}"

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck source=/dev/null
source .venv/bin/activate

python -m pip install -q -U pip
python -m pip install -q -e ".[dev]"

cd "${ROOT}"
python scripts/generate-python.py

# Codegen drift check — generated Python files must be committed
git diff --exit-code -- generated/python/order_manager_contracts/generated/ || {
  echo "::error::Python generated files out of date. Run 'pnpm generate:python' and commit." >&2
  exit 1
}

cd "${PY}"
python -m ruff check order_manager_contracts
python -m mypy order_manager_contracts
