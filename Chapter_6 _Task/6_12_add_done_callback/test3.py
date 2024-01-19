import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


def run_decode(task):
    msg = task.result()
    ind = messages.index(msg)
    code = codes[ind]
    if int(code[-1],16)%2 == 0:
        print(f'Сообщение: Неверный код, сообщение скрыто')
        print(f'Код: {code}')
    else:
        print(f'Сообщение: {task.result()}')
        print(f'Код: {code}')


async def send_message(txt):
    await asyncio.sleep(0.2)
    return txt


async def main():

    for mess in messages:
        task = asyncio.create_task(send_message(mess))
        task.add_done_callback(run_decode)
        await task


asyncio.run(main())

# result:
# Sample Output:
#
# Сообщение: Привет, мир!
# Код: 56FF4D
# Сообщение: Как дела?
# Код: A3D2F7
# Сообщение: Что нового?
# Код: B1C94E
# Сообщение: Добрый день!
# Код: F56A1D
# Сообщение: Пока!
# Код: D4E6F1
