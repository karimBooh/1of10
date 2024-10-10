import base64
import json

from fastapi import APIRouter, Depends, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from starlette.requests import Request

from api.db.database import get_db
from api.lib.groq.groq import feedback_tumbnail
from api.thumbnails.crud import create_thumbnails
from api.thumbnails.schema import ThumbnailCreate

router = APIRouter(prefix='/thumbnail')

def encode_image(image_content: bytes) -> str:
    return base64.b64encode(image_content).decode('utf-8')

@router.get("/")
def thumbnail() -> str:
    return "get"


@router.post("/feedback")
async def feedback(request: Request, thumbnail: UploadFile , db:Session=Depends(get_db)):
    image_content = await thumbnail.read()
    image_base64 = encode_image(image_content)
    message = feedback_tumbnail(image_base64)
    print(message)
    try:
        body = json.loads(message)
    except json.JSONDecodeError:
        return JSONResponse(content={"error": "Invalid JSON response from feedback_tumbnail"}, status_code=400)

    print(body)
    json_compatible_item_data = jsonable_encoder(message)
    create_thumbnails(db, ThumbnailCreate(image=image_base64, feedback= body.get("feedback", "")) )
    return JSONResponse(content=json_compatible_item_data)
