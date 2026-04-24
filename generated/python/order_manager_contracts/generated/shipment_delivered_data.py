# Auto-generated from shipment-delivered.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class ShipmentDeliveredData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    shipment_id: Annotated[UUID, Field(description='Branded shipment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    delivered_at: AwareDatetime
    signed_by: str | None = None
