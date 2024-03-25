import asyncio


async def monitor_cpu(status_list):
    for status in status_list:
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0.1)


async def monitor_memory(status_list):
    for status in status_list:
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0.1)


async def monitor_disk_space(status_list):
    for status in status_list:
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0.1)

async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]

    task_cpu = asyncio.create_task(monitor_cpu(status_list), name='CPU')
    task_memory = asyncio.create_task(monitor_memory(status_list), name='Память')
    task_disk_space = asyncio.create_task(monitor_disk_space(status_list), name='Дисковое пространство')
    await asyncio.gather(task_cpu, task_memory, task_disk_space)


asyncio.run(main())