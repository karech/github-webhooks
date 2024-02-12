import logging
from typing import Optional

from fastapi import BackgroundTasks
from starlette.requests import QueryParams

from github_webhooks.schemas import WebhookCommonPayload, WebhookHeaders


class PingPayload(WebhookCommonPayload):
    zen: str
    hook_id: int


async def handle_ping(
    payload: PingPayload, headers: WebhookHeaders, query_params: QueryParams, background_tasks: BackgroundTasks
) -> Optional[str]:
    logging.debug(
        'ping event, headers: %s, payload: %s, query_params: %s, background_tasks: %s',
        headers,
        payload,
        query_params,
        background_tasks,
    )
    return 'OK'
