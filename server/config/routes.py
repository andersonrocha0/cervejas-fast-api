from typing import Optional


def routes():
    from server import app
    from server.controllers import cerveja_controller

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    app.include_router(cerveja_controller.router)
