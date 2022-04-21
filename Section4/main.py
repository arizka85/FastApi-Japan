from typing import Optional, List
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()



class ShopInfo(BaseModel):
  name: str
  location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
  shop_info: Optional[ShopInfo] = None  #shop_info: ShopInfo
  items: List[Item]






"""
Ex json output:


{
  "shopInfo": {
    "name": "ABC store",
    "location": "Surabaya"
  },
  "items": [
      {
        "name": "White shoes",
        "description": null,
        "price": 122,
        "tax": 1.2
      },
      {
        "name": "Black Shirt",
        "description": "Shirt with black color",
        "price": 15,
        "tax": 1.2
      }
  ]

}

"""


@app.post("/items/")
async def create_item(data: Data):
    # return item
    return {
        "data": data
    }




if __name__ == "__main__":
    #uvicorn.run(app, reload = True)
    uvicorn.run("main:app", reload = True)


    # OR from command line
    # uvicorn main:app --reload