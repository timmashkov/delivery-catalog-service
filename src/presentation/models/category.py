from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    from presentation.models.product import ReadProductModel


class CreateCategoryModel(BaseModel):
    name: str
    description: str | None
    parent_uuid: UUID | None


class ReadCategoryModel(CreateCategoryModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    #products: list["ReadProductModel"] | None = []
