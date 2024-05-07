# Напишите асинхронный код для распределения пациентов по специалистам-врачам в медицинском центре.
# Код должен управлять очередями пациентов, где каждый пациент имеет направление к врачу определенного профиля.
# Всего должно быть 3 очереди.
#
# Разработка асинхронного кода для управления очередями пациентов:
#
# Каждый пациент описан в словаре с информацией о его имени, направлении к специалисту и процедуре.
# Пациенты должны быть распределены по трем различным очередям в зависимости от их направления:
# к терапевту, хирургу и ЛОРу.


import asyncio

patient_info = [
        {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
        {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
        {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
        {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
        {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
        {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
        {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
        {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
        {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
        {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
    ]


async def producer(queues):
    queue_therapist, queue_surgeon, queue_throat = queues
    for patient in patient_info:
        await asyncio.sleep(0.5)
        print(f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")
        if patient['direction'] == 'Терапевт':
            await queue_therapist.put(patient)
            await asyncio.create_task(consumer(queue_therapist, 'Терапевт'))
        elif patient['direction'] == 'Хирург':
            await queue_surgeon.put(patient)
            await asyncio.create_task(consumer(queue_surgeon, 'Хирург'))
        else: # patient['direction'] == 'ЛОР':
            await queue_throat.put(patient)
            await asyncio.create_task(consumer(queue_throat, 'ЛОР'))


async def consumer(queue, doctor_type):
    await asyncio.sleep(0.5)
    patient = await queue.get()
    print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")


async def main():
    queue_therapist = asyncio.Queue()
    queue_surgeon = asyncio.Queue()
    queue_throat = asyncio.Queue()
    queues = (queue_therapist , queue_surgeon, queue_throat)
    await asyncio.gather(producer(queues))


asyncio.run(main())