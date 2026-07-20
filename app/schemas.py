# These models validate incoming requests and outgoing responses automatically.

from pydantic import BaseModel


class ModerationRequest(BaseModel):
    text: str


class ModerationResponse(BaseModel):
    allowed: bool
    category: str | None
    confidence: float
    reason: str | None