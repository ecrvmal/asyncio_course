async def some_coroutine():
    await lock.acquire()
    try:
        # код, который требует эксклюзивного доступа к общим ресурсам
    finally:
        lock.release()

