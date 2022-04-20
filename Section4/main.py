from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}



if __name__ == "__main__":
    uvicorn.run(app)


    # OR
    # uvicorn main:app --reload