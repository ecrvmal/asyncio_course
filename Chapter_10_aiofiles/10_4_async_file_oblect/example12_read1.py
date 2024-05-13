# Вот пример использования read1() с использованием библиотеки asyncio и aiofiles:

import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        while True:
            chunk = await f.read1(1024)
            if not chunk:
                break
            print(chunk)

asyncio.run(read_file('myfile.txt'))

