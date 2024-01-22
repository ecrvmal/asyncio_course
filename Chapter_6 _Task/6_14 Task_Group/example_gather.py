import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


# Базовая корутина
async def main():
    tasks = asyncio.gather(
        get_data(1),
        get_data(2),
        # Передаем имя несуществующего файла, чтобы вызвать ошибку
        file_reader('fake.png'),
        # Этот вызов тоже должен вызвать ошибку
        get_data(0),
        return_exceptions=True
    )
    result = await tasks
    print('Готово!!!', result)

asyncio.run(main())