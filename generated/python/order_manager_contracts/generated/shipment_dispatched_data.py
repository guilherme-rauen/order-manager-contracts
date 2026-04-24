# Auto-generated from shipment-dispatched.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Carrier(StrEnum):
    dhl = 'DHL'
    ups = 'UPS'
    fedex = 'FEDEX'
    dpd = 'DPD'


class ShipmentDispatchedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    shipment_id: Annotated[UUID, Field(description='Branded shipment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    carrier: Carrier
    tracking_code: str
    estimated_delivery: AwareDatetime
    dispatched_at: AwareDatetime
