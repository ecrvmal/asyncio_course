import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', errors='ignore') as f:
        content = await f.read()
    return content