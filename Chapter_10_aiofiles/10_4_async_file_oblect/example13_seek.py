# Пример использования  f.seek():

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        await f.seek(10)  # Перемещаемся на 10-й байт в файле
        data = await f.read()  # Читаем остаток файла с этой позиции
        print(data)

asyncio.run(main())


