/**
 * @guilherme-rauen/order-manager-contracts
 *
 * Generated artifacts live under ./generated/ (committed to git for audit trail).
 * Run `pnpm generate:typescript` to regenerate from JSON Schema sources.
 */

export const CONTRACTS_VERSION = '0.0.0' as const;

// CloudEvents envelope
export { envelopeSchema, type Envelope } from './generated/envelope.zod.js';

// Event data schemas
export {
  orderCreatedDataSchema,
  type OrderCreatedData,
} from './generated/order-created.data.zod.js';

// Primitives
export { correlationIdSchema, type CorrelationId } from './generated/correlation-id.zod.js';
export { customerIdSchema, type CustomerId } from './generated/customer-id.zod.js';
export { orderIdSchema, type OrderId } from './generated/order-id.zod.js';
export { paymentIdSchema, type PaymentId } from './generated/payment-id.zod.js';
export { shipmentIdSchema, type ShipmentId } from './generated/shipment-id.zod.js';
