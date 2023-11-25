def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

#print(106732561**0.25) # 101
#print(152673836**0.25) # 112

for x in range(102, 111):
    d = f(x**4)
    if len(d) == 3:
        print(x**4, x**3)
