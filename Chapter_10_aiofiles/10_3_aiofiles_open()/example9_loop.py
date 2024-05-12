import asyncio
import aiofiles

async def main():
    loop = asyncio.get_running_loop()
    async with aiofiles.open('example.txt', mode='r', loop=loop) as f:
        content = await f.read()
    print(content)

asyncio.run(main())