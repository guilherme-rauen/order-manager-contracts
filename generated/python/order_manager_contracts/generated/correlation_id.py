# Auto-generated from correlation-id.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import Field, RootModel


class CorrelationId(RootModel[UUID]):
    root: Annotated[
        UUID,
        Field(
            description='Correlation identifier for distributed tracing and saga coordination'
        ),
    ]
