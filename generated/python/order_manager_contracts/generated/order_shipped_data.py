# Auto-generated from order-shipped.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class OrderShippedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    shipment_id: Annotated[UUID, Field(description='Branded shipment identifier')]
    carrier: str
    tracking_code: str
    shipped_at: AwareDatetime
