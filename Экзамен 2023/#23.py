def f(x, y):
    if x == y:
        return 1
    if x < y or x in (9, 16):
        return 0
    return f(x-1, y) + f(x-2, y) + f(x//3, y)

print(f(19, 3))
