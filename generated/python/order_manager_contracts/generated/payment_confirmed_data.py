# Auto-generated from payment-confirmed.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class PaymentConfirmedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    payment_id: Annotated[UUID, Field(description='Branded payment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    amount: Annotated[float, Field(ge=0.0)]
    currency: Annotated[str, Field(pattern='^[A-Z]{3}$')]
    provider_transaction_id: Annotated[
        str, Field(description='External payment service provider reference')
    ]
    confirmed_at: AwareDatetime
