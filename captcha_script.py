import io
import os
import random
from typing import Tuple
import uvicorn
import requests

from fastapi import FastAPI, File, Form, UploadFile
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

app = FastAPI()

#font tayyor qilish / loading
roboto_url = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Black.ttf?raw=true'
roboto = requests.get(roboto_url, allow_redirects=True)



@app.get("/captcha")
async def generate_captcha():
    font = ImageFont.truetype(io.BytesIO(roboto.content), size=30)
    image = Image.new("RGB", (200, 50), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    number = random.randint(1000, 9999)
    draw.text((10, 10), str(number), font=font, fill=(0, 0, 0))
    for i in range(10):
        draw.line(
            (
                random.randint(0, 200),
                random.randint(0, 50),
                random.randint(0, 200),
                random.randint(0, 50),
            ),
            fill=(0, 0, 0),
            width=2,
        )
    #send image
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    return {"image": image_bytes.read(), "number": number}

@app.post("/validate")
async def validate_captcha(captcha: bytes = File(...), answer: str = Form(...)):
    return {"captcha": captcha, "answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=6060)
