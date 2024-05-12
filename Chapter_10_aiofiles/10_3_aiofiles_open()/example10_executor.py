# Вот пример использования параметра executor:

import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor

async def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        async with aiofiles.open('example.txt', mode='r', executor=executor) as f:
            content = await f.read()
        print(content)

asyncio.run(main())

