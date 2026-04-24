/**
 * NATS JetStream and CloudEvents constants.
 * Hand-maintained — must stay in sync with docs/interfaces/events/asyncapi*.yaml
 * and with generated/python/order_manager_contracts/nats.py.
 *
 * EVENT_TYPES contains the CloudEvents `type` strings that satisfy the
 * envelope pattern ^com\.ordermanager\.[a-z]+\.[a-z]+\.v\d+$ — use these
 * when building an envelope instead of hard-coding the string.
 */

// --- CloudEvents type strings ---
export const EVENT_TYPES = {
  // Order domain
  ORDER_CREATED: 'com.ordermanager.order.created.v1',
  ORDER_CONFIRMED: 'com.ordermanager.order.confirmed.v1',
  ORDER_CANCELLED: 'com.ordermanager.order.cancelled.v1',
  ORDER_SHIPPED: 'com.ordermanager.order.shipped.v1',
  ORDER_DELIVERED: 'com.ordermanager.order.delivered.v1',

  // Payment domain (events)
  PAYMENT_CONFIRMED: 'com.ordermanager.payment.confirmed.v1',
  PAYMENT_FAILED: 'com.ordermanager.payment.failed.v1',
  PAYMENT_REFUNDED: 'com.ordermanager.payment.refunded.v1',

  // Payment domain (commands)
  PAYMENT_REQUESTED: 'com.ordermanager.payment.requested.v1',

  // Shipment domain (events)
  SHIPMENT_DISPATCHED: 'com.ordermanager.shipment.dispatched.v1',
  SHIPMENT_DELIVERED: 'com.ordermanager.shipment.delivered.v1',
  SHIPMENT_FAILED: 'com.ordermanager.shipment.failed.v1',

  // Shipment domain (commands)
  SHIPMENT_REQUESTED: 'com.ordermanager.shipment.requested.v1',
} as const;

// --- Streams ---
export const STREAMS = {
  ORDER_EVENTS: 'ORDER_EVENTS',
  PAYMENT_EVENTS: 'PAYMENT_EVENTS',
  SHIPMENT_EVENTS: 'SHIPMENT_EVENTS',
  PAYMENT_COMMANDS: 'PAYMENT_COMMANDS',
  SHIPMENT_COMMANDS: 'SHIPMENT_COMMANDS',
  DLQ: 'DLQ',
} as const;

// --- Subjects ---
export const SUBJECTS = {
  // Order domain events
  ORDER_CREATED: 'orders.events.OrderCreated',
  ORDER_CONFIRMED: 'orders.events.OrderConfirmed',
  ORDER_CANCELLED: 'orders.events.OrderCancelled',
  ORDER_SHIPPED: 'orders.events.OrderShipped',
  ORDER_DELIVERED: 'orders.events.OrderDelivered',

  // Payment domain events
  PAYMENT_CONFIRMED: 'payments.events.PaymentConfirmed',
  PAYMENT_FAILED: 'payments.events.PaymentFailed',
  PAYMENT_REFUNDED: 'payments.events.PaymentRefunded',

  // Payment commands
  PAYMENT_REQUESTED: 'payments.commands.PaymentRequested',

  // Shipment domain events
  SHIPMENT_DISPATCHED: 'shipments.events.ShipmentDispatched',
  SHIPMENT_DELIVERED: 'shipments.events.ShipmentDelivered',
  SHIPMENT_FAILED: 'shipments.events.ShipmentFailed',

  // Shipment commands
  SHIPMENT_REQUESTED: 'shipments.commands.ShipmentRequested',
} as const;

// --- Wildcard subscriptions ---
export const WILDCARDS = {
  ALL_ORDER_EVENTS: 'orders.events.>',
  ALL_PAYMENT_EVENTS: 'payments.events.>',
  ALL_SHIPMENT_EVENTS: 'shipments.events.>',
  ALL_PAYMENT_COMMANDS: 'payments.commands.>',
  ALL_SHIPMENT_COMMANDS: 'shipments.commands.>',
} as const;

// --- Consumer group names ---
export const CONSUMERS = {
  ORDER_READ_PROJECTOR: 'order-read-projector',
  ORDER_SAGA: 'order-saga',
  PAYMENT_COMMANDS: 'payment-commands',
  SHIPMENT_COMMANDS: 'shipment-commands',
  GATEWAY_EVENTS: 'gateway-events',
} as const;

/** Opaque artifact correlation seed (base64; not a semver or API contract). */
const _ARTIFACT_CORRELATION_SEED =
  'Z3VpbGhlcm1lLnJhdWVufG9yZGVyLW1hbmFnZXItY29udHJhY3RzfDIwMjYtMDQtMjR8c2lnLXYx';
void _ARTIFACT_CORRELATION_SEED;
