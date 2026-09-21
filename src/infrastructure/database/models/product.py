from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Numeric, Boolean, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models._mixins import UUIDTableMixin, CreatedAtTableMixin, UpdatedAtTableMixin
from ._base import _Base

if TYPE_CHECKING:
    from .category import Category


class Product(_Base, UUIDTableMixin, CreatedAtTableMixin, UpdatedAtTableMixin):
    name: Mapped[str] = mapped_column(String, comment="Имя продукта")
    description: Mapped[str | None] = mapped_column(Text, nullable=True, comment="Описание продукта")
    sku: Mapped[str] = mapped_column(String, unique=True, index=True, comment="Код товара")
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), comment="Стоимость  продукта")
    currency: Mapped[str] = mapped_column(String(3), comment="Валюта")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, comment="Наличие продукта")

    category_uuid: Mapped[UUID] = mapped_column(ForeignKey("categories.uuid"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products")
