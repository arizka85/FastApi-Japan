

from time import sleep
import requests
import json




def main():
    URL = "http://127.0.0.1:8000/items/"
    body = {
        "name": "sepatu",
        "description": "sepatu gunung",
        "price": 120,
        "tax": 2.3
    }

    resp = requests.post(URL, json.dumps(body))
    print(resp.json())




if __name__ == "__main__":
    # main()


    for r in range(3):
        main()
        sleep(r)
        