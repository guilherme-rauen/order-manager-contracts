# order-manager-contracts

**Source of truth** for the Order Manager platform: AsyncAPI, JSON Schema (CloudEvents + domain payloads), and codegen to **TypeScript** and **Python**.

- **Interfaces**: `docs/interfaces/` — events (`events/`), REST (`api/`), schemas (`schemas/`)
- **Generated consumers** (committed to git for audit trail)
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
pnpm lint                 # ESLint on scripts/ + Spectral on AsyncAPI
pnpm format:check         # Prettier check
pnpm generate:typescript  # JSON Schema → Zod (generated/typescript/src/generated/, committed)
pnpm generate:python      # JSON Schema → Pydantic (order_manager_contracts/generated/, committed)
pnpm generate             # both of the above
pnpm build                # tsc for generated/typescript (run generate:typescript first)
pnpm check                # lint + generate:typescript + build (no Python — fast)
pnpm check:python         # venv, codegen, drift check, ruff, mypy
pnpm check:full           # check + check:python (what CI runs)
```

**Generated code is committed** for audit trail and to support `git blame` on cross-service contracts. CI runs a drift check (`git diff --exit-code -- generated/`) to verify committed output matches what codegen produces.

**Python locally:** once — `cd generated/python && python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"` — then `pnpm generate:python` or `pnpm check:python` works.
