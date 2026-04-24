# Auto-generated from customer-id.yaml — do not edit.

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import Field, RootModel


class CustomerId(RootModel[UUID]):
    root: Annotated[UUID, Field(description='Branded customer identifier')]
