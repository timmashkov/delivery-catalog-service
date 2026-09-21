from dishka import Provider, Scope, provide

from application.use_cases import ProductUseCase, CategoryUseCase
from infrastructure.database import UnitOfWork


class UseCaseProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_product_use_cases(self, unit_of_work: UnitOfWork) -> ProductUseCase:
        return ProductUseCase(unit_of_work)

    @provide(scope=Scope.REQUEST)
    def provide_category_use_cases(self, unit_of_work: UnitOfWork) -> CategoryUseCase:
        return CategoryUseCase(unit_of_work)
