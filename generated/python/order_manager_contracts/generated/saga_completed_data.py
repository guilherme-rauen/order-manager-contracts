# Auto-generated from saga-completed.data.yaml — do not edit.

from __future__ import annotations

from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class FinalState(StrEnum):
    completed_delivered = 'COMPLETED_DELIVERED'
    completed_cancelled = 'COMPLETED_CANCELLED'


class SagaCompletedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    saga_id: Annotated[
        UUID,
        Field(
            description='Correlation identifier for distributed tracing and saga coordination'
        ),
    ]
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    final_state: FinalState
    completed_at: AwareDatetime
    duration_ms: Annotated[int, Field(ge=0)]
