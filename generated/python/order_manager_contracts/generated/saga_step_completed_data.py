# Auto-generated from saga-step-completed.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Step(StrEnum):
    payment_requested = 'PAYMENT_REQUESTED'
    payment_confirmed = 'PAYMENT_CONFIRMED'
    shipment_requested = 'SHIPMENT_REQUESTED'
    shipment_dispatched = 'SHIPMENT_DISPATCHED'
    shipment_delivered = 'SHIPMENT_DELIVERED'


class SagaStepCompletedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    saga_id: Annotated[
        UUID,
        Field(
            description='Correlation identifier for distributed tracing and saga coordination'
        ),
    ]
    step: Step
    previous_state: str
    new_state: str
    completed_at: AwareDatetime
