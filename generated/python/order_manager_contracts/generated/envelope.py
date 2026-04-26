# Auto-generated from envelope.yaml — do not edit.

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, Field


class Envelope(BaseModel):
    specversion: Literal['1.0']
    id: UUID
    source: Annotated[str, Field(description='URI identifying the event producer')]
    type: Annotated[
        str,
        Field(
            description='Event type — com.ordermanager.{domain}.{event}.v{n}. The {event} segment may itself contain dots for hierarchical names (e.g. saga.step.completed).',
            pattern='^com\\.ordermanager\\.[a-z]+(\\.[a-z]+)+\\.v\\d+$',
        ),
    ]
    time: AwareDatetime
    subject: Annotated[str, Field(description='Aggregate identifier')]
    datacontenttype: Literal['application/json']
    data: Annotated[
        dict[str, Any],
        Field(
            description='Event-specific payload. Kept loosely typed in the envelope; validated at consumption time by the event-specific Zod schema (TS) or Pydantic model (Python).'
        ),
    ]
    correlationid: UUID
    causationid: UUID | None = None
    aggregateversion: Annotated[int, Field(ge=1)]
