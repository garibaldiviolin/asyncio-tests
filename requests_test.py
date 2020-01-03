import requests
import time


def run(begin, end):
    url = "http://localhost:8000/v3/address/zipcode/{}/"

    session = requests.Session()
    for i in range(begin, end):
        response = session.get(url.format(i))
        x = response.json()


s = time.perf_counter()
run(1_000_000, 1_001_000)
elapsed = time.perf_counter() - s
print(f"{__file__} executed in {elapsed:0.2f} seconds.")
