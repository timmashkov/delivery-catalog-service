from dishka import Provider, Scope, provide

from application.use_cases import ProductUseCase
from infrastructure.database import UnitOfWork


class UseCaseProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_product_use_cases(self, unit_of_work: UnitOfWork) -> ProductUseCase:
        return ProductUseCase(unit_of_work)
