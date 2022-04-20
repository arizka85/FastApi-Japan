from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
async def index():
    return {"message": "Hello World"}



# order path is important!!
@app.get("/countries/indonesia")
async def indo():
    return {"message", "This is Indonesia"}

# Path parameter
@app.get("/countries/{country_name}")
async def country(country_name: str):  #async def country(country_name: int):
    return {"country_name": country_name}


# @app.get("/countries/indonesia")
# async def indo():
#     return {"message", "This is Indonesia"}





if __name__ == "__main__":
    #uvicorn.run(app, reload = True)
    uvicorn.run("main:app", reload = True)


    # OR from command line
    # uvicorn main:app --reload