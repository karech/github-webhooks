from typing import Any, Callable, Union, cast

from github_webhooks.schemas import WebhookHeaders

from .default import handle_default
from .types import AnyHandlerWithHeaders, AnyHandlerWithoutHeaders, DefaultHandler, Handler, HandlerResult, PayloadT


class HandlersRegistry:
    _handlers: dict[str, tuple[PayloadT, Handler]]
    _default_handler: DefaultHandler

    def __init__(self) -> None:
        self._handlers = {}
        self._default_handler = handle_default

    def set_default_handler(self, handler: DefaultHandler) -> None:
        self._default_handler = handler

    def add_handler(self, event: str, payload_cls: PayloadT, handler: Handler) -> None:
        self._handlers[event] = (payload_cls, handler)

    def register(self, event: str, payload_cls: PayloadT) -> Callable[[Handler], Handler]:
        def deco(func: Handler) -> Handler:
            self.add_handler(event, payload_cls, func)
            return func

        return deco

    async def handle(self, event: str, payload: bytes, headers: WebhookHeaders) -> HandlerResult:
        if event not in self._handlers:
            return await self._call_with_headers(self._default_handler, event, payload, headers=headers)

        payload_cls, handler = self._handlers[event]

        payload_parsed = payload_cls.parse_raw(payload)
        return await self._call_with_headers(handler, payload_parsed, headers=headers)

    @staticmethod
    async def _call_with_headers(
        handler: Union[DefaultHandler, Handler],
        *args: Any,
        headers: WebhookHeaders,
    ) -> HandlerResult:
        h_varnames = handler.__code__.co_varnames  # type: ignore

        if 'headers' in h_varnames:
            handler = cast(AnyHandlerWithHeaders, handler)
            return await handler(*args, headers=headers)

        handler = cast(AnyHandlerWithoutHeaders, handler)
        return await handler(*args)
