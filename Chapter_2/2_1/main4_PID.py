import time
import os

print(f'Программа запущена в процессе PID {os.getpid()}')
print('Программа спит')
time.sleep(20)
print('Программа завершена')