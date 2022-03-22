from typing import Optional

import uvicorn
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadimages")
async def parse_image(image_id: str = Form(...), image_type: int = Form(...), rgb_image_array: bytes = Form(...), depth_to_rgb_image_array: bytes = Form(...)):
    print(image_id)
    print(image_type)
    print(len(rgb_image_array))
    print(len(depth_to_rgb_image_array))
    return {"l1": 2.0, "l2": 4.0, "l3": 6.0, "l4": 8.0, "l5": 10.0, "l6": 12.0,
    "l7": 14.0, "l8": 16.0, "l9": 18.0, "l10": 20.0, "l11": 22.0, "l12": 24.0}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

