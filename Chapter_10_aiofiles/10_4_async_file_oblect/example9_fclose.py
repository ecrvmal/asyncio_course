# Вот пример использования f.close():

import asyncio
import aiofiles

async def main():
    f = await aiofiles.open('myfile.txt', mode='w')
    await f.write('Hello, world!')
    await f.close()

asyncio.run(main())