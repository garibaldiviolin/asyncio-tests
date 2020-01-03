"""Comparison of fetching web pages sequentially vs. asynchronously
Requirements: Python 3.5+, Requests, aiohttp, cchardet
For a walkthrough see this blog post:
http://mahugh.com/2017/05/23/http-requests-asyncio-aiohttp-vs-requests/
"""
import asyncio
from timeit import default_timer

from aiohttp import ClientSession
import requests

BEGIN = 2_000_000
END = 2_005_000


def demo_sequential(url):
    """Fetch list of web pages sequentially."""
    start_time = default_timer()
    for i in range(BEGIN, END):
        start_time_url = default_timer()
        _ = requests.get(url.format(i))
        elapsed = default_timer() - start_time_url
        # print('{0:30}{1:5.2f} {2}'.format(url, elapsed, asterisks(elapsed)))
    return default_timer() - start_time


def demo_async(url):
    """Fetch list of web pages asynchronously."""
    start_time = default_timer()

    loop = asyncio.get_event_loop()  # event loop
    future = asyncio.ensure_future(fetch_all(url))  # tasks to do
    loop.run_until_complete(future)  # loop until done

    return default_timer() - start_time


async def fetch_all(url):
    """Launch requests for all web pages."""
    tasks = []
    fetch.start_time = dict()  # dictionary of start times for each url
    async with ClientSession() as session:
        for i in range(BEGIN, END):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)  # create list of tasks
        _ = await asyncio.gather(*tasks)  # gather task responses


async def fetch(url, session):
    """Fetch a url, using specified ClientSession."""
    fetch.start_time[url] = default_timer()
    async with session.get(url) as response:
        resp = await response.read()
        elapsed = default_timer() - fetch.start_time[url]
        # print('{0:30}{1:5.2f} {2}'.format(url, elapsed, asterisks(elapsed)))
        return resp


def asterisks(num):
    """Returns a string of asterisks reflecting the magnitude of a number."""
    return int(num * 10) * '*'


if __name__ == '__main__':
    URL = 'http://localhost:8000/v3/address/zipcode/{}/'
    sequencial_time = demo_sequential(URL)
    async_time = demo_async(URL)

    print(' TOTAL SECONDS: '.rjust(30, '-') + '{0:5.2f} {1}'.format(
        sequencial_time, asterisks(sequencial_time)) + '\n'
    )
    print(' WITH ASYNCIO: '.rjust(30, '-') + '{0:5.2f} {1}'.format(
        async_time, asterisks(async_time)
    ))
