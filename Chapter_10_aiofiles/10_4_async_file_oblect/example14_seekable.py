# Вот пример использования f.seekable() с aiofiles:

import aiofiles

async def check_seekable(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        if await f.seekable():
            print(f"{file_path} supports random access.")
        else:
            print(f"{file_path} does not support random access.")

# Используйте asyncio для запуска функции
import asyncio
asyncio.run(check_seekable('your_file.txt'))


