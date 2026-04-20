# order-manager-contracts

**Source of truth** for the Order Manager platform: AsyncAPI, JSON Schema (CloudEvents + domain payloads), and codegen to **TypeScript** and **Python**.

- **Interfaces**: `docs/interfaces/` — events (`events/`), REST (`api/`), schemas (`schemas/`)
- **Generated consumers**
  - `generated/typescript` — npm package `@guilherme-rauen/order-manager-contracts`
  - `generated/python` — PyPI-style package `order-manager-contracts` (Pydantic v2)
- **Runtimes**: Node **24.x** (`.nvmrc`), Python **3.13** (`.python-version`)

## Toolchain versions (pinned together)

| Tool                      | Version                           | Notes                                                                                |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------------------------ |
| pnpm                      | 10.33.0                           | `packageManager` in root `package.json`                                              |
| `@asyncapi/cli`           | 6.0.0                             | Latest on npm; internally aligns with Spectral **6.15.0**                            |
| `@stoplight/spectral-cli` | **6.15.0**                        | Matches the dependency `@asyncapi/cli@6.0.0` uses — avoids duplicate Spectral copies |
| `tsx`                     | 4.21.0                            | Run TS scripts                                                                       |
| TypeScript                | **5.9.3**                         | Latest **5.x** stable; shared by root scripts and `generated/typescript`             |
| Python                    | ≥3.13 (matches `.python-version`) | `generated/python/pyproject.toml`                                                    |

There is **no** `@asyncapi/ruleset` package on npm. Spectral loads **`spectral:asyncapi`** from `@stoplight/spectral-rulesets` (bundled with `spectral-cli`).

To move to **TypeScript 6.x** later, bump `typescript` in both root (if you add root `tsc`) and `generated/typescript/package.json` together and re-run builds.

## Commands

```bash
pnpm install
pnpm lint                 # Spectral on AsyncAPI
pnpm generate:typescript  # JSON Schema → Zod (under generated/typescript/src/generated/, gitignored)
pnpm generate:python      # JSON Schema → Pydantic (under order_manager_contracts/generated/, gitignored; needs generated/python/.venv)
pnpm generate             # both of the above
pnpm build                # tsc for generated/typescript (run generate:typescript first)
pnpm check                # lint + generate:typescript + build (no Python — fast)
pnpm check:python         # venv, codegen, ruff, mypy
pnpm check:full           # check + check:python (what CI runs)
```

**Plan B (payload-only slice):** codegen targets `docs/interfaces/schemas/order-created.data.yaml`. Generated files are **not committed** (see `.gitignore`); CI runs generators then builds/lints.

**Python locally:** once — `cd generated/python && python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"` — then `pnpm generate:python` or `pnpm check:python` works.
