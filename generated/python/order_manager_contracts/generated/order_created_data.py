# Auto-generated from order-created.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class OrderItem(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    product_id: str
    quantity: Annotated[int, Field(ge=1)]
    unit_price: Annotated[float, Field(ge=0.0)]


class OrderCreatedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    customer_id: Annotated[UUID, Field(description='Branded customer identifier')]
    items: Annotated[list[OrderItem], Field(min_length=1)]
    total_amount: Annotated[float, Field(ge=0.0)]
    currency: Annotated[str, Field(pattern='^[A-Z]{3}$')]
