from typing import Any, Optional, Protocol, Union

from pydantic import BaseModel

from github_webhooks.schemas import WebhookHeaders

PayloadT = type[BaseModel]
HandlerResult = Optional[str]


class HandlerBasic(Protocol):
    async def __call__(self, payload: Any) -> HandlerResult:
        # actually payload will be parsed pydantic model
        ...


class HandlerWithHeaders(Protocol):
    async def __call__(self, payload: Any, *, headers: WebhookHeaders) -> HandlerResult:
        # actually payload will be parsed pydantic model
        ...


class DefaultHandlerBasic(Protocol):
    async def __call__(self, event: str, payload: bytes) -> HandlerResult:
        ...


class DefaultHandlerWithHeaders(Protocol):
    async def __call__(self, event: str, payload: bytes, *, headers: WebhookHeaders) -> HandlerResult:
        ...


Handler = Union[HandlerBasic, HandlerWithHeaders]
DefaultHandler = Union[DefaultHandlerBasic, DefaultHandlerWithHeaders]
AnyHandlerWithHeaders = Union[HandlerWithHeaders, DefaultHandlerWithHeaders]
AnyHandlerWithoutHeaders = Union[HandlerBasic, DefaultHandlerBasic]
