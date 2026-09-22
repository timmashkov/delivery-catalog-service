from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database import UnitOfWork, RepositoryMixin, Category, category_query_modifier


class CategoryUseCase(RepositoryMixin):

    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._model = Category
        self._query_modifier = category_query_modifier

    async def get_categories_list(self, filters: Filter) -> list:
        async with self.read_repository() as read_repository:
            categories_list = await read_repository.get_all_objects(filters)
        return [category for category in categories_list]

    async def read_single_category(self, category_uuid: UUID):
        async with self.read_repository() as read_repository:
            result = await read_repository.get_object_by_uuid(category_uuid)
            return result

    async def create_new_category(self, **kwargs):
        async with self.write_repository() as write_repository:
            return await write_repository.create_object(**kwargs)

    async def update_category(self, **kwargs):
        uuid = kwargs.pop("category_uuid")
        async with self.write_repository() as write_repository:
            return await write_repository.update_object(**kwargs, uuid=uuid)

    async def delete_category(self, category_uuid: UUID):
        async with self.write_repository() as write_repository:
            return await write_repository.delete_object(category_uuid)
