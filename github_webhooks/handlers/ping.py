import logging
from typing import Optional
from starlette.requests import QueryParams

from github_webhooks.schemas import WebhookCommonPayload, WebhookHeaders


class PingPayload(WebhookCommonPayload):
    zen: str
    hook_id: int


async def handle_ping(payload: PingPayload, headers: WebhookHeaders, query_params: QueryParams) -> Optional[str]:
    logging.debug('ping event, headers: %s, payload: %s, query_params: %s', headers, payload, query_params)
    return 'OK'
