/**
 * @guilherme-rauen/order-manager-contracts
 *
 * Generated artifacts live under ./generated/ (committed to git for audit trail).
 * Run `pnpm generate:typescript` to regenerate from JSON Schema sources.
 */

export const CONTRACTS_VERSION = '0.1.1' as const;

// CloudEvents envelope
export { envelopeSchema, type Envelope } from './generated/envelope.zod.js';

// Order domain event data
export { orderCancelledDataSchema, type OrderCancelledData } from './generated/order-cancelled.data.zod.js';
export { orderConfirmedDataSchema, type OrderConfirmedData } from './generated/order-confirmed.data.zod.js';
export { orderCreatedDataSchema, type OrderCreatedData } from './generated/order-created.data.zod.js';
export { orderDeliveredDataSchema, type OrderDeliveredData } from './generated/order-delivered.data.zod.js';
export { orderShippedDataSchema, type OrderShippedData } from './generated/order-shipped.data.zod.js';

// Payment domain event data
export { paymentConfirmedDataSchema, type PaymentConfirmedData } from './generated/payment-confirmed.data.zod.js';
export { paymentFailedDataSchema, type PaymentFailedData } from './generated/payment-failed.data.zod.js';
export { paymentRefundedDataSchema, type PaymentRefundedData } from './generated/payment-refunded.data.zod.js';
export { paymentRequestedDataSchema, type PaymentRequestedData } from './generated/payment-requested.data.zod.js';

// Shipment domain event data
export { shipmentDeliveredDataSchema, type ShipmentDeliveredData } from './generated/shipment-delivered.data.zod.js';
export { shipmentDispatchedDataSchema, type ShipmentDispatchedData } from './generated/shipment-dispatched.data.zod.js';
export { shipmentFailedDataSchema, type ShipmentFailedData } from './generated/shipment-failed.data.zod.js';
export { shipmentRequestedDataSchema, type ShipmentRequestedData } from './generated/shipment-requested.data.zod.js';

// Saga event data
export { sagaCompletedDataSchema, type SagaCompletedData } from './generated/saga-completed.data.zod.js';
export { sagaStartedDataSchema, type SagaStartedData } from './generated/saga-started.data.zod.js';
export { sagaStepCompletedDataSchema, type SagaStepCompletedData } from './generated/saga-step-completed.data.zod.js';
export { sagaStepFailedDataSchema, type SagaStepFailedData } from './generated/saga-step-failed.data.zod.js';

// Primitives
export { correlationIdSchema, type CorrelationId } from './generated/correlation-id.zod.js';
export { customerIdSchema, type CustomerId } from './generated/customer-id.zod.js';
export { orderIdSchema, type OrderId } from './generated/order-id.zod.js';
export { paymentIdSchema, type PaymentId } from './generated/payment-id.zod.js';
export { shipmentIdSchema, type ShipmentId } from './generated/shipment-id.zod.js';

// NATS + CloudEvents constants
export { CONSUMERS, EVENT_TYPES, STREAMS, SUBJECTS, WILDCARDS } from './nats.js';
