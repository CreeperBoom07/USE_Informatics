def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
lst = []
for x in range(125_697, 125_721+1):
    d = [i for i in f(x) if p(i)]
    if len(d) == 2 and d[0]*d[1]==x:
        lst += [[d[0], d[1]]]
print(*sorted(lst, key=lambda y: y[0]*y[1]), sep='\n')
