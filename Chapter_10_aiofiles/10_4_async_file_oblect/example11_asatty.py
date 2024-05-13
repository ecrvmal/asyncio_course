# Вот пример использования f.isatty():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        print(f'Is file connected to a terminal: {await f.isatty()}')

asyncio.run(main())

