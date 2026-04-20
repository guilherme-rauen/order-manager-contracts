# order-manager-contracts (Python)

Pydantic v2 models generated from `docs/interfaces/schemas/`. Generated files are committed for audit trail.

Install in editable mode for local work:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Regenerate after schema changes:

```bash
# From repo root:
pnpm generate:python
```

## Installing from other repos

Git-based install (no PyPI registry needed for now):

```bash
pip install "order-manager-contracts @ git+https://github.com/guilherme-rauen/order-manager-contracts.git#subdirectory=generated/python"
```

PyPI publish will be added when the Python services (Phase 11+) are under active development.
