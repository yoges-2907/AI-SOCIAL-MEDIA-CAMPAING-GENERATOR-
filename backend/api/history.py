from fastapi import APIRouter
from database.db import get_campaigns

router = APIRouter()

@router.get("/history")
async def history():

    rows = get_campaigns()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "prompt": row[1],
            "platform": row[2],
            "tone": row[3],
            "caption": row[4],
            "image_url": row[5],
            "created_at": row[6]
        })

    return result