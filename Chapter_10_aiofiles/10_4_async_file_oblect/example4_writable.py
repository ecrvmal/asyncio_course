# Вот пример использования f.writable():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        print(f'File is writable: {await f.writable()}')

asyncio.run(main())

# >>> File is writable: True
