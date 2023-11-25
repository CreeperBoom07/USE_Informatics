def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x == 15:
        return f(x//3, y) + f(x-5, y)
    return f(x//3, y) + f(x-5, y) + f(x-2, y)
print(f(32, 9))
# 36
