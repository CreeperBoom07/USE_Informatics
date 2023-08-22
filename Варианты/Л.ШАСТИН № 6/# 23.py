def s_num(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

    
def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x-s_num(x), y) + f(x//2, y) + f(x-1, y)
print(f(40, 25) * f(25, 10))
