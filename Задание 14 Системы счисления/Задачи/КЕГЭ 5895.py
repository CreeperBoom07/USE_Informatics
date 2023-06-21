def generator_loops():
    for y in range(9, 16):
        for x in range(0, y):
            yield x, y


s = set()
for x, y, in generator_loops():
    n1 = 5*16**3 + x*16**2 + y*16 + 12
    n2 = 8*y**3 + x*y**2 + x*y + 7
    s.add(n1+n2)
print(len(s))

# 84
