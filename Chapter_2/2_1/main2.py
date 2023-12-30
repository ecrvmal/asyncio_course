import time

start = time.time()  # Время начала эксперимента!)

def sleeping(n):
    print(f'start operation# {n}: {time.time() - start:4f}')
    time.sleep(1)
    print(f'Long operation# {n} completed')

def main():
    # run 30 operations
    all_results = [sleeping(i) for i in range(1, 31)]
    print(f'completed {len(all_results)} operations')
    print(f'Programm completed in {time.time() - start:.4f} seconds')

main()
