import asyncio

async def task(lock, name):
    print(f"{name} пытается захватить мьютекс.")
    async with lock:
        print(f"{name} начал выполнение.")
        await asyncio.sleep(1)
    print(f"{name} завершил выполнение.")

async def main():
    lock = asyncio.Lock()
    tasks = [task(lock, f"Task {i}") for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())
#
# Task 1 пытается захватить мьютекс.
# Task 1 начал выполнение.
# Task 2 пытается захватить мьютекс.
# Task 3 пытается захватить мьютекс.
# Task 1 завершил выполнение.
# Task 2 начал выполнение.
# Task 2 завершил выполнение.
# Task 3 начал выполнение.
# Task 3 завершил выполнение.