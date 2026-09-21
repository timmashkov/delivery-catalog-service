from typing import TYPE_CHECKING

from sqlalchemy import String, Text, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models._mixins import UUIDTableMixin, CreatedAtTableMixin, UpdatedAtTableMixin
from ._base import _Base

if TYPE_CHECKING:
    from .product import Product


class Category(_Base, UUIDTableMixin, CreatedAtTableMixin, UpdatedAtTableMixin):
    name: Mapped[str] = mapped_column(String, comment="Имя категории")
    description: Mapped[str | None] = mapped_column(Text, nullable=True, comment="Описание категории")
    parent_uuid: Mapped[UUID | None] = mapped_column(
                ForeignKey("categories.uuid", ondelete="SET NULL"),
                nullable=True,
    )
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    parent: Mapped["Category | None"] = relationship(
        "Category",
        remote_side="Category.uuid",
        back_populates="children",
    )
    children: Mapped[list["Category"]] = relationship("Category", back_populates="parent")
