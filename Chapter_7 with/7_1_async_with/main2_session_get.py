import aiohttp
import asyncio


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:      # Используем async with для создания асинхронной сессии aiohttp
        async with session.get(url) as response:        # Используем async with для выполнения асинхронного GET-запроса
            content = await response.text()             # Читаем содержимое ответа асинхронно
            print(content)                              # Выводим содержимое ответа


asyncio.run(fetch_url('https://example.com'))           # Запускаем асинхронную функцию для получения содержимого веб-страницы
