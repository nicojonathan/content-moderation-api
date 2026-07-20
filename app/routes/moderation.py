from fastapi import APIRouter
from app.schemas import ModerationRequest
from app.services.moderation import ModerationService

router = APIRouter()
service = ModerationService()


@router.post("/moderate")
async def moderate(request: ModerationRequest):
    result = await service.moderate(request.text)

    return {
        "response": result
    }