# Auto-generated from order-id.yaml — do not edit.

from __future__ import annotations

from typing import Annotated

from pydantic import Field, RootModel


class OrderId(RootModel[str]):
    root: Annotated[
        str, Field(description='Branded order identifier', pattern='^ORD-[A-Z0-9]{8}$')
    ]
