from datetime import datetime
from typing import TYPE_CHECKING, ForwardRef
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.database.models import Category
from presentation.models.patched_filter import PatchedFilter

if TYPE_CHECKING:
    from presentation.models.product import ReadProductModel


class CreateCategoryModel(BaseModel):
    name: str
    description: str | None
    parent_uuid: UUID | None = None


class ReadCategoryChildModel(BaseModel):
    name: str
    description: str | None
    parent_uuid: UUID | None
    uuid: UUID
    created_at: datetime
    updated_at: datetime


class ReadCategoryModel(CreateCategoryModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    children: list[ReadCategoryChildModel] = Field(
        default_factory=list
    )

class CategoryFilter(PatchedFilter):
    uuid: UUID | None = None
    name: str | None = None
    parent_uuid: UUID | None = None

    class Constants(PatchedFilter.Constants):
        model = Category
