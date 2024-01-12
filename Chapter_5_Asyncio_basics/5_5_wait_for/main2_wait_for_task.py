import asyncio

async def long_running_task():
    # Эмуляция долгой задачи
    await asyncio.sleep(10)

async def main():
    # Создаем задачу
    task = asyncio.create_task(long_running_task())

    try:
        # Ожидаем завершения задачи в течение 5 секунд
        await asyncio.wait_for(task, timeout=5)
    except asyncio.TimeoutError:
        print("Задача не была завершена в установленное время")

asyncio.run(main())
