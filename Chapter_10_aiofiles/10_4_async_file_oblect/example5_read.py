# Вот пример использования f.read(n=-1):

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        contents = await f.read(5)
        print(contents)

asyncio.run(main())

