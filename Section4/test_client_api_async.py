

import asyncio
import json
import aiohttp




async def main():
    URL = "http://127.0.0.1:8000/items/"

    body = {
        "name": "sepatu",
        "description": "sepatu gunung",
        "price": 120,
        "tax": 2.3
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(URL, json=body) as resp:
            print(resp.status)
            print(await resp.json())

 


if __name__ == "__main__":
    asyncio.run(main())


