"""Pydantic models for Order Manager contracts.

Committed to the repo; refresh with ``pnpm generate:python``.
"""

from .generated.correlation_id import CorrelationId
from .generated.customer_id import CustomerId
from .generated.envelope import Envelope
from .generated.order_cancelled_data import OrderCancelledData
from .generated.order_confirmed_data import OrderConfirmedData
from .generated.order_created_data import OrderCreatedData
from .generated.order_delivered_data import OrderDeliveredData
from .generated.order_id import OrderId
from .generated.order_shipped_data import OrderShippedData
from .generated.payment_confirmed_data import PaymentConfirmedData
from .generated.payment_failed_data import PaymentFailedData
from .generated.payment_id import PaymentId
from .generated.payment_refunded_data import PaymentRefundedData
from .generated.payment_requested_data import PaymentRequestedData
from .generated.saga_completed_data import SagaCompletedData
from .generated.saga_started_data import SagaStartedData
from .generated.saga_step_completed_data import SagaStepCompletedData
from .generated.saga_step_failed_data import SagaStepFailedData
from .generated.shipment_delivered_data import ShipmentDeliveredData
from .generated.shipment_dispatched_data import ShipmentDispatchedData
from .generated.shipment_failed_data import ShipmentFailedData
from .generated.shipment_id import ShipmentId
from .generated.shipment_requested_data import ShipmentRequestedData
from .nats import CONSUMERS, EVENT_TYPES, STREAMS, SUBJECTS, WILDCARDS

__version__ = "0.1.2"

__all__ = [
    "CONSUMERS",
    "EVENT_TYPES",
    "STREAMS",
    "SUBJECTS",
    "WILDCARDS",
    "CorrelationId",
    "CustomerId",
    "Envelope",
    "OrderCancelledData",
    "OrderConfirmedData",
    "OrderCreatedData",
    "OrderDeliveredData",
    "OrderId",
    "OrderShippedData",
    "PaymentConfirmedData",
    "PaymentFailedData",
    "PaymentId",
    "PaymentRefundedData",
    "PaymentRequestedData",
    "SagaCompletedData",
    "SagaStartedData",
    "SagaStepCompletedData",
    "SagaStepFailedData",
    "ShipmentDeliveredData",
    "ShipmentDispatchedData",
    "ShipmentFailedData",
    "ShipmentId",
    "ShipmentRequestedData",
    "__version__",
]
