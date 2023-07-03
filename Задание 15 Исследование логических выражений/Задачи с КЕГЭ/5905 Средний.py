def f(x, y, z):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x*y*z > (a // 8))


for a in range(1, 1000):
    if all(f(x, y, z) for z in range(1, 100) for y in range(1, 100) for x in range(1, 100)):
        print(a)

# 63
