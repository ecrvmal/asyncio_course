# Открытие файла с использованием пользовательских прав доступа
# (только для Unix-подобных систем):

import os

def custom_mode_opener(file, flags):
    return os.open(file, flags, mode=0o644)  # права доступа rw-r--r--

with open('example.txt', 'w', opener=custom_mode_opener) as f:
    f.write('Hello, world!')

