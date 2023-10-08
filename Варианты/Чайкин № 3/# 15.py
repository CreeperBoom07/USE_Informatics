def f(x, y):
    return (2*x + y < a) or (x > 15) or (y > 21)

for a in range(1000):
    if all(f(x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break
