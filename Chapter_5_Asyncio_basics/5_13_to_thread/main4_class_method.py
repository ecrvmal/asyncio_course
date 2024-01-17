import asyncio
import threading
import time

class MyProcessor:
    def process_data(self, data):
        print(f"Обработка данных \"{data}\" в потоке c id {threading.current_thread().ident}")
        time.sleep(2)  # Имитация длительной операции
        return f"Обработанные данные: {data}"

async def main():
    processor = MyProcessor()
    data = "Какие-то данные"
    print(f"Старт main в потоке с id {threading.current_thread().ident}")
    result = await asyncio.to_thread(processor.process_data, data)
    print(result)

asyncio.run(main())

#
# output:
# Старт main в потоке с id 23176
# Обработка данных "Какие-то данные" в потоке c id 14268
# Обработанные данные: Какие-то данные
