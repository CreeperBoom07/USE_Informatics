def f(x, y):
    return (x >= 11) or (3*x < y) or (x*y < a)

for a in range(1000):
    if all(f(x, y) for y in range(150) for x in range(150)):
        print(a)
        break
