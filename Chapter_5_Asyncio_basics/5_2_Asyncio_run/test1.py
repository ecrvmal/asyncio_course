# Задача: Напишите асинхронный код, который имитирует обработку логов событий сервера.
# Каждое событие имеет свою уникальную задержку обработки(на ответ сервера).

import asyncio

log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Запрос на выход", "delay": 2.0},
    {"event": "Ошибка авторизации", "delay": 2.5},
    {"event": "Успешное соединение с БД", "delay": 3.0},
    {"event": "Ошибка соединения с БД", "delay": 3.5},
    {"event": "Запрос к API", "delay": 4.0},
    {"event": "Ошибка запроса к API", "delay": 4.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0},]

async def fetch_log(event):
    await asyncio.sleep(event["delay"])
    event_name=f'{event["event"]}'
    event_delay=f'{event["delay"]}'
    print(f"Событие: '{event_name}' обработано с задержкой {event_delay} сек.")

async def main():
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    await asyncio.gather(*tasks)

asyncio.run(main())



