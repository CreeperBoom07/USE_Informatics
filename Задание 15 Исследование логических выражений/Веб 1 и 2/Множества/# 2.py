from functools import reduce

a = set()
p = {i for i in range(2, 13, 2)}
q = {i for i in range(3, 16, 3)}

def f(x):
    P = x in p
    Q = x in q
    A = x in a
    return (not P) or ((not Q) <= A)


for x in range(1, 1000):
    if not f(x):
        a.add(x)

print(a)
print(reduce(lambda x, y: x*y, a, 1))
# 640
