import logging
from typing import Optional

import uvicorn
from pydantic import BaseModel
from starlette.requests import QueryParams

from github_webhooks import create_app
from github_webhooks.schemas import WebhookCommonPayload


class PullPayload(WebhookCommonPayload):
    class Pull(BaseModel):
        title: str
        url: str

    action: str
    pull_request: Pull


class CommentPayload(WebhookCommonPayload):
    class Comment(BaseModel):
        url: str
        body: str

    action: str
    comment: Comment


# Init the App
app = create_app(secret_token='super-secret-token')


# Register new handler via deco
@app.hooks.register('pull_request', PullPayload)
async def handle_pull_request(payload: PullPayload, query_params: QueryParams) -> Optional[str]:
    logging.info(
        'PR <%s> opened by <%s>\nlink: %s',
        payload.pull_request.title,
        payload.sender.login,
        payload.pull_request.url,
    )
    return 'OK'


# define new async function event handling
async def handle_pull_request_review_comment(payload: CommentPayload) -> None:
    logging.info('PR comment by <%s>: <%s>', payload.sender.login, payload.comment.body)


# Register new handler via `add_handler` function
app.hooks.add_handler('pull_request_review_comment', CommentPayload, handle_pull_request)


if __name__ == '__main__':
    # start uvicorn server
    uvicorn.run(app)
