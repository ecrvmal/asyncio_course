# 1. рекомендуется всегда приобретать и освобождать блокировку в структуре try/finally.

# приобретаем блокировку
lock.acquire()                 # Метод acquire() используется для приобретения блокировки. Это необходимо, чтобы защитить критическую секцию кода от одновременного доступа нескольких корутин.

try:
    # критический участок кода...
    # Здесь выполняется код, который требует синхронизации доступа. Когда блокировка устанавлена, никакая другая корутина не может получить доступ к этому участку кода.
finally:
    # всегда освобождаем блокировку
    lock.release()              # Метод release() используется для освобождения блокировки после завершения работы с критическим участком кода. Это позволяет другим корутинам получить доступ к защищенному участку кода.

# 2. Менеджер контекста
# Устанавливаем блокировку
async with lock:  # Конструкция with автоматически устанавливает и освобождает блокировку. Это позволяет обеспечить безопасность кода при работе с ресурсами, которые требуют синхронизации доступа.
    # критический участок кода...
    # Здесь выполняется код, который требует синхронизации доступа. Когда блокировка приобретена, никакая другая корутина не может получить доступ к этому участку кода.


3. timeout

try:
    # пытаемся приобрести блокировку, ожидая не более 10 секунд
    await asyncio.wait_for(lock.acquire(), timeout=10)  # Метод wait_for() asyncio используется для ограничения времени ожидания при попытке приобретения блокировки. Это полезно в случаях, когда блокировка может быть не освобождена длительное время, и мы не хотим, чтобы наш код заблокировался навсегда, ожидая приобретения блокировки.
except asyncio.TimeoutError:
    # здесь обрабатываем ситуацию, когда время ожидания истекло
    # ... 
