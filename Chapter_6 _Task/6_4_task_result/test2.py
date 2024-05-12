import asyncio

async def coroutine():
    await asyncio.sleep(.5)
    raise Exception('Произошла ошибка')

async def main():
    task = asyncio.create_task(coroutine())

    try:
        result = task.result()
        print(f'Результат: {result}')
    except Exception as e:
        print(f'Завершилось с ошибкой: {e}')

asyncio.run(main())