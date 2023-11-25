def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

for x in range(6_080_068, 6_080_176):
    if p(x):
        print(x)
