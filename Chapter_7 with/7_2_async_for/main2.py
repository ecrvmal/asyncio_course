# Импортируем необходимые библиотеки: aiohttp для асинхронных HTTP-запросов и asyncio для работы с асинхронностью
import aiohttp
import asyncio


async def async_url_generator(urls):                                # Определяем асинхронный генератор async_url_generator, который принимает список URL-адресов
    for url in urls:                                                # Итерируемся по списку URL-адресов
        yield url                                                   # Возвращаем текущий URL-адрес с помощью оператора yield


async def fetch(session, url):                                      # Определяем асинхронную функцию fetch, которая принимает объект сессии и URL-адрес
    async with session.get(url) as response:                        # Выполняем асинхронный HTTP-запрос с помощью объекта сессии
        return await response.text()                                # Возвращаем текст ответа, дождавшись его загрузки


async def main():                                                   # Определяем асинхронную функцию main, которая является основной точкой входа в программу
                                                                    # Создаем список URL-адресов, к которым будем выполнять HTTP-запросы
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net',
    ]
    async with aiohttp.ClientSession() as session:                  # Создаем асинхронный контекстный менеджер сессии для выполнения HTTP-запросов
        async for url in async_url_generator(urls):                 # Итерируемся по URL-адресам с помощью асинхронного генератора async_url_generator
            content = await fetch(session, url)                     # Выполняем асинхронный HTTP-запрос с помощью функции fetch
            print(f'Fetched content from {url}: {content[:100]}')   # Выводим первые 100 символов содержимого ответа


asyncio.run(main())                                                 # Вызываем асинхронную функцию main с помощью asyncio.run()



