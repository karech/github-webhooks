import logging
from typing import Optional

from github_webhooks.schemas import WebhookHeaders
from starlette.requests import QueryParams

async def handle_default(event: str, payload: bytes, headers: WebhookHeaders, query_params: QueryParams) -> Optional[str]:
    logging.debug('Default handler for <%s> event, headers: %s, payload: %s, query_params: %s', event, headers, payload, query_params)
    return 'OK'
