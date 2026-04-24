# Auto-generated from payment-refunded.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class PaymentRefundedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    payment_id: Annotated[UUID, Field(description='Branded payment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    refund_amount: Annotated[float, Field(ge=0.0)]
    currency: Annotated[str, Field(pattern='^[A-Z]{3}$')]
    reason: str
    refunded_at: AwareDatetime
