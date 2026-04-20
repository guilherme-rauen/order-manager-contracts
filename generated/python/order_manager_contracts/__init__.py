"""Pydantic models for Order Manager contracts.
Committed to the repo; refresh with ``pnpm generate:python``.
"""

from order_manager_contracts.generated.correlation_id import CorrelationId
from order_manager_contracts.generated.customer_id import CustomerId
from order_manager_contracts.generated.envelope import Envelope
from order_manager_contracts.generated.order_created_data import OrderCreatedData
from order_manager_contracts.generated.order_id import OrderId
from order_manager_contracts.generated.payment_id import PaymentId
from order_manager_contracts.generated.shipment_id import ShipmentId

__version__ = "0.0.0"

__all__ = [
    "CorrelationId",
    "CustomerId",
    "Envelope",
    "OrderCreatedData",
    "OrderId",
    "PaymentId",
    "ShipmentId",
    "__version__",
]
