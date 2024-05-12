# Вот пример использования параметра buffering:

import asyncio
import aiofiles


async def main():
    # Буферизация отключена, используется режим чтения бинарных данных
    async with aiofiles.open('myfile.txt', mode='rb', buffering=0) as f:
        data = await f.read()
        print(data)  # Увидим бинарные данные файла

    # Буферизация отключена, но приведет к ошибке
    try:
        async with aiofiles.open('myfile.txt', mode='r', buffering=0) as f:
            data = await f.read()
            print(data)
    except ValueError as eq:
        print(f"Обнаружена ошибка: {eq}")

    # Строковый буфер
    async with aiofiles.open('myfile.txt', mode='r', buffering=1) as f:
        print(await f.read())

    # Буферизация блока с размером буфера 4096
    async with aiofiles.open('myfile.txt', mode='r', buffering=4096) as f:
        print(await f.read())


asyncio.run(main())

# output /example11_buffering.py
# b'Hello'
# Обнаружена ошибка: can't have unbuffered text I/O
# Hello
# Hello
#
# Process finished with exit code 0
