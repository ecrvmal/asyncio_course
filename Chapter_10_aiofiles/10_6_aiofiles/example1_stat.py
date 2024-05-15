# Пример использования aiofiles.os.stat():

import asyncio

import aiofiles.os as aos

async def print_file_info(file_path):
    file_info = await aos.stat(file_path)
    print(file_info)


asyncio.run(print_file_info('myfile.txt'))