from ollama import chat

from app.config import OLLAMA_MODEL
from app.prompts import SYSTEM_PROMPT


class ModerationService:

    async def moderate(self, text: str):

        response = chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response["message"]["content"]