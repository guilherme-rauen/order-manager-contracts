# Auto-generated from order-confirmed.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class OrderConfirmedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    payment_id: Annotated[UUID, Field(description='Branded payment identifier')]
    confirmed_amount: Annotated[float, Field(ge=0.0)]
    confirmed_at: AwareDatetime
