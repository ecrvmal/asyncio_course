# Вот пример использования f.flush():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        await f.write('Hello, world!')
        await f.flush()

asyncio.run(main())

