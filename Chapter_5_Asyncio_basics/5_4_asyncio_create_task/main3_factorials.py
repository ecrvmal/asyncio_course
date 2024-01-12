import asyncio

async def factor(num: int):
    fact = 1
    for i in range(1,num+1):
        fact *=i
    await asyncio.sleep(1)
    print(f'fact calculated = {fact}')
    return fact


async def print_factorial(num: int):
    await asyncio.sleep(1)
    result = await factor(num)
    print(f'printing {result}')

async def main():
    task1 = asyncio.create_task(print_factorial(5))
    task2 = asyncio.create_task(factor(4))
    await task1
    await task2

asyncio.run(main())