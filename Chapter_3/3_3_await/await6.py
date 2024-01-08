import asyncio


async def hello_world_message() -> str:
    # Имитация выполнения длительной I/O операции (1 секунда)
    await asyncio.sleep(1)
    return 'Hello World!'


async def main() -> None:
    # Приостановка main() до выполнения hello_world_message/получения результатов ее работы.
    message = await hello_world_message()
    print(f'{message=}')

asyncio.run(main())