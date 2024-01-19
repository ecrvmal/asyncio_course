import asyncio


async def simulate_async_operation():                   # Асинхронная функция, имитирующая асинхронную операцию (тренер занимается другими делами)
    await asyncio.sleep(3)


def notify_start_training(task):                        # Callback-функция, которая вызывается, когда тренировка начинается
    print("Тренировка начинается, идите в спортзал.")


def cancel_training(task):                              # Callback-функция, которая вызывается, когда тренировка отменяется
    print("Тренировка отменена.")


async def prepare_training():                           # Асинхронная функция для подготовки тренировки
    await simulate_async_operation()


async def main(is_training_scheduled):                  # Основная асинхронная функция
    task = asyncio.create_task(prepare_training())      # Создание задачи из асинхронной функции prepare_training
    task.add_done_callback(notify_start_training)       # Регистрация callback-функций
    task.add_done_callback(cancel_training)
    print(task)
    if is_training_scheduled:                           # Если тренировка назначена, удаляем callback-функцию cancel_training
        task.remove_done_callback(cancel_training)
    else:                                               # Если тренировка отменена, удаляем callback-функцию notify_start_training
        task.remove_done_callback(notify_start_training)
    await task                                          # Ждем завершения задачи

# Флаг для определения состояния тренировки:
# True - тренировка назначена
# False - тренировка отменена
asyncio.run(main(True))


# Вывод:
#
# # При передаче флага False в asyncio.run(main(False))
# Тренировка отменена.
#
# # При передаче флага True в asyncio.run(main(True))
# Тренировка начинается, идите в спортзал.
