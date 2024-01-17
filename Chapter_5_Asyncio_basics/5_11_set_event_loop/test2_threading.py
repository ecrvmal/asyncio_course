import asyncio
import threading


async def task_func(id1: int) -> None:
    print(f'task {id1} starting at loop {id(asyncio.get_running_loop())}')
    await asyncio.sleep(id1)
    print(f'task {id1} ended at loop {id(asyncio.get_running_loop())}')

def thr_task(loop, coro):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro)

async def main():
    print(f'current loop : {id(asyncio.get_running_loop())}')
    loop1 = asyncio.new_event_loop()
    print(f'loop 1 creaated with id : {id(loop1)}')
    loop2 = asyncio.new_event_loop()
    print(f'loop 2 creaated with id : {id(loop2)}')

    task1 = task_func(1)
    task2 = task_func(5)

    thr1 = threading.Thread(target=thr_task, args=(loop1, task1))
    thr2 = threading.Thread(target=thr_task, args=(loop2, task2))

    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()


asyncio.run(main())
