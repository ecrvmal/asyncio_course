import asyncio

total_requests: int = 0
sem = asyncio.Semaphore(3)

async def server_request(name):
    global total_requests

    async with sem:
        print(f'Пользователь {name} делает запрос')
        total_requests += 1
        await asyncio.sleep(0.1)
        print(f'Запрос от пользователя {name} завершен')
        print(f'Всего запросов: {total_requests}')

async def main():
    users = ["sasha", "petya", "masha", "katya", "dima",
             "olya", "igor", "sveta", "nikita", "lena",
             "vova", "yana", "kolya", "anya", "roma",
             "nastya", "artem", "vera", "misha", "liza"]

    tasks =[server_request(name) for name in users]
    await asyncio.gather(*tasks)


asyncio.run(main())