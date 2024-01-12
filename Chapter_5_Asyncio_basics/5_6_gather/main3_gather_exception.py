import asyncio

async def my_coro1():             # Определяем асинхронную функцию (корутину) my_coro1
    print("Корутина 1 началась")  # Выводим сообщение о начале работы корутины 1
    await asyncio.sleep(1)        # Используем асинхронный sleep, чтобы "приостановить" выполнение этой корутины на 1 секунду
    print("Корутина 1 raised exception")# Выводим сообщение о завершении работы корутины 1
    raise Exception("Error in coro 1")

async def my_coro2():             # Определяем асинхронную функцию (корутину) my_coro2
    print("Корутина 2 началась")  # Выводим сообщение о начале работы корутины 2
    await asyncio.sleep(2)        # Используем асинхронный sleep, чтобы "приостановить" выполнение этой корутины на 2 секунды
    print("Корутина 2 закончилась")# Выводим сообщение о завершении работы корутины 2

async def main():                 # Определяем основную асинхронную функцию main
    result = await asyncio.gather(my_coro1(), my_coro2(), return_exceptions=True) # Используем asyncio.gather, чтобы запустить обе корутины одновременно и дождаться их выполнения

    print(f'{result=} ')

asyncio.run(main())


# Вывод:
#
# Корутина 1 началась
# Корутина 2 началась
# Корутина 1 raised exception
# Корутина 2 закончилась
# a=Exception('Error in coro 1')
#  b=None
#
# result=[Exception('Error in coro 1'), None]