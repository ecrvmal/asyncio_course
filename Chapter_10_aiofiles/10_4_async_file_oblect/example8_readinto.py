# Вот пример использования f.readinto(b):

import asyncio
import aiofiles

async def main():
    ba = bytearray(10)  # Создайте байтовый массив для хранения данных
    async with aiofiles.open('myfile.bin', mode='rb') as f:
        num_bytes = await f.readinto(ba)
        print(f'Считать {num_bytes} байт в байтовый массив.')

asyncio.run(main())
