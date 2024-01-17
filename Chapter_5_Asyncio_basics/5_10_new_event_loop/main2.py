import asyncio
import threading

async def task1(id1, loop):
    print(f"Task {id1} starting, loop = {loop}")
    print(f"Task {id1} starting, loop = {asyncio.get_event_loop()}")
    print(f"Task {id1} starting, loop = {id(asyncio.get_running_loop())}")  # loop = 1983384279440
    await asyncio.sleep(2)
    print(f"Task {id1} completed")

async def task2(id1, loop):
    print(f"Task {id1} starting, loop = {loop}")
    print(f"Task {id1} starting, loop = {asyncio.get_event_loop()}")
    print(f"Task {id1} starting, loop = {id(asyncio.get_running_loop())}")  # loop = 1983384279824
    await asyncio.sleep(3)
    print(f"Task {id1} completed")

def start_loop(loop, coroutine):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)

async def main():
    loop1 = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()

    coroutine1 = task1(1, loop1)
    coroutine2 = task2(2, loop2)

    thread1 = threading.Thread(target=start_loop, args=(loop1, coroutine1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, coroutine2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

asyncio.run(main())

# output:
#
# Task 1 starting, loop = <ProactorEventLoop running=True closed=False debug=False>
# Task 1 starting, loop = <ProactorEventLoop running=True closed=False debug=False>
# Task 1 starting, loop = 1983384279440
# Task 2 starting, loop = <ProactorEventLoop running=True closed=False debug=False>
# Task 2 starting, loop = <ProactorEventLoop running=True closed=False debug=False>
# Task 2 starting, loop = 1983384279824
# Task 1 completed
# Task 2 completed