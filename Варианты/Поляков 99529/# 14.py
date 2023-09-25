def f(num, osn):
    l = len(num)
    s = 0
    for i in range(0, l):
        s += int(num[i])*osn**(l-i-1)
    return s

k = 0

for x in range(6, 100):
    n1 = f('13152', x)
    n2 = f(f'7{x}25', 100)
    if (n1+n2) % 11 == 0:
        k += 1
print(k)
