'''
A - 10
B - 11
C - 12 => c/c p минимум 13
D - 13 => c/c q минимум 14
'''
def generator_loops():
    for p in range(13, 100):
        for q in range(14, 100):
            yield p, q


for p, q in generator_loops():
    n1 = 10*p**2 + 11*p + 12
    n2 = 11*q**2 + 12*q + 13
    if n1 == n2:
        print(p, q, n1)

# 41676






