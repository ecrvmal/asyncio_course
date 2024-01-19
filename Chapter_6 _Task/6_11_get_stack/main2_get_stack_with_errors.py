import asyncio

async def foo():
    await asyncio.sleep(1)
    raise RuntimeError('Возникла ошибка')

async def main():
    await asyncio.gather(foo(), foo())

asyncio.run(main())