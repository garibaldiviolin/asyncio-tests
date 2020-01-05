# aiohttp_test.py
from aiohttp import ClientSession

import asyncio
import time


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.json()


async def run(begin, end):
    url = "http://localhost:8000/v3/address/zipcode/{}/"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(begin, end):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        # print(responses)


def print_responses(result):
    print(result)


loop = asyncio.get_event_loop()
s = time.perf_counter()
future = asyncio.ensure_future(run(1_000_000, 1_001_000))
loop.run_until_complete(future)
elapsed = time.perf_counter() - s
print(f"{__file__} executed in {elapsed:0.2f} seconds.")
