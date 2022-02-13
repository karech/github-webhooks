from typing import Callable

from github_webhooks.schemas import WebhookHeaders

from .default import handle_default
from .types import DefaultHandlerCallable, HandlerCallable, HandlerResult, PayloadT


class HandlersRegistry:
    _handlers: dict[str, tuple[PayloadT, HandlerCallable]]
    _default_handler: DefaultHandlerCallable

    def __init__(self) -> None:
        self._handlers = {}
        self._default_handler = handle_default

    def set_default_handler(self, handler: DefaultHandlerCallable) -> None:
        self._default_handler = handler

    def add_handler(self, event: str, payload_cls: PayloadT, handler: HandlerCallable) -> None:
        self._handlers[event] = (payload_cls, handler)

    def register(self, event: str, payload_cls: PayloadT) -> Callable[[HandlerCallable], HandlerCallable]:
        def deco(func: HandlerCallable) -> HandlerCallable:
            self.add_handler(event, payload_cls, func)
            return func

        return deco

    async def handle(self, event: str, headers: WebhookHeaders, payload: bytes) -> HandlerResult:
        if event not in self._handlers:
            return await self._default_handler(event, headers, payload)

        payload_cls, handler = self._handlers[event]

        payload_parsed = payload_cls.parse_raw(payload)
        return await handler(headers, payload_parsed)
