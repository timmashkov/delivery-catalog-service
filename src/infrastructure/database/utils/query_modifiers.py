from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.database.models.product import Product


def product_query_modifier(query: type[select]) -> type[select]:
    return query.options(joinedload(Product.category))
