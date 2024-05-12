import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r') as f:
        content = await f.read()
    return content