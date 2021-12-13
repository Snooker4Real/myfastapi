from fastapi import FastAPI

import uvicorn

from typing import Optional

from pydantic import BaseModel

app = FastAPI()


class CoordIn(BaseModel):
    password: str
    lat: float
    lon: float
    zoom: Optional[int] = None


class CoordOut(BaseModel):
    lat: float
    lon: float
    zoom: Optional[int] = None


# get, put, delete, patch, ...

# get
@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.post("/position/", response_model=CoordOut)
async def make_position(coord: CoordIn):
    # db write completed
    return coord


# @app.get("/component/{component_id}")  # path parameter/variable
# async def get_component(component_id: int):
#     return {"component_id": component_id}
#
#
# # http://127.0.0.1:8000/component/?number=42&text=vie
# @app.get("/component/")
# async def read_component(number: int, text: Optional[str]):
#     return {"number": number, "text": text}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8050, reload=True)
