def p(x):
    return 150 <= x <= 390


def q(x):
    return 440 <= x <= 570


def f(x, a1, a2):
    return (p(x) <= (a1 <= x <= a2)) and (q(x) <= (a1 <= x <= a2))


m = 10**8
for a1 in range(100, 600):
    for a2 in range(a1+1, 600):
        if all(f(x, a1, a2) for x in range(100, 600)):
            m = min(m, a2-a1)

print(m//10)

# 42
