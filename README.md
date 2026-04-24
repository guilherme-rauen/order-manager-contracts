# order-manager-contracts

![](https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif)

---

# Overview

The `order-manager-contracts` repository is the **source of truth** for all Order Manager platform contracts: AsyncAPI event definitions, OpenAPI REST definitions, and JSON Schemas that drive the generated TypeScript (Zod + types) and Python (Pydantic v2) consumer packages. It centralizes contract evolution, enforces CloudEvents-compatible envelopes, and keeps generated artifacts versioned for cross-service auditability. For instructions on how to use this repository locally, please refer to the [_`Getting Started`_](#getting-started) section.

## Interface Artifacts Overview

| Artifact           | Path                                   | Description                                                                                                                                                      |
| ------------------ | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AsyncAPI           | `docs/interfaces/events/asyncapi.yaml` | Root event catalog — split per-domain (`asyncapi_order.yaml`, `asyncapi_payment.yaml`, `asyncapi_shipment.yaml`), bundled into `final-asyncapi.yaml` during lint |
| OpenAPI            | `docs/interfaces/api/openapi.yaml`     | REST contract scaffolding — root bundle + per-service partials under `order-service/`, `payment-service/`, `shipment-service/` (endpoints to be added)           |
| JSON Schemas       | `docs/interfaces/schemas/`             | CloudEvents envelope + domain payload schemas (`*.data.yaml`) + branded primitive types (`primitives/`)                                                          |
| TypeScript package | `generated/typescript`                 | `@guilherme-rauen/order-manager-contracts` — Zod validators + inferred types + NATS/CloudEvents constants                                                        |
| Python package     | `generated/python`                     | `order-manager-contracts` — Pydantic v2 models + NATS/CloudEvents constants                                                                                      |

For full contract details, check [`docs/interfaces/`](./docs/interfaces/).

## Contract Health Checks

| Check               | Command             | Description                                                  |
| ------------------- | ------------------- | ------------------------------------------------------------ |
| Lint contracts      | `pnpm lint`         | ESLint + AsyncAPI bundle + Spectral validation               |
| Format check        | `pnpm format:check` | Prettier (non-mutating)                                      |
| TS generation/build | `pnpm check`        | Lint + TypeScript codegen + `tsc` build                      |
| Python validation   | `pnpm check:python` | Python codegen + drift check + Ruff + Mypy                   |
| Security audit      | `pnpm check:audit`  | `pnpm audit --audit-level=high` (matches CI)                 |
| Full validation     | `pnpm check:full`   | All contract checks: lint + codegen + build + Python + audit |

## Published Packages

| Package                                    | Registry          | Install                                                                                                                                    |
| ------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `@guilherme-rauen/order-manager-contracts` | GitHub Packages   | `pnpm add @guilherme-rauen/order-manager-contracts --registry https://npm.pkg.github.com`                                                  |
| `order-manager-contracts` (Python)         | Git (no PyPI yet) | `pip install "order-manager-contracts @ git+https://github.com/guilherme-rauen/order-manager-contracts.git#subdirectory=generated/python"` |

## CloudEvents Envelope

All events use a shared CloudEvents v1.0 envelope with an enforced `type` pattern: `com.ordermanager.{domain}.{event}.v{n}`. Producers and consumers should import the canonical event-type strings and NATS subjects from the contracts package rather than hard-coding them:

```ts
import {
  EVENT_TYPES,
  SUBJECTS,
  envelopeSchema,
  orderCreatedDataSchema,
} from '@guilherme-rauen/order-manager-contracts';

const data = orderCreatedDataSchema.parse({
  order_id: 'ORD-ABCDEF01',
  customer_id: '9c2b0e3d-4f5a-6b7c-8d9e-0a1b2c3d4e5f',
  items: [{ product_id: 'SKU-1', quantity: 2, unit_price: 19.99 }],
  total_amount: 39.98,
  // currency defaults to 'EUR'
});

const envelope = envelopeSchema.parse({
  specversion: '1.0',
  id: '7b0f2f41-8b5e-4c2b-9a3e-8f2a0a8d1234',
  source: 'urn:order-manager:order-service',
  type: EVENT_TYPES.ORDER_CREATED, // 'com.ordermanager.order.created.v1'
  time: '2026-04-24T10:56:35Z',
  subject: 'ORD-ABCDEF01',
  datacontenttype: 'application/json',
  data,
  correlationid: '1d3b7e0c-2a5b-4e7f-b1c5-1f2e3d4c5b6a',
  aggregateversion: 1,
});

// Canonical subject — transport (NATS client) lives in your message-bus package.
const subject = SUBJECTS.ORDER_CREATED; // 'orders.events.OrderCreated'
```

## Relevance [CRITICAL]

If this repository is outdated or inconsistent:

- Producers and consumers can diverge on event payloads
- Integrations break silently across services
- Cross-language contract trust (TS ↔ Python) is lost
- Release confidence drops due to schema drift

## Sub-Components, Infrastructure/Service Dependencies

- [**AsyncAPI CLI**](https://www.asyncapi.com/tools/cli) — bundles per-domain AsyncAPI files into a single deref'd catalog
- [**Spectral**](https://stoplight.io/open-source/spectral) — lints the bundled AsyncAPI against `spectral:asyncapi` rules
- [**json-schema-to-zod**](https://github.com/StefanTerdell/json-schema-to-zod) — TypeScript codegen
- [**datamodel-code-generator**](https://github.com/koxudaxi/datamodel-code-generator) — Python (Pydantic v2) codegen
- [**pnpm workspaces**](https://pnpm.io/workspaces) — mono-package workspace (`generated/typescript`)

## Architecture & Technologies

- **Architecture**: A source-of-truth contracts repository with **committed generated artifacts** for cross-service audit trail and PR-level drift visibility. Contracts live as language-agnostic YAML under [`docs/interfaces/`](./docs/interfaces/) and fan out via codegen into versioned TypeScript and Python consumer packages.

  The layout follows:
  - [`docs/interfaces/events/`](./docs/interfaces/events/) — AsyncAPI catalog (split per-domain)
  - [`docs/interfaces/api/`](./docs/interfaces/api/) — OpenAPI specifications
  - [`docs/interfaces/schemas/`](./docs/interfaces/schemas/) — JSON Schemas (envelope, event `*.data.yaml`, branded primitives)
  - [`scripts/`](./scripts/) — codegen + verification scripts
  - [`generated/typescript/`](./generated/typescript/) — published npm package
  - [`generated/python/`](./generated/python/) — installable Python package

- **Languages**:
  - [**TypeScript**](https://www.typescriptlang.org/) (see [tsconfig.json](./tsconfig.json)) for codegen scripts + generated consumer package
  - [**Python 3.13+**](https://www.python.org/) (see [.python-version](./.python-version) and [generated/python/pyproject.toml](./generated/python/pyproject.toml)) for the Pydantic package
  - [**YAML**](https://yaml.org/) as the authoring language for all contracts

- **Contract DSLs**:
  - [**AsyncAPI 3.1**](https://www.asyncapi.com/docs/reference/specification/latest) for event channels and messages
  - [**OpenAPI 3.1**](https://spec.openapis.org/oas/v3.1.0) for REST endpoints
  - [**JSON Schema (draft 2020-12)**](https://json-schema.org/draft/2020-12/schema) for payloads and primitives

- **Validation Libraries**:
  - [**Zod**](https://zod.dev/) for runtime validation + inferred types on the TypeScript side
  - [**Pydantic v2**](https://docs.pydantic.dev/) for runtime validation + typed models on the Python side

- **Codegen**:
  - [**json-schema-to-zod**](https://github.com/StefanTerdell/json-schema-to-zod) with `$ref` dereferencing via [`@apidevtools/json-schema-ref-parser`](https://github.com/APIDevTools/json-schema-ref-parser) ([`scripts/generate-typescript.ts`](./scripts/generate-typescript.ts))
  - [**datamodel-code-generator**](https://github.com/koxudaxi/datamodel-code-generator) with pre-resolved schemas ([`scripts/generate-python.py`](./scripts/generate-python.py))

- **Linting & Type Checking**:
  - [**ESLint**](https://eslint.org/) (see [eslint.config.mjs](./eslint.config.mjs)) with `typescript-eslint` strict + `eslint-plugin-import`
  - [**Spectral**](https://stoplight.io/open-source/spectral) over the bundled AsyncAPI catalog (rule set: `spectral:asyncapi`)
  - [**Ruff**](https://docs.astral.sh/ruff/) for Python linting and import organization
  - [**Mypy**](https://mypy.readthedocs.io/) for Python type checking

- **Code Style**:
  - [**Prettier**](https://prettier.io/) (see [.prettierrc](./.prettierrc) and [.prettierignore](./.prettierignore))

- **Tooling & Release**:
  - [**pnpm**](https://pnpm.io/) workspaces (see [pnpm-workspace.yaml](./pnpm-workspace.yaml) and [packageManager](./package.json) in root)
  - [**Husky**](https://typicode.github.io/husky/) `commit-msg` hook running [**Commitlint**](https://commitlint.js.org/) with [Conventional Commits](https://www.conventionalcommits.org/) (see [.commitlintrc.yml](./.commitlintrc.yml))
  - [**GitHub Actions**](./.github/workflows/ci.yml) for lint, codegen drift check, build, Python validation, security audit, and publish to [GitHub Packages](https://github.com/guilherme-rauen/order-manager-contracts/pkgs/npm/order-manager-contracts)
  - [**pnpm audit**](https://pnpm.io/cli/audit) gate at `--audit-level=high` (see [`check:audit`](./package.json) script)
  - Supply-chain overrides in [`pnpm.overrides`](./package.json) keep transitive CVEs patched without waiting for upstream bumps

## Getting Started

1. **Install Node/pnpm dependencies**:

   ```bash
   pnpm install
   ```

2. **First-time Python setup** (one-off; creates `generated/python/.venv`):

   ```bash
   pnpm check:python
   ```

3. **Validate contracts quickly** (lint + TS codegen + TS build):

   ```bash
   pnpm check
   ```

4. **Run all contract checks** (lint + codegen + build + Python + audit):

   ```bash
   pnpm check:full
   ```

5. **Regenerate artifacts after schema changes**:

   ```bash
   pnpm generate
   ```

## For Developers

When changing any contract in [`docs/interfaces/`](./docs/interfaces/):

1. Edit the source YAML (`docs/interfaces/events/`, `docs/interfaces/api/`, or `docs/interfaces/schemas/`).
2. Regenerate outputs: `pnpm generate`.
3. Run the full checks: `pnpm check:full`.
4. Commit **source contracts and generated outputs together** — CI enforces a drift check (`git diff --exit-code -- generated/`) and will fail if the committed files don't match what codegen produces.
5. Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat(events): add order-refunded`) — the `commit-msg` hook runs Commitlint locally and CI re-runs it on PRs.

## License

All rights reserved. Distributed under a proprietary license — see [LICENSE](./LICENSE) for terms. Published to GitHub Packages under `UNLICENSED`.
