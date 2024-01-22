import asyncio

# Корутина для создания задач
async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


# Базовая корутина
async def main():
    async with asyncio.TaskGroup() as group:
        [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 6)]

    print('Все задачи были выполнены!')


asyncio.run(main())