from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field
from infrastructure.database.models import Product
from presentation.models.category import ReadCategoryModel
from presentation.models.patched_filter import PatchedFilter


class CreateProductModel(BaseModel):
    name: str = Field(description=Product.name.comment)
    description: str | None = Field(description=Product.description.comment)
    price: Decimal = Field(description=Product.price.comment)
    currency: str = Field(description=Product.currency.comment)
    is_active: bool = Field(default=True, description=Product.is_active.comment)
    data: dict | None = Field(default_factory=dict, description=Product.data.comment)
    category_uuid: UUID = Field(description="Айди категории")


class ReadProductModel(CreateProductModel):
    uuid: UUID = Field(description=Product.uuid.comment)
    sku: str = Field(description=Product.sku.comment)
    created_at: datetime = Field(description=Product.created_at.comment)
    updated_at: datetime = Field(description=Product.updated_at.comment)
    category: ReadCategoryModel | None = None


class ProductFilter(PatchedFilter):
    uuid: UUID | None = None
    name: str | None = None
    price: Decimal | None = None
    currency: str | None = None
    is_active: bool = True
    category_uuid: UUID | None = None

    class Constants(PatchedFilter.Constants):
        model = Product
