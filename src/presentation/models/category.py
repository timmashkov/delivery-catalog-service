from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

from infrastructure.database.models import Category
from presentation.models.patched_filter import PatchedFilter

if TYPE_CHECKING:
    from presentation.models.product import ReadProductModel


class CreateCategoryModel(BaseModel):
    name: str
    description: str | None
    parent_uuid: UUID | None = None


class ReadCategoryModel(CreateCategoryModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    #products: list["ReadProductModel"] | None = []


class CategoryFilter(PatchedFilter):
    uuid: UUID | None = None
    name: str | None = None
    parent_uuid: UUID | None = None

    class Constants(PatchedFilter.Constants):
        model = Category
