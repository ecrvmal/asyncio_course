import asyncio


async def add_one(num: int) -> int:
    return num + 1


async def main() -> None:
    # Приостановка main() до получения результатов работы add_one(1).
    one_plus_one = await add_one(1)
    # Приостановка main() до получения результатов работы two_plus_one(2).
    two_plus_one = await add_one(2)
    print(f'{one_plus_one=}')
    print(f'{two_plus_one=}')


asyncio.run(main())