from typing import Any, Optional, Protocol, Union

from fastapi import BackgroundTasks
from pydantic import BaseModel
from starlette.requests import QueryParams

from github_webhooks.schemas import WebhookHeaders

PayloadT = type[BaseModel]
HandlerResult = Optional[str]


class HandlerBasic(Protocol):
    async def __call__(
        self, payload: Any, query_params: QueryParams, background_tasks: BackgroundTasks
    ) -> HandlerResult:
        # actually payload will be parsed pydantic model
        ...


class HandlerWithHeaders(Protocol):
    async def __call__(
        self, payload: Any, *, headers: WebhookHeaders, query_params: QueryParams, background_tasks: BackgroundTasks
    ) -> HandlerResult:
        # actually payload will be parsed pydantic model
        ...


class DefaultHandlerBasic(Protocol):
    async def __call__(
        self, event: str, payload: bytes, query_params: QueryParams, background_tasks: BackgroundTasks
    ) -> HandlerResult: ...


class DefaultHandlerWithHeaders(Protocol):
    async def __call__(
        self,
        event: str,
        payload: bytes,
        *,
        headers: WebhookHeaders,
        query_params: QueryParams,
        background_tasks: BackgroundTasks,
    ) -> HandlerResult: ...


Handler = Union[HandlerBasic, HandlerWithHeaders]
DefaultHandler = Union[DefaultHandlerBasic, DefaultHandlerWithHeaders]
AnyHandlerWithHeaders = Union[HandlerWithHeaders, DefaultHandlerWithHeaders]
AnyHandlerWithoutHeaders = Union[HandlerBasic, DefaultHandlerBasic]
