# Auto-generated from saga-started.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class SagaStartedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    saga_id: Annotated[
        UUID,
        Field(
            description='Correlation identifier for distributed tracing and saga coordination'
        ),
    ]
    saga_type: Literal['ORDER_LIFECYCLE']
    order_id: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
    initial_state: Literal['AWAITING_PAYMENT']
    started_at: AwareDatetime
