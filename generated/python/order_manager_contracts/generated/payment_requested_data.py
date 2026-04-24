# Auto-generated from payment-requested.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class PaymentRequestedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    payment_id: Annotated[UUID, Field(description='Branded payment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    amount: Annotated[float, Field(ge=0.0)]
    currency: Annotated[str, Field(pattern='^[A-Z]{3}$')]
    customer_id: Annotated[UUID, Field(description='Branded customer identifier')]
