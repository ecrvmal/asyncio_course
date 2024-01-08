import aiohttp
import asyncio

async def fetch_data(url):                           # Определяем асинхронную функцию для получения данных с указанного URL
    async with aiohttp.ClientSession() as session:   # Создаем асинхронную сессию HTTP запросов, используя модуль aiohttp для оптимального управления ресурсами
        async with session.get(url) as response:     # Осуществляем асинхронный GET запрос к URL, чтобы не блокировать выполнение других операций
            return await response.text()             # Возвращаем текстовые данные ответа, используем await, чтобы дождаться полного получения данных

async def main():                                    # Определяем асинхронную функцию, которая будет запускаться при выполнении программы
    data = await fetch_data('http://python.org')     # Получаем данные с сайта python.org, используем await, чтобы дождаться получения данных
    print(data)                                      # Выводим полученные данные

asyncio.run(main())                                  # Запускаем асинхронную функцию main(), используя asyncio.run для создания и выполнения нового событийного цикла