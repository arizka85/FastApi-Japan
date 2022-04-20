from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()


@app.get("/countries/")
# async def country(country_name: str = "indonesia", country_no: int = 62):
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }




if __name__ == "__main__":
    #uvicorn.run(app, reload = True)
    uvicorn.run("main:app", reload = True)


    # OR from command line
    # uvicorn main:app --reload