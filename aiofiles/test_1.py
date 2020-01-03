import asyncio
from pathlib import Path

import aiofiles as aiof

FILENAME = "foo.txt"


async def bad():
    async with aiof.open(FILENAME, "w") as out:
        out.write("hello world")
        out.flush()
    print("done")


async def good():
    async with aiof.open(FILENAME, "w") as out:
        await out.write("hello world")
        await out.flush()
    print("done")


loop = asyncio.get_event_loop()

server = loop.run_until_complete(bad())
print(Path(FILENAME).stat().st_size)  # prints 0

server = loop.run_until_complete(good())
print(Path(FILENAME).stat().st_size)  # prints 11
