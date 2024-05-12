# Вот пример использования f.readlines():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        lines = await f.readlines()
        print(lines)

asyncio.run(main())

