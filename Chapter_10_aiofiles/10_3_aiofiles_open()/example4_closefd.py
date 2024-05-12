# Пример использования параметра closefd:

import os
import aiofiles

# Открываем файл и получаем файловый дескриптор
fd = os.open('example.txt', os.O_RDONLY)

async def read_from_file(fd):
    async with aiofiles.open(fd, mode='r', closefd=False) as f:
        content = await f.read()
    return content