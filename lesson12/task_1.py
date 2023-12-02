from collections import deque
from typing import Any
import json


class Fractorial:
    def __init__(self, k):
        self.store = deque(maxlen=k)

    def __call__(self, number):
        result = 1
        for i in range(2, number + 1):
            result *= i
        self.store.append({number: result})
        return result

    def __str__(self) -> str:
        return f"{self.store}"

    def __enter__(self):
        return self

    def __exet__(self, exc_type, exv_val, exc_tb):
        with open("fact.json", "w") as f:
            json.dump(list(self.store), f, indent=2)


with Fractorial(3) as fact:
    fact(5)
    fact(3)
    fact(8)
