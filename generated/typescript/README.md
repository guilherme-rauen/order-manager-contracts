# @guilherme-rauen/order-manager-contracts

TypeScript types and Zod validators for the Order Manager platform. Generated from JSON Schema sources in `docs/interfaces/schemas/`.

## Install

```bash
pnpm add @guilherme-rauen/order-manager-contracts --registry https://npm.pkg.github.com
```

## Usage

```typescript
import { envelopeSchema, orderCreatedDataSchema, type OrderCreatedData } from '@guilherme-rauen/order-manager-contracts';
import { orderIdSchema, type OrderId } from '@guilherme-rauen/order-manager-contracts';
```

## Prepack

The `prepack` script re-runs codegen from the workspace root via `pnpm --filter`. This is intentional — the package is always published via `npm publish` inside `generated/typescript/` (driven by CI), never via standalone `npm pack`.

## License

UNLICENSED — All rights reserved. See repository root LICENSE.
