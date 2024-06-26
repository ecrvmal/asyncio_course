# Напишите асинхронный код, который моделирует процесс регистрации и приема пациентов в поликлинике.
# Сценарий включает в себя две ключевые функции:
# producer(), который регистрирует пациентов и добавляет их в очередь, и consumer(),
# который обрабатывает каждого пациента, имитируя процесс их приема врачом.

import asyncio

# Список вшит в задачу, вставлять его в поле ответа не нужно
patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]


async def producer(queue):
    # patient_info = []
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queue.put(patient)
        print(f'Регистратор добавил в очередь: {patient}')
    await queue.put(None)

async def consumer(queue):
    while True:
        el = await queue.get()
        if el is None:
            break
        print(f'Врач принял пациента: {el}')

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())