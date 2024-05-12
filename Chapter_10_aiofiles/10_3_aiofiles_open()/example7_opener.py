# Открытие файла с эксклюзивным доступом (только для Unix-подобных систем):

import os

def exclusive_opener(file, flags):
    return os.open(file, flags | os.O_EXCL)

with open('example.txt', 'w', opener=exclusive_opener) as f:
    f.write('Hello, world!')
