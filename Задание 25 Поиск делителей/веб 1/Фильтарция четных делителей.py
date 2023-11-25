def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(250_000, 250_200+1):
    d = [n for n in f(x) if n%2 == 0]
    if len(d) == 6:
        print(*d[-2:])
##125012 250024
##125036 250072
##125068 250136
##50030 250150
##125084 250168
