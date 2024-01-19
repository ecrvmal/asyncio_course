def outer(x):
    def inner(y):
        return x*y
    return inner

a = outer(7)

print(type(a))
print(a(2))







