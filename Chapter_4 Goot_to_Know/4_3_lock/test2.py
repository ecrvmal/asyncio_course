# Что произойдет при возникновении исключения в "Task 1"?

import asyncio

async def task(lock, name):
    try:
        await lock.acquire()
        print(f"{name} захватил мьютекс.")
        await asyncio.sleep(1)
        if name == "Task 1":
            raise Exception("Ошибка в задаче 1")
    finally:
        lock.release()
        print(f"{name} освободил мьютекс.")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(task(lock, "Task 1"), task(lock, "Task 2"), return_exceptions=True)

asyncio.run(main())


# Task 1 захватил мьютекс.
# Task 1 освободил мьютекс.
# Task 2 захватил мьютекс.
# Task 2 освободил мьютекс.