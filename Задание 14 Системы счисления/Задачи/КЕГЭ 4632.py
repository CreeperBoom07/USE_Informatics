def f(num):
    s = ''
    while num:
        s = str(num % 9) + s
        num //= 9
    return s


for x in range(1, 1000):
    n = 9**1942 + 9*6**971 + 214 - x
    n_9 = f(n)
    if abs(n_9.count('2')-n_9.count('8')) == 471:
        print(x)
        break

# 215
