import asyncio


async def generate(num):
    print(f'Корутина generate с аргументом {num}')


async def main():
    for i in range(10):
        await generate(i)


asyncio.run(main())
