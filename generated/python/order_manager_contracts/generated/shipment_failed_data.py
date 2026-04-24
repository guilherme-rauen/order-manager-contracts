# Auto-generated from shipment-failed.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class FailureReason(StrEnum):
    address_invalid = 'ADDRESS_INVALID'
    carrier_error = 'CARRIER_ERROR'
    customs_hold = 'CUSTOMS_HOLD'
    lost = 'LOST'


class ShipmentFailedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    shipment_id: Annotated[UUID, Field(description='Branded shipment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    failure_reason: FailureReason
    failed_at: AwareDatetime
