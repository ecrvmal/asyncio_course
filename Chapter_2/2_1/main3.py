import time
import asyncio

start = time.time()  # Время начала эксперимента!)

async def sleeping(n):
    print(f'start operation# {n}: {time.time() - start:4f}')
    await asyncio.sleep(1)
    print(f'Long operation# {n} completed')
    return f'result operation# : {n}'

async def main():
    # run 30 operations
    # all_results = [sleeping(i) for i in range(1, 31)]
    task = [sleeping(i) for i in range(1, 31)]
    all_results = await asyncio.gather(*task)
    print(f'completed {len(all_results)} operations')
    print(f'Programm completed in {time.time() - start:.4f} seconds')

# main()
asyncio.run(main())