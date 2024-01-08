import asyncio
async def add_one(num: int) -> int:
    await asyncio.sleep(1)
    return num + 1

async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'


async def main() -> None:
    # Приостановка main() до выполнения hello_world_message/получения результатов ее работы.
    message = await hello_world_message()
    print(f'{message=}')
    # Приостановка main() до выполнения add_one/получения результатов ее работы.
    one_plus_one = await add_one(1)
    print(f'{one_plus_one=}')


asyncio.run(main())


