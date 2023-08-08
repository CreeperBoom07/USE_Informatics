def f(x, y):
    return (x+2*y > a) or (y < x) or (x < 30)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 150) for x in range(0, 150)):
        print(a)
