
from typing import List, Dict


price: int = 100
tax: float = 1.1

def calculate_price_including_tax(price: int, tax: float) -> int:
    return int(price * tax)


sample_list: List[int] = [1,2,3,4]
sample_dict: Dict[str, str] = {"username": "abcd"}



if __name__ == "__main__":


    print(f"Rp.{calculate_price_including_tax(price, tax)}")

    print(sample_list)
    print(sample_dict)
