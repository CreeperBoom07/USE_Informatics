def f(x, y, p):
    if x == y:
        return 1
    if x > y:
        return 0
    if p == 1:
        return f(x+2, y, 0) + f(x+3, y, 0)
    else:
        return f(x+2, y, 0) + f(x+3, y, 0) + f(x*2, y, 0)
print(f(5, 30, 1))
# 580
