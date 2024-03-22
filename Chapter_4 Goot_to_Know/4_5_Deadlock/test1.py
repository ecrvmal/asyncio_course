# Ваша задача — модифицировать исходный код так, чтобы устранить проблему условий гонки
# с помощью асинхронного замка asyncio.Lock().
# Код должен вывести корректное значение global_counter.

import asyncio

global_counter = 0

async def increment(lock):
    global global_counter
    await lock.acquire()
    temp = global_counter
    await asyncio.sleep(.01)
    global_counter = temp + 2.39
    lock.release()

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[increment(lock) for x in range(99)])

asyncio.run(main())
print(f"global_counter: {round(global_counter,2)}")

