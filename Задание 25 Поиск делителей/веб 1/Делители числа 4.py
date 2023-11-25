def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(135790, 163228+1):
    d = f(x)
    if sum(d) > 460_000:
        print(len(d), sum(d))
##142 473759
##118 462767
##126 464999
##118 461969
##118 477071
