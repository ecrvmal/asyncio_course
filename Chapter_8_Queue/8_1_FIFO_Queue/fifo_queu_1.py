from random import random
import asyncio


async def producer(queue):
    print('Производитель: Запущен')
    for i in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print('Производитель: Done')


async def consumer(queue):
    print('Потребитель: Запущен')
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'>Потребитель получил: {item}')
    print('Потребитель: Done')


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))



asyncio.run(main())