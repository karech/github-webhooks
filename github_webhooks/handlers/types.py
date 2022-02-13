from typing import Any, Optional, Protocol

from pydantic import BaseModel

from github_webhooks.schemas import WebhookHeaders

PayloadT = type[BaseModel]
HandlerResult = Optional[str]


class HandlerCallable(Protocol):
    async def __call__(self, headers: WebhookHeaders, payload: Any) -> HandlerResult:
        # actually payload will be parsed pydantic model
        ...


class DefaultHandlerCallable(Protocol):
    async def __call__(self, event: str, headers: WebhookHeaders, payload: bytes) -> HandlerResult:
        ...
