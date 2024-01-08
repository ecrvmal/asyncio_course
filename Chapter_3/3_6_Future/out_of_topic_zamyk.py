def func_b(y):
    def func_a (x):
        return x*2 + y*3
    return func_a

b = func_b(5)

print ( b(7))         # 29