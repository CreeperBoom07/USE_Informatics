def f(x, y, p):
    if x == y:
        return 1
    if x > y:
        return 0
    if p == 1:
        return f(x+2, y, 0) + f(x*3, y, 0)
    return f(x+2, y, 0) + f(x**2, y, 1) + f(x*3, y, 0)
print(f(2, 64, 0))
# 55
