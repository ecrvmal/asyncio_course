# Вот пример использования f.write(string):

import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        num_chars = await f.write('Hello, world!')
        print(f'Записано {num_chars} символов в файл.')

asyncio.run(main())

# >>> Записано 13 символов в файл.
