
def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for x in range(5*10**5, 10**6+1):
    d = [i for i in f(x) if str(i)[-1] == '0' and len(str(i)) == 4]
    if len(d) > 45:
        print(x, len(d))
#554400 46
#831600 48
#982800 48
