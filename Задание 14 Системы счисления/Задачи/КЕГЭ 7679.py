def generator_loops():
    for x in range(0, 20):
        for y in range(0, 11):
            for t in range(1, 8):
                yield x, y, t


lst = []
for x, y, t in generator_loops():
    n1 = 1*20**2 + x*20 + y
    n2 = 3*11 + y
    n3 = 4*11 + y
    n4 = t*8 + 1
    if n3 - n4 == 0:
        continue
    else:
        total = (n1+n2)/(n3-n4)
        if total % 5 == 0:
            lst.append(total)
print(max(lst))


# 825
