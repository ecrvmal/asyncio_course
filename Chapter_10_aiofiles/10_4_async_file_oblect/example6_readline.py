# Вот пример использования f.readline():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        line = await f.readline()
        print(line)

asyncio.run(main())
