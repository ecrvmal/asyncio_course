import aiofiles
import os

def custom_opener(file, flags):
    return os.open(file, flags | os.O_NONBLOCK)

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', opener=custom_opener) as f:
        content = await f.read()
    return content
