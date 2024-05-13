# Вот пример использования f.tell():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        print(await f.read(5))  # Читаем и печатаем 5 символов из файла
        position = await f.tell()
        print(f'Текущая позиция в файле: {position} bytes')

asyncio.run(main())


