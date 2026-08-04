from fastapi import APIRouter
from pydantic import BaseModel
import traceback

from services.text_generator import generate_caption
from services.image_generator import generate_image
from database.db import save_campaign

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    platform: str
    tone: str

@router.post("/generate")
async def generate_post(req: GenerateRequest):

    try:
        print("Received request:", req)

        caption = generate_caption(
            req.prompt,
            req.platform,
            req.tone
        )

        print("Caption generated")

        image_path = generate_image(req.prompt)

        print("Image generated:", image_path)

        save_campaign(
            req.prompt,
            req.platform,
            req.tone,
            caption,
            image_path
        )

        return {
            "caption": caption,
            "image_url": image_path
        }

    except Exception as e:
        print("ERROR:", str(e))
        traceback.print_exc()

        return {
            "caption": f"Error: {str(e)}",
            "image_url": ""
        }