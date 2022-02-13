import logging
from typing import Optional

from github_webhooks.schemas import WebhookCommonPayload, WebhookHeaders


class PingPayload(WebhookCommonPayload):
    zen: str
    hook_id: int


async def handle_ping(payload: PingPayload, headers: WebhookHeaders) -> Optional[str]:
    logging.debug('ping event, headers: %s, payload: %s', headers, payload)
    return 'OK'
