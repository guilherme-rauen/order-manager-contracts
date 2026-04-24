# Auto-generated from order-cancelled.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Reason(StrEnum):
    payment_failed = 'PAYMENT_FAILED'
    customer_request = 'CUSTOMER_REQUEST'
    shipment_failed = 'SHIPMENT_FAILED'
    timeout = 'TIMEOUT'


class CancelledBy(StrEnum):
    system = 'SYSTEM'
    customer = 'CUSTOMER'


class OrderCancelledData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    reason: Reason
    cancelled_at: AwareDatetime
    cancelled_by: CancelledBy
