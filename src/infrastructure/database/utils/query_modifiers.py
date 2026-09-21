from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from infrastructure.database.models.product import Product
from infrastructure.database.models.category import Category


def product_query_modifier(query: select) -> select:
    return query.options(joinedload(Product.category))


def category_query_modifier(query: select) -> select:
    return query.options(selectinload(Category.children))
