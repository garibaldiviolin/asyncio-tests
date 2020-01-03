from time import monotonic
import asyncio

import aiofiles


def sync_read_file(path):
    line_counter = 0
    with open(path) as file:
        while True:
            x = file.readline()
            if not x:
                print('line_counter={}'.format(line_counter))
                return
            line_counter += 1


async def async_read_file(path):
    line_counter = 0
    async with aiofiles.open(path) as file:
        while True:
            x = await file.readline()
            if not x:
                print('line_counter={}'.format(line_counter))
                return
            # print(x, end='')
            line_counter += 1


async def main():
    tasks = [async_read_file('aaa.txt'), async_read_file('bbb.txt')]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
start = monotonic()
loop.run_until_complete(main())
end = monotonic()
print('Async time={}'.format(end - start))
loop.close()


start = monotonic()
sync_read_file('aaa.txt')
sync_read_file('bbb.txt')
end = monotonic()
print('Synchronous time={}'.format(end - start))
