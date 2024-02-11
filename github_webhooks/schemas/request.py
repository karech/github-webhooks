from typing import Optional

from pydantic import BaseModel, Field

from .objects import Organization, Repository, User


class WebhookHeaders(BaseModel):
    event: str = Field(alias='x-github-event')
    hook_id: int = Field(alias='x-github-hook-id')
    delivery: str = Field(alias='x-github-delivery')
    signature: Optional[str] = Field(alias='x-hub-signature')
    signature_256: Optional[str] = Field(alias='x-hub-signature-256')


class WebhookCommonPayload(BaseModel):
    sender: User
    repository: Optional[Repository]
    organization: Organization | None = None
