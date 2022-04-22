from fastapi import FastAPI
from pydantic import BaseModel




class Data(BaseModel):
    x: float
    y: float




app = FastAPI()



@app.get("/")
async def main():
    return {
        "message": "Hello Deta"
    }


@app.post("/")
async def calc(data: Data):
    z = data.x * data.y
    
    return {
        "result": z
    }



"""
uvicorn deploy_api.main:app --reload
"""