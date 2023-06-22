a = set()
p = {i for i in range(2, 13, 2)}
q = {i for i in range(3, 16, 3)}


def f(x):
    return (x in p) <= (((x in q) and (x not in a)) <= (x not in p))


for x in range(1, 1000):
    if not f(x):
        a.add(x)

print(a)
print(sum(a))

# 18
