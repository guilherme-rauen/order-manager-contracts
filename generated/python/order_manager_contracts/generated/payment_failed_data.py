# Auto-generated from payment-failed.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class FailureReason(StrEnum):
    insufficient_funds = 'INSUFFICIENT_FUNDS'
    card_declined = 'CARD_DECLINED'
    provider_error = 'PROVIDER_ERROR'
    timeout = 'TIMEOUT'


class PaymentFailedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    payment_id: Annotated[UUID, Field(description='Branded payment identifier')]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    amount: Annotated[float, Field(ge=0.0)]
    currency: Annotated[str, Field(pattern='^[A-Z]{3}$')]
    failure_reason: FailureReason
    failed_at: AwareDatetime
