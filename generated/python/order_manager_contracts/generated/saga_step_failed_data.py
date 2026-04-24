# Auto-generated from saga-step-failed.data.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class SagaStepFailedData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    saga_id: Annotated[
        UUID,
        Field(
            description='Correlation identifier for distributed tracing and saga coordination'
        ),
    ]
    step: str
    previous_state: str
    new_state: str
    failure_reason: str
    failed_at: AwareDatetime
