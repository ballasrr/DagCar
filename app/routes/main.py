from fastapi.responses import RedirectResponse

from app.routes.base import BaseRouter


class MainRouter(BaseRouter):
    """
    Класс роутера для главной страницы приложения.
    """

    def __init__(self):
        super().__init__(prefix="", tags=["Главная"])

    def configure(self):
        @self.router.get("/")
        async def root() -> RedirectResponse:
            """
            🏠 **Перенаправление на документацию.**

            **Returns**:
            - **RedirectResponse**: Перенаправление по адресу **/docs**
            """
            return RedirectResponse(url="/docs")
