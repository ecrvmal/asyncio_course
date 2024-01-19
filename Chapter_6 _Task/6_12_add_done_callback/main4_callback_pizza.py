import asyncio
import random


async def prepare_pizza():  # Асинхронная функция для имитации приготовления пиццы
    print("Готовим пиццу...")
    await asyncio.sleep(5)  # Имитация времени на приготовление пиццы
    return "Пицца готова!"


def notify_delivery(task):  # Callback-функция для уведомления о доставке пиццы
    print(f"{task.result()} \n Курьер: Ваш заказ доставлен!")


def cancel_notification(task):  # Callback-функция для отмены уведомления о доставке
    print(f"{task.result()} \n Курьер: Уведомление отменено, заберите пиццу самостоятельно.")


async def main():  # Основная асинхронная функция
    task = asyncio.create_task(prepare_pizza())  # Создание задачи из асинхронной функции prepare_pizza
    task.add_done_callback(notify_delivery)  # Регистрация callback-функций
    task.add_done_callback(cancel_notification)
    if random.choice([True, False]):  # Вероятность отмены уведомления (50%)
        print('Доставка подтверждена, везём пиццу')
        task.remove_done_callback(cancel_notification)  # Отмена уведомления об отмене доставки
    else:
        print('Доставка отменена, самовывоз')
        task.remove_done_callback(notify_delivery)  # Отмена уведомления о доставке

    await task


asyncio.run(main())

# Доставка подтверждена, везём пиццу
# Готовим пиццу...
# Пицца готова!
#  Курьер: Ваш заказ доставлен!