import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', encoding='windows-1251') as f:
        content = await f.read()
    return content