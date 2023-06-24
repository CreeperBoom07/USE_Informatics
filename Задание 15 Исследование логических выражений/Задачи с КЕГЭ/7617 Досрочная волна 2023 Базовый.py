def f(x, y):
    return (x >= 9) or (2*x < y) or (x*y < a)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 250) for x in range(0, 250)):
        print(a)
        break

# 129
