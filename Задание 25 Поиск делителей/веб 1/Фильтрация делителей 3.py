def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(500_001, 500_100):
    d = [n for n in f(x) if n%10==8 and n != 8 and n != x]
    if d:
        print(x, min(d))
        
# 500002 178
##500004 18
##500016 48
##500018 58
##500020 4348
