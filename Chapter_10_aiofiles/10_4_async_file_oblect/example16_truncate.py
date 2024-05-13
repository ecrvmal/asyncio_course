# Вот пример использования truncate() с помощью библиотеки asyncio и aiofiles:

import asyncio
import aiofiles

async def truncate_file():
    async with aiofiles.open('test.txt', mode='a+') as f:
        await f.write('Hello, world!')
        await f.flush()
        # Асинхронно сбрасываем буфер записи файла, чтобы убедиться,
        # что все данные записаны на диск.

        await f.seek(0)
        # Асинхронно перемещаем позицию в файле в начало файла.

        print(await f.read())
        # Асинхронно читаем все данные из файла и выводим их на экран.
        # Ожидается вывод 'Hello, world!'.

        await f.seek(0)
        # Асинхронно перемещаем позицию в файле в начало файла снова.

        await f.truncate(5)
        # Асинхронно обрезаем файл до первых 5 байт.

        await f.seek(0)
        # Асинхронно перемещаем позицию в файле в начало файла снова.

        print(await f.read())
        # Асинхронно читаем все данные из файла и выводим их на экран.
        # Теперь ожидается вывод 'Hello', так как мы обрезали файл до первых 5 байт.

asyncio.run(truncate_file())

