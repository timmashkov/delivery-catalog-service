from dishka import Provider, Scope, provide

from application.config import Settings
from application.server import APIServer
from presentation.routers import product_router


class ServerProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_api_server(self, settings: Settings) -> APIServer:
        """Создаёт экземпляр APIServer с инжектированными settings."""
        return APIServer(
            settings=settings,
            routers=[product_router],
        )
