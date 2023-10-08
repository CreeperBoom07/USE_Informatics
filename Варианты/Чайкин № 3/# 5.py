def f(n):
    s = ''
    while n:
        s = str(n%6) + s
        n //= 6
    return s

lst = []
for n in range(1, 1000):
    R = f(n)
    if n % 4 == 0:
        R = R + R[:3]
    else:
        R = R + f((n%4)*3)
    if int(R, 6) < 119:
        lst.append(int(R, 6))
print(max(lst))
