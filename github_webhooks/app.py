from typing import Optional

from fastapi import FastAPI

from . import handlers, web


class App(FastAPI):
    secret_token: Optional[str] = None

    hooks: handlers.HandlersRegistry


def create_app(secret_token: Optional[str] = None) -> App:
    app = App()

    app.hooks = handlers.registry
    app.secret_token = secret_token

    app.include_router(web.router)

    return app
