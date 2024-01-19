import asyncio


async def raise_exception():
    raise RuntimeError("--Установленное исключение--")      # Генерируем ошибку RuntimeError с сообщением "Произошла ошибка"


async def main():                                           # Определяем асинхронную функцию main
    task = asyncio.create_task(raise_exception())           # Создаем асинхронное задание, выполняющее функцию raise_exception()
    await asyncio.sleep(0.1)                                # Ожидаем 0.1 секунды, позволяя другим задачам выполняться
    try:                                                    # Обработка исключений в блоке try-except
        await task                                          # Ожидаем завершения задания task
    except Exception as e:                                  # Обработка исключения типа Exception
        print(f"Пойманное исключение: {e}")                 # Вывод сообщения с информацией о пойманном исключении
    exception = task.exception()                            # Получаем исключение, которое возникло во время выполнения задания (если оно возникло)
    if exception:                                           # Если исключение возникло, выводим его, или при необходимости обрабатываем
        print(f"Тут можно обработать возникшее исключение: {exception}")


asyncio.run(main())