from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI()



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

"""
{
  "name": "shoes",
  "description": null,
  "price": 122,
  "tax": null
}

{
  "name": "shoes",
  "description": "some description",
  "price": 122,
  "tax": 1.2
}



"""


@app.post("/items/")
async def create_item(item: Item):
    # return item
    return {
        "message": f"{item.name} has total price with tax: {int(item.price*item.tax)}"
    }




if __name__ == "__main__":
    #uvicorn.run(app, reload = True)
    uvicorn.run("main:app", reload = True)


    # OR from command line
    # uvicorn main:app --reload