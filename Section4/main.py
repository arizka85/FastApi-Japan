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




# Query parameter - required parameter!
"""
http://127.0.0.1:8000/negara/?country_name=indonesia&country_no=62
"""
# @app.get("/negara/")
# async def negara(country_name: str, country_no: int):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }


# Query parameter - default parameter!
"""
http://127.0.0.1:8000/negara/
http://127.0.0.1:8000/negara/?country_name=japan&country_no=1
"""
# @app.get("/negara/")
# async def negara(country_name: str = "indonesia", country_no: int = 62):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }



# Path parameter & Query parameter
@app.get("/negara/{country_name}")
async def negara2(country_name: str, city_name: str):  # async def negara2(country_name: str = "indonesia", city_name: str = "surabaya"):
    return {
        "country_name": country_name,
        "city_name": city_name
    }















if __name__ == "__main__":
    #uvicorn.run(app, reload = True)
    uvicorn.run("main:app", reload = True)


    # OR from command line
    # uvicorn main:app --reload