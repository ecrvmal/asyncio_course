import asyncio
import random
import types

async def coro(name: str) -> None:
    print(f'task "{name}" started')
    await asyncio.sleep(random.randint(2, 6))
    print(f'task "{name}" completed')


async def main() -> None:
    tasks: list[asyncio.Task] = []
    for i in range(1,6):
        task = asyncio.create_task(coro(name=f'task_{i}'))
        # print(type(task))      # asyncio.Task
        tasks.append(task)
    print('All tasks created')

    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        print(f'tasks done:{len(done)}, tasks left: {len(tasks)}')
        for task in done:
            print(f'task {task.get_name()} completed, status done: {task.done()}')


asyncio.run(main())