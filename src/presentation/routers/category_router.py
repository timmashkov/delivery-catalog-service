from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases import CategoryUseCase
from presentation.models import CreateCategoryModel, ReadCategoryModel, CategoryFilter

category_router = APIRouter(prefix="/category", tags=["Category"])


@category_router.get("/{category_uuid}", response_model=ReadCategoryModel)
@inject
async def read_category(category_uuid: UUID, category_provider: FromDishka[CategoryUseCase]):
    return await category_provider.read_single_category(category_uuid)


@category_router.get("/", response_model=list[ReadCategoryModel])
@inject
async def read_categories(
    category_provider: FromDishka[CategoryUseCase],
    category_filters: CategoryFilter = FilterDepends(CategoryFilter),
):
    return await category_provider.get_categories_list(category_filters)


@category_router.post("/", response_model=ReadCategoryModel)
@inject
async def create_category(
    user_data: CreateCategoryModel, category_provider: FromDishka[CategoryUseCase]
):
    return await category_provider.create_new_category(**user_data.model_dump())


@category_router.patch("/{category_uuid}", response_model=ReadCategoryModel)
@inject
async def update_category(
    category_uuid: UUID, user_data: CreateCategoryModel, category_provider: FromDishka[CategoryUseCase]
):
    return await category_provider.update_category( **user_data.model_dump(), category_uuid=category_uuid)


@category_router.delete("/{category_uuid}", response_model=ReadCategoryModel)
@inject
async def delete_category(category_uuid: UUID, category_provider: FromDishka[CategoryUseCase]):
    return await category_provider.delete_category(category_uuid)
