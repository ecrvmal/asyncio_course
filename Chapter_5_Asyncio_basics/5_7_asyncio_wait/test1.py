# определения самого быстрого процессора из предложенного списка
# Код должен вывести только одну строку с самым быстрым процессором.

# Полный словарь вшит в задачу

processors_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 1.53,
}

import asyncio

async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = []
    for key, value in processors_delays.items():
        task = asyncio.create_task(simulate_processing(value), name=key)
        tasks.append(task)
    done, pending = await asyncio.wait(tasks, timeout=2, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"Первый завершенный процесс: {task.get_name()}")


asyncio.run(main())
