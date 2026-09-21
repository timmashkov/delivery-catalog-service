from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases import ProductUseCase
from presentation.models import CreateProductModel, ReadProductModel, ProductFilter

product_router = APIRouter(prefix="/product", tags=["Products"])


@product_router.get("/{product_uuid}", response_model=ReadProductModel)
@inject
async def read_product(product_uuid: UUID, product_provider: FromDishka[ProductUseCase]):
    return await product_provider.read_single_product(product_uuid)


@product_router.get("/", response_model=list[ReadProductModel])
@inject
async def read_products(
    product_provider: FromDishka[ProductUseCase],
    product_filters: ProductFilter = FilterDepends(ProductFilter),
):
    return await product_provider.get_products_list(product_filters)


@product_router.post("/", response_model=ReadProductModel)
@inject
async def create_product(
    user_data: CreateProductModel, product_provider: FromDishka[ProductUseCase]
):
    return await product_provider.create_new_product(**user_data.model_dump())


@product_router.patch("/{product_uuid}", response_model=ReadProductModel)
@inject
async def update_product(
    product_uuid: UUID, user_data: CreateProductModel, product_provider: FromDishka[ProductUseCase]
):
    return await product_provider.update_product( **user_data.model_dump(), product_uuid=product_uuid)


@product_router.delete("/{product_uuid}", response_model=ReadProductModel)
@inject
async def delete_product(product_uuid: UUID, product_provider: FromDishka[ProductUseCase]):
    return await product_provider.delete_product(product_uuid)
