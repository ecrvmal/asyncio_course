import asyncio
import aiofiles

async def read_file_async(filename):
    async with aiofiles.open(filename, mode='r') as file:
        content = await file.read()
    return content

content = asyncio.run(read_file_async('myfile.txt'))
print(content)

