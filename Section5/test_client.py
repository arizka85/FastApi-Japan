

import requests
import json


def main():
    # URL = "http://127.0.0.1:8000/"
    URL = "https://8hxo7h.deta.dev/"

    data = {
        "x": 10.5,
        "y": 5
    }


    resp = requests.post(URL, json.dumps(data))
    print(resp.status_code)
    print(resp.json())




if __name__ == "__main__":
    main()

