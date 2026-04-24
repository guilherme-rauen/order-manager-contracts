# Auto-generated from shipment-requested.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DeliveryAddress(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    street: str
    city: str
    postal_code: str
    country: Annotated[
        str, Field(description='ISO 3166-1 alpha-2 country code', pattern='^[A-Z]{2}$')
    ]


class ShipmentItem(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    product_id: str
    quantity: Annotated[int, Field(ge=1)]


class ShipmentRequestedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    shipment_id: Annotated[UUID, Field(description='Branded shipment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    customer_id: Annotated[UUID, Field(description='Branded customer identifier')]
    delivery_address: Annotated[DeliveryAddress, Field(title='DeliveryAddress')]
    items: Annotated[list[ShipmentItem], Field(min_length=1)]
