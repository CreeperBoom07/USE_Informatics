def f(n):
    s = ''
    while n:
        s = str(n%6) + s
        n //= 6
    return s
lst = []
for n in range(1, 1000):
    R = f(n)
    if n % 3 == 0:
        R = R + R[:2]
    else:
        R = R + f((n%3)*10)

    if int(R, 6) > 680:
        lst.append(int(R, 6))
print(min(lst))
