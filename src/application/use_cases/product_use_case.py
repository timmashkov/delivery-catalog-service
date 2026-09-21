from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from domain import ProductDomainModel
from infrastructure.database import UnitOfWork, RepositoryMixin, Product, product_query_modifier


class ProductUseCase(RepositoryMixin):

    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._model = Product
        self._query_modifier = product_query_modifier

    async def get_products_list(self, filters: Filter) -> list:
        async with self.read_repository() as read_repository:
            products_list = await read_repository.get_all_objects(filters)
        return [product for product in products_list]

    async def read_single_product(self, product_uuid: UUID):
        async with self.read_repository() as read_repository:
            result = await read_repository.get_object_by_uuid(product_uuid)
            print(result.__dict__["category"].__dict__, 666)
            return result

    async def create_new_product(self, **kwargs):
        new_product = ProductDomainModel(**kwargs)
        async with self.write_repository() as write_repository:
            return await write_repository.create_object(**new_product.to_dict())

    async def update_product(self, **kwargs):
        uuid = kwargs.pop("product_uuid")
        async with self.write_repository() as write_repository:
            return await write_repository.update_object(**kwargs, uuid=uuid)

    async def delete_product(self, product_uuid: UUID):
        async with self.write_repository() as write_repository:
            return await write_repository.delete_object(product_uuid)
